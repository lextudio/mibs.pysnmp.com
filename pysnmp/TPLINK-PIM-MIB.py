# SNMP MIB module (TPLINK-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:27 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77)
)
tplinkPimMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPimMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPimMIBObjects = _TplinkPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1)
)
_TpPim_ObjectIdentity = ObjectIdentity
tpPim = _TpPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1)
)


class _TpSGExpiryTimer_Type(Integer32):
    """Custom type tpSGExpiryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_TpSGExpiryTimer_Type.__name__ = "Integer32"
_TpSGExpiryTimer_Object = MibScalar
tpSGExpiryTimer = _TpSGExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 1),
    _TpSGExpiryTimer_Type()
)
tpSGExpiryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSGExpiryTimer.setStatus("current")
if mibBuilder.loadTexts:
    tpSGExpiryTimer.setUnits("seconds")


class _TpPimdataThresholdRate_Type(Integer32):
    """Custom type tpPimdataThresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("infinity", 1),
          ("zero", 0))
    )


_TpPimdataThresholdRate_Type.__name__ = "Integer32"
_TpPimdataThresholdRate_Object = MibScalar
tpPimdataThresholdRate = _TpPimdataThresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 2),
    _TpPimdataThresholdRate_Type()
)
tpPimdataThresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimdataThresholdRate.setStatus("current")
if mibBuilder.loadTexts:
    tpPimdataThresholdRate.setUnits("seconds")
_TpPimInterfaceTable_Object = MibTable
tpPimInterfaceTable = _TpPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tpPimInterfaceTable.setStatus("current")
_TpPimInterfaceEntry_Object = MibTableRow
tpPimInterfaceEntry = _TpPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1)
)
tpPimInterfaceEntry.setIndexNames(
    (0, "TPLINK-PIM-MIB", "tpPimInterfaceIndex"),
)
if mibBuilder.loadTexts:
    tpPimInterfaceEntry.setStatus("current")


class _TpPimInterface_Type(OctetString):
    """Custom type tpPimInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpPimInterface_Type.__name__ = "OctetString"
_TpPimInterface_Object = MibTableColumn
tpPimInterface = _TpPimInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 1),
    _TpPimInterface_Type()
)
tpPimInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimInterface.setStatus("current")
_TpPimInterfaceIndex_Type = Integer32
_TpPimInterfaceIndex_Object = MibTableColumn
tpPimInterfaceIndex = _TpPimInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 2),
    _TpPimInterfaceIndex_Type()
)
tpPimInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimInterfaceIndex.setStatus("current")


class _TpPimInterfaceType_Type(Integer32):
    """Custom type tpPimInterfaceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("routeport", 2),
          ("vlan", 0))
    )


_TpPimInterfaceType_Type.__name__ = "Integer32"
_TpPimInterfaceType_Object = MibTableColumn
tpPimInterfaceType = _TpPimInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 3),
    _TpPimInterfaceType_Type()
)
tpPimInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimInterfaceType.setStatus("current")
_TpPimInterfaceAddress_Type = IpAddress
_TpPimInterfaceAddress_Object = MibTableColumn
tpPimInterfaceAddress = _TpPimInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 4),
    _TpPimInterfaceAddress_Type()
)
tpPimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimInterfaceAddress.setStatus("current")
_TpPimInterfaceNetMask_Type = IpAddress
_TpPimInterfaceNetMask_Object = MibTableColumn
tpPimInterfaceNetMask = _TpPimInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 5),
    _TpPimInterfaceNetMask_Type()
)
tpPimInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimInterfaceNetMask.setStatus("current")


class _TpPimInterfaceMode_Type(Integer32):
    """Custom type tpPimInterfaceMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("disable", 0),
          ("sparse", 2))
    )


_TpPimInterfaceMode_Type.__name__ = "Integer32"
_TpPimInterfaceMode_Object = MibTableColumn
tpPimInterfaceMode = _TpPimInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 6),
    _TpPimInterfaceMode_Type()
)
tpPimInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimInterfaceMode.setStatus("current")


class _TpPimInterfaceDRPriority_Type(Integer32):
    """Custom type tpPimInterfaceDRPriority based on Integer32"""
    defaultValue = 1


_TpPimInterfaceDRPriority_Object = MibTableColumn
tpPimInterfaceDRPriority = _TpPimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 7),
    _TpPimInterfaceDRPriority_Type()
)
tpPimInterfaceDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimInterfaceDRPriority.setStatus("current")
_TpPimInterfaceDRAddress_Type = IpAddress
_TpPimInterfaceDRAddress_Object = MibTableColumn
tpPimInterfaceDRAddress = _TpPimInterfaceDRAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 8),
    _TpPimInterfaceDRAddress_Type()
)
tpPimInterfaceDRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimInterfaceDRAddress.setStatus("current")


class _TpPimInterfaceHelloInterval_Type(Integer32):
    """Custom type tpPimInterfaceHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18725),
    )


