from flask import Flask, render_template, request, redirect, url_for, Response

app = Flask(__name__)

BUSINESS = {
    "name": "AquaPrime",
    "tagline": "PRAWN SEEDS",
    "owner": "Uday Garikina",
    "designation": "Owner",
    "phone1": "+91 99515 53436",
    "phone2": "+91 96521 03332",
    "whatsapp": "919951553436",
    "address": "Nakkapalli, Tuni, Andhra Pradesh – 531081",
}


def page(template, title, active):
    return render_template(
        template,
        title=title,
        active=active,
        business=BUSINESS
    )


@app.route("/")
def home():
    return page("home.html", "Home", "home")


@app.route("/about")
def about():
    return page("about.html", "About", "about")


@app.route("/why-us")
def why_us():
    return page("why.html", "Why Us", "why")


@app.route("/gallery")
def gallery():
    return page("gallery.html", "Gallery", "gallery")


@app.route("/enquiry")
def enquiry():
    return page("enquiry.html", "Enquiry", "enquiry")


@app.route("/enquiry/submit", methods=["POST"])
def submit_enquiry():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    location = request.form.get("location", "").strip()
    quantity = request.form.get("quantity", "").strip()
    message = request.form.get("message", "").strip()

    # Temporary: print enquiry in terminal.
    # Next upgrade: save to SQLite/PostgreSQL and show in admin dashboard.
    print("=" * 60)
    print("NEW AQUAPRIME ENQUIRY")
    print("Name:", name)
    print("Phone:", phone)
    print("Location:", location)
    print("Quantity:", quantity)
    print("Message:", message)
    print("=" * 60)

    return redirect(url_for("enquiry", sent="1"))


@app.route("/contact")
def contact():
    return page("contact.html", "Contact", "contact")


# ---------------------------------------------------------
# GOOGLE SEO - SITEMAP
# ---------------------------------------------------------

@app.route("/sitemap.xml")
def sitemap():
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>https://aqua-prime.in/</loc>
    </url>

    <url>
        <loc>https://aqua-prime.in/about</loc>
    </url>

    <url>
        <loc>https://aqua-prime.in/why-us</loc>
    </url>

    <url>
        <loc>https://aqua-prime.in/gallery</loc>
    </url>

    <url>
        <loc>https://aqua-prime.in/enquiry</loc>
    </url>

    <url>
        <loc>https://aqua-prime.in/contact</loc>
    </url>

</urlset>
"""

    return Response(
        sitemap_xml,
        mimetype="application/xml"
    )


# ---------------------------------------------------------
# GOOGLE SEO - ROBOTS.TXT
# ---------------------------------------------------------

@app.route("/robots.txt")
def robots():
    robots_txt = """User-agent: *
Allow: /

Sitemap: https://aqua-prime.in/sitemap.xml
"""

    return Response(
        robots_txt,
        mimetype="text/plain"
    )


# ---------------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)