# SNMP MIB module (Unisphere-Data-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:14 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pimInterfaceIfIndex,
 pimRPSetAddress,
 pimRPSetComponent,
 pimRPSetGroupAddress,
 pimRPSetGroupMask) = mibBuilder.importSymbols(
    "PIM-MIB",
    "pimInterfaceIfIndex",
    "pimRPSetAddress",
    "pimRPSetComponent",
    "pimRPSetGroupAddress",
    "pimRPSetGroupMask")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43)
)
usdPimMIB.setRevisions(
        ("2001-03-19 15:37",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdPimType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("invalid", 0),
          ("sparse", 2),
          ("sparseAndDense", 3))
    )



# MIB Managed Objects in the order of their OIDs

_UsdPimMIBObjects_ObjectIdentity = ObjectIdentity
usdPimMIBObjects = _UsdPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1)
)
_UsdPimTraps_ObjectIdentity = ObjectIdentity
usdPimTraps = _UsdPimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 0)
)
_UsdPimGlobal_ObjectIdentity = ObjectIdentity
usdPimGlobal = _UsdPimGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1)
)
_UsdPimNumHelloRcvd_Type = Integer32
_UsdPimNumHelloRcvd_Object = MibScalar
usdPimNumHelloRcvd = _UsdPimNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 1),
    _UsdPimNumHelloRcvd_Type()
)
usdPimNumHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumHelloRcvd.setStatus("current")
_UsdPimNumJoinPruneRcvd_Type = Integer32
_UsdPimNumJoinPruneRcvd_Object = MibScalar
usdPimNumJoinPruneRcvd = _UsdPimNumJoinPruneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 2),
    _UsdPimNumJoinPruneRcvd_Type()
)
usdPimNumJoinPruneRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumJoinPruneRcvd.setStatus("current")
_UsdPimNumAssertRcvd_Type = Integer32
_UsdPimNumAssertRcvd_Object = MibScalar
usdPimNumAssertRcvd = _UsdPimNumAssertRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 3),
    _UsdPimNumAssertRcvd_Type()
)
usdPimNumAssertRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumAssertRcvd.setStatus("current")
_UsdPimNumGraftRcvd_Type = Integer32
_UsdPimNumGraftRcvd_Object = MibScalar
usdPimNumGraftRcvd = _UsdPimNumGraftRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 4),
    _UsdPimNumGraftRcvd_Type()
)
usdPimNumGraftRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumGraftRcvd.setStatus("current")
_UsdPimNumGraftAckRcvd_Type = Integer32
_UsdPimNumGraftAckRcvd_Object = MibScalar
usdPimNumGraftAckRcvd = _UsdPimNumGraftAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 5),
    _UsdPimNumGraftAckRcvd_Type()
)
usdPimNumGraftAckRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumGraftAckRcvd.setStatus("current")
_UsdPimNumHelloSent_Type = Integer32
_UsdPimNumHelloSent_Object = MibScalar
usdPimNumHelloSent = _UsdPimNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 6),
    _UsdPimNumHelloSent_Type()
)
usdPimNumHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumHelloSent.setStatus("current")
_UsdPimNumJoinPruneSent_Type = Integer32
_UsdPimNumJoinPruneSent_Object = MibScalar
usdPimNumJoinPruneSent = _UsdPimNumJoinPruneSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 7),
    _UsdPimNumJoinPruneSent_Type()
)
usdPimNumJoinPruneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumJoinPruneSent.setStatus("current")
_UsdPimNumAssertSent_Type = Integer32
_UsdPimNumAssertSent_Object = MibScalar
usdPimNumAssertSent = _UsdPimNumAssertSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 8),
    _UsdPimNumAssertSent_Type()
)
usdPimNumAssertSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumAssertSent.setStatus("current")
_UsdPimNumGraftSent_Type = Integer32
_UsdPimNumGraftSent_Object = MibScalar
usdPimNumGraftSent = _UsdPimNumGraftSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 9),
    _UsdPimNumGraftSent_Type()
)
usdPimNumGraftSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumGraftSent.setStatus("current")
_UsdPimNumGraftAckSent_Type = Integer32
_UsdPimNumGraftAckSent_Object = MibScalar
usdPimNumGraftAckSent = _UsdPimNumGraftAckSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 10),
    _UsdPimNumGraftAckSent_Type()
)
usdPimNumGraftAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimNumGraftAckSent.setStatus("current")
_UsdPimInterfaceTable_Object = MibTable
usdPimInterfaceTable = _UsdPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11)
)
if mibBuilder.loadTexts:
    usdPimInterfaceTable.setStatus("current")
_UsdPimInterfaceEntry_Object = MibTableRow
usdPimInterfaceEntry = _UsdPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1)
)
usdPimInterfaceEntry.setIndexNames(
    (0, "PIM-MIB", "pimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    usdPimInterfaceEntry.setStatus("current")
_UsdPimIntfNumHelloRcvd_Type = Integer32
_UsdPimIntfNumHelloRcvd_Object = MibTableColumn
usdPimIntfNumHelloRcvd = _UsdPimIntfNumHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 1),
    _UsdPimIntfNumHelloRcvd_Type()
)
usdPimIntfNumHelloRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumHelloRcvd.setStatus("current")
_UsdPimIntfNumJoinPruneRcvd_Type = Integer32
_UsdPimIntfNumJoinPruneRcvd_Object = MibTableColumn
usdPimIntfNumJoinPruneRcvd = _UsdPimIntfNumJoinPruneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 2),
    _UsdPimIntfNumJoinPruneRcvd_Type()
)
usdPimIntfNumJoinPruneRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumJoinPruneRcvd.setStatus("current")
_UsdPimIntfNumAssertRcvd_Type = Integer32
_UsdPimIntfNumAssertRcvd_Object = MibTableColumn
usdPimIntfNumAssertRcvd = _UsdPimIntfNumAssertRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 3),
    _UsdPimIntfNumAssertRcvd_Type()
)
usdPimIntfNumAssertRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumAssertRcvd.setStatus("current")
_UsdPimIntfNumGraftRcvd_Type = Integer32
_UsdPimIntfNumGraftRcvd_Object = MibTableColumn
usdPimIntfNumGraftRcvd = _UsdPimIntfNumGraftRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 4),
    _UsdPimIntfNumGraftRcvd_Type()
)
usdPimIntfNumGraftRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumGraftRcvd.setStatus("current")
_UsdPimIntfNumGraftAckRcvd_Type = Integer32
_UsdPimIntfNumGraftAckRcvd_Object = MibTableColumn
usdPimIntfNumGraftAckRcvd = _UsdPimIntfNumGraftAckRcvd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 5),
    _UsdPimIntfNumGraftAckRcvd_Type()
)
usdPimIntfNumGraftAckRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumGraftAckRcvd.setStatus("current")
_UsdPimIntfNumHelloSent_Type = Integer32
_UsdPimIntfNumHelloSent_Object = MibTableColumn
usdPimIntfNumHelloSent = _UsdPimIntfNumHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 6),
    _UsdPimIntfNumHelloSent_Type()
)
usdPimIntfNumHelloSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumHelloSent.setStatus("current")
_UsdPimIntfNumJoinPruneSent_Type = Integer32
_UsdPimIntfNumJoinPruneSent_Object = MibTableColumn
usdPimIntfNumJoinPruneSent = _UsdPimIntfNumJoinPruneSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 7),
    _UsdPimIntfNumJoinPruneSent_Type()
)
usdPimIntfNumJoinPruneSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumJoinPruneSent.setStatus("current")
_UsdPimIntfNumAssertSent_Type = Integer32
_UsdPimIntfNumAssertSent_Object = MibTableColumn
usdPimIntfNumAssertSent = _UsdPimIntfNumAssertSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 8),
    _UsdPimIntfNumAssertSent_Type()
)
usdPimIntfNumAssertSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumAssertSent.setStatus("current")
_UsdPimIntfNumGraftSent_Type = Integer32
_UsdPimIntfNumGraftSent_Object = MibTableColumn
usdPimIntfNumGraftSent = _UsdPimIntfNumGraftSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 9),
    _UsdPimIntfNumGraftSent_Type()
)
usdPimIntfNumGraftSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumGraftSent.setStatus("current")
_UsdPimIntfNumGraftAckSent_Type = Integer32
_UsdPimIntfNumGraftAckSent_Object = MibTableColumn
usdPimIntfNumGraftAckSent = _UsdPimIntfNumGraftAckSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 10),
    _UsdPimIntfNumGraftAckSent_Type()
)
usdPimIntfNumGraftAckSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimIntfNumGraftAckSent.setStatus("current")


