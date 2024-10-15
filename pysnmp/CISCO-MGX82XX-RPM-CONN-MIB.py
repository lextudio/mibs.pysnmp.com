# SNMP MIB module (CISCO-MGX82XX-RPM-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-RPM-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:35 2024
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

(rpmChanGrp,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "rpmChanGrp")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoMgx82xxRpmConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 62)
)
ciscoMgx82xxRpmConnMIB.setRevisions(
        ("2002-09-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RpmNsapAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_RpmChanGrpTable_Object = MibTable
rpmChanGrpTable = _RpmChanGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    rpmChanGrpTable.setStatus("current")
_RpmChanGrpEntry_Object = MibTableRow
rpmChanGrpEntry = _RpmChanGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1)
)
rpmChanGrpEntry.setIndexNames(
    (0, "CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanSlotNum"),
    (0, "CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanNum"),
)
if mibBuilder.loadTexts:
    rpmChanGrpEntry.setStatus("current")


class _RpmChanSlotNum_Type(Integer32):
    """Custom type rpmChanSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RpmChanSlotNum_Type.__name__ = "Integer32"
_RpmChanSlotNum_Object = MibTableColumn
rpmChanSlotNum = _RpmChanSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 1),
    _RpmChanSlotNum_Type()
)
rpmChanSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanSlotNum.setStatus("current")
_RpmChanInterface_Type = Integer32
_RpmChanInterface_Object = MibTableColumn
rpmChanInterface = _RpmChanInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 2),
    _RpmChanInterface_Type()
)
rpmChanInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanInterface.setStatus("current")


class _RpmChanNum_Type(Integer32):
    """Custom type rpmChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 4095),
    )


_RpmChanNum_Type.__name__ = "Integer32"
_RpmChanNum_Object = MibTableColumn
rpmChanNum = _RpmChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 3),
    _RpmChanNum_Type()
)
rpmChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanNum.setStatus("current")


class _RpmChanRowStatus_Type(Integer32):
    """Custom type rpmChanRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_RpmChanRowStatus_Type.__name__ = "Integer32"
_RpmChanRowStatus_Object = MibTableColumn
rpmChanRowStatus = _RpmChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 4),
    _RpmChanRowStatus_Type()
)
rpmChanRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRowStatus.setStatus("current")


class _RpmChanVcd_Type(Integer32):
    """Custom type rpmChanVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RpmChanVcd_Type.__name__ = "Integer32"
_RpmChanVcd_Object = MibTableColumn
rpmChanVcd = _RpmChanVcd_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 5),
    _RpmChanVcd_Type()
)
rpmChanVcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanVcd.setStatus("current")


class _RpmChanVpi_Type(Integer32):
    """Custom type rpmChanVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpmChanVpi_Type.__name__ = "Integer32"
_RpmChanVpi_Object = MibTableColumn
rpmChanVpi = _RpmChanVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 6),
    _RpmChanVpi_Type()
)
rpmChanVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanVpi.setStatus("current")


class _RpmChanVci_Type(Integer32):
    """Custom type rpmChanVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpmChanVci_Type.__name__ = "Integer32"
_RpmChanVci_Object = MibTableColumn
rpmChanVci = _RpmChanVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 7),
    _RpmChanVci_Type()
)
rpmChanVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanVci.setStatus("current")


class _RpmChanSubInterface_Type(Integer32):
    """Custom type rpmChanSubInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpmChanSubInterface_Type.__name__ = "Integer32"
_RpmChanSubInterface_Object = MibTableColumn
rpmChanSubInterface = _RpmChanSubInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 8),
    _RpmChanSubInterface_Type()
)
rpmChanSubInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanSubInterface.setStatus("current")


class _RpmChanLocalVpi_Type(Integer32):
    """Custom type rpmChanLocalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpmChanLocalVpi_Type.__name__ = "Integer32"
_RpmChanLocalVpi_Object = MibTableColumn
rpmChanLocalVpi = _RpmChanLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 9),
    _RpmChanLocalVpi_Type()
)
rpmChanLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanLocalVpi.setStatus("current")