_TpPimInterfaceHelloInterval_Type.__name__ = "Integer32"
_TpPimInterfaceHelloInterval_Object = MibTableColumn
tpPimInterfaceHelloInterval = _TpPimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 9),
    _TpPimInterfaceHelloInterval_Type()
)
tpPimInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tpPimInterfaceHelloInterval.setUnits("seconds")


class _TpPimInterfaceBsrBorder_Type(Integer32):
    """Custom type tpPimInterfaceBsrBorder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPimInterfaceBsrBorder_Type.__name__ = "Integer32"
_TpPimInterfaceBsrBorder_Object = MibTableColumn
tpPimInterfaceBsrBorder = _TpPimInterfaceBsrBorder_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 10),
    _TpPimInterfaceBsrBorder_Type()
)
tpPimInterfaceBsrBorder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimInterfaceBsrBorder.setStatus("current")


class _TpPimInterfaceJoinPruneInterval_Type(Integer32):
    """Custom type tpPimInterfaceJoinPruneInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18724),
    )


_TpPimInterfaceJoinPruneInterval_Type.__name__ = "Integer32"
_TpPimInterfaceJoinPruneInterval_Object = MibTableColumn
tpPimInterfaceJoinPruneInterval = _TpPimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 3, 1, 11),
    _TpPimInterfaceJoinPruneInterval_Type()
)
tpPimInterfaceJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    tpPimInterfaceJoinPruneInterval.setUnits("seconds")
_TpPimNeighborTable_Object = MibTable
tpPimNeighborTable = _TpPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tpPimNeighborTable.setStatus("current")
_TpPimNeighborEntry_Object = MibTableRow
tpPimNeighborEntry = _TpPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1)
)
tpPimNeighborEntry.setIndexNames(
    (0, "TPLINK-PIM-MIB", "tpPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    tpPimNeighborEntry.setStatus("current")


class _TpPimNeighborInterface_Type(OctetString):
    """Custom type tpPimNeighborInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpPimNeighborInterface_Type.__name__ = "OctetString"
_TpPimNeighborInterface_Object = MibTableColumn
tpPimNeighborInterface = _TpPimNeighborInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 1),
    _TpPimNeighborInterface_Type()
)
tpPimNeighborInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimNeighborInterface.setStatus("current")
_TpPimNeighborInterfaceIndex_Type = Integer32
_TpPimNeighborInterfaceIndex_Object = MibTableColumn
tpPimNeighborInterfaceIndex = _TpPimNeighborInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 2),
    _TpPimNeighborInterfaceIndex_Type()
)
tpPimNeighborInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimNeighborInterfaceIndex.setStatus("current")
_TpPimNeighborAddress_Type = IpAddress
_TpPimNeighborAddress_Object = MibTableColumn
tpPimNeighborAddress = _TpPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 3),
    _TpPimNeighborAddress_Type()
)
tpPimNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimNeighborAddress.setStatus("current")
_TpPimNeighborUpTime_Type = TimeTicks
_TpPimNeighborUpTime_Object = MibTableColumn
tpPimNeighborUpTime = _TpPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 4),
    _TpPimNeighborUpTime_Type()
)
tpPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimNeighborUpTime.setStatus("current")
_TpPimNeighborExpiryTime_Type = TimeTicks
_TpPimNeighborExpiryTime_Object = MibTableColumn
tpPimNeighborExpiryTime = _TpPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 5),
    _TpPimNeighborExpiryTime_Type()
)
tpPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimNeighborExpiryTime.setStatus("current")


class _TpPimNeighborMode_Type(Integer32):
    """Custom type tpPimNeighborMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_TpPimNeighborMode_Type.__name__ = "Integer32"
_TpPimNeighborMode_Object = MibTableColumn
tpPimNeighborMode = _TpPimNeighborMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 4, 1, 6),
    _TpPimNeighborMode_Type()
)
tpPimNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimNeighborMode.setStatus("deprecated")
_TpPimCandidateBSRSet_ObjectIdentity = ObjectIdentity
tpPimCandidateBSRSet = _TpPimCandidateBSRSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5)
)