class _UsdPimIntfVersion_Type(Integer32):
    """Custom type usdPimIntfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdPimIntfVersion_Type.__name__ = "Integer32"
_UsdPimIntfVersion_Object = MibTableColumn
usdPimIntfVersion = _UsdPimIntfVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 11),
    _UsdPimIntfVersion_Type()
)
usdPimIntfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimIntfVersion.setStatus("current")
_UsdPimIntfNumNbrs_Type = Integer32
_UsdPimIntfNumNbrs_Object = MibTableColumn
usdPimIntfNumNbrs = _UsdPimIntfNumNbrs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 11, 1, 12),
    _UsdPimIntfNumNbrs_Type()
)
usdPimIntfNumNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimIntfNumNbrs.setStatus("current")
_UsdPimMRouteTable_Object = MibTable
usdPimMRouteTable = _UsdPimMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12)
)
if mibBuilder.loadTexts:
    usdPimMRouteTable.setStatus("current")
_UsdPimMRouteEntry_Object = MibTableRow
usdPimMRouteEntry = _UsdPimMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1)
)
usdPimMRouteEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteGroup"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteSource"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteSourceMask"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteRPAddress"),
)
if mibBuilder.loadTexts:
    usdPimMRouteEntry.setStatus("current")
_UsdPimMRouteGroup_Type = IpAddress
_UsdPimMRouteGroup_Object = MibTableColumn
usdPimMRouteGroup = _UsdPimMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 1),
    _UsdPimMRouteGroup_Type()
)
usdPimMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteGroup.setStatus("current")
_UsdPimMRouteSource_Type = IpAddress
_UsdPimMRouteSource_Object = MibTableColumn
usdPimMRouteSource = _UsdPimMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 2),
    _UsdPimMRouteSource_Type()
)
usdPimMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteSource.setStatus("current")
_UsdPimMRouteSourceMask_Type = IpAddress
_UsdPimMRouteSourceMask_Object = MibTableColumn
usdPimMRouteSourceMask = _UsdPimMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 3),
    _UsdPimMRouteSourceMask_Type()
)
usdPimMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteSourceMask.setStatus("current")
_UsdPimMRouteRPAddress_Type = IpAddress
_UsdPimMRouteRPAddress_Object = MibTableColumn
usdPimMRouteRPAddress = _UsdPimMRouteRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 4),
    _UsdPimMRouteRPAddress_Type()
)
usdPimMRouteRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteRPAddress.setStatus("current")
_UsdPimMRouteUpstreamAssertTimer_Type = TimeTicks
_UsdPimMRouteUpstreamAssertTimer_Object = MibTableColumn
usdPimMRouteUpstreamAssertTimer = _UsdPimMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 5),
    _UsdPimMRouteUpstreamAssertTimer_Type()
)
usdPimMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteUpstreamAssertTimer.setStatus("current")
_UsdPimMRouteAssertMetric_Type = Integer32
_UsdPimMRouteAssertMetric_Object = MibTableColumn
usdPimMRouteAssertMetric = _UsdPimMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 6),
    _UsdPimMRouteAssertMetric_Type()
)
usdPimMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteAssertMetric.setStatus("current")
_UsdPimMRouteAssertPref_Type = Integer32
_UsdPimMRouteAssertPref_Object = MibTableColumn
usdPimMRouteAssertPref = _UsdPimMRouteAssertPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 7),
    _UsdPimMRouteAssertPref_Type()
)
usdPimMRouteAssertPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteAssertPref.setStatus("current")
_UsdPimMRouteAssertRPTBit_Type = TruthValue
_UsdPimMRouteAssertRPTBit_Object = MibTableColumn
usdPimMRouteAssertRPTBit = _UsdPimMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 8),
    _UsdPimMRouteAssertRPTBit_Type()
)
usdPimMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteAssertRPTBit.setStatus("current")


class _UsdPimMRouteBits_Type(Bits):
    """Custom type usdPimMRouteBits based on Bits"""
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )

_UsdPimMRouteBits_Type.__name__ = "Bits"
_UsdPimMRouteBits_Object = MibTableColumn
usdPimMRouteBits = _UsdPimMRouteBits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 9),
    _UsdPimMRouteBits_Type()
)
usdPimMRouteBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteBits.setStatus("current")
_UsdPimMRouteRPAddrInUse_Type = IpAddress
_UsdPimMRouteRPAddrInUse_Object = MibTableColumn
usdPimMRouteRPAddrInUse = _UsdPimMRouteRPAddrInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 10),
    _UsdPimMRouteRPAddrInUse_Type()
)
usdPimMRouteRPAddrInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteRPAddrInUse.setStatus("current")
_UsdPimMRouteUpstreamNbr_Type = IpAddress
_UsdPimMRouteUpstreamNbr_Object = MibTableColumn
usdPimMRouteUpstreamNbr = _UsdPimMRouteUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 11),
    _UsdPimMRouteUpstreamNbr_Type()
)
usdPimMRouteUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteUpstreamNbr.setStatus("current")
_UsdPimMRouteIifAddr_Type = IpAddress
_UsdPimMRouteIifAddr_Object = MibTableColumn
usdPimMRouteIifAddr = _UsdPimMRouteIifAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 12),
    _UsdPimMRouteIifAddr_Type()
)
usdPimMRouteIifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteIifAddr.setStatus("current")
_UsdPimMRouteIsWaitingToSwitchToSPT_Type = TruthValue
_UsdPimMRouteIsWaitingToSwitchToSPT_Object = MibTableColumn
usdPimMRouteIsWaitingToSwitchToSPT = _UsdPimMRouteIsWaitingToSwitchToSPT_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 13),
    _UsdPimMRouteIsWaitingToSwitchToSPT_Type()
)
usdPimMRouteIsWaitingToSwitchToSPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteIsWaitingToSwitchToSPT.setStatus("current")
_UsdPimMRouteEntryExpiryTimer_Type = TimeTicks
_UsdPimMRouteEntryExpiryTimer_Object = MibTableColumn
usdPimMRouteEntryExpiryTimer = _UsdPimMRouteEntryExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 14),
    _UsdPimMRouteEntryExpiryTimer_Type()
)
usdPimMRouteEntryExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteEntryExpiryTimer.setStatus("current")
_UsdPimMRouteSenderDRAddr_Type = IpAddress
_UsdPimMRouteSenderDRAddr_Object = MibTableColumn
usdPimMRouteSenderDRAddr = _UsdPimMRouteSenderDRAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 15),
    _UsdPimMRouteSenderDRAddr_Type()
)
usdPimMRouteSenderDRAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteSenderDRAddr.setStatus("current")
_UsdPimMRouteRouteAddr_Type = IpAddress
_UsdPimMRouteRouteAddr_Object = MibTableColumn
usdPimMRouteRouteAddr = _UsdPimMRouteRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 16),
    _UsdPimMRouteRouteAddr_Type()
)
usdPimMRouteRouteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteRouteAddr.setStatus("current")
_UsdPimMRouteRouteMask_Type = IpAddress
_UsdPimMRouteRouteMask_Object = MibTableColumn
usdPimMRouteRouteMask = _UsdPimMRouteRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 17),
    _UsdPimMRouteRouteMask_Type()
)
usdPimMRouteRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteRouteMask.setStatus("current")
_UsdPimMRouteGRPAddr_Type = IpAddress
_UsdPimMRouteGRPAddr_Object = MibTableColumn
usdPimMRouteGRPAddr = _UsdPimMRouteGRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 18),
    _UsdPimMRouteGRPAddr_Type()
)
usdPimMRouteGRPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteGRPAddr.setStatus("current")
_UsdPimMRouteGRPMask_Type = IpAddress
_UsdPimMRouteGRPMask_Object = MibTableColumn
usdPimMRouteGRPMask = _UsdPimMRouteGRPMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 19),
    _UsdPimMRouteGRPMask_Type()
)
usdPimMRouteGRPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteGRPMask.setStatus("current")
_UsdPimMRouteOtherProtoOifJoinTypeAll_Type = TruthValue
_UsdPimMRouteOtherProtoOifJoinTypeAll_Object = MibTableColumn
usdPimMRouteOtherProtoOifJoinTypeAll = _UsdPimMRouteOtherProtoOifJoinTypeAll_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 20),
    _UsdPimMRouteOtherProtoOifJoinTypeAll_Type()
)
usdPimMRouteOtherProtoOifJoinTypeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteOtherProtoOifJoinTypeAll.setStatus("current")
_UsdPimMRouteOtherProtoOifJoinTypeG_Type = TruthValue
_UsdPimMRouteOtherProtoOifJoinTypeG_Object = MibTableColumn
usdPimMRouteOtherProtoOifJoinTypeG = _UsdPimMRouteOtherProtoOifJoinTypeG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 21),
    _UsdPimMRouteOtherProtoOifJoinTypeG_Type()
)
usdPimMRouteOtherProtoOifJoinTypeG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteOtherProtoOifJoinTypeG.setStatus("current")
_UsdPimMRouteOtherProtoOifJoinTypeSG_Type = TruthValue
_UsdPimMRouteOtherProtoOifJoinTypeSG_Object = MibTableColumn
usdPimMRouteOtherProtoOifJoinTypeSG = _UsdPimMRouteOtherProtoOifJoinTypeSG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 22),
    _UsdPimMRouteOtherProtoOifJoinTypeSG_Type()
)
usdPimMRouteOtherProtoOifJoinTypeSG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteOtherProtoOifJoinTypeSG.setStatus("current")
_UsdPimMRoutePimType_Type = UsdPimType
_UsdPimMRoutePimType_Object = MibTableColumn
usdPimMRoutePimType = _UsdPimMRoutePimType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 12, 1, 23),
    _UsdPimMRoutePimType_Type()
)
usdPimMRoutePimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRoutePimType.setStatus("current")
_UsdPimMRouteNextHopTable_Object = MibTable
usdPimMRouteNextHopTable = _UsdPimMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13)
)
if mibBuilder.loadTexts:
    usdPimMRouteNextHopTable.setStatus("current")
_UsdPimMRouteNextHopEntry_Object = MibTableRow
usdPimMRouteNextHopEntry = _UsdPimMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1)
)
usdPimMRouteNextHopEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopGroupAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopSrcAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopSrcMask"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopRPAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopIfId"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    usdPimMRouteNextHopEntry.setStatus("current")
_UsdPimMRouteNextHopGroupAddr_Type = IpAddress
_UsdPimMRouteNextHopGroupAddr_Object = MibTableColumn
usdPimMRouteNextHopGroupAddr = _UsdPimMRouteNextHopGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 2),
    _UsdPimMRouteNextHopGroupAddr_Type()
)
usdPimMRouteNextHopGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopGroupAddr.setStatus("current")
_UsdPimMRouteNextHopSrcAddr_Type = IpAddress
_UsdPimMRouteNextHopSrcAddr_Object = MibTableColumn
usdPimMRouteNextHopSrcAddr = _UsdPimMRouteNextHopSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 3),
    _UsdPimMRouteNextHopSrcAddr_Type()
)
usdPimMRouteNextHopSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopSrcAddr.setStatus("current")
_UsdPimMRouteNextHopSrcMask_Type = IpAddress
_UsdPimMRouteNextHopSrcMask_Object = MibTableColumn
usdPimMRouteNextHopSrcMask = _UsdPimMRouteNextHopSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 4),
    _UsdPimMRouteNextHopSrcMask_Type()
)
usdPimMRouteNextHopSrcMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopSrcMask.setStatus("current")
_UsdPimMRouteNextHopRPAddr_Type = IpAddress
_UsdPimMRouteNextHopRPAddr_Object = MibTableColumn
usdPimMRouteNextHopRPAddr = _UsdPimMRouteNextHopRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 5),
    _UsdPimMRouteNextHopRPAddr_Type()
)
usdPimMRouteNextHopRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopRPAddr.setStatus("current")
_UsdPimMRouteNextHopIfId_Type = InterfaceIndex
_UsdPimMRouteNextHopIfId_Object = MibTableColumn
usdPimMRouteNextHopIfId = _UsdPimMRouteNextHopIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 6),
    _UsdPimMRouteNextHopIfId_Type()
)
usdPimMRouteNextHopIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopIfId.setStatus("current")
_UsdPimMRouteNextHopAddress_Type = IpAddress
_UsdPimMRouteNextHopAddress_Object = MibTableColumn
usdPimMRouteNextHopAddress = _UsdPimMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 7),
    _UsdPimMRouteNextHopAddress_Type()
)
usdPimMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopAddress.setStatus("current")


class _UsdPimMRouteNextHopPruneReason_Type(Integer32):
    """Custom type usdPimMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assert", 3),
          ("other", 1),
          ("prune", 2))
    )


_UsdPimMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_UsdPimMRouteNextHopPruneReason_Object = MibTableColumn
usdPimMRouteNextHopPruneReason = _UsdPimMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 8),
    _UsdPimMRouteNextHopPruneReason_Type()
)
usdPimMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopPruneReason.setStatus("current")
_UsdPimMRouteNextHopJoinTypeSSRP_Type = TruthValue
_UsdPimMRouteNextHopJoinTypeSSRP_Object = MibTableColumn
usdPimMRouteNextHopJoinTypeSSRP = _UsdPimMRouteNextHopJoinTypeSSRP_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 9),
    _UsdPimMRouteNextHopJoinTypeSSRP_Type()
)
usdPimMRouteNextHopJoinTypeSSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopJoinTypeSSRP.setStatus("current")
_UsdPimMRouteNextHopJoinTypeG_Type = TruthValue
_UsdPimMRouteNextHopJoinTypeG_Object = MibTableColumn
usdPimMRouteNextHopJoinTypeG = _UsdPimMRouteNextHopJoinTypeG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 10),
    _UsdPimMRouteNextHopJoinTypeG_Type()
)
usdPimMRouteNextHopJoinTypeG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopJoinTypeG.setStatus("current")
_UsdPimMRouteNextHopJoinTypeSG_Type = TruthValue
_UsdPimMRouteNextHopJoinTypeSG_Object = MibTableColumn
usdPimMRouteNextHopJoinTypeSG = _UsdPimMRouteNextHopJoinTypeSG_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 11),
    _UsdPimMRouteNextHopJoinTypeSG_Type()
)
usdPimMRouteNextHopJoinTypeSG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopJoinTypeSG.setStatus("current")
_UsdPimMRouteNextHopHasLGM_Type = TruthValue
_UsdPimMRouteNextHopHasLGM_Object = MibTableColumn
usdPimMRouteNextHopHasLGM = _UsdPimMRouteNextHopHasLGM_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 12),
    _UsdPimMRouteNextHopHasLGM_Type()
)
usdPimMRouteNextHopHasLGM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopHasLGM.setStatus("current")
_UsdPimMRouteNextHopHasOifAW_Type = TruthValue
_UsdPimMRouteNextHopHasOifAW_Object = MibTableColumn
usdPimMRouteNextHopHasOifAW = _UsdPimMRouteNextHopHasOifAW_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 13),
    _UsdPimMRouteNextHopHasOifAW_Type()
)
usdPimMRouteNextHopHasOifAW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopHasOifAW.setStatus("current")
_UsdPimMRouteNextHopHasOifSendAssert_Type = TruthValue
_UsdPimMRouteNextHopHasOifSendAssert_Object = MibTableColumn
usdPimMRouteNextHopHasOifSendAssert = _UsdPimMRouteNextHopHasOifSendAssert_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 14),
    _UsdPimMRouteNextHopHasOifSendAssert_Type()
)
usdPimMRouteNextHopHasOifSendAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopHasOifSendAssert.setStatus("current")
_UsdPimMRouteNextHopHasOifRegister_Type = TruthValue
_UsdPimMRouteNextHopHasOifRegister_Object = MibTableColumn
usdPimMRouteNextHopHasOifRegister = _UsdPimMRouteNextHopHasOifRegister_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 15),
    _UsdPimMRouteNextHopHasOifRegister_Type()
)
usdPimMRouteNextHopHasOifRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopHasOifRegister.setStatus("current")
_UsdPimMRouteNextHopHasOifBorderBit_Type = TruthValue
_UsdPimMRouteNextHopHasOifBorderBit_Object = MibTableColumn
usdPimMRouteNextHopHasOifBorderBit = _UsdPimMRouteNextHopHasOifBorderBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 16),
    _UsdPimMRouteNextHopHasOifBorderBit_Type()
)
usdPimMRouteNextHopHasOifBorderBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopHasOifBorderBit.setStatus("current")
_UsdPimMRouteNextHopHasOifNullEncapsBit_Type = TruthValue
_UsdPimMRouteNextHopHasOifNullEncapsBit_Object = MibTableColumn
usdPimMRouteNextHopHasOifNullEncapsBit = _UsdPimMRouteNextHopHasOifNullEncapsBit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 17),
    _UsdPimMRouteNextHopHasOifNullEncapsBit_Type()
)
usdPimMRouteNextHopHasOifNullEncapsBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopHasOifNullEncapsBit.setStatus("current")
_UsdPimMRouteNextHopJoinEndTimer_Type = TimeTicks
_UsdPimMRouteNextHopJoinEndTimer_Object = MibTableColumn
usdPimMRouteNextHopJoinEndTimer = _UsdPimMRouteNextHopJoinEndTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 18),
    _UsdPimMRouteNextHopJoinEndTimer_Type()
)
usdPimMRouteNextHopJoinEndTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopJoinEndTimer.setStatus("current")
_UsdPimMRouteNextHopAssertEndTimer_Type = TimeTicks
_UsdPimMRouteNextHopAssertEndTimer_Object = MibTableColumn
usdPimMRouteNextHopAssertEndTimer = _UsdPimMRouteNextHopAssertEndTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 19),
    _UsdPimMRouteNextHopAssertEndTimer_Type()
)
usdPimMRouteNextHopAssertEndTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopAssertEndTimer.setStatus("current")
_UsdPimMRouteNextHopNextAssertTimer_Type = TimeTicks
_UsdPimMRouteNextHopNextAssertTimer_Object = MibTableColumn
usdPimMRouteNextHopNextAssertTimer = _UsdPimMRouteNextHopNextAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 20),
    _UsdPimMRouteNextHopNextAssertTimer_Type()
)
usdPimMRouteNextHopNextAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopNextAssertTimer.setStatus("current")
_UsdPimMRouteNextHopAssertSrcAddress_Type = IpAddress
_UsdPimMRouteNextHopAssertSrcAddress_Object = MibTableColumn
usdPimMRouteNextHopAssertSrcAddress = _UsdPimMRouteNextHopAssertSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 21),
    _UsdPimMRouteNextHopAssertSrcAddress_Type()
)
usdPimMRouteNextHopAssertSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopAssertSrcAddress.setStatus("current")
_UsdPimMRouteNextHopRegisterSuppressionTimer_Type = TimeTicks
_UsdPimMRouteNextHopRegisterSuppressionTimer_Object = MibTableColumn
usdPimMRouteNextHopRegisterSuppressionTimer = _UsdPimMRouteNextHopRegisterSuppressionTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 22),
    _UsdPimMRouteNextHopRegisterSuppressionTimer_Type()
)
usdPimMRouteNextHopRegisterSuppressionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopRegisterSuppressionTimer.setStatus("current")
_UsdPimMRouteNextHopPimType_Type = UsdPimType
_UsdPimMRouteNextHopPimType_Object = MibTableColumn
usdPimMRouteNextHopPimType = _UsdPimMRouteNextHopPimType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 23),
    _UsdPimMRouteNextHopPimType_Type()
)
usdPimMRouteNextHopPimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopPimType.setStatus("current")
_UsdPimMRouteNextHopPruneTimeLeft_Type = TimeTicks
_UsdPimMRouteNextHopPruneTimeLeft_Object = MibTableColumn
usdPimMRouteNextHopPruneTimeLeft = _UsdPimMRouteNextHopPruneTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 24),
    _UsdPimMRouteNextHopPruneTimeLeft_Type()
)
usdPimMRouteNextHopPruneTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopPruneTimeLeft.setStatus("current")
_UsdPimMRouteNextHopsendingIpAddress_Type = IpAddress
_UsdPimMRouteNextHopsendingIpAddress_Object = MibTableColumn
usdPimMRouteNextHopsendingIpAddress = _UsdPimMRouteNextHopsendingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 13, 1, 25),
    _UsdPimMRouteNextHopsendingIpAddress_Type()
)
usdPimMRouteNextHopsendingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimMRouteNextHopsendingIpAddress.setStatus("current")
_UsdPimRPSetTable_Object = MibTable
usdPimRPSetTable = _UsdPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14)
)
if mibBuilder.loadTexts:
    usdPimRPSetTable.setStatus("current")