class _RpmChanLocalVci_Type(Integer32):
    """Custom type rpmChanLocalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpmChanLocalVci_Type.__name__ = "Integer32"
_RpmChanLocalVci_Object = MibTableColumn
rpmChanLocalVci = _RpmChanLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 10),
    _RpmChanLocalVci_Type()
)
rpmChanLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanLocalVci.setStatus("current")
_RpmChanLocalNsap_Type = RpmNsapAddress
_RpmChanLocalNsap_Object = MibTableColumn
rpmChanLocalNsap = _RpmChanLocalNsap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 11),
    _RpmChanLocalNsap_Type()
)
rpmChanLocalNsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanLocalNsap.setStatus("current")


class _RpmChanRemoteVpi_Type(Integer32):
    """Custom type rpmChanRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RpmChanRemoteVpi_Type.__name__ = "Integer32"
_RpmChanRemoteVpi_Object = MibTableColumn
rpmChanRemoteVpi = _RpmChanRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 12),
    _RpmChanRemoteVpi_Type()
)
rpmChanRemoteVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRemoteVpi.setStatus("current")


class _RpmChanRemoteVci_Type(Integer32):
    """Custom type rpmChanRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpmChanRemoteVci_Type.__name__ = "Integer32"
_RpmChanRemoteVci_Object = MibTableColumn
rpmChanRemoteVci = _RpmChanRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 13),
    _RpmChanRemoteVci_Type()
)
rpmChanRemoteVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRemoteVci.setStatus("current")
_RpmChanRemoteNsap_Type = RpmNsapAddress
_RpmChanRemoteNsap_Object = MibTableColumn
rpmChanRemoteNsap = _RpmChanRemoteNsap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 14),
    _RpmChanRemoteNsap_Type()
)
rpmChanRemoteNsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRemoteNsap.setStatus("current")


class _RpmChanType_Type(Integer32):
    """Custom type rpmChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 2),
          ("spvc", 3),
          ("svc", 1))
    )


_RpmChanType_Type.__name__ = "Integer32"
_RpmChanType_Object = MibTableColumn
rpmChanType = _RpmChanType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 15),
    _RpmChanType_Type()
)
rpmChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanType.setStatus("current")


class _RpmChanConnType_Type(Integer32):
    """Custom type rpmChanConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )


_RpmChanConnType_Type.__name__ = "Integer32"
_RpmChanConnType_Object = MibTableColumn
rpmChanConnType = _RpmChanConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 16),
    _RpmChanConnType_Type()
)
rpmChanConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanConnType.setStatus("current")


class _RpmChanServiceType_Type(Integer32):
    """Custom type rpmChanServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abrfst", 7),
          ("abrstd", 6),
          ("atfr", 5),
          ("cbr", 1),
          ("ubr", 4),
          ("vbr", 2))
    )


_RpmChanServiceType_Type.__name__ = "Integer32"
_RpmChanServiceType_Object = MibTableColumn
rpmChanServiceType = _RpmChanServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 17),
    _RpmChanServiceType_Type()
)
rpmChanServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanServiceType.setStatus("current")


class _RpmChanMastership_Type(Integer32):
    """Custom type rpmChanMastership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_RpmChanMastership_Type.__name__ = "Integer32"
_RpmChanMastership_Object = MibTableColumn
rpmChanMastership = _RpmChanMastership_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 18),
    _RpmChanMastership_Type()
)
rpmChanMastership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanMastership.setStatus("current")


class _RpmChanRtePriority_Type(Integer32):
    """Custom type rpmChanRtePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RpmChanRtePriority_Type.__name__ = "Integer32"
_RpmChanRtePriority_Object = MibTableColumn
rpmChanRtePriority = _RpmChanRtePriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 19),
    _RpmChanRtePriority_Type()
)
rpmChanRtePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRtePriority.setStatus("current")


