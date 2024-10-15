# SNMP MIB module (WLSX-CTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-CTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:05 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TimeTicks,
 Unsigned32,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "TextualConvention",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxCtsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11)
)
wlsxCtsMIB.setRevisions(
        ("1907-08-06 05:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxCtsOpGroup_ObjectIdentity = ObjectIdentity
wlsxCtsOpGroup = _WlsxCtsOpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1)
)
_WlsxCtsRequestTable_Object = MibTable
wlsxCtsRequestTable = _WlsxCtsRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxCtsRequestTable.setStatus("current")
_WlsxCtsRequestEntry_Object = MibTableRow
wlsxCtsRequestEntry = _WlsxCtsRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1)
)
wlsxCtsRequestEntry.setIndexNames(
    (0, "WLSX-CTS-MIB", "wlsxCtsIndex"),
)
if mibBuilder.loadTexts:
    wlsxCtsRequestEntry.setStatus("current")
_WlsxCtsIndex_Type = Integer32
_WlsxCtsIndex_Object = MibTableColumn
wlsxCtsIndex = _WlsxCtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 1),
    _WlsxCtsIndex_Type()
)
wlsxCtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxCtsIndex.setStatus("current")
_WlsxCtsOpcode_Type = DisplayString
_WlsxCtsOpcode_Object = MibTableColumn
wlsxCtsOpcode = _WlsxCtsOpcode_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 2),
    _WlsxCtsOpcode_Type()
)
wlsxCtsOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxCtsOpcode.setStatus("current")
_WlsxCtsCookie_Type = DisplayString
_WlsxCtsCookie_Object = MibTableColumn
wlsxCtsCookie = _WlsxCtsCookie_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 3),
    _WlsxCtsCookie_Type()
)
wlsxCtsCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxCtsCookie.setStatus("current")
_WlsxCtsURL_Type = DisplayString
_WlsxCtsURL_Object = MibTableColumn
wlsxCtsURL = _WlsxCtsURL_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 4),
    _WlsxCtsURL_Type()
)
wlsxCtsURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxCtsURL.setStatus("current")


class _WlsxCtsFlags_Type(Bits):
    """Custom type wlsxCtsFlags based on Bits"""
    namedValues = NamedValues(
        *(("wlsxCtsFlagForce", 0),
          ("wlsxCtsFlagUseCert", 1))
    )

_WlsxCtsFlags_Type.__name__ = "Bits"
_WlsxCtsFlags_Object = MibTableColumn
wlsxCtsFlags = _WlsxCtsFlags_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 5),
    _WlsxCtsFlags_Type()
)
wlsxCtsFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxCtsFlags.setStatus("current")
_WlsxCtsStatus_Type = RowStatus
_WlsxCtsStatus_Object = MibTableColumn
wlsxCtsStatus = _WlsxCtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 6),
    _WlsxCtsStatus_Type()
)
wlsxCtsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxCtsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-CTS-MIB",
    **{"wlsxCtsMIB": wlsxCtsMIB,
       "wlsxCtsOpGroup": wlsxCtsOpGroup,
       "wlsxCtsRequestTable": wlsxCtsRequestTable,
       "wlsxCtsRequestEntry": wlsxCtsRequestEntry,
       "wlsxCtsIndex": wlsxCtsIndex,
       "wlsxCtsOpcode": wlsxCtsOpcode,
       "wlsxCtsCookie": wlsxCtsCookie,
       "wlsxCtsURL": wlsxCtsURL,
       "wlsxCtsFlags": wlsxCtsFlags,
       "wlsxCtsStatus": wlsxCtsStatus}
)