_UsdPimRPSetEntry_Object = MibTableRow
usdPimRPSetEntry = _UsdPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1)
)
usdPimRPSetEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPSetComponent"),
    (0, "PIM-MIB", "pimRPSetGroupAddress"),
    (0, "PIM-MIB", "pimRPSetGroupMask"),
    (0, "PIM-MIB", "pimRPSetAddress"),
)
if mibBuilder.loadTexts:
    usdPimRPSetEntry.setStatus("current")


class _UsdPimRPSetPriority_Type(Integer32):
    """Custom type usdPimRPSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdPimRPSetPriority_Type.__name__ = "Integer32"
_UsdPimRPSetPriority_Object = MibTableColumn
usdPimRPSetPriority = _UsdPimRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1, 1),
    _UsdPimRPSetPriority_Type()
)
usdPimRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimRPSetPriority.setStatus("current")


class _UsdPimRPSetTypeInfo_Type(Integer32):
    """Custom type usdPimRPSetTypeInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("pimRPTypeAutoRP", 3),
          ("pimRPTypeAutoRPNegative", 7),
          ("pimRPTypeBSR", 4),
          ("pimRPTypeBSRNegative", 8),
          ("pimRPTypeInvalid", 0),
          ("pimRPTypeStatic", 1),
          ("pimRPTypeStaticNegative", 5),
          ("pimRPTypeStaticOverride", 2),
          ("pimRPTypeStaticOverrideNegative", 6))
    )


_UsdPimRPSetTypeInfo_Type.__name__ = "Integer32"
_UsdPimRPSetTypeInfo_Object = MibTableColumn
usdPimRPSetTypeInfo = _UsdPimRPSetTypeInfo_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1, 2),
    _UsdPimRPSetTypeInfo_Type()
)
usdPimRPSetTypeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimRPSetTypeInfo.setStatus("current")


class _UsdPimRPSetAccessListName_Type(OctetString):
    """Custom type usdPimRPSetAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdPimRPSetAccessListName_Type.__name__ = "OctetString"
_UsdPimRPSetAccessListName_Object = MibTableColumn
usdPimRPSetAccessListName = _UsdPimRPSetAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 14, 1, 3),
    _UsdPimRPSetAccessListName_Type()
)
usdPimRPSetAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimRPSetAccessListName.setStatus("current")
_UsdPimStaticRPConfTable_Object = MibTable
usdPimStaticRPConfTable = _UsdPimStaticRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15)
)
if mibBuilder.loadTexts:
    usdPimStaticRPConfTable.setStatus("current")
_UsdPimStaticRPConfEntry_Object = MibTableRow
usdPimStaticRPConfEntry = _UsdPimStaticRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1)
)
usdPimStaticRPConfEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimStaticRPConfComponentIndex"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimStaticRPConfRPAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimStaticRPConfAccessListName"),
)
if mibBuilder.loadTexts:
    usdPimStaticRPConfEntry.setStatus("current")


class _UsdPimStaticRPConfComponentIndex_Type(Integer32):
    """Custom type usdPimStaticRPConfComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPimStaticRPConfComponentIndex_Type.__name__ = "Integer32"
_UsdPimStaticRPConfComponentIndex_Object = MibTableColumn
usdPimStaticRPConfComponentIndex = _UsdPimStaticRPConfComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 1),
    _UsdPimStaticRPConfComponentIndex_Type()
)
usdPimStaticRPConfComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimStaticRPConfComponentIndex.setStatus("current")
_UsdPimStaticRPConfRPAddr_Type = IpAddress
_UsdPimStaticRPConfRPAddr_Object = MibTableColumn
usdPimStaticRPConfRPAddr = _UsdPimStaticRPConfRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 2),
    _UsdPimStaticRPConfRPAddr_Type()
)
usdPimStaticRPConfRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimStaticRPConfRPAddr.setStatus("current")


class _UsdPimStaticRPConfAccessListName_Type(OctetString):
    """Custom type usdPimStaticRPConfAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdPimStaticRPConfAccessListName_Type.__name__ = "OctetString"
_UsdPimStaticRPConfAccessListName_Object = MibTableColumn
usdPimStaticRPConfAccessListName = _UsdPimStaticRPConfAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 3),
    _UsdPimStaticRPConfAccessListName_Type()
)
usdPimStaticRPConfAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimStaticRPConfAccessListName.setStatus("current")
_UsdPimStaticRPConfRowStatus_Type = RowStatus
_UsdPimStaticRPConfRowStatus_Object = MibTableColumn
usdPimStaticRPConfRowStatus = _UsdPimStaticRPConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 4),
    _UsdPimStaticRPConfRowStatus_Type()
)
usdPimStaticRPConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimStaticRPConfRowStatus.setStatus("current")


class _UsdPimStaticRPConfOverride_Type(TruthValue):
    """Custom type usdPimStaticRPConfOverride based on TruthValue"""


_UsdPimStaticRPConfOverride_Object = MibTableColumn
usdPimStaticRPConfOverride = _UsdPimStaticRPConfOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 15, 1, 5),
    _UsdPimStaticRPConfOverride_Type()
)
usdPimStaticRPConfOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimStaticRPConfOverride.setStatus("current")
_UsdPimAutoRPConfTable_Object = MibTable
usdPimAutoRPConfTable = _UsdPimAutoRPConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16)
)
if mibBuilder.loadTexts:
    usdPimAutoRPConfTable.setStatus("current")
_UsdPimAutoRPConfEntry_Object = MibTableRow
usdPimAutoRPConfEntry = _UsdPimAutoRPConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1)
)
usdPimAutoRPConfEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPConfComponentIndex"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPConfCandRPAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPConfGroupAccessListName"),
)
if mibBuilder.loadTexts:
    usdPimAutoRPConfEntry.setStatus("current")


class _UsdPimAutoRPConfComponentIndex_Type(Integer32):
    """Custom type usdPimAutoRPConfComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPimAutoRPConfComponentIndex_Type.__name__ = "Integer32"
_UsdPimAutoRPConfComponentIndex_Object = MibTableColumn
usdPimAutoRPConfComponentIndex = _UsdPimAutoRPConfComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 1),
    _UsdPimAutoRPConfComponentIndex_Type()
)
usdPimAutoRPConfComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPConfComponentIndex.setStatus("current")
_UsdPimAutoRPConfCandRPAddr_Type = IpAddress
_UsdPimAutoRPConfCandRPAddr_Object = MibTableColumn
usdPimAutoRPConfCandRPAddr = _UsdPimAutoRPConfCandRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 2),
    _UsdPimAutoRPConfCandRPAddr_Type()
)
usdPimAutoRPConfCandRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPConfCandRPAddr.setStatus("current")