class _RpmChanMaxCost_Type(Integer32):
    """Custom type rpmChanMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RpmChanMaxCost_Type.__name__ = "Integer32"
_RpmChanMaxCost_Object = MibTableColumn
rpmChanMaxCost = _RpmChanMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 20),
    _RpmChanMaxCost_Type()
)
rpmChanMaxCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanMaxCost.setStatus("current")


class _RpmChanRestrictTrkType_Type(Integer32):
    """Custom type rpmChanRestrictTrkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRestriction", 1),
          ("satelliteTrunk", 3),
          ("terrestrialTrunk", 2))
    )


_RpmChanRestrictTrkType_Type.__name__ = "Integer32"
_RpmChanRestrictTrkType_Object = MibTableColumn
rpmChanRestrictTrkType = _RpmChanRestrictTrkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 21),
    _RpmChanRestrictTrkType_Type()
)
rpmChanRestrictTrkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRestrictTrkType.setStatus("current")


class _RpmChanPCR_Type(Integer32):
    """Custom type rpmChanPCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_RpmChanPCR_Type.__name__ = "Integer32"
_RpmChanPCR_Object = MibTableColumn
rpmChanPCR = _RpmChanPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 22),
    _RpmChanPCR_Type()
)
rpmChanPCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanPCR.setStatus("current")
if mibBuilder.loadTexts:
    rpmChanPCR.setUnits("cells-per-second")


class _RpmChanRemotePCR_Type(Integer32):
    """Custom type rpmChanRemotePCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_RpmChanRemotePCR_Type.__name__ = "Integer32"
_RpmChanRemotePCR_Object = MibTableColumn
rpmChanRemotePCR = _RpmChanRemotePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 23),
    _RpmChanRemotePCR_Type()
)
rpmChanRemotePCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRemotePCR.setStatus("current")


class _RpmChanMCR_Type(Integer32):
    """Custom type rpmChanMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_RpmChanMCR_Type.__name__ = "Integer32"
_RpmChanMCR_Object = MibTableColumn
rpmChanMCR = _RpmChanMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 24),
    _RpmChanMCR_Type()
)
rpmChanMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanMCR.setStatus("current")
if mibBuilder.loadTexts:
    rpmChanMCR.setUnits("cells-per-second")


class _RpmChanRemoteMCR_Type(Integer32):
    """Custom type rpmChanRemoteMCR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 353208),
    )


_RpmChanRemoteMCR_Type.__name__ = "Integer32"
_RpmChanRemoteMCR_Object = MibTableColumn
rpmChanRemoteMCR = _RpmChanRemoteMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 25),
    _RpmChanRemoteMCR_Type()
)
rpmChanRemoteMCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRemoteMCR.setStatus("current")


class _RpmChanPercentUtil_Type(Integer32):
    """Custom type rpmChanPercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RpmChanPercentUtil_Type.__name__ = "Integer32"
_RpmChanPercentUtil_Object = MibTableColumn
rpmChanPercentUtil = _RpmChanPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 26),
    _RpmChanPercentUtil_Type()
)
rpmChanPercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanPercentUtil.setStatus("current")


class _RpmChanRemotePercentUtil_Type(Integer32):
    """Custom type rpmChanRemotePercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RpmChanRemotePercentUtil_Type.__name__ = "Integer32"
_RpmChanRemotePercentUtil_Object = MibTableColumn
rpmChanRemotePercentUtil = _RpmChanRemotePercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 27),
    _RpmChanRemotePercentUtil_Type()
)
rpmChanRemotePercentUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanRemotePercentUtil.setStatus("current")


class _RpmChanEncapType_Type(Integer32):
    """Custom type rpmChanEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aal34smds", 2),
          ("aal5muxDECNET", 9),
          ("aal5muxIP", 7),
          ("aal5muxNOVELL1", 10),
          ("aal5muxVINES", 8),
          ("aal5muxXNS", 6),
          ("aal5nlpid", 3),
          ("aal5snap", 1),
          ("ilmi", 5),
          ("ppp", 11),
          ("qsaal", 4),
          ("unknown", 12))
    )


_RpmChanEncapType_Type.__name__ = "Integer32"
_RpmChanEncapType_Object = MibTableColumn
rpmChanEncapType = _RpmChanEncapType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 28),
    _RpmChanEncapType_Type()
)
rpmChanEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanEncapType.setStatus("current")


class _RpmChanMidLow_Type(Integer32):
    """Custom type rpmChanMidLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RpmChanMidLow_Type.__name__ = "Integer32"