class _TpPimCBSRInterface_Type(OctetString):
    """Custom type tpPimCBSRInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpPimCBSRInterface_Type.__name__ = "OctetString"
_TpPimCBSRInterface_Object = MibScalar
tpPimCBSRInterface = _TpPimCBSRInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 1),
    _TpPimCBSRInterface_Type()
)
tpPimCBSRInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimCBSRInterface.setStatus("current")
_TpPimCBSRInterfaceIndex_Type = Integer32
_TpPimCBSRInterfaceIndex_Object = MibScalar
tpPimCBSRInterfaceIndex = _TpPimCBSRInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 2),
    _TpPimCBSRInterfaceIndex_Type()
)
tpPimCBSRInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCBSRInterfaceIndex.setStatus("current")


class _TpPimCBSRHashMaskLength_Type(Integer32):
    """Custom type tpPimCBSRHashMaskLength based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TpPimCBSRHashMaskLength_Type.__name__ = "Integer32"
_TpPimCBSRHashMaskLength_Object = MibScalar
tpPimCBSRHashMaskLength = _TpPimCBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 3),
    _TpPimCBSRHashMaskLength_Type()
)
tpPimCBSRHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCBSRHashMaskLength.setStatus("current")


class _TpPimCBSRPriority_Type(Integer32):
    """Custom type tpPimCBSRPriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TpPimCBSRPriority_Type.__name__ = "Integer32"
_TpPimCBSRPriority_Object = MibScalar
tpPimCBSRPriority = _TpPimCBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 5, 4),
    _TpPimCBSRPriority_Type()
)
tpPimCBSRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCBSRPriority.setStatus("current")
_TpPimStaticRpSet_ObjectIdentity = ObjectIdentity
tpPimStaticRpSet = _TpPimStaticRpSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 6)
)
_TpPimStaticRpAddress_Type = IpAddress
_TpPimStaticRpAddress_Object = MibScalar
tpPimStaticRpAddress = _TpPimStaticRpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 6, 1),
    _TpPimStaticRpAddress_Type()
)
tpPimStaticRpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimStaticRpAddress.setStatus("current")


class _TpPimStaticRpOverride_Type(Integer32):
    """Custom type tpPimStaticRpOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPimStaticRpOverride_Type.__name__ = "Integer32"
_TpPimStaticRpOverride_Object = MibScalar
tpPimStaticRpOverride = _TpPimStaticRpOverride_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 6, 2),
    _TpPimStaticRpOverride_Type()
)
tpPimStaticRpOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimStaticRpOverride.setStatus("current")
_TpPimCandidateRPSetTable_Object = MibTable
tpPimCandidateRPSetTable = _TpPimCandidateRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tpPimCandidateRPSetTable.setStatus("current")
_TpPimCandidateRPSetEntry_Object = MibTableRow
tpPimCandidateRPSetEntry = _TpPimCandidateRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1)
)
tpPimCandidateRPSetEntry.setIndexNames(
    (0, "TPLINK-PIM-MIB", "tpPimCRPSetInterfaceIndex"),
)
if mibBuilder.loadTexts:
    tpPimCandidateRPSetEntry.setStatus("current")


class _TpPimCRPSetInterface_Type(OctetString):
    """Custom type tpPimCRPSetInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TpPimCRPSetInterface_Type.__name__ = "OctetString"
_TpPimCRPSetInterface_Object = MibTableColumn
tpPimCRPSetInterface = _TpPimCRPSetInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 1),
    _TpPimCRPSetInterface_Type()
)
tpPimCRPSetInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimCRPSetInterface.setStatus("current")
_TpPimCRPSetInterfaceIndex_Type = Integer32
_TpPimCRPSetInterfaceIndex_Object = MibTableColumn
tpPimCRPSetInterfaceIndex = _TpPimCRPSetInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 2),
    _TpPimCRPSetInterfaceIndex_Type()
)
tpPimCRPSetInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCRPSetInterfaceIndex.setStatus("current")


class _TpPimCRPSetInterfaceType_Type(Integer32):
    """Custom type tpPimCRPSetInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("routeport", 2),
          ("vlan", 0))
    )