class _UsdPimAutoRPConfGroupAccessListName_Type(OctetString):
    """Custom type usdPimAutoRPConfGroupAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdPimAutoRPConfGroupAccessListName_Type.__name__ = "OctetString"
_UsdPimAutoRPConfGroupAccessListName_Object = MibTableColumn
usdPimAutoRPConfGroupAccessListName = _UsdPimAutoRPConfGroupAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 3),
    _UsdPimAutoRPConfGroupAccessListName_Type()
)
usdPimAutoRPConfGroupAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPConfGroupAccessListName.setStatus("current")
_UsdPimAutoRPConfRowStatus_Type = RowStatus
_UsdPimAutoRPConfRowStatus_Object = MibTableColumn
usdPimAutoRPConfRowStatus = _UsdPimAutoRPConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 4),
    _UsdPimAutoRPConfRowStatus_Type()
)
usdPimAutoRPConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimAutoRPConfRowStatus.setStatus("current")


class _UsdPimAutoRPConfTTL_Type(Integer32):
    """Custom type usdPimAutoRPConfTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdPimAutoRPConfTTL_Type.__name__ = "Integer32"
_UsdPimAutoRPConfTTL_Object = MibTableColumn
usdPimAutoRPConfTTL = _UsdPimAutoRPConfTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 5),
    _UsdPimAutoRPConfTTL_Type()
)
usdPimAutoRPConfTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimAutoRPConfTTL.setStatus("current")


class _UsdPimAutoRPConfAncmntIntvl_Type(TimeTicks):
    """Custom type usdPimAutoRPConfAncmntIntvl based on TimeTicks"""
    defaultValue = 60


_UsdPimAutoRPConfAncmntIntvl_Object = MibTableColumn
usdPimAutoRPConfAncmntIntvl = _UsdPimAutoRPConfAncmntIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 6),
    _UsdPimAutoRPConfAncmntIntvl_Type()
)
usdPimAutoRPConfAncmntIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimAutoRPConfAncmntIntvl.setStatus("current")
_UsdPimAutoRPConfifId_Type = InterfaceIndex
_UsdPimAutoRPConfifId_Object = MibTableColumn
usdPimAutoRPConfifId = _UsdPimAutoRPConfifId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 16, 1, 7),
    _UsdPimAutoRPConfifId_Type()
)
usdPimAutoRPConfifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimAutoRPConfifId.setStatus("current")
_UsdPimAutoRPCandTable_Object = MibTable
usdPimAutoRPCandTable = _UsdPimAutoRPCandTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17)
)
if mibBuilder.loadTexts:
    usdPimAutoRPCandTable.setStatus("current")
_UsdPimAutoRPCandEntry_Object = MibTableRow
usdPimAutoRPCandEntry = _UsdPimAutoRPCandEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1)
)
usdPimAutoRPCandEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPCandComponentIndex"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPCandRPAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPCandGroupAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimAutoRPCandGroupMask"),
)
if mibBuilder.loadTexts:
    usdPimAutoRPCandEntry.setStatus("current")


class _UsdPimAutoRPCandComponentIndex_Type(Integer32):
    """Custom type usdPimAutoRPCandComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPimAutoRPCandComponentIndex_Type.__name__ = "Integer32"
_UsdPimAutoRPCandComponentIndex_Object = MibTableColumn
usdPimAutoRPCandComponentIndex = _UsdPimAutoRPCandComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 1),
    _UsdPimAutoRPCandComponentIndex_Type()
)
usdPimAutoRPCandComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPCandComponentIndex.setStatus("current")
_UsdPimAutoRPCandRPAddr_Type = IpAddress
_UsdPimAutoRPCandRPAddr_Object = MibTableColumn
usdPimAutoRPCandRPAddr = _UsdPimAutoRPCandRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 2),
    _UsdPimAutoRPCandRPAddr_Type()
)
usdPimAutoRPCandRPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPCandRPAddr.setStatus("current")
_UsdPimAutoRPCandGroupAddr_Type = IpAddress
_UsdPimAutoRPCandGroupAddr_Object = MibTableColumn
usdPimAutoRPCandGroupAddr = _UsdPimAutoRPCandGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 3),
    _UsdPimAutoRPCandGroupAddr_Type()
)
usdPimAutoRPCandGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPCandGroupAddr.setStatus("current")
_UsdPimAutoRPCandGroupMask_Type = IpAddress
_UsdPimAutoRPCandGroupMask_Object = MibTableColumn
usdPimAutoRPCandGroupMask = _UsdPimAutoRPCandGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 4),
    _UsdPimAutoRPCandGroupMask_Type()
)
usdPimAutoRPCandGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimAutoRPCandGroupMask.setStatus("current")
_UsdPimAutoRPCandRowStatus_Type = RowStatus
_UsdPimAutoRPCandRowStatus_Object = MibTableColumn
usdPimAutoRPCandRowStatus = _UsdPimAutoRPCandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 5),
    _UsdPimAutoRPCandRowStatus_Type()
)
usdPimAutoRPCandRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimAutoRPCandRowStatus.setStatus("current")


class _UsdPimAutoRPCandAccessListName_Type(OctetString):
    """Custom type usdPimAutoRPCandAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdPimAutoRPCandAccessListName_Type.__name__ = "OctetString"
_UsdPimAutoRPCandAccessListName_Object = MibTableColumn
usdPimAutoRPCandAccessListName = _UsdPimAutoRPCandAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 6),
    _UsdPimAutoRPCandAccessListName_Type()
)
usdPimAutoRPCandAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimAutoRPCandAccessListName.setStatus("current")


class _UsdPimAutoRPCandAutoRPTTL_Type(Integer32):
    """Custom type usdPimAutoRPCandAutoRPTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdPimAutoRPCandAutoRPTTL_Type.__name__ = "Integer32"
_UsdPimAutoRPCandAutoRPTTL_Object = MibTableColumn
usdPimAutoRPCandAutoRPTTL = _UsdPimAutoRPCandAutoRPTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 7),
    _UsdPimAutoRPCandAutoRPTTL_Type()
)
usdPimAutoRPCandAutoRPTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimAutoRPCandAutoRPTTL.setStatus("current")
_UsdPimAutoRPCandAutoRPAncmntIntvl_Type = TimeTicks
_UsdPimAutoRPCandAutoRPAncmntIntvl_Object = MibTableColumn
usdPimAutoRPCandAutoRPAncmntIntvl = _UsdPimAutoRPCandAutoRPAncmntIntvl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 8),
    _UsdPimAutoRPCandAutoRPAncmntIntvl_Type()
)
usdPimAutoRPCandAutoRPAncmntIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimAutoRPCandAutoRPAncmntIntvl.setStatus("current")
_UsdPimAutoRPCandIfId_Type = InterfaceIndex
_UsdPimAutoRPCandIfId_Object = MibTableColumn
usdPimAutoRPCandIfId = _UsdPimAutoRPCandIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 17, 1, 9),
    _UsdPimAutoRPCandIfId_Type()
)
usdPimAutoRPCandIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimAutoRPCandIfId.setStatus("current")
_UsdPimComponentTable_Object = MibTable
usdPimComponentTable = _UsdPimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18)
)
if mibBuilder.loadTexts:
    usdPimComponentTable.setStatus("current")
_UsdPimComponentEntry_Object = MibTableRow
usdPimComponentEntry = _UsdPimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1)
)
usdPimComponentEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimComponentIndex"),
)
if mibBuilder.loadTexts:
    usdPimComponentEntry.setStatus("current")


class _UsdPimComponentIndex_Type(Integer32):
    """Custom type usdPimComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPimComponentIndex_Type.__name__ = "Integer32"
_UsdPimComponentIndex_Object = MibTableColumn
usdPimComponentIndex = _UsdPimComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 1),
    _UsdPimComponentIndex_Type()
)
usdPimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimComponentIndex.setStatus("current")
_UsdPimComponentAutoRPMappingAgentRowStatus_Type = RowStatus
_UsdPimComponentAutoRPMappingAgentRowStatus_Object = MibTableColumn
usdPimComponentAutoRPMappingAgentRowStatus = _UsdPimComponentAutoRPMappingAgentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 2),
    _UsdPimComponentAutoRPMappingAgentRowStatus_Type()
)
usdPimComponentAutoRPMappingAgentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimComponentAutoRPMappingAgentRowStatus.setStatus("current")
_UsdPimComponentConfiguredAutoRPMappingAgentIfId_Type = InterfaceIndex
_UsdPimComponentConfiguredAutoRPMappingAgentIfId_Object = MibTableColumn
usdPimComponentConfiguredAutoRPMappingAgentIfId = _UsdPimComponentConfiguredAutoRPMappingAgentIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 3),
    _UsdPimComponentConfiguredAutoRPMappingAgentIfId_Type()
)
usdPimComponentConfiguredAutoRPMappingAgentIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimComponentConfiguredAutoRPMappingAgentIfId.setStatus("current")


class _UsdPimComponentAutoRPMappingAgentInterval_Type(TimeTicks):
    """Custom type usdPimComponentAutoRPMappingAgentInterval based on TimeTicks"""
    defaultValue = 60


_UsdPimComponentAutoRPMappingAgentInterval_Object = MibTableColumn
usdPimComponentAutoRPMappingAgentInterval = _UsdPimComponentAutoRPMappingAgentInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 4),
    _UsdPimComponentAutoRPMappingAgentInterval_Type()
)
usdPimComponentAutoRPMappingAgentInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimComponentAutoRPMappingAgentInterval.setStatus("current")


