# SNMP MIB module (MIME-MHS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIME-MHS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:02 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 internet,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "internet",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mail_ObjectIdentity = ObjectIdentity
mail = _Mail_ObjectIdentity(
    (1, 3, 6, 1, 7)
)
_Mime_mhs_ObjectIdentity = ObjectIdentity
mime_mhs = _Mime_mhs_ObjectIdentity(
    (1, 3, 6, 1, 7, 1)
)
_Mime_mhs_headings_ObjectIdentity = ObjectIdentity
mime_mhs_headings = _Mime_mhs_headings_ObjectIdentity(
    (1, 3, 6, 1, 7, 1, 1)
)
_Id_hex_partial_message_ObjectIdentity = ObjectIdentity
id_hex_partial_message = _Id_hex_partial_message_ObjectIdentity(
    (1, 3, 6, 1, 7, 1, 1, 1)
)
_Id_hex_multipart_message_ObjectIdentity = ObjectIdentity
id_hex_multipart_message = _Id_hex_multipart_message_ObjectIdentity(
    (1, 3, 6, 1, 7, 1, 1, 2)
)
_Mime_mhs_bodies_ObjectIdentity = ObjectIdentity
mime_mhs_bodies = _Mime_mhs_bodies_ObjectIdentity(
    (1, 3, 6, 1, 7, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIME-MHS",
    **{"mail": mail,
       "mime-mhs": mime_mhs,
       "mime-mhs-headings": mime_mhs_headings,
       "id-hex-partial-message": id_hex_partial_message,
       "id-hex-multipart-message": id_hex_multipart_message,
       "mime-mhs-bodies": mime_mhs_bodies}
)