_TpPimCRPSetInterfaceType_Type.__name__ = "Integer32"
_TpPimCRPSetInterfaceType_Object = MibTableColumn
tpPimCRPSetInterfaceType = _TpPimCRPSetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 3),
    _TpPimCRPSetInterfaceType_Type()
)
tpPimCRPSetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimCRPSetInterfaceType.setStatus("deprecated")


class _TpPimCRPSetPriority_Type(Integer32):
    """Custom type tpPimCRPSetPriority based on Integer32"""
    defaultValue = 192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TpPimCRPSetPriority_Type.__name__ = "Integer32"
_TpPimCRPSetPriority_Object = MibTableColumn
tpPimCRPSetPriority = _TpPimCRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 4),
    _TpPimCRPSetPriority_Type()
)
tpPimCRPSetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCRPSetPriority.setStatus("current")


class _TpPimCRPSetInterVal_Type(Integer32):
    """Custom type tpPimCRPSetInterVal based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpPimCRPSetInterVal_Type.__name__ = "Integer32"
_TpPimCRPSetInterVal_Object = MibTableColumn
tpPimCRPSetInterVal = _TpPimCRPSetInterVal_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 5),
    _TpPimCRPSetInterVal_Type()
)
tpPimCRPSetInterVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCRPSetInterVal.setStatus("current")
_TpPimCRPSetNextAdvertisementTime_Type = TimeTicks
_TpPimCRPSetNextAdvertisementTime_Object = MibTableColumn
tpPimCRPSetNextAdvertisementTime = _TpPimCRPSetNextAdvertisementTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 6),
    _TpPimCRPSetNextAdvertisementTime_Type()
)
tpPimCRPSetNextAdvertisementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimCRPSetNextAdvertisementTime.setStatus("current")


class _TpPimCRPSetInterfaceStatus_Type(Integer32):
    """Custom type tpPimCRPSetInterfaceStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpPimCRPSetInterfaceStatus_Type.__name__ = "Integer32"
_TpPimCRPSetInterfaceStatus_Object = MibTableColumn
tpPimCRPSetInterfaceStatus = _TpPimCRPSetInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 7, 1, 7),
    _TpPimCRPSetInterfaceStatus_Type()
)
tpPimCRPSetInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpPimCRPSetInterfaceStatus.setStatus("deprecated")
_TpPimRPMappingTable_Object = MibTable
tpPimRPMappingTable = _TpPimRPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tpPimRPMappingTable.setStatus("deprecated")
_TpPimRPMappingEntry_Object = MibTableRow
tpPimRPMappingEntry = _TpPimRPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1)
)
tpPimRPMappingEntry.setIndexNames(
    (0, "TPLINK-PIM-MIB", "tpPimRPGroupAddress"),
    (0, "TPLINK-PIM-MIB", "tpPimRPAddress"),
)
if mibBuilder.loadTexts:
    tpPimRPMappingEntry.setStatus("deprecated")
