# SNMP MIB module (AVAM-SNMPv1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAM-SNMPv1
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:28 2024
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

(DateAndTime,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "DateAndTime")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Availant_ObjectIdentity = ObjectIdentity
availant = _Availant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5910)
)
_AvProducts_ObjectIdentity = ObjectIdentity
avProducts = _AvProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5910, 1)
)
_AvamMIB_ObjectIdentity = ObjectIdentity
avamMIB = _AvamMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3)
)
_AvamVisObj_ObjectIdentity = ObjectIdentity
avamVisObj = _AvamVisObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 1)
)
_AvVersionString_Type = DisplayString
_AvVersionString_Object = MibScalar
avVersionString = _AvVersionString_Object(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 1, 1),
    _AvVersionString_Type()
)
avVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avVersionString.setStatus("mandatory")
_AvamNotify_ObjectIdentity = ObjectIdentity
avamNotify = _AvamNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 2)
)
_AvEventDateTime_Type = DisplayString
_AvEventDateTime_Object = MibScalar
avEventDateTime = _AvEventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 1),
    _AvEventDateTime_Type()
)
avEventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEventDateTime.setStatus("mandatory")
_AvEventAgent_Type = DisplayString
_AvEventAgent_Object = MibScalar
avEventAgent = _AvEventAgent_Object(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 2),
    _AvEventAgent_Type()
)
avEventAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEventAgent.setStatus("mandatory")
_AvHostURL_Type = DisplayString
_AvHostURL_Object = MibScalar
avHostURL = _AvHostURL_Object(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 4),
    _AvHostURL_Type()
)
avHostURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avHostURL.setStatus("mandatory")

# Managed Objects groups


# Notification objects

avEventNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 5910, 1, 3, 0, 1)
)
avEventNotify.setObjects(
      *(("AVAM-SNMPv1", "avEventDateTime"),
        ("AVAM-SNMPv1", "avEventAgent"),
        ("AVAM-SNMPv1", "avHostURL"))
)
if mibBuilder.loadTexts:
    avEventNotify.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAM-SNMPv1",
    **{"availant": availant,
       "avProducts": avProducts,
       "avamMIB": avamMIB,
       "avEventNotify": avEventNotify,
       "avamVisObj": avamVisObj,
       "avVersionString": avVersionString,
       "avamNotify": avamNotify,
       "avEventDateTime": avEventDateTime,
       "avEventAgent": avEventAgent,
       "avHostURL": avHostURL}
)
