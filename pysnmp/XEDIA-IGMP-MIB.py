# SNMP MIB module (XEDIA-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:53 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xigmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XigmpMIBObjects_ObjectIdentity = ObjectIdentity
xigmpMIBObjects = _XigmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1)
)
_Xigmp_ObjectIdentity = ObjectIdentity
xigmp = _Xigmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1)
)
_XigmpInMsgs_Type = Counter32
_XigmpInMsgs_Object = MibScalar
xigmpInMsgs = _XigmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 1),
    _XigmpInMsgs_Type()
)
xigmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInMsgs.setStatus("current")
_XigmpInErrors_Type = Counter32
_XigmpInErrors_Object = MibScalar
xigmpInErrors = _XigmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 2),
    _XigmpInErrors_Type()
)
xigmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInErrors.setStatus("current")
_XigmpInReports_Type = Counter32
_XigmpInReports_Object = MibScalar
xigmpInReports = _XigmpInReports_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 3),
    _XigmpInReports_Type()
)
xigmpInReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInReports.setStatus("current")
_XigmpInV1Reports_Type = Counter32
_XigmpInV1Reports_Object = MibScalar
xigmpInV1Reports = _XigmpInV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 4),
    _XigmpInV1Reports_Type()
)
xigmpInV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInV1Reports.setStatus("current")
_XigmpInLeaves_Type = Counter32
_XigmpInLeaves_Object = MibScalar
xigmpInLeaves = _XigmpInLeaves_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 5),
    _XigmpInLeaves_Type()
)
xigmpInLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInLeaves.setStatus("current")
_XigmpInQueries_Type = Counter32
_XigmpInQueries_Object = MibScalar
xigmpInQueries = _XigmpInQueries_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 6),
    _XigmpInQueries_Type()
)
xigmpInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInQueries.setStatus("current")
_XigmpInUnknowns_Type = Counter32
_XigmpInUnknowns_Object = MibScalar
xigmpInUnknowns = _XigmpInUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 7),
    _XigmpInUnknowns_Type()
)
xigmpInUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInUnknowns.setStatus("current")
_XigmpOutMsgs_Type = Counter32
_XigmpOutMsgs_Object = MibScalar
xigmpOutMsgs = _XigmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 8),
    _XigmpOutMsgs_Type()
)
xigmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpOutMsgs.setStatus("current")
_XigmpInterfaceTable_Object = MibTable
xigmpInterfaceTable = _XigmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 9)
)
if mibBuilder.loadTexts:
    xigmpInterfaceTable.setStatus("current")
_XigmpInterfaceEntry_Object = MibTableRow
xigmpInterfaceEntry = _XigmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 9, 1)
)
xigmpInterfaceEntry.setIndexNames(
    (0, "XEDIA-IGMP-MIB", "xigmpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    xigmpInterfaceEntry.setStatus("current")
_XigmpInterfaceIfIndex_Type = InterfaceIndex
_XigmpInterfaceIfIndex_Object = MibTableColumn
xigmpInterfaceIfIndex = _XigmpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 9, 1, 1),
    _XigmpInterfaceIfIndex_Type()
)
xigmpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xigmpInterfaceIfIndex.setStatus("current")


class _XigmpInterfaceState_Type(Integer32):
    """Custom type xigmpInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XigmpInterfaceState_Type.__name__ = "Integer32"
_XigmpInterfaceState_Object = MibTableColumn
xigmpInterfaceState = _XigmpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 33, 1, 1, 9, 1, 2),
    _XigmpInterfaceState_Type()
)
xigmpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xigmpInterfaceState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-IGMP-MIB",
    **{"xigmpMIB": xigmpMIB,
       "xigmpMIBObjects": xigmpMIBObjects,
       "xigmp": xigmp,
       "xigmpInMsgs": xigmpInMsgs,
       "xigmpInErrors": xigmpInErrors,
       "xigmpInReports": xigmpInReports,
       "xigmpInV1Reports": xigmpInV1Reports,
       "xigmpInLeaves": xigmpInLeaves,
       "xigmpInQueries": xigmpInQueries,
       "xigmpInUnknowns": xigmpInUnknowns,
       "xigmpOutMsgs": xigmpOutMsgs,
       "xigmpInterfaceTable": xigmpInterfaceTable,
       "xigmpInterfaceEntry": xigmpInterfaceEntry,
       "xigmpInterfaceIfIndex": xigmpInterfaceIfIndex,
       "xigmpInterfaceState": xigmpInterfaceState}
)