_TpPimRPGroupAddress_Type = IpAddress
_TpPimRPGroupAddress_Object = MibTableColumn
tpPimRPGroupAddress = _TpPimRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 1),
    _TpPimRPGroupAddress_Type()
)
tpPimRPGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimRPGroupAddress.setStatus("deprecated")
_TpPimRPAddress_Type = IpAddress
_TpPimRPAddress_Object = MibTableColumn
tpPimRPAddress = _TpPimRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 2),
    _TpPimRPAddress_Type()
)
tpPimRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimRPAddress.setStatus("deprecated")
_TpPimRPInfoSource_Type = IpAddress
_TpPimRPInfoSource_Object = MibTableColumn
tpPimRPInfoSource = _TpPimRPInfoSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 3),
    _TpPimRPInfoSource_Type()
)
tpPimRPInfoSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimRPInfoSource.setStatus("deprecated")
_TpPimRPPriority_Type = Integer32
_TpPimRPPriority_Object = MibTableColumn
tpPimRPPriority = _TpPimRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 4),
    _TpPimRPPriority_Type()
)
tpPimRPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimRPPriority.setStatus("deprecated")
_TpPimRPHoldTime_Type = TimeTicks
_TpPimRPHoldTime_Object = MibTableColumn
tpPimRPHoldTime = _TpPimRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 5),
    _TpPimRPHoldTime_Type()
)
tpPimRPHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimRPHoldTime.setStatus("deprecated")
_TpPimRPExpire_Type = TimeTicks
_TpPimRPExpire_Object = MibTableColumn
tpPimRPExpire = _TpPimRPExpire_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 1, 1, 8, 1, 6),
    _TpPimRPExpire_Type()
)
tpPimRPExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPimRPExpire.setStatus("deprecated")
_TplinkPimNotifications_ObjectIdentity = ObjectIdentity
tplinkPimNotifications = _TplinkPimNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 77, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PIM-MIB",
    **{"tplinkPimMIB": tplinkPimMIB,
       "tplinkPimMIBObjects": tplinkPimMIBObjects,
       "tpPim": tpPim,
       "tpSGExpiryTimer": tpSGExpiryTimer,
       "tpPimdataThresholdRate": tpPimdataThresholdRate,
       "tpPimInterfaceTable": tpPimInterfaceTable,
       "tpPimInterfaceEntry": tpPimInterfaceEntry,
       "tpPimInterface": tpPimInterface,
       "tpPimInterfaceIndex": tpPimInterfaceIndex,
       "tpPimInterfaceType": tpPimInterfaceType,
       "tpPimInterfaceAddress": tpPimInterfaceAddress,
       "tpPimInterfaceNetMask": tpPimInterfaceNetMask,
       "tpPimInterfaceMode": tpPimInterfaceMode,
       "tpPimInterfaceDRPriority": tpPimInterfaceDRPriority,
       "tpPimInterfaceDRAddress": tpPimInterfaceDRAddress,
       "tpPimInterfaceHelloInterval": tpPimInterfaceHelloInterval,
       "tpPimInterfaceBsrBorder": tpPimInterfaceBsrBorder,
       "tpPimInterfaceJoinPruneInterval": tpPimInterfaceJoinPruneInterval,
       "tpPimNeighborTable": tpPimNeighborTable,
       "tpPimNeighborEntry": tpPimNeighborEntry,
       "tpPimNeighborInterface": tpPimNeighborInterface,
       "tpPimNeighborInterfaceIndex": tpPimNeighborInterfaceIndex,
       "tpPimNeighborAddress": tpPimNeighborAddress,
       "tpPimNeighborUpTime": tpPimNeighborUpTime,
       "tpPimNeighborExpiryTime": tpPimNeighborExpiryTime,
       "tpPimNeighborMode": tpPimNeighborMode,
       "tpPimCandidateBSRSet": tpPimCandidateBSRSet,
       "tpPimCBSRInterface": tpPimCBSRInterface,
       "tpPimCBSRInterfaceIndex": tpPimCBSRInterfaceIndex,
       "tpPimCBSRHashMaskLength": tpPimCBSRHashMaskLength,
       "tpPimCBSRPriority": tpPimCBSRPriority,
       "tpPimStaticRpSet": tpPimStaticRpSet,
       "tpPimStaticRpAddress": tpPimStaticRpAddress,
       "tpPimStaticRpOverride": tpPimStaticRpOverride,
       "tpPimCandidateRPSetTable": tpPimCandidateRPSetTable,
       "tpPimCandidateRPSetEntry": tpPimCandidateRPSetEntry,
       "tpPimCRPSetInterface": tpPimCRPSetInterface,
       "tpPimCRPSetInterfaceIndex": tpPimCRPSetInterfaceIndex,
       "tpPimCRPSetInterfaceType": tpPimCRPSetInterfaceType,
       "tpPimCRPSetPriority": tpPimCRPSetPriority,
       "tpPimCRPSetInterVal": tpPimCRPSetInterVal,
       "tpPimCRPSetNextAdvertisementTime": tpPimCRPSetNextAdvertisementTime,
       "tpPimCRPSetInterfaceStatus": tpPimCRPSetInterfaceStatus,
       "tpPimRPMappingTable": tpPimRPMappingTable,
       "tpPimRPMappingEntry": tpPimRPMappingEntry,
       "tpPimRPGroupAddress": tpPimRPGroupAddress,
       "tpPimRPAddress": tpPimRPAddress,
       "tpPimRPInfoSource": tpPimRPInfoSource,
       "tpPimRPPriority": tpPimRPPriority,
       "tpPimRPHoldTime": tpPimRPHoldTime,
       "tpPimRPExpire": tpPimRPExpire,
       "tplinkPimNotifications": tplinkPimNotifications}
)