class _UsdPimComponentAutoRPMappingTTL_Type(Integer32):
    """Custom type usdPimComponentAutoRPMappingTTL based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdPimComponentAutoRPMappingTTL_Type.__name__ = "Integer32"
_UsdPimComponentAutoRPMappingTTL_Object = MibTableColumn
usdPimComponentAutoRPMappingTTL = _UsdPimComponentAutoRPMappingTTL_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 5),
    _UsdPimComponentAutoRPMappingTTL_Type()
)
usdPimComponentAutoRPMappingTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPimComponentAutoRPMappingTTL.setStatus("current")
_UsdPimComponentAutoRPMappingAgentIntfAddr_Type = IpAddress
_UsdPimComponentAutoRPMappingAgentIntfAddr_Object = MibTableColumn
usdPimComponentAutoRPMappingAgentIntfAddr = _UsdPimComponentAutoRPMappingAgentIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 6),
    _UsdPimComponentAutoRPMappingAgentIntfAddr_Type()
)
usdPimComponentAutoRPMappingAgentIntfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimComponentAutoRPMappingAgentIntfAddr.setStatus("current")
_UsdPimComponentAutoRPMappingAgentWinnerAddr_Type = IpAddress
_UsdPimComponentAutoRPMappingAgentWinnerAddr_Object = MibTableColumn
usdPimComponentAutoRPMappingAgentWinnerAddr = _UsdPimComponentAutoRPMappingAgentWinnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 7),
    _UsdPimComponentAutoRPMappingAgentWinnerAddr_Type()
)
usdPimComponentAutoRPMappingAgentWinnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimComponentAutoRPMappingAgentWinnerAddr.setStatus("current")
_UsdPimComponentAutoRPMappingAgentWinnerLastHeard_Type = TimeTicks
_UsdPimComponentAutoRPMappingAgentWinnerLastHeard_Object = MibTableColumn
usdPimComponentAutoRPMappingAgentWinnerLastHeard = _UsdPimComponentAutoRPMappingAgentWinnerLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 18, 1, 8),
    _UsdPimComponentAutoRPMappingAgentWinnerLastHeard_Type()
)
usdPimComponentAutoRPMappingAgentWinnerLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimComponentAutoRPMappingAgentWinnerLastHeard.setStatus("current")
_UsdPimUnicastRouteTable_Object = MibTable
usdPimUnicastRouteTable = _UsdPimUnicastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19)
)
if mibBuilder.loadTexts:
    usdPimUnicastRouteTable.setStatus("current")
_UsdPimUnicastRouteEntry_Object = MibTableRow
usdPimUnicastRouteEntry = _UsdPimUnicastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1)
)
usdPimUnicastRouteEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryAddr"),
    (0, "Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryMask"),
)
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntry.setStatus("current")
_UsdPimUnicastRouteEntryAddr_Type = IpAddress
_UsdPimUnicastRouteEntryAddr_Object = MibTableColumn
usdPimUnicastRouteEntryAddr = _UsdPimUnicastRouteEntryAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 1),
    _UsdPimUnicastRouteEntryAddr_Type()
)
usdPimUnicastRouteEntryAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryAddr.setStatus("current")
_UsdPimUnicastRouteEntryMask_Type = IpAddress
_UsdPimUnicastRouteEntryMask_Object = MibTableColumn
usdPimUnicastRouteEntryMask = _UsdPimUnicastRouteEntryMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 2),
    _UsdPimUnicastRouteEntryMask_Type()
)
usdPimUnicastRouteEntryMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryMask.setStatus("current")
_UsdPimUnicastRouteEntryRpfNbr_Type = IpAddress
_UsdPimUnicastRouteEntryRpfNbr_Object = MibTableColumn
usdPimUnicastRouteEntryRpfNbr = _UsdPimUnicastRouteEntryRpfNbr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 3),
    _UsdPimUnicastRouteEntryRpfNbr_Type()
)
usdPimUnicastRouteEntryRpfNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryRpfNbr.setStatus("current")
_UsdPimUnicastRouteEntryIifId_Type = InterfaceIndex
_UsdPimUnicastRouteEntryIifId_Object = MibTableColumn
usdPimUnicastRouteEntryIifId = _UsdPimUnicastRouteEntryIifId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 4),
    _UsdPimUnicastRouteEntryIifId_Type()
)
usdPimUnicastRouteEntryIifId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryIifId.setStatus("current")
_UsdPimUnicastRouteEntryIifAddr_Type = IpAddress
_UsdPimUnicastRouteEntryIifAddr_Object = MibTableColumn
usdPimUnicastRouteEntryIifAddr = _UsdPimUnicastRouteEntryIifAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 5),
    _UsdPimUnicastRouteEntryIifAddr_Type()
)
usdPimUnicastRouteEntryIifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryIifAddr.setStatus("current")
_UsdPimUnicastRouteEntryPref_Type = Integer32
_UsdPimUnicastRouteEntryPref_Object = MibTableColumn
usdPimUnicastRouteEntryPref = _UsdPimUnicastRouteEntryPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 6),
    _UsdPimUnicastRouteEntryPref_Type()
)
usdPimUnicastRouteEntryPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryPref.setStatus("current")
_UsdPimUnicastRouteEntryMetric_Type = Integer32
_UsdPimUnicastRouteEntryMetric_Object = MibTableColumn
usdPimUnicastRouteEntryMetric = _UsdPimUnicastRouteEntryMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 7),
    _UsdPimUnicastRouteEntryMetric_Type()
)
usdPimUnicastRouteEntryMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryMetric.setStatus("current")
_UsdPimUnicastRouteEntryPimType_Type = UsdPimType
_UsdPimUnicastRouteEntryPimType_Object = MibTableColumn
usdPimUnicastRouteEntryPimType = _UsdPimUnicastRouteEntryPimType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 19, 1, 8),
    _UsdPimUnicastRouteEntryPimType_Type()
)
usdPimUnicastRouteEntryPimType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPimUnicastRouteEntryPimType.setStatus("current")
_UsdPimSPTThresholdTable_Object = MibTable
usdPimSPTThresholdTable = _UsdPimSPTThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20)
)
if mibBuilder.loadTexts:
    usdPimSPTThresholdTable.setStatus("current")
_UsdPimSPTThresholdEntry_Object = MibTableRow
usdPimSPTThresholdEntry = _UsdPimSPTThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1)
)
usdPimSPTThresholdEntry.setIndexNames(
    (0, "Unisphere-Data-PIM-MIB", "usdPimSPTThresholdAccessListName"),
)
if mibBuilder.loadTexts:
    usdPimSPTThresholdEntry.setStatus("current")


class _UsdPimSPTThresholdAccessListName_Type(OctetString):
    """Custom type usdPimSPTThresholdAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdPimSPTThresholdAccessListName_Type.__name__ = "OctetString"
_UsdPimSPTThresholdAccessListName_Object = MibTableColumn
usdPimSPTThresholdAccessListName = _UsdPimSPTThresholdAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1, 1),
    _UsdPimSPTThresholdAccessListName_Type()
)
usdPimSPTThresholdAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPimSPTThresholdAccessListName.setStatus("current")
_UsdPimSPTThresHoldRowStatus_Type = RowStatus
_UsdPimSPTThresHoldRowStatus_Object = MibTableColumn
usdPimSPTThresHoldRowStatus = _UsdPimSPTThresHoldRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1, 2),
    _UsdPimSPTThresHoldRowStatus_Type()
)
usdPimSPTThresHoldRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimSPTThresHoldRowStatus.setStatus("current")


class _UsdPimSPTThresholdKbps_Type(Integer32):
    """Custom type usdPimSPTThresholdKbps based on Integer32"""
    defaultValue = 0


_UsdPimSPTThresholdKbps_Object = MibTableColumn
usdPimSPTThresholdKbps = _UsdPimSPTThresholdKbps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 1, 1, 20, 1, 3),
    _UsdPimSPTThresholdKbps_Type()
)
usdPimSPTThresholdKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPimSPTThresholdKbps.setStatus("current")
_UsdPimConformance_ObjectIdentity = ObjectIdentity
usdPimConformance = _UsdPimConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2)
)
_UsdPimCompliances_ObjectIdentity = ObjectIdentity
usdPimCompliances = _UsdPimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 1)
)
_UsdPimGroups_ObjectIdentity = ObjectIdentity
usdPimGroups = _UsdPimGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2)
)

# Managed Objects groups

usdPimGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 1)
)
usdPimGeneralGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimNumHelloRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumJoinPruneRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumAssertRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumGraftRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumGraftAckRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumHelloSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumJoinPruneSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumAssertSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumGraftSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimNumGraftAckSent"))
)
if mibBuilder.loadTexts:
    usdPimGeneralGroup.setStatus("current")

usdPimInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 2)
)
usdPimInterfaceGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimIntfNumHelloRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumJoinPruneRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumAssertRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumGraftRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumGraftAckRcvd"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumHelloSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumJoinPruneSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumAssertSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumGraftSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumGraftAckSent"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfVersion"),
        ("Unisphere-Data-PIM-MIB", "usdPimIntfNumNbrs"))
)
if mibBuilder.loadTexts:
    usdPimInterfaceGroup.setStatus("current")

usdPimMRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 3)
)
usdPimMRouteConfGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimMRouteUpstreamAssertTimer"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteAssertMetric"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteAssertPref"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteAssertRPTBit"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteBits"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteRPAddrInUse"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteUpstreamNbr"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteIifAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteIsWaitingToSwitchToSPT"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteEntryExpiryTimer"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteSenderDRAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteRouteAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteRouteMask"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteGRPAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteGRPMask"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteOtherProtoOifJoinTypeAll"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteOtherProtoOifJoinTypeG"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteOtherProtoOifJoinTypeSG"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRoutePimType"))
)
if mibBuilder.loadTexts:
    usdPimMRouteConfGroup.setStatus("current")

usdPimMRouteNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 4)
)
usdPimMRouteNextHopGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopPruneReason"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopJoinTypeSSRP"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopJoinTypeG"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopJoinTypeSG"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopHasLGM"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopHasOifAW"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopHasOifSendAssert"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopHasOifRegister"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopHasOifBorderBit"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopHasOifNullEncapsBit"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopJoinEndTimer"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopAssertEndTimer"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopNextAssertTimer"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopAssertSrcAddress"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopRegisterSuppressionTimer"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopPimType"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopPruneTimeLeft"),
        ("Unisphere-Data-PIM-MIB", "usdPimMRouteNextHopsendingIpAddress"))
)
if mibBuilder.loadTexts:
    usdPimMRouteNextHopGroup.setStatus("current")

usdPimRPSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 5)
)
usdPimRPSetGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimRPSetPriority"),
        ("Unisphere-Data-PIM-MIB", "usdPimRPSetTypeInfo"),
        ("Unisphere-Data-PIM-MIB", "usdPimRPSetAccessListName"))
)
if mibBuilder.loadTexts:
    usdPimRPSetGroup.setStatus("current")

usdPimStaticRPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 6)
)
usdPimStaticRPConfGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimStaticRPConfRowStatus"),
        ("Unisphere-Data-PIM-MIB", "usdPimStaticRPConfOverride"))
)
if mibBuilder.loadTexts:
    usdPimStaticRPConfGroup.setStatus("current")

usdPimAutoRPConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 7)
)
usdPimAutoRPConfGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimAutoRPConfRowStatus"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPConfTTL"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPConfAncmntIntvl"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPConfifId"))
)
if mibBuilder.loadTexts:
    usdPimAutoRPConfGroup.setStatus("current")

usdPimAutoRPCandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 8)
)
usdPimAutoRPCandGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimAutoRPCandRowStatus"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPCandAccessListName"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPCandAutoRPTTL"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPCandAutoRPAncmntIntvl"),
        ("Unisphere-Data-PIM-MIB", "usdPimAutoRPCandIfId"))
)
if mibBuilder.loadTexts:
    usdPimAutoRPCandGroup.setStatus("current")

usdPimComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 9)
)
usdPimComponentGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimComponentAutoRPMappingAgentRowStatus"),
        ("Unisphere-Data-PIM-MIB", "usdPimComponentConfiguredAutoRPMappingAgentIfId"),
        ("Unisphere-Data-PIM-MIB", "usdPimComponentAutoRPMappingAgentInterval"),
        ("Unisphere-Data-PIM-MIB", "usdPimComponentAutoRPMappingTTL"),
        ("Unisphere-Data-PIM-MIB", "usdPimComponentAutoRPMappingAgentIntfAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimComponentAutoRPMappingAgentWinnerAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimComponentAutoRPMappingAgentWinnerLastHeard"))
)
if mibBuilder.loadTexts:
    usdPimComponentGroup.setStatus("current")

usdPimUnicastRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 10)
)
usdPimUnicastRouteGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryRpfNbr"),
        ("Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryIifId"),
        ("Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryIifAddr"),
        ("Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryPref"),
        ("Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryMetric"),
        ("Unisphere-Data-PIM-MIB", "usdPimUnicastRouteEntryPimType"))
)
if mibBuilder.loadTexts:
    usdPimUnicastRouteGroup.setStatus("current")

usdPimSPTThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 2, 11)
)
usdPimSPTThresholdGroup.setObjects(
      *(("Unisphere-Data-PIM-MIB", "usdPimSPTThresHoldRowStatus"),
        ("Unisphere-Data-PIM-MIB", "usdPimSPTThresholdKbps"))
)
if mibBuilder.loadTexts:
    usdPimSPTThresholdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdPimCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 43, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdPimCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PIM-MIB",
    **{"UsdPimType": UsdPimType,
       "usdPimMIB": usdPimMIB,
       "usdPimMIBObjects": usdPimMIBObjects,
       "usdPimTraps": usdPimTraps,
       "usdPimGlobal": usdPimGlobal,
       "usdPimNumHelloRcvd": usdPimNumHelloRcvd,
       "usdPimNumJoinPruneRcvd": usdPimNumJoinPruneRcvd,
       "usdPimNumAssertRcvd": usdPimNumAssertRcvd,
       "usdPimNumGraftRcvd": usdPimNumGraftRcvd,
       "usdPimNumGraftAckRcvd": usdPimNumGraftAckRcvd,
       "usdPimNumHelloSent": usdPimNumHelloSent,
       "usdPimNumJoinPruneSent": usdPimNumJoinPruneSent,
       "usdPimNumAssertSent": usdPimNumAssertSent,
       "usdPimNumGraftSent": usdPimNumGraftSent,
       "usdPimNumGraftAckSent": usdPimNumGraftAckSent,
       "usdPimInterfaceTable": usdPimInterfaceTable,
       "usdPimInterfaceEntry": usdPimInterfaceEntry,
       "usdPimIntfNumHelloRcvd": usdPimIntfNumHelloRcvd,
       "usdPimIntfNumJoinPruneRcvd": usdPimIntfNumJoinPruneRcvd,
       "usdPimIntfNumAssertRcvd": usdPimIntfNumAssertRcvd,
       "usdPimIntfNumGraftRcvd": usdPimIntfNumGraftRcvd,
       "usdPimIntfNumGraftAckRcvd": usdPimIntfNumGraftAckRcvd,
       "usdPimIntfNumHelloSent": usdPimIntfNumHelloSent,
       "usdPimIntfNumJoinPruneSent": usdPimIntfNumJoinPruneSent,
       "usdPimIntfNumAssertSent": usdPimIntfNumAssertSent,
       "usdPimIntfNumGraftSent": usdPimIntfNumGraftSent,
       "usdPimIntfNumGraftAckSent": usdPimIntfNumGraftAckSent,
       "usdPimIntfVersion": usdPimIntfVersion,
       "usdPimIntfNumNbrs": usdPimIntfNumNbrs,
       "usdPimMRouteTable": usdPimMRouteTable,
       "usdPimMRouteEntry": usdPimMRouteEntry,
       "usdPimMRouteGroup": usdPimMRouteGroup,
       "usdPimMRouteSource": usdPimMRouteSource,
       "usdPimMRouteSourceMask": usdPimMRouteSourceMask,
       "usdPimMRouteRPAddress": usdPimMRouteRPAddress,
       "usdPimMRouteUpstreamAssertTimer": usdPimMRouteUpstreamAssertTimer,
       "usdPimMRouteAssertMetric": usdPimMRouteAssertMetric,
       "usdPimMRouteAssertPref": usdPimMRouteAssertPref,
       "usdPimMRouteAssertRPTBit": usdPimMRouteAssertRPTBit,
       "usdPimMRouteBits": usdPimMRouteBits,
       "usdPimMRouteRPAddrInUse": usdPimMRouteRPAddrInUse,
       "usdPimMRouteUpstreamNbr": usdPimMRouteUpstreamNbr,
       "usdPimMRouteIifAddr": usdPimMRouteIifAddr,
       "usdPimMRouteIsWaitingToSwitchToSPT": usdPimMRouteIsWaitingToSwitchToSPT,
       "usdPimMRouteEntryExpiryTimer": usdPimMRouteEntryExpiryTimer,
       "usdPimMRouteSenderDRAddr": usdPimMRouteSenderDRAddr,
       "usdPimMRouteRouteAddr": usdPimMRouteRouteAddr,
       "usdPimMRouteRouteMask": usdPimMRouteRouteMask,
       "usdPimMRouteGRPAddr": usdPimMRouteGRPAddr,
       "usdPimMRouteGRPMask": usdPimMRouteGRPMask,
       "usdPimMRouteOtherProtoOifJoinTypeAll": usdPimMRouteOtherProtoOifJoinTypeAll,
       "usdPimMRouteOtherProtoOifJoinTypeG": usdPimMRouteOtherProtoOifJoinTypeG,
       "usdPimMRouteOtherProtoOifJoinTypeSG": usdPimMRouteOtherProtoOifJoinTypeSG,
       "usdPimMRoutePimType": usdPimMRoutePimType,
       "usdPimMRouteNextHopTable": usdPimMRouteNextHopTable,
       "usdPimMRouteNextHopEntry": usdPimMRouteNextHopEntry,
       "usdPimMRouteNextHopGroupAddr": usdPimMRouteNextHopGroupAddr,
       "usdPimMRouteNextHopSrcAddr": usdPimMRouteNextHopSrcAddr,
       "usdPimMRouteNextHopSrcMask": usdPimMRouteNextHopSrcMask,
       "usdPimMRouteNextHopRPAddr": usdPimMRouteNextHopRPAddr,
       "usdPimMRouteNextHopIfId": usdPimMRouteNextHopIfId,
       "usdPimMRouteNextHopAddress": usdPimMRouteNextHopAddress,
       "usdPimMRouteNextHopPruneReason": usdPimMRouteNextHopPruneReason,
       "usdPimMRouteNextHopJoinTypeSSRP": usdPimMRouteNextHopJoinTypeSSRP,
       "usdPimMRouteNextHopJoinTypeG": usdPimMRouteNextHopJoinTypeG,
       "usdPimMRouteNextHopJoinTypeSG": usdPimMRouteNextHopJoinTypeSG,
       "usdPimMRouteNextHopHasLGM": usdPimMRouteNextHopHasLGM,
       "usdPimMRouteNextHopHasOifAW": usdPimMRouteNextHopHasOifAW,
       "usdPimMRouteNextHopHasOifSendAssert": usdPimMRouteNextHopHasOifSendAssert,
       "usdPimMRouteNextHopHasOifRegister": usdPimMRouteNextHopHasOifRegister,
       "usdPimMRouteNextHopHasOifBorderBit": usdPimMRouteNextHopHasOifBorderBit,
       "usdPimMRouteNextHopHasOifNullEncapsBit": usdPimMRouteNextHopHasOifNullEncapsBit,
       "usdPimMRouteNextHopJoinEndTimer": usdPimMRouteNextHopJoinEndTimer,
       "usdPimMRouteNextHopAssertEndTimer": usdPimMRouteNextHopAssertEndTimer,
       "usdPimMRouteNextHopNextAssertTimer": usdPimMRouteNextHopNextAssertTimer,
       "usdPimMRouteNextHopAssertSrcAddress": usdPimMRouteNextHopAssertSrcAddress,
       "usdPimMRouteNextHopRegisterSuppressionTimer": usdPimMRouteNextHopRegisterSuppressionTimer,
       "usdPimMRouteNextHopPimType": usdPimMRouteNextHopPimType,
       "usdPimMRouteNextHopPruneTimeLeft": usdPimMRouteNextHopPruneTimeLeft,
       "usdPimMRouteNextHopsendingIpAddress": usdPimMRouteNextHopsendingIpAddress,
       "usdPimRPSetTable": usdPimRPSetTable,
       "usdPimRPSetEntry": usdPimRPSetEntry,
       "usdPimRPSetPriority": usdPimRPSetPriority,
       "usdPimRPSetTypeInfo": usdPimRPSetTypeInfo,
       "usdPimRPSetAccessListName": usdPimRPSetAccessListName,
       "usdPimStaticRPConfTable": usdPimStaticRPConfTable,
       "usdPimStaticRPConfEntry": usdPimStaticRPConfEntry,
       "usdPimStaticRPConfComponentIndex": usdPimStaticRPConfComponentIndex,
       "usdPimStaticRPConfRPAddr": usdPimStaticRPConfRPAddr,
       "usdPimStaticRPConfAccessListName": usdPimStaticRPConfAccessListName,
       "usdPimStaticRPConfRowStatus": usdPimStaticRPConfRowStatus,
       "usdPimStaticRPConfOverride": usdPimStaticRPConfOverride,
       "usdPimAutoRPConfTable": usdPimAutoRPConfTable,
       "usdPimAutoRPConfEntry": usdPimAutoRPConfEntry,
       "usdPimAutoRPConfComponentIndex": usdPimAutoRPConfComponentIndex,
       "usdPimAutoRPConfCandRPAddr": usdPimAutoRPConfCandRPAddr,
       "usdPimAutoRPConfGroupAccessListName": usdPimAutoRPConfGroupAccessListName,
       "usdPimAutoRPConfRowStatus": usdPimAutoRPConfRowStatus,
       "usdPimAutoRPConfTTL": usdPimAutoRPConfTTL,
       "usdPimAutoRPConfAncmntIntvl": usdPimAutoRPConfAncmntIntvl,
       "usdPimAutoRPConfifId": usdPimAutoRPConfifId,
       "usdPimAutoRPCandTable": usdPimAutoRPCandTable,
       "usdPimAutoRPCandEntry": usdPimAutoRPCandEntry,
       "usdPimAutoRPCandComponentIndex": usdPimAutoRPCandComponentIndex,
       "usdPimAutoRPCandRPAddr": usdPimAutoRPCandRPAddr,
       "usdPimAutoRPCandGroupAddr": usdPimAutoRPCandGroupAddr,
       "usdPimAutoRPCandGroupMask": usdPimAutoRPCandGroupMask,
       "usdPimAutoRPCandRowStatus": usdPimAutoRPCandRowStatus,
       "usdPimAutoRPCandAccessListName": usdPimAutoRPCandAccessListName,
       "usdPimAutoRPCandAutoRPTTL": usdPimAutoRPCandAutoRPTTL,
       "usdPimAutoRPCandAutoRPAncmntIntvl": usdPimAutoRPCandAutoRPAncmntIntvl,
       "usdPimAutoRPCandIfId": usdPimAutoRPCandIfId,
       "usdPimComponentTable": usdPimComponentTable,
       "usdPimComponentEntry": usdPimComponentEntry,
       "usdPimComponentIndex": usdPimComponentIndex,
       "usdPimComponentAutoRPMappingAgentRowStatus": usdPimComponentAutoRPMappingAgentRowStatus,
       "usdPimComponentConfiguredAutoRPMappingAgentIfId": usdPimComponentConfiguredAutoRPMappingAgentIfId,
       "usdPimComponentAutoRPMappingAgentInterval": usdPimComponentAutoRPMappingAgentInterval,
       "usdPimComponentAutoRPMappingTTL": usdPimComponentAutoRPMappingTTL,
       "usdPimComponentAutoRPMappingAgentIntfAddr": usdPimComponentAutoRPMappingAgentIntfAddr,
       "usdPimComponentAutoRPMappingAgentWinnerAddr": usdPimComponentAutoRPMappingAgentWinnerAddr,
       "usdPimComponentAutoRPMappingAgentWinnerLastHeard": usdPimComponentAutoRPMappingAgentWinnerLastHeard,
       "usdPimUnicastRouteTable": usdPimUnicastRouteTable,
       "usdPimUnicastRouteEntry": usdPimUnicastRouteEntry,
       "usdPimUnicastRouteEntryAddr": usdPimUnicastRouteEntryAddr,
       "usdPimUnicastRouteEntryMask": usdPimUnicastRouteEntryMask,
       "usdPimUnicastRouteEntryRpfNbr": usdPimUnicastRouteEntryRpfNbr,
       "usdPimUnicastRouteEntryIifId": usdPimUnicastRouteEntryIifId,
       "usdPimUnicastRouteEntryIifAddr": usdPimUnicastRouteEntryIifAddr,
       "usdPimUnicastRouteEntryPref": usdPimUnicastRouteEntryPref,
       "usdPimUnicastRouteEntryMetric": usdPimUnicastRouteEntryMetric,
       "usdPimUnicastRouteEntryPimType": usdPimUnicastRouteEntryPimType,
       "usdPimSPTThresholdTable": usdPimSPTThresholdTable,
       "usdPimSPTThresholdEntry": usdPimSPTThresholdEntry,
       "usdPimSPTThresholdAccessListName": usdPimSPTThresholdAccessListName,
       "usdPimSPTThresHoldRowStatus": usdPimSPTThresHoldRowStatus,
       "usdPimSPTThresholdKbps": usdPimSPTThresholdKbps,
       "usdPimConformance": usdPimConformance,
       "usdPimCompliances": usdPimCompliances,
       "usdPimCompliance": usdPimCompliance,
       "usdPimGroups": usdPimGroups,
       "usdPimGeneralGroup": usdPimGeneralGroup,
       "usdPimInterfaceGroup": usdPimInterfaceGroup,
       "usdPimMRouteConfGroup": usdPimMRouteConfGroup,
       "usdPimMRouteNextHopGroup": usdPimMRouteNextHopGroup,
       "usdPimRPSetGroup": usdPimRPSetGroup,
       "usdPimStaticRPConfGroup": usdPimStaticRPConfGroup,
       "usdPimAutoRPConfGroup": usdPimAutoRPConfGroup,
       "usdPimAutoRPCandGroup": usdPimAutoRPCandGroup,
       "usdPimComponentGroup": usdPimComponentGroup,
       "usdPimUnicastRouteGroup": usdPimUnicastRouteGroup,
       "usdPimSPTThresholdGroup": usdPimSPTThresholdGroup}
)