_RpmChanMidLow_Object = MibTableColumn
rpmChanMidLow = _RpmChanMidLow_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 29),
    _RpmChanMidLow_Type()
)
rpmChanMidLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanMidLow.setStatus("current")


class _RpmChanMidHigh_Type(Integer32):
    """Custom type rpmChanMidHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_RpmChanMidHigh_Type.__name__ = "Integer32"
_RpmChanMidHigh_Object = MibTableColumn
rpmChanMidHigh = _RpmChanMidHigh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 30),
    _RpmChanMidHigh_Type()
)
rpmChanMidHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanMidHigh.setStatus("current")


class _RpmChanBurstSize_Type(Integer32):
    """Custom type rpmChanBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RpmChanBurstSize_Type.__name__ = "Integer32"
_RpmChanBurstSize_Object = MibTableColumn
rpmChanBurstSize = _RpmChanBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 31),
    _RpmChanBurstSize_Type()
)
rpmChanBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanBurstSize.setStatus("current")


class _RpmChanInArpFreq_Type(Integer32):
    """Custom type rpmChanInArpFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_RpmChanInArpFreq_Type.__name__ = "Integer32"
_RpmChanInArpFreq_Object = MibTableColumn
rpmChanInArpFreq = _RpmChanInArpFreq_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 32),
    _RpmChanInArpFreq_Type()
)
rpmChanInArpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanInArpFreq.setStatus("current")
if mibBuilder.loadTexts:
    rpmChanInArpFreq.setUnits("minutes")


class _RpmChanOAMloopback_Type(Integer32):
    """Custom type rpmChanOAMloopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_RpmChanOAMloopback_Type.__name__ = "Integer32"
_RpmChanOAMloopback_Object = MibTableColumn
rpmChanOAMloopback = _RpmChanOAMloopback_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 33),
    _RpmChanOAMloopback_Type()
)
rpmChanOAMloopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanOAMloopback.setStatus("current")
if mibBuilder.loadTexts:
    rpmChanOAMloopback.setUnits("seconds")


