# REST APIs with Flask

## What are Rest APIs?

**REST:** Representational state transfer

**RESTful API:** an application program interface that
uses HTTP methods to access and manipulate textual
representations of web resources.

## HTTP methods from [Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)

<table class="wikitable">
<caption>HTTP methods</caption>
<tbody><tr>
<th>Uniform Resource Locator (URL)</th>
<th>GET</th>
<th>PUT</th>
<th>PATCH</th>
<th>POST</th>
<th>DELETE</th>
</tr>
<tr>
<th>Collection, such as <code>https://api.example.com/resources/</code></th>
<td><b>List</b> the URIs and perhaps other details of the collection's members.</td>
<td><b>Replace</b> the entire collection with another collection.</td>
<td>Not generally used</td>
<td><b>Create</b> a new entry in the collection. The new entry's URI is assigned automatically and is usually returned by the operation.<sup id="cite_ref-thereisnorightway_17-0" class="reference"><a href="#cite_note-thereisnorightway-17">[17]</a></sup></td>
<td><b>Delete</b> the entire collection.</td>
</tr>
<tr>
<th>Element, such as <code>https://api.example.com/resources/item17</code></th>
<td><b>Retrieve</b> a representation of the addressed member of the collection, expressed in an appropriate Internet media type.</td>
<td><b>Replace</b> the addressed member of the collection, or if it does not exist, <b>create</b> it.</td>
<td><b>Update</b> the addressed member of the collection.</td>
<td>Not generally used. Treat the addressed member as a collection in its own right and <b>create</b> a new entry within it.<sup id="cite_ref-thereisnorightway_17-1" class="reference"><a href="#cite_note-thereisnorightway-17">[17]</a></sup></td>
<td><b>Delete</b> the addressed member of the collection.</td>
</tr>
</tbody>
</table>

## Example python application

The following application will help you see REST endpoints in Flask.

### Set up

```bash
# in this directory, run:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

### Test the application

```bash
# in another terminal also in this directory:
source venv/bin/activate

# test GET, POST, PUT, and DELETE
make GET
make PUT
make POST
make DELETE
```

## Written by

Samuel Roeca *samuel.roeca@gmail.com*