class _RpmChanState_Type(Integer32):
    """Custom type rpmChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failed", 3),
          ("notConfigured", 1))
    )


_RpmChanState_Type.__name__ = "Integer32"
_RpmChanState_Object = MibTableColumn
rpmChanState = _RpmChanState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 34),
    _RpmChanState_Type()
)
rpmChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanState.setStatus("current")
_RpmChanVirtualTemplate_Type = Integer32
_RpmChanVirtualTemplate_Object = MibTableColumn
rpmChanVirtualTemplate = _RpmChanVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 35),
    _RpmChanVirtualTemplate_Type()
)
rpmChanVirtualTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanVirtualTemplate.setStatus("current")
_RpmChanAbrRDF_Type = Integer32
_RpmChanAbrRDF_Object = MibTableColumn
rpmChanAbrRDF = _RpmChanAbrRDF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 36),
    _RpmChanAbrRDF_Type()
)
rpmChanAbrRDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanAbrRDF.setStatus("current")
_RpmChanAbrRIF_Type = Integer32
_RpmChanAbrRIF_Object = MibTableColumn
rpmChanAbrRIF = _RpmChanAbrRIF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 10, 1, 1, 1, 37),
    _RpmChanAbrRIF_Type()
)
rpmChanAbrRIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmChanAbrRIF.setStatus("current")
_CmrConnMIBConformance_ObjectIdentity = ObjectIdentity
cmrConnMIBConformance = _CmrConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 62, 2)
)
_CmrConnMIBCompliances_ObjectIdentity = ObjectIdentity
cmrConnMIBCompliances = _CmrConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 62, 2, 1)
)
_CmrConnMIBGroups_ObjectIdentity = ObjectIdentity
cmrConnMIBGroups = _CmrConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 62, 2, 2)
)

# Managed Objects groups

cmrConnConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 62, 2, 2, 1)
)
cmrConnConfGroup.setObjects(
      *(("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanSlotNum"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanInterface"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanNum"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRowStatus"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanVcd"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanVpi"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanVci"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanSubInterface"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanLocalVpi"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanLocalVci"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanLocalNsap"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRemoteVpi"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRemoteVci"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRemoteNsap"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanType"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanConnType"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanServiceType"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanMastership"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRtePriority"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanMaxCost"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRestrictTrkType"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanPCR"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRemotePCR"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanMCR"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRemoteMCR"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanPercentUtil"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanRemotePercentUtil"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanMidLow"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanMidHigh"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanBurstSize"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanEncapType"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanInArpFreq"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanOAMloopback"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanState"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanVirtualTemplate"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanAbrRDF"),
        ("CISCO-MGX82XX-RPM-CONN-MIB", "rpmChanAbrRIF"))
)
if mibBuilder.loadTexts:
    cmrConnConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmrConnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 62, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmrConnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-RPM-CONN-MIB",
    **{"RpmNsapAddress": RpmNsapAddress,
       "rpmChanGrpTable": rpmChanGrpTable,
       "rpmChanGrpEntry": rpmChanGrpEntry,
       "rpmChanSlotNum": rpmChanSlotNum,
       "rpmChanInterface": rpmChanInterface,
       "rpmChanNum": rpmChanNum,
       "rpmChanRowStatus": rpmChanRowStatus,
       "rpmChanVcd": rpmChanVcd,
       "rpmChanVpi": rpmChanVpi,
       "rpmChanVci": rpmChanVci,
       "rpmChanSubInterface": rpmChanSubInterface,
       "rpmChanLocalVpi": rpmChanLocalVpi,
       "rpmChanLocalVci": rpmChanLocalVci,
       "rpmChanLocalNsap": rpmChanLocalNsap,
       "rpmChanRemoteVpi": rpmChanRemoteVpi,
       "rpmChanRemoteVci": rpmChanRemoteVci,
       "rpmChanRemoteNsap": rpmChanRemoteNsap,
       "rpmChanType": rpmChanType,
       "rpmChanConnType": rpmChanConnType,
       "rpmChanServiceType": rpmChanServiceType,
       "rpmChanMastership": rpmChanMastership,
       "rpmChanRtePriority": rpmChanRtePriority,
       "rpmChanMaxCost": rpmChanMaxCost,
       "rpmChanRestrictTrkType": rpmChanRestrictTrkType,
       "rpmChanPCR": rpmChanPCR,
       "rpmChanRemotePCR": rpmChanRemotePCR,
       "rpmChanMCR": rpmChanMCR,
       "rpmChanRemoteMCR": rpmChanRemoteMCR,
       "rpmChanPercentUtil": rpmChanPercentUtil,
       "rpmChanRemotePercentUtil": rpmChanRemotePercentUtil,
       "rpmChanEncapType": rpmChanEncapType,
       "rpmChanMidLow": rpmChanMidLow,
       "rpmChanMidHigh": rpmChanMidHigh,
       "rpmChanBurstSize": rpmChanBurstSize,
       "rpmChanInArpFreq": rpmChanInArpFreq,
       "rpmChanOAMloopback": rpmChanOAMloopback,
       "rpmChanState": rpmChanState,
       "rpmChanVirtualTemplate": rpmChanVirtualTemplate,
       "rpmChanAbrRDF": rpmChanAbrRDF,
       "rpmChanAbrRIF": rpmChanAbrRIF,
       "ciscoMgx82xxRpmConnMIB": ciscoMgx82xxRpmConnMIB,
       "cmrConnMIBConformance": cmrConnMIBConformance,
       "cmrConnMIBCompliances": cmrConnMIBCompliances,
       "cmrConnMIBCompliance": cmrConnMIBCompliance,
       "cmrConnMIBGroups": cmrConnMIBGroups,
       "cmrConnConfGroup": cmrConnConfGroup}
)
