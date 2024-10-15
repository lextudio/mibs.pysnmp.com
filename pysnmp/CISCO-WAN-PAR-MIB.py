# SNMP MIB module (CISCO-WAN-PAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-PAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:12 2024
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

(par,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "par")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanParMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 63)
)
ciscoWanParMIB.setRevisions(
        ("2002-09-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ParSelfNode_ObjectIdentity = ObjectIdentity
parSelfNode = _ParSelfNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 1)
)


class _ParSnNodeId_Type(Integer32):
    """Custom type parSnNodeId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 223),
    )


_ParSnNodeId_Type.__name__ = "Integer32"
_ParSnNodeId_Object = MibScalar
parSnNodeId = _ParSnNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 1, 1),
    _ParSnNodeId_Type()
)
parSnNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSnNodeId.setStatus("current")
_ParSnNodeIP_Type = IpAddress
_ParSnNodeIP_Object = MibScalar
parSnNodeIP = _ParSnNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 1, 2),
    _ParSnNodeIP_Type()
)
parSnNodeIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSnNodeIP.setStatus("current")


class _ParSnNodeName_Type(DisplayString):
    """Custom type parSnNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ParSnNodeName_Type.__name__ = "DisplayString"
_ParSnNodeName_Object = MibScalar
parSnNodeName = _ParSnNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 1, 3),
    _ParSnNodeName_Type()
)
parSnNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSnNodeName.setStatus("current")
_ParSnRevision_Type = DisplayString
_ParSnRevision_Object = MibScalar
parSnRevision = _ParSnRevision_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 1, 4),
    _ParSnRevision_Type()
)
parSnRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSnRevision.setStatus("current")


class _ParSnNodeAlarmStatus_Type(Integer32):
    """Custom type parSnNodeAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("major", 3),
          ("minor", 2),
          ("unreach", 4))
    )


_ParSnNodeAlarmStatus_Type.__name__ = "Integer32"
_ParSnNodeAlarmStatus_Object = MibScalar
parSnNodeAlarmStatus = _ParSnNodeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 1, 5),
    _ParSnNodeAlarmStatus_Type()
)
parSnNodeAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSnNodeAlarmStatus.setStatus("current")


class _ParSnNumberOfTrunks_Type(Integer32):
    """Custom type parSnNumberOfTrunks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ParSnNumberOfTrunks_Type.__name__ = "Integer32"
_ParSnNumberOfTrunks_Object = MibScalar
parSnNumberOfTrunks = _ParSnNumberOfTrunks_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 1, 6),
    _ParSnNumberOfTrunks_Type()
)
parSnNumberOfTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSnNumberOfTrunks.setStatus("current")
_ParInterfaces_ObjectIdentity = ObjectIdentity
parInterfaces = _ParInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 2)
)
_ParIfTable_Object = MibTable
parIfTable = _ParIfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1)
)
if mibBuilder.loadTexts:
    parIfTable.setStatus("current")
_ParIfEntry_Object = MibTableRow
parIfEntry = _ParIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1)
)
parIfEntry.setIndexNames(
    (0, "CISCO-WAN-PAR-MIB", "parIfLogicalInterface"),
)
if mibBuilder.loadTexts:
    parIfEntry.setStatus("current")


class _ParIfLogicalInterface_Type(Integer32):
    """Custom type parIfLogicalInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ParIfLogicalInterface_Type.__name__ = "Integer32"
_ParIfLogicalInterface_Object = MibTableColumn
parIfLogicalInterface = _ParIfLogicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 1),
    _ParIfLogicalInterface_Type()
)
parIfLogicalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfLogicalInterface.setStatus("current")


class _ParIfType_Type(Integer32):
    """Custom type parIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clkport", 4),
          ("feedertrunk", 3),
          ("routingtrunk", 2),
          ("userport", 1),
          ("virtualtrunk", 5))
    )


_ParIfType_Type.__name__ = "Integer32"
_ParIfType_Object = MibTableColumn
parIfType = _ParIfType_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 2),
    _ParIfType_Type()
)
parIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parIfType.setStatus("current")


class _ParIfOperStatus_Type(Integer32):
    """Custom type parIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("added", 2),
          ("added-failed", 4),
          ("failed", 3),
          ("up", 1))
    )


_ParIfOperStatus_Type.__name__ = "Integer32"
_ParIfOperStatus_Object = MibTableColumn
parIfOperStatus = _ParIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 3),
    _ParIfOperStatus_Type()
)
parIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfOperStatus.setStatus("current")
_ParIfTxBw_Type = Integer32
_ParIfTxBw_Object = MibTableColumn
parIfTxBw = _ParIfTxBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 4),
    _ParIfTxBw_Type()
)
parIfTxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfTxBw.setStatus("current")
if mibBuilder.loadTexts:
    parIfTxBw.setUnits("cells-per-second")
_ParIfRxBw_Type = Integer32
_ParIfRxBw_Object = MibTableColumn
parIfRxBw = _ParIfRxBw_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 5),
    _ParIfRxBw_Type()
)
parIfRxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfRxBw.setStatus("current")
if mibBuilder.loadTexts:
    parIfRxBw.setUnits("cells-per-second")
_ParIfMaxConn_Type = Integer32
_ParIfMaxConn_Object = MibTableColumn
parIfMaxConn = _ParIfMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 6),
    _ParIfMaxConn_Type()
)
parIfMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfMaxConn.setStatus("current")
_ParIfHiAddrMin_Type = Integer32
_ParIfHiAddrMin_Object = MibTableColumn
parIfHiAddrMin = _ParIfHiAddrMin_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 7),
    _ParIfHiAddrMin_Type()
)
parIfHiAddrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfHiAddrMin.setStatus("current")
_ParIfHiAddrMax_Type = Integer32
_ParIfHiAddrMax_Object = MibTableColumn
parIfHiAddrMax = _ParIfHiAddrMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 8),
    _ParIfHiAddrMax_Type()
)
parIfHiAddrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfHiAddrMax.setStatus("current")
_ParIfLoAddrMin_Type = Integer32
_ParIfLoAddrMin_Object = MibTableColumn
parIfLoAddrMin = _ParIfLoAddrMin_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 9),
    _ParIfLoAddrMin_Type()
)
parIfLoAddrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfLoAddrMin.setStatus("current")
_ParIfLoAddrMax_Type = Integer32
_ParIfLoAddrMax_Object = MibTableColumn
parIfLoAddrMax = _ParIfLoAddrMax_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 1, 1, 10),
    _ParIfLoAddrMax_Type()
)
parIfLoAddrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parIfLoAddrMax.setStatus("current")
_ParTrkTable_Object = MibTable
parTrkTable = _ParTrkTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2)
)
if mibBuilder.loadTexts:
    parTrkTable.setStatus("current")
_ParTrkEntry_Object = MibTableRow
parTrkEntry = _ParTrkEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1)
)
parTrkEntry.setIndexNames(
    (0, "CISCO-WAN-PAR-MIB", "parIfLogicalInterface"),
)
if mibBuilder.loadTexts:
    parTrkEntry.setStatus("current")
_ParTrkId_Type = Integer32
_ParTrkId_Object = MibTableColumn
parTrkId = _ParTrkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 1),
    _ParTrkId_Type()
)
parTrkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkId.setStatus("current")


class _ParTrkStatReserve_Type(Integer32):
    """Custom type parTrkStatReserve based on Integer32"""
    defaultValue = 1000


_ParTrkStatReserve_Object = MibTableColumn
parTrkStatReserve = _ParTrkStatReserve_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 2),
    _ParTrkStatReserve_Type()
)
parTrkStatReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkStatReserve.setStatus("current")
if mibBuilder.loadTexts:
    parTrkStatReserve.setUnits("cells-per-second")


class _ParTrkCnfgCcRestrict_Type(TruthValue):
    """Custom type parTrkCnfgCcRestrict based on TruthValue"""


_ParTrkCnfgCcRestrict_Object = MibTableColumn
parTrkCnfgCcRestrict = _ParTrkCnfgCcRestrict_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 3),
    _ParTrkCnfgCcRestrict_Type()
)
parTrkCnfgCcRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgCcRestrict.setStatus("current")


class _ParTrkCnfgLineType_Type(Integer32):
    """Custom type parTrkCnfgLineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("satellite", 2),
          ("terrestrial", 1))
    )


_ParTrkCnfgLineType_Type.__name__ = "Integer32"
_ParTrkCnfgLineType_Object = MibTableColumn
parTrkCnfgLineType = _ParTrkCnfgLineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 4),
    _ParTrkCnfgLineType_Type()
)
parTrkCnfgLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgLineType.setStatus("current")


class _ParTrkCnfgPassSync_Type(TruthValue):
    """Custom type parTrkCnfgPassSync based on TruthValue"""


_ParTrkCnfgPassSync_Object = MibTableColumn
parTrkCnfgPassSync = _ParTrkCnfgPassSync_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 5),
    _ParTrkCnfgPassSync_Type()
)
parTrkCnfgPassSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgPassSync.setStatus("current")


class _ParTrkCnfgDerouteDelay_Type(Integer32):
    """Custom type parTrkCnfgDerouteDelay based on Integer32"""
    defaultValue = 0


_ParTrkCnfgDerouteDelay_Object = MibTableColumn
parTrkCnfgDerouteDelay = _ParTrkCnfgDerouteDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 6),
    _ParTrkCnfgDerouteDelay_Type()
)
parTrkCnfgDerouteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgDerouteDelay.setStatus("current")
if mibBuilder.loadTexts:
    parTrkCnfgDerouteDelay.setUnits("seconds")


class _ParTrkCnfgTrafficClassFst_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassFst based on TruthValue"""


_ParTrkCnfgTrafficClassFst_Object = MibTableColumn
parTrkCnfgTrafficClassFst = _ParTrkCnfgTrafficClassFst_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 7),
    _ParTrkCnfgTrafficClassFst_Type()
)
parTrkCnfgTrafficClassFst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassFst.setStatus("current")


class _ParTrkCnfgTrafficClassFr_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassFr based on TruthValue"""


_ParTrkCnfgTrafficClassFr_Object = MibTableColumn
parTrkCnfgTrafficClassFr = _ParTrkCnfgTrafficClassFr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 8),
    _ParTrkCnfgTrafficClassFr_Type()
)
parTrkCnfgTrafficClassFr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassFr.setStatus("current")


class _ParTrkCnfgTrafficClassNts_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassNts based on TruthValue"""


_ParTrkCnfgTrafficClassNts_Object = MibTableColumn
parTrkCnfgTrafficClassNts = _ParTrkCnfgTrafficClassNts_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 9),
    _ParTrkCnfgTrafficClassNts_Type()
)
parTrkCnfgTrafficClassNts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassNts.setStatus("current")


class _ParTrkCnfgTrafficClassTs_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassTs based on TruthValue"""


_ParTrkCnfgTrafficClassTs_Object = MibTableColumn
parTrkCnfgTrafficClassTs = _ParTrkCnfgTrafficClassTs_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 10),
    _ParTrkCnfgTrafficClassTs_Type()
)
parTrkCnfgTrafficClassTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassTs.setStatus("current")


class _ParTrkCnfgTrafficClassVoice_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassVoice based on TruthValue"""


_ParTrkCnfgTrafficClassVoice_Object = MibTableColumn
parTrkCnfgTrafficClassVoice = _ParTrkCnfgTrafficClassVoice_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 11),
    _ParTrkCnfgTrafficClassVoice_Type()
)
parTrkCnfgTrafficClassVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassVoice.setStatus("current")


class _ParTrkCnfgTrafficClassCbr_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassCbr based on TruthValue"""


_ParTrkCnfgTrafficClassCbr_Object = MibTableColumn
parTrkCnfgTrafficClassCbr = _ParTrkCnfgTrafficClassCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 12),
    _ParTrkCnfgTrafficClassCbr_Type()
)
parTrkCnfgTrafficClassCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassCbr.setStatus("current")


class _ParTrkCnfgTrafficClassVbr_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassVbr based on TruthValue"""


_ParTrkCnfgTrafficClassVbr_Object = MibTableColumn
parTrkCnfgTrafficClassVbr = _ParTrkCnfgTrafficClassVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 13),
    _ParTrkCnfgTrafficClassVbr_Type()
)
parTrkCnfgTrafficClassVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassVbr.setStatus("current")


class _ParTrkCnfgTrafficClassAbr_Type(TruthValue):
    """Custom type parTrkCnfgTrafficClassAbr based on TruthValue"""


_ParTrkCnfgTrafficClassAbr_Object = MibTableColumn
parTrkCnfgTrafficClassAbr = _ParTrkCnfgTrafficClassAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 14),
    _ParTrkCnfgTrafficClassAbr_Type()
)
parTrkCnfgTrafficClassAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgTrafficClassAbr.setStatus("current")


class _ParTrkCnfgAdminStatus_Type(Integer32):
    """Custom type parTrkCnfgAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_ParTrkCnfgAdminStatus_Type.__name__ = "Integer32"
_ParTrkCnfgAdminStatus_Object = MibTableColumn
parTrkCnfgAdminStatus = _ParTrkCnfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 15),
    _ParTrkCnfgAdminStatus_Type()
)
parTrkCnfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgAdminStatus.setStatus("current")


class _ParTrkCnfgRoutingCost_Type(Integer32):
    """Custom type parTrkCnfgRoutingCost based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ParTrkCnfgRoutingCost_Type.__name__ = "Integer32"
_ParTrkCnfgRoutingCost_Object = MibTableColumn
parTrkCnfgRoutingCost = _ParTrkCnfgRoutingCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 16),
    _ParTrkCnfgRoutingCost_Type()
)
parTrkCnfgRoutingCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgRoutingCost.setStatus("current")
_ParTrkCnfgVccConids_Type = Integer32
_ParTrkCnfgVccConids_Object = MibTableColumn
parTrkCnfgVccConids = _ParTrkCnfgVccConids_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 17),
    _ParTrkCnfgVccConids_Type()
)
parTrkCnfgVccConids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgVccConids.setStatus("current")
_ParTrkCnfgVpcConids_Type = Integer32
_ParTrkCnfgVpcConids_Object = MibTableColumn
parTrkCnfgVpcConids = _ParTrkCnfgVpcConids_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 18),
    _ParTrkCnfgVpcConids_Type()
)
parTrkCnfgVpcConids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parTrkCnfgVpcConids.setStatus("current")


class _ParTrkLocalSlotNumber_Type(Integer32):
    """Custom type parTrkLocalSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ParTrkLocalSlotNumber_Type.__name__ = "Integer32"
_ParTrkLocalSlotNumber_Object = MibTableColumn
parTrkLocalSlotNumber = _ParTrkLocalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 19),
    _ParTrkLocalSlotNumber_Type()
)
parTrkLocalSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLocalSlotNumber.setStatus("current")


class _ParTrkLocalPortNumber_Type(Integer32):
    """Custom type parTrkLocalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ParTrkLocalPortNumber_Type.__name__ = "Integer32"
_ParTrkLocalPortNumber_Object = MibTableColumn
parTrkLocalPortNumber = _ParTrkLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 20),
    _ParTrkLocalPortNumber_Type()
)
parTrkLocalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLocalPortNumber.setStatus("current")


class _ParTrkLocalVTrunkId_Type(Integer32):
    """Custom type parTrkLocalVTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ParTrkLocalVTrunkId_Type.__name__ = "Integer32"
_ParTrkLocalVTrunkId_Object = MibTableColumn
parTrkLocalVTrunkId = _ParTrkLocalVTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 21),
    _ParTrkLocalVTrunkId_Type()
)
parTrkLocalVTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLocalVTrunkId.setStatus("current")


class _ParTrkRemoteNodeId_Type(Integer32):
    """Custom type parTrkRemoteNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 223),
    )


_ParTrkRemoteNodeId_Type.__name__ = "Integer32"
_ParTrkRemoteNodeId_Object = MibTableColumn
parTrkRemoteNodeId = _ParTrkRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 22),
    _ParTrkRemoteNodeId_Type()
)
parTrkRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteNodeId.setStatus("current")


class _ParTrkRemoteTrunkId_Type(Integer32):
    """Custom type parTrkRemoteTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ParTrkRemoteTrunkId_Type.__name__ = "Integer32"
_ParTrkRemoteTrunkId_Object = MibTableColumn
parTrkRemoteTrunkId = _ParTrkRemoteTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 23),
    _ParTrkRemoteTrunkId_Type()
)
parTrkRemoteTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteTrunkId.setStatus("current")


class _ParTrkRemoteSlotNumber_Type(Integer32):
    """Custom type parTrkRemoteSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ParTrkRemoteSlotNumber_Type.__name__ = "Integer32"
_ParTrkRemoteSlotNumber_Object = MibTableColumn
parTrkRemoteSlotNumber = _ParTrkRemoteSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 24),
    _ParTrkRemoteSlotNumber_Type()
)
parTrkRemoteSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteSlotNumber.setStatus("current")


class _ParTrkRemotePortNumber_Type(Integer32):
    """Custom type parTrkRemotePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ParTrkRemotePortNumber_Type.__name__ = "Integer32"
_ParTrkRemotePortNumber_Object = MibTableColumn
parTrkRemotePortNumber = _ParTrkRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 25),
    _ParTrkRemotePortNumber_Type()
)
parTrkRemotePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemotePortNumber.setStatus("current")


class _ParTrkRemoteVTrunkId_Type(Integer32):
    """Custom type parTrkRemoteVTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ParTrkRemoteVTrunkId_Type.__name__ = "Integer32"
_ParTrkRemoteVTrunkId_Object = MibTableColumn
parTrkRemoteVTrunkId = _ParTrkRemoteVTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 26),
    _ParTrkRemoteVTrunkId_Type()
)
parTrkRemoteVTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteVTrunkId.setStatus("current")
_ParTrkRemoteNodeIP_Type = IpAddress
_ParTrkRemoteNodeIP_Object = MibTableColumn
parTrkRemoteNodeIP = _ParTrkRemoteNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 27),
    _ParTrkRemoteNodeIP_Type()
)
parTrkRemoteNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteNodeIP.setStatus("current")


class _ParTrkRemoteNodeType_Type(Integer32):
    """Custom type parTrkRemoteNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bpx", 3),
          ("igx", 2),
          ("ipx", 1),
          ("par", 4),
          ("unknown", 5))
    )


_ParTrkRemoteNodeType_Type.__name__ = "Integer32"
_ParTrkRemoteNodeType_Object = MibTableColumn
parTrkRemoteNodeType = _ParTrkRemoteNodeType_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 28),
    _ParTrkRemoteNodeType_Type()
)
parTrkRemoteNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteNodeType.setStatus("current")
_ParTrkRemoteNodeName_Type = DisplayString
_ParTrkRemoteNodeName_Object = MibTableColumn
parTrkRemoteNodeName = _ParTrkRemoteNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 29),
    _ParTrkRemoteNodeName_Type()
)
parTrkRemoteNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkRemoteNodeName.setStatus("current")


class _ParTrkAlarmStatus_Type(Integer32):
    """Custom type parTrkAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("major", 3),
          ("minor", 2))
    )


_ParTrkAlarmStatus_Type.__name__ = "Integer32"
_ParTrkAlarmStatus_Object = MibTableColumn
parTrkAlarmStatus = _ParTrkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 30),
    _ParTrkAlarmStatus_Type()
)
parTrkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkAlarmStatus.setStatus("current")


class _ParTrkAlarmType_Type(Integer32):
    """Custom type parTrkAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commfail", 2),
          ("failed", 4),
          ("looped", 5),
          ("rsrcunavail", 1),
          ("unknown", 3))
    )


_ParTrkAlarmType_Type.__name__ = "Integer32"
_ParTrkAlarmType_Object = MibTableColumn
parTrkAlarmType = _ParTrkAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 31),
    _ParTrkAlarmType_Type()
)
parTrkAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkAlarmType.setStatus("current")
_ParTrkBwCapacity_Type = Integer32
_ParTrkBwCapacity_Object = MibTableColumn
parTrkBwCapacity = _ParTrkBwCapacity_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 32),
    _ParTrkBwCapacity_Type()
)
parTrkBwCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkBwCapacity.setStatus("current")
_ParTrkLineLoad_Type = Integer32
_ParTrkLineLoad_Object = MibTableColumn
parTrkLineLoad = _ParTrkLineLoad_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 2, 1, 33),
    _ParTrkLineLoad_Type()
)
parTrkLineLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLineLoad.setStatus("current")
_ParTrkLoadTable_Object = MibTable
parTrkLoadTable = _ParTrkLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3)
)
if mibBuilder.loadTexts:
    parTrkLoadTable.setStatus("current")
_ParTrkLoadEntry_Object = MibTableRow
parTrkLoadEntry = _ParTrkLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1)
)
parTrkLoadEntry.setIndexNames(
    (0, "CISCO-WAN-PAR-MIB", "parIfLogicalInterface"),
)
if mibBuilder.loadTexts:
    parTrkLoadEntry.setStatus("current")
_ParTrkLoadXmtUsedCbr_Type = Integer32
_ParTrkLoadXmtUsedCbr_Object = MibTableColumn
parTrkLoadXmtUsedCbr = _ParTrkLoadXmtUsedCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 1),
    _ParTrkLoadXmtUsedCbr_Type()
)
parTrkLoadXmtUsedCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedCbr.setStatus("current")
_ParTrkLoadRcvUsedCbr_Type = Integer32
_ParTrkLoadRcvUsedCbr_Object = MibTableColumn
parTrkLoadRcvUsedCbr = _ParTrkLoadRcvUsedCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 2),
    _ParTrkLoadRcvUsedCbr_Type()
)
parTrkLoadRcvUsedCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedCbr.setStatus("current")
_ParTrkLoadXmtUsedVbr_Type = Integer32
_ParTrkLoadXmtUsedVbr_Object = MibTableColumn
parTrkLoadXmtUsedVbr = _ParTrkLoadXmtUsedVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 3),
    _ParTrkLoadXmtUsedVbr_Type()
)
parTrkLoadXmtUsedVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedVbr.setStatus("current")
_ParTrkLoadRcvUsedVbr_Type = Integer32
_ParTrkLoadRcvUsedVbr_Object = MibTableColumn
parTrkLoadRcvUsedVbr = _ParTrkLoadRcvUsedVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 4),
    _ParTrkLoadRcvUsedVbr_Type()
)
parTrkLoadRcvUsedVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedVbr.setStatus("current")
_ParTrkLoadXmtUsedAbr_Type = Integer32
_ParTrkLoadXmtUsedAbr_Object = MibTableColumn
parTrkLoadXmtUsedAbr = _ParTrkLoadXmtUsedAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 5),
    _ParTrkLoadXmtUsedAbr_Type()
)
parTrkLoadXmtUsedAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedAbr.setStatus("current")
_ParTrkLoadRcvUsedAbr_Type = Integer32
_ParTrkLoadRcvUsedAbr_Object = MibTableColumn
parTrkLoadRcvUsedAbr = _ParTrkLoadRcvUsedAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 6),
    _ParTrkLoadRcvUsedAbr_Type()
)
parTrkLoadRcvUsedAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedAbr.setStatus("current")
_ParTrkLoadXmtUsedNts_Type = Integer32
_ParTrkLoadXmtUsedNts_Object = MibTableColumn
parTrkLoadXmtUsedNts = _ParTrkLoadXmtUsedNts_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 7),
    _ParTrkLoadXmtUsedNts_Type()
)
parTrkLoadXmtUsedNts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedNts.setStatus("current")
_ParTrkLoadRcvUsedNts_Type = Integer32
_ParTrkLoadRcvUsedNts_Object = MibTableColumn
parTrkLoadRcvUsedNts = _ParTrkLoadRcvUsedNts_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 8),
    _ParTrkLoadRcvUsedNts_Type()
)
parTrkLoadRcvUsedNts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedNts.setStatus("current")
_ParTrkLoadXmtUsedTs_Type = Integer32
_ParTrkLoadXmtUsedTs_Object = MibTableColumn
parTrkLoadXmtUsedTs = _ParTrkLoadXmtUsedTs_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 9),
    _ParTrkLoadXmtUsedTs_Type()
)
parTrkLoadXmtUsedTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedTs.setStatus("current")
_ParTrkLoadRcvUsedTs_Type = Integer32
_ParTrkLoadRcvUsedTs_Object = MibTableColumn
parTrkLoadRcvUsedTs = _ParTrkLoadRcvUsedTs_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 10),
    _ParTrkLoadRcvUsedTs_Type()
)
parTrkLoadRcvUsedTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedTs.setStatus("current")
_ParTrkLoadXmtUsedVoice_Type = Integer32
_ParTrkLoadXmtUsedVoice_Object = MibTableColumn
parTrkLoadXmtUsedVoice = _ParTrkLoadXmtUsedVoice_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 11),
    _ParTrkLoadXmtUsedVoice_Type()
)
parTrkLoadXmtUsedVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedVoice.setStatus("current")
_ParTrkLoadRcvUsedVoice_Type = Integer32
_ParTrkLoadRcvUsedVoice_Object = MibTableColumn
parTrkLoadRcvUsedVoice = _ParTrkLoadRcvUsedVoice_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 12),
    _ParTrkLoadRcvUsedVoice_Type()
)
parTrkLoadRcvUsedVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedVoice.setStatus("current")
_ParTrkLoadXmtUsedBdataA_Type = Integer32
_ParTrkLoadXmtUsedBdataA_Object = MibTableColumn
parTrkLoadXmtUsedBdataA = _ParTrkLoadXmtUsedBdataA_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 13),
    _ParTrkLoadXmtUsedBdataA_Type()
)
parTrkLoadXmtUsedBdataA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedBdataA.setStatus("current")
_ParTrkLoadRcvUsedBdataA_Type = Integer32
_ParTrkLoadRcvUsedBdataA_Object = MibTableColumn
parTrkLoadRcvUsedBdataA = _ParTrkLoadRcvUsedBdataA_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 14),
    _ParTrkLoadRcvUsedBdataA_Type()
)
parTrkLoadRcvUsedBdataA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedBdataA.setStatus("current")
_ParTrkLoadXmtUsedBdataB_Type = Integer32
_ParTrkLoadXmtUsedBdataB_Object = MibTableColumn
parTrkLoadXmtUsedBdataB = _ParTrkLoadXmtUsedBdataB_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 15),
    _ParTrkLoadXmtUsedBdataB_Type()
)
parTrkLoadXmtUsedBdataB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadXmtUsedBdataB.setStatus("current")
_ParTrkLoadRcvUsedBdataB_Type = Integer32
_ParTrkLoadRcvUsedBdataB_Object = MibTableColumn
parTrkLoadRcvUsedBdataB = _ParTrkLoadRcvUsedBdataB_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 16),
    _ParTrkLoadRcvUsedBdataB_Type()
)
parTrkLoadRcvUsedBdataB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadRcvUsedBdataB.setStatus("current")
_ParTrkLoadVccConidsUsed_Type = Integer32
_ParTrkLoadVccConidsUsed_Object = MibTableColumn
parTrkLoadVccConidsUsed = _ParTrkLoadVccConidsUsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 17),
    _ParTrkLoadVccConidsUsed_Type()
)
parTrkLoadVccConidsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadVccConidsUsed.setStatus("current")
_ParTrkLoadVpcConidsUsed_Type = Integer32
_ParTrkLoadVpcConidsUsed_Object = MibTableColumn
parTrkLoadVpcConidsUsed = _ParTrkLoadVpcConidsUsed_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 2, 3, 1, 19),
    _ParTrkLoadVpcConidsUsed_Type()
)
parTrkLoadVpcConidsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parTrkLoadVpcConidsUsed.setStatus("current")
_ParConnection_ObjectIdentity = ObjectIdentity
parConnection = _ParConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 3)
)
_ParConnectionTable_Object = MibTable
parConnectionTable = _ParConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1)
)
if mibBuilder.loadTexts:
    parConnectionTable.setStatus("current")
_ParConnectionEntry_Object = MibTableRow
parConnectionEntry = _ParConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1)
)
parConnectionEntry.setIndexNames(
    (0, "CISCO-WAN-PAR-MIB", "parConnLocalSlot"),
    (0, "CISCO-WAN-PAR-MIB", "parConnLocalPort"),
    (0, "CISCO-WAN-PAR-MIB", "parConnLocalVpi"),
    (0, "CISCO-WAN-PAR-MIB", "parConnLocalVci"),
)
if mibBuilder.loadTexts:
    parConnectionEntry.setStatus("current")


class _ParConnLocalSlot_Type(Integer32):
    """Custom type parConnLocalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ParConnLocalSlot_Type.__name__ = "Integer32"
_ParConnLocalSlot_Object = MibTableColumn
parConnLocalSlot = _ParConnLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 1),
    _ParConnLocalSlot_Type()
)
parConnLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnLocalSlot.setStatus("current")


class _ParConnLocalPort_Type(Integer32):
    """Custom type parConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ParConnLocalPort_Type.__name__ = "Integer32"
_ParConnLocalPort_Object = MibTableColumn
parConnLocalPort = _ParConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 2),
    _ParConnLocalPort_Type()
)
parConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnLocalPort.setStatus("current")


class _ParConnLocalVpi_Type(Integer32):
    """Custom type parConnLocalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ParConnLocalVpi_Type.__name__ = "Integer32"
_ParConnLocalVpi_Object = MibTableColumn
parConnLocalVpi = _ParConnLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 3),
    _ParConnLocalVpi_Type()
)
parConnLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnLocalVpi.setStatus("current")


class _ParConnLocalVci_Type(Integer32):
    """Custom type parConnLocalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ParConnLocalVci_Type.__name__ = "Integer32"
_ParConnLocalVci_Object = MibTableColumn
parConnLocalVci = _ParConnLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 4),
    _ParConnLocalVci_Type()
)
parConnLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnLocalVci.setStatus("current")
_ParConnMasterShip_Type = TruthValue
_ParConnMasterShip_Object = MibTableColumn
parConnMasterShip = _ParConnMasterShip_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 5),
    _ParConnMasterShip_Type()
)
parConnMasterShip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnMasterShip.setStatus("current")
_ParConnLocalVcIndx_Type = Integer32
_ParConnLocalVcIndx_Object = MibTableColumn
parConnLocalVcIndx = _ParConnLocalVcIndx_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 6),
    _ParConnLocalVcIndx_Type()
)
parConnLocalVcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnLocalVcIndx.setStatus("current")
_ParConnLocalEndpt_Type = DisplayString
_ParConnLocalEndpt_Object = MibTableColumn
parConnLocalEndpt = _ParConnLocalEndpt_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 7),
    _ParConnLocalEndpt_Type()
)
parConnLocalEndpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnLocalEndpt.setStatus("current")
_ParConnRemoteNodeName_Type = DisplayString
_ParConnRemoteNodeName_Object = MibTableColumn
parConnRemoteNodeName = _ParConnRemoteNodeName_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 8),
    _ParConnRemoteNodeName_Type()
)
parConnRemoteNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemoteNodeName.setStatus("current")


class _ParConnRemoteSlot_Type(Integer32):
    """Custom type parConnRemoteSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ParConnRemoteSlot_Type.__name__ = "Integer32"
_ParConnRemoteSlot_Object = MibTableColumn
parConnRemoteSlot = _ParConnRemoteSlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 9),
    _ParConnRemoteSlot_Type()
)
parConnRemoteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemoteSlot.setStatus("current")


class _ParConnRemotePort_Type(Integer32):
    """Custom type parConnRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ParConnRemotePort_Type.__name__ = "Integer32"
_ParConnRemotePort_Object = MibTableColumn
parConnRemotePort = _ParConnRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 10),
    _ParConnRemotePort_Type()
)
parConnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemotePort.setStatus("current")
_ParConnRemoteVpi_Type = Integer32
_ParConnRemoteVpi_Object = MibTableColumn
parConnRemoteVpi = _ParConnRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 11),
    _ParConnRemoteVpi_Type()
)
parConnRemoteVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemoteVpi.setStatus("current")
_ParConnRemoteVci_Type = Integer32
_ParConnRemoteVci_Object = MibTableColumn
parConnRemoteVci = _ParConnRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 12),
    _ParConnRemoteVci_Type()
)
parConnRemoteVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemoteVci.setStatus("current")
_ParConnRemoteVcIndx_Type = Integer32
_ParConnRemoteVcIndx_Object = MibTableColumn
parConnRemoteVcIndx = _ParConnRemoteVcIndx_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 13),
    _ParConnRemoteVcIndx_Type()
)
parConnRemoteVcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemoteVcIndx.setStatus("current")


class _ParConnOperStatus_Type(Integer32):
    """Custom type parConnOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lmifail", 3),
          ("routed", 1),
          ("unknown", 4),
          ("unrouted", 2))
    )


_ParConnOperStatus_Type.__name__ = "Integer32"
_ParConnOperStatus_Object = MibTableColumn
parConnOperStatus = _ParConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 14),
    _ParConnOperStatus_Type()
)
parConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnOperStatus.setStatus("current")


class _ParConnAdminStatus_Type(Integer32):
    """Custom type parConnAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("reroute", 3),
          ("up", 2))
    )


_ParConnAdminStatus_Type.__name__ = "Integer32"
_ParConnAdminStatus_Object = MibTableColumn
parConnAdminStatus = _ParConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 15),
    _ParConnAdminStatus_Type()
)
parConnAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parConnAdminStatus.setStatus("current")
_ParConnRoute_Type = DisplayString
_ParConnRoute_Object = MibTableColumn
parConnRoute = _ParConnRoute_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 16),
    _ParConnRoute_Type()
)
parConnRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRoute.setStatus("current")
_ParConnRemoteEndpt_Type = DisplayString
_ParConnRemoteEndpt_Object = MibTableColumn
parConnRemoteEndpt = _ParConnRemoteEndpt_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 17),
    _ParConnRemoteEndpt_Type()
)
parConnRemoteEndpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRemoteEndpt.setStatus("current")
_ParPrefRoute_Type = DisplayString
_ParPrefRoute_Object = MibTableColumn
parPrefRoute = _ParPrefRoute_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 18),
    _ParPrefRoute_Type()
)
parPrefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parPrefRoute.setStatus("current")


class _ParConnFailRsn_Type(Integer32):
    """Custom type parConnFailRsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abitalm", 3),
          ("down", 1),
          ("hwalm", 2),
          ("incomplete", 6),
          ("lmifail", 4),
          ("rrtfail", 5))
    )


_ParConnFailRsn_Type.__name__ = "Integer32"
_ParConnFailRsn_Object = MibTableColumn
parConnFailRsn = _ParConnFailRsn_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 19),
    _ParConnFailRsn_Type()
)
parConnFailRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnFailRsn.setStatus("current")
_ParRrtFailRsn_Type = DisplayString
_ParRrtFailRsn_Object = MibTableColumn
parRrtFailRsn = _ParRrtFailRsn_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 20),
    _ParRrtFailRsn_Type()
)
parRrtFailRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parRrtFailRsn.setStatus("current")


class _ParConnRstrTyp_Type(Integer32):
    """Custom type parConnRstrTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("norestrict", 1),
          ("satrestrict", 3),
          ("terrestrict", 2),
          ("undefrestrict", 4))
    )


_ParConnRstrTyp_Type.__name__ = "Integer32"
_ParConnRstrTyp_Object = MibTableColumn
parConnRstrTyp = _ParConnRstrTyp_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 21),
    _ParConnRstrTyp_Type()
)
parConnRstrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRstrTyp.setStatus("current")
_ParConnRstrZcs_Type = TruthValue
_ParConnRstrZcs_Object = MibTableColumn
parConnRstrZcs = _ParConnRstrZcs_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 22),
    _ParConnRstrZcs_Type()
)
parConnRstrZcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnRstrZcs.setStatus("current")


class _ParConnCos_Type(Integer32):
    """Custom type parConnCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ParConnCos_Type.__name__ = "Integer32"
_ParConnCos_Object = MibTableColumn
parConnCos = _ParConnCos_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 3, 1, 1, 23),
    _ParConnCos_Type()
)
parConnCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parConnCos.setStatus("current")
_ParNetworkClock_ObjectIdentity = ObjectIdentity
parNetworkClock = _ParNetworkClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 4)
)
_ParClockTable_Object = MibTable
parClockTable = _ParClockTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1)
)
if mibBuilder.loadTexts:
    parClockTable.setStatus("current")
_ParClockEntry_Object = MibTableRow
parClockEntry = _ParClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1)
)
parClockEntry.setIndexNames(
    (0, "CISCO-WAN-PAR-MIB", "parClockIndex"),
)
if mibBuilder.loadTexts:
    parClockEntry.setStatus("current")


class _ParClockIndex_Type(Integer32):
    """Custom type parClockIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ParClockIndex_Type.__name__ = "Integer32"
_ParClockIndex_Object = MibTableColumn
parClockIndex = _ParClockIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1, 1),
    _ParClockIndex_Type()
)
parClockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parClockIndex.setStatus("current")


class _ParClockType_Type(Integer32):
    """Custom type parClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("null", 4),
          ("primary", 1),
          ("secondary", 2),
          ("tertiary", 3))
    )


_ParClockType_Type.__name__ = "Integer32"
_ParClockType_Object = MibTableColumn
parClockType = _ParClockType_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1, 2),
    _ParClockType_Type()
)
parClockType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parClockType.setStatus("current")


class _ParClockSource_Type(Integer32):
    """Custom type parClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("interface", 2),
          ("internal", 1))
    )


_ParClockSource_Type.__name__ = "Integer32"
_ParClockSource_Object = MibTableColumn
parClockSource = _ParClockSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1, 3),
    _ParClockSource_Type()
)
parClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parClockSource.setStatus("current")


class _ParClockCurSource_Type(TruthValue):
    """Custom type parClockCurSource based on TruthValue"""


_ParClockCurSource_Object = MibTableColumn
parClockCurSource = _ParClockCurSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1, 4),
    _ParClockCurSource_Type()
)
parClockCurSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parClockCurSource.setStatus("current")
_ParClockSourceId_Type = Integer32
_ParClockSourceId_Object = MibTableColumn
parClockSourceId = _ParClockSourceId_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1, 5),
    _ParClockSourceId_Type()
)
parClockSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parClockSourceId.setStatus("current")
_ParClockPath_Type = DisplayString
_ParClockPath_Object = MibTableColumn
parClockPath = _ParClockPath_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 4, 1, 1, 6),
    _ParClockPath_Type()
)
parClockPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parClockPath.setStatus("current")
_ParConfigParms_ObjectIdentity = ObjectIdentity
parConfigParms = _ParConfigParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5)
)
_ParVsiConfigParms_ObjectIdentity = ObjectIdentity
parVsiConfigParms = _ParVsiConfigParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 1)
)
_ParCmParms_ObjectIdentity = ObjectIdentity
parCmParms = _ParCmParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2)
)


class _ParCmParmsMaxRoutingBundle_Type(Integer32):
    """Custom type parCmParmsMaxRoutingBundle based on Integer32"""
    defaultValue = 24


_ParCmParmsMaxRoutingBundle_Object = MibScalar
parCmParmsMaxRoutingBundle = _ParCmParmsMaxRoutingBundle_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 1),
    _ParCmParmsMaxRoutingBundle_Type()
)
parCmParmsMaxRoutingBundle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsMaxRoutingBundle.setStatus("current")


class _ParCmParmsRerouteTimer_Type(Integer32):
    """Custom type parCmParmsRerouteTimer based on Integer32"""
    defaultValue = 0


_ParCmParmsRerouteTimer_Object = MibScalar
parCmParmsRerouteTimer = _ParCmParmsRerouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 2),
    _ParCmParmsRerouteTimer_Type()
)
parCmParmsRerouteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsRerouteTimer.setStatus("current")


class _ParCmParmsResetTimer_Type(TruthValue):
    """Custom type parCmParmsResetTimer based on TruthValue"""


_ParCmParmsResetTimer_Object = MibScalar
parCmParmsResetTimer = _ParCmParmsResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 3),
    _ParCmParmsResetTimer_Type()
)
parCmParmsResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsResetTimer.setStatus("current")


class _ParCmParmsDnUpPerPass_Type(Integer32):
    """Custom type parCmParmsDnUpPerPass based on Integer32"""
    defaultValue = 50


_ParCmParmsDnUpPerPass_Object = MibScalar
parCmParmsDnUpPerPass = _ParCmParmsDnUpPerPass_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 4),
    _ParCmParmsDnUpPerPass_Type()
)
parCmParmsDnUpPerPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsDnUpPerPass.setStatus("current")


class _ParCmParmsDnUpTimer_Type(Integer32):
    """Custom type parCmParmsDnUpTimer based on Integer32"""
    defaultValue = 30000


_ParCmParmsDnUpTimer_Object = MibScalar
parCmParmsDnUpTimer = _ParCmParmsDnUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 5),
    _ParCmParmsDnUpTimer_Type()
)
parCmParmsDnUpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsDnUpTimer.setStatus("current")
if mibBuilder.loadTexts:
    parCmParmsDnUpTimer.setUnits("milliseconds")


class _ParCmParmsRrtErrsPerCycle_Type(Integer32):
    """Custom type parCmParmsRrtErrsPerCycle based on Integer32"""
    defaultValue = 50


_ParCmParmsRrtErrsPerCycle_Object = MibScalar
parCmParmsRrtErrsPerCycle = _ParCmParmsRrtErrsPerCycle_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 6),
    _ParCmParmsRrtErrsPerCycle_Type()
)
parCmParmsRrtErrsPerCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsRrtErrsPerCycle.setStatus("current")


class _ParCmParmsRrtCycleInterval_Type(Integer32):
    """Custom type parCmParmsRrtCycleInterval based on Integer32"""
    defaultValue = 5


_ParCmParmsRrtCycleInterval_Object = MibScalar
parCmParmsRrtCycleInterval = _ParCmParmsRrtCycleInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 7),
    _ParCmParmsRrtCycleInterval_Type()
)
parCmParmsRrtCycleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsRrtCycleInterval.setStatus("current")
if mibBuilder.loadTexts:
    parCmParmsRrtCycleInterval.setUnits("minutes")


class _ParCmParmsMaxRrtCycles_Type(Integer32):
    """Custom type parCmParmsMaxRrtCycles based on Integer32"""
    defaultValue = 10


_ParCmParmsMaxRrtCycles_Object = MibScalar
parCmParmsMaxRrtCycles = _ParCmParmsMaxRrtCycles_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 8),
    _ParCmParmsMaxRrtCycles_Type()
)
parCmParmsMaxRrtCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsMaxRrtCycles.setStatus("current")


class _ParCmParmsRrtPauseTime_Type(Integer32):
    """Custom type parCmParmsRrtPauseTime based on Integer32"""
    defaultValue = 0


_ParCmParmsRrtPauseTime_Object = MibScalar
parCmParmsRrtPauseTime = _ParCmParmsRrtPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 9),
    _ParCmParmsRrtPauseTime_Type()
)
parCmParmsRrtPauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsRrtPauseTime.setStatus("current")
if mibBuilder.loadTexts:
    parCmParmsRrtPauseTime.setUnits("milliseconds")


class _ParCmParmsMaxUpdates_Type(Integer32):
    """Custom type parCmParmsMaxUpdates based on Integer32"""
    defaultValue = 10


_ParCmParmsMaxUpdates_Object = MibScalar
parCmParmsMaxUpdates = _ParCmParmsMaxUpdates_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 10),
    _ParCmParmsMaxUpdates_Type()
)
parCmParmsMaxUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsMaxUpdates.setStatus("current")


class _ParCmParmsRerouteGroups_Type(Integer32):
    """Custom type parCmParmsRerouteGroups based on Integer32"""
    defaultValue = 50


_ParCmParmsRerouteGroups_Object = MibScalar
parCmParmsRerouteGroups = _ParCmParmsRerouteGroups_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 11),
    _ParCmParmsRerouteGroups_Type()
)
parCmParmsRerouteGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsRerouteGroups.setStatus("current")


class _ParCmParmsMinRrGroupSize_Type(Integer32):
    """Custom type parCmParmsMinRrGroupSize based on Integer32"""
    defaultValue = 0


_ParCmParmsMinRrGroupSize_Object = MibScalar
parCmParmsMinRrGroupSize = _ParCmParmsMinRrGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 12),
    _ParCmParmsMinRrGroupSize_Type()
)
parCmParmsMinRrGroupSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsMinRrGroupSize.setStatus("current")


class _ParCmParmsRrGroupInc_Type(Integer32):
    """Custom type parCmParmsRrGroupInc based on Integer32"""
    defaultValue = 100


_ParCmParmsRrGroupInc_Object = MibScalar
parCmParmsRrGroupInc = _ParCmParmsRrGroupInc_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 13),
    _ParCmParmsRrGroupInc_Type()
)
parCmParmsRrGroupInc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsRrGroupInc.setStatus("current")


class _ParCmParmsCostBased_Type(TruthValue):
    """Custom type parCmParmsCostBased based on TruthValue"""


_ParCmParmsCostBased_Object = MibScalar
parCmParmsCostBased = _ParCmParmsCostBased_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 14),
    _ParCmParmsCostBased_Type()
)
parCmParmsCostBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsCostBased.setStatus("current")


class _ParCmParmsUseCache_Type(TruthValue):
    """Custom type parCmParmsUseCache based on TruthValue"""


_ParCmParmsUseCache_Object = MibScalar
parCmParmsUseCache = _ParCmParmsUseCache_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 15),
    _ParCmParmsUseCache_Type()
)
parCmParmsUseCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsUseCache.setStatus("current")


class _ParCmParmsUseDelay_Type(TruthValue):
    """Custom type parCmParmsUseDelay based on TruthValue"""


_ParCmParmsUseDelay_Object = MibScalar
parCmParmsUseDelay = _ParCmParmsUseDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 16),
    _ParCmParmsUseDelay_Type()
)
parCmParmsUseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmsUseDelay.setStatus("current")


class _ParCmParmMaxViaCons_Type(Integer32):
    """Custom type parCmParmMaxViaCons based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80000),
    )


_ParCmParmMaxViaCons_Type.__name__ = "Integer32"
_ParCmParmMaxViaCons_Object = MibScalar
parCmParmMaxViaCons = _ParCmParmMaxViaCons_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 2, 17),
    _ParCmParmMaxViaCons_Type()
)
parCmParmMaxViaCons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parCmParmMaxViaCons.setStatus("current")
_ParMnUpdt_ObjectIdentity = ObjectIdentity
parMnUpdt = _ParMnUpdt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 3)
)


class _ParMnUpdtInterval_Type(Integer32):
    """Custom type parMnUpdtInterval based on Integer32"""
    defaultValue = 15


_ParMnUpdtInterval_Object = MibScalar
parMnUpdtInterval = _ParMnUpdtInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 3, 1),
    _ParMnUpdtInterval_Type()
)
parMnUpdtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parMnUpdtInterval.setStatus("current")
if mibBuilder.loadTexts:
    parMnUpdtInterval.setUnits("seconds")


class _ParMnUpdtNodesPerInt_Type(Integer32):
    """Custom type parMnUpdtNodesPerInt based on Integer32"""
    defaultValue = 20


_ParMnUpdtNodesPerInt_Object = MibScalar
parMnUpdtNodesPerInt = _ParMnUpdtNodesPerInt_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 3, 2),
    _ParMnUpdtNodesPerInt_Type()
)
parMnUpdtNodesPerInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parMnUpdtNodesPerInt.setStatus("current")


class _ParMnUpdtBatchSend_Type(TruthValue):
    """Custom type parMnUpdtBatchSend based on TruthValue"""


_ParMnUpdtBatchSend_Object = MibScalar
parMnUpdtBatchSend = _ParMnUpdtBatchSend_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 3, 3),
    _ParMnUpdtBatchSend_Type()
)
parMnUpdtBatchSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parMnUpdtBatchSend.setStatus("current")
_ParSwFunc_ObjectIdentity = ObjectIdentity
parSwFunc = _ParSwFunc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 4)
)


class _ParSwFuncAbrVsvd_Type(TruthValue):
    """Custom type parSwFuncAbrVsvd based on TruthValue"""


_ParSwFuncAbrVsvd_Object = MibScalar
parSwFuncAbrVsvd = _ParSwFuncAbrVsvd_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 4, 1),
    _ParSwFuncAbrVsvd_Type()
)
parSwFuncAbrVsvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSwFuncAbrVsvd.setStatus("current")


class _ParSwFuncNodeType_Type(Integer32):
    """Custom type parSwFuncNodeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("feeder", 2),
          ("routing", 1))
    )


_ParSwFuncNodeType_Type.__name__ = "Integer32"
_ParSwFuncNodeType_Object = MibScalar
parSwFuncNodeType = _ParSwFuncNodeType_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 4, 2),
    _ParSwFuncNodeType_Type()
)
parSwFuncNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSwFuncNodeType.setStatus("current")
_ParOnOff_ObjectIdentity = ObjectIdentity
parOnOff = _ParOnOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5)
)


class _ParOnOffBackgroundUpdt_Type(TruthValue):
    """Custom type parOnOffBackgroundUpdt based on TruthValue"""


_ParOnOffBackgroundUpdt_Object = MibScalar
parOnOffBackgroundUpdt = _ParOnOffBackgroundUpdt_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 1),
    _ParOnOffBackgroundUpdt_Type()
)
parOnOffBackgroundUpdt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffBackgroundUpdt.setStatus("current")


class _ParOnOffDynamicBwAlloc_Type(TruthValue):
    """Custom type parOnOffDynamicBwAlloc based on TruthValue"""


_ParOnOffDynamicBwAlloc_Object = MibScalar
parOnOffDynamicBwAlloc = _ParOnOffDynamicBwAlloc_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 2),
    _ParOnOffDynamicBwAlloc_Type()
)
parOnOffDynamicBwAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffDynamicBwAlloc.setStatus("current")


class _ParOnOffCmUpdts_Type(TruthValue):
    """Custom type parOnOffCmUpdts based on TruthValue"""


_ParOnOffCmUpdts_Object = MibScalar
parOnOffCmUpdts = _ParOnOffCmUpdts_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 3),
    _ParOnOffCmUpdts_Type()
)
parOnOffCmUpdts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffCmUpdts.setStatus("current")


class _ParOnOffRouting_Type(TruthValue):
    """Custom type parOnOffRouting based on TruthValue"""


_ParOnOffRouting_Object = MibScalar
parOnOffRouting = _ParOnOffRouting_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 4),
    _ParOnOffRouting_Type()
)
parOnOffRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffRouting.setStatus("current")


class _ParOnOffCommFailTest_Type(TruthValue):
    """Custom type parOnOffCommFailTest based on TruthValue"""


_ParOnOffCommFailTest_Object = MibScalar
parOnOffCommFailTest = _ParOnOffCommFailTest_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 5),
    _ParOnOffCommFailTest_Type()
)
parOnOffCommFailTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffCommFailTest.setStatus("current")


class _ParOnOffDrtDelay_Type(TruthValue):
    """Custom type parOnOffDrtDelay based on TruthValue"""


_ParOnOffDrtDelay_Object = MibScalar
parOnOffDrtDelay = _ParOnOffDrtDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 6),
    _ParOnOffDrtDelay_Type()
)
parOnOffDrtDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffDrtDelay.setStatus("current")


class _ParOnOffRenumRec_Type(TruthValue):
    """Custom type parOnOffRenumRec based on TruthValue"""


_ParOnOffRenumRec_Object = MibScalar
parOnOffRenumRec = _ParOnOffRenumRec_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 7),
    _ParOnOffRenumRec_Type()
)
parOnOffRenumRec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffRenumRec.setStatus("current")


class _ParOnOffCommBreak_Type(TruthValue):
    """Custom type parOnOffCommBreak based on TruthValue"""


_ParOnOffCommBreak_Object = MibScalar
parOnOffCommBreak = _ParOnOffCommBreak_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 5, 8),
    _ParOnOffCommBreak_Type()
)
parOnOffCommBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parOnOffCommBreak.setStatus("current")
_ParSysParms_ObjectIdentity = ObjectIdentity
parSysParms = _ParSysParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6)
)


class _ParSysParmsTsPacketAge_Type(Integer32):
    """Custom type parSysParmsTsPacketAge based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ParSysParmsTsPacketAge_Type.__name__ = "Integer32"
_ParSysParmsTsPacketAge_Object = MibScalar
parSysParmsTsPacketAge = _ParSysParmsTsPacketAge_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 1),
    _ParSysParmsTsPacketAge_Type()
)
parSysParmsTsPacketAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSysParmsTsPacketAge.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsTsPacketAge.setUnits("milliseconds")


class _ParSysParmsConnFail_Type(TruthValue):
    """Custom type parSysParmsConnFail based on TruthValue"""


_ParSysParmsConnFail_Object = MibScalar
parSysParmsConnFail = _ParSysParmsConnFail_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 2),
    _ParSysParmsConnFail_Type()
)
parSysParmsConnFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSysParmsConnFail.setStatus("current")
_ParSysParmsVcPollRate_Type = Integer32
_ParSysParmsVcPollRate_Object = MibScalar
parSysParmsVcPollRate = _ParSysParmsVcPollRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 3),
    _ParSysParmsVcPollRate_Type()
)
parSysParmsVcPollRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsVcPollRate.setStatus("current")
_ParSysParmsMaxVDelay_Type = Integer32
_ParSysParmsMaxVDelay_Object = MibScalar
parSysParmsMaxVDelay = _ParSysParmsMaxVDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 4),
    _ParSysParmsMaxVDelay_Type()
)
parSysParmsMaxVDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxVDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxVDelay.setUnits("milliseconds")
_ParSysParmsMaxCDelay_Type = Integer32
_ParSysParmsMaxCDelay_Object = MibScalar
parSysParmsMaxCDelay = _ParSysParmsMaxCDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 5),
    _ParSysParmsMaxCDelay_Type()
)
parSysParmsMaxCDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxCDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxCDelay.setUnits("milliseconds")
_ParSysParmsMaxDDelay_Type = Integer32
_ParSysParmsMaxDDelay_Object = MibScalar
parSysParmsMaxDDelay = _ParSysParmsMaxDDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 6),
    _ParSysParmsMaxDDelay_Type()
)
parSysParmsMaxDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxDDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxDDelay.setUnits("milliseconds")
_ParSysParmsMaxADelay_Type = Integer32
_ParSysParmsMaxADelay_Object = MibScalar
parSysParmsMaxADelay = _ParSysParmsMaxADelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 7),
    _ParSysParmsMaxADelay_Type()
)
parSysParmsMaxADelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxADelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxADelay.setUnits("milliseconds")
_ParSysParmsMaxHsdDelay_Type = Integer32
_ParSysParmsMaxHsdDelay_Object = MibScalar
parSysParmsMaxHsdDelay = _ParSysParmsMaxHsdDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 8),
    _ParSysParmsMaxHsdDelay_Type()
)
parSysParmsMaxHsdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxHsdDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxHsdDelay.setUnits("milliseconds")
_ParSysParmsDeEnable_Type = TruthValue
_ParSysParmsDeEnable_Object = MibScalar
parSysParmsDeEnable = _ParSysParmsDeEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 9),
    _ParSysParmsDeEnable_Type()
)
parSysParmsDeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsDeEnable.setStatus("current")
_ParSysParmsFrStandard_Type = TruthValue
_ParSysParmsFrStandard_Object = MibScalar
parSysParmsFrStandard = _ParSysParmsFrStandard_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 10),
    _ParSysParmsFrStandard_Type()
)
parSysParmsFrStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsFrStandard.setStatus("current")


class _ParSysParmsDrtDelay_Type(TruthValue):
    """Custom type parSysParmsDrtDelay based on TruthValue"""


_ParSysParmsDrtDelay_Object = MibScalar
parSysParmsDrtDelay = _ParSysParmsDrtDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 11),
    _ParSysParmsDrtDelay_Type()
)
parSysParmsDrtDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parSysParmsDrtDelay.setStatus("current")


class _ParSysParmsInvLogAlarmThres_Type(Integer32):
    """Custom type parSysParmsInvLogAlarmThres based on Integer32"""
    defaultValue = 0


_ParSysParmsInvLogAlarmThres_Object = MibScalar
parSysParmsInvLogAlarmThres = _ParSysParmsInvLogAlarmThres_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 12),
    _ParSysParmsInvLogAlarmThres_Type()
)
parSysParmsInvLogAlarmThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsInvLogAlarmThres.setStatus("current")
_ParSysParmsMaxCdpVDelay_Type = Integer32
_ParSysParmsMaxCdpVDelay_Object = MibScalar
parSysParmsMaxCdpVDelay = _ParSysParmsMaxCdpVDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 13),
    _ParSysParmsMaxCdpVDelay_Type()
)
parSysParmsMaxCdpVDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpVDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpVDelay.setUnits("milliseconds")
_ParSysParmsMaxCdpCDelay_Type = Integer32
_ParSysParmsMaxCdpCDelay_Object = MibScalar
parSysParmsMaxCdpCDelay = _ParSysParmsMaxCdpCDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 14),
    _ParSysParmsMaxCdpCDelay_Type()
)
parSysParmsMaxCdpCDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpCDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpCDelay.setUnits("milliseconds")
_ParSysParmsMaxCdpDDelay_Type = Integer32
_ParSysParmsMaxCdpDDelay_Object = MibScalar
parSysParmsMaxCdpDDelay = _ParSysParmsMaxCdpDDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 15),
    _ParSysParmsMaxCdpDDelay_Type()
)
parSysParmsMaxCdpDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpDDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpDDelay.setUnits("milliseconds")
_ParSysParmsMaxCdpADelay_Type = Integer32
_ParSysParmsMaxCdpADelay_Object = MibScalar
parSysParmsMaxCdpADelay = _ParSysParmsMaxCdpADelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 16),
    _ParSysParmsMaxCdpADelay_Type()
)
parSysParmsMaxCdpADelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpADelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpADelay.setUnits("milliseconds")
_ParSysParmsMaxCdpHsdDelay_Type = Integer32
_ParSysParmsMaxCdpHsdDelay_Object = MibScalar
parSysParmsMaxCdpHsdDelay = _ParSysParmsMaxCdpHsdDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 17),
    _ParSysParmsMaxCdpHsdDelay_Type()
)
parSysParmsMaxCdpHsdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpHsdDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxCdpHsdDelay.setUnits("milliseconds")
_ParSysParmsMaxIpcdpVDelay_Type = Integer32
_ParSysParmsMaxIpcdpVDelay_Object = MibScalar
parSysParmsMaxIpcdpVDelay = _ParSysParmsMaxIpcdpVDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 18),
    _ParSysParmsMaxIpcdpVDelay_Type()
)
parSysParmsMaxIpcdpVDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpVDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpVDelay.setUnits("milliseconds")
_ParSysParmsMaxIpcdpCDelay_Type = Integer32
_ParSysParmsMaxIpcdpCDelay_Object = MibScalar
parSysParmsMaxIpcdpCDelay = _ParSysParmsMaxIpcdpCDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 19),
    _ParSysParmsMaxIpcdpCDelay_Type()
)
parSysParmsMaxIpcdpCDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpCDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpCDelay.setUnits("milliseconds")
_ParSysParmsMaxIpcdpDDelay_Type = Integer32
_ParSysParmsMaxIpcdpDDelay_Object = MibScalar
parSysParmsMaxIpcdpDDelay = _ParSysParmsMaxIpcdpDDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 20),
    _ParSysParmsMaxIpcdpDDelay_Type()
)
parSysParmsMaxIpcdpDDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpDDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpDDelay.setUnits("milliseconds")
_ParSysParmsMaxIpcdpADelay_Type = Integer32
_ParSysParmsMaxIpcdpADelay_Object = MibScalar
parSysParmsMaxIpcdpADelay = _ParSysParmsMaxIpcdpADelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 21),
    _ParSysParmsMaxIpcdpADelay_Type()
)
parSysParmsMaxIpcdpADelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpADelay.setStatus("current")
_ParSysParmsMaxIpcdpHsdDelay_Type = Integer32
_ParSysParmsMaxIpcdpHsdDelay_Object = MibScalar
parSysParmsMaxIpcdpHsdDelay = _ParSysParmsMaxIpcdpHsdDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 22),
    _ParSysParmsMaxIpcdpHsdDelay_Type()
)
parSysParmsMaxIpcdpHsdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxIpcdpHsdDelay.setStatus("current")
_ParSysParmsMaxIphsdDelay_Type = Integer32
_ParSysParmsMaxIphsdDelay_Object = MibScalar
parSysParmsMaxIphsdDelay = _ParSysParmsMaxIphsdDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 23),
    _ParSysParmsMaxIphsdDelay_Type()
)
parSysParmsMaxIphsdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsMaxIphsdDelay.setStatus("current")
if mibBuilder.loadTexts:
    parSysParmsMaxIphsdDelay.setUnits("milliseconds")
_ParSysParmsFpdDeJitter_Type = Integer32
_ParSysParmsFpdDeJitter_Object = MibScalar
parSysParmsFpdDeJitter = _ParSysParmsFpdDeJitter_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 6, 24),
    _ParSysParmsFpdDeJitter_Type()
)
parSysParmsFpdDeJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parSysParmsFpdDeJitter.setStatus("current")
_ParNetworkingParms_ObjectIdentity = ObjectIdentity
parNetworkingParms = _ParNetworkingParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7)
)


class _ParNetParmCondInitialStgr_Type(Integer32):
    """Custom type parNetParmCondInitialStgr based on Integer32"""
    defaultValue = 5000


_ParNetParmCondInitialStgr_Object = MibScalar
parNetParmCondInitialStgr = _ParNetParmCondInitialStgr_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 1),
    _ParNetParmCondInitialStgr_Type()
)
parNetParmCondInitialStgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCondInitialStgr.setStatus("current")
if mibBuilder.loadTexts:
    parNetParmCondInitialStgr.setUnits("milliseconds")


class _ParNetParmCondPerNodeInterval_Type(Integer32):
    """Custom type parNetParmCondPerNodeInterval based on Integer32"""
    defaultValue = 30000


_ParNetParmCondPerNodeInterval_Object = MibScalar
parNetParmCondPerNodeInterval = _ParNetParmCondPerNodeInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 2),
    _ParNetParmCondPerNodeInterval_Type()
)
parNetParmCondPerNodeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCondPerNodeInterval.setStatus("current")
if mibBuilder.loadTexts:
    parNetParmCondPerNodeInterval.setUnits("milliseconds")


class _ParNetParmCbDelay_Type(Integer32):
    """Custom type parNetParmCbDelay based on Integer32"""
    defaultValue = 30000


_ParNetParmCbDelay_Object = MibScalar
parNetParmCbDelay = _ParNetParmCbDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 3),
    _ParNetParmCbDelay_Type()
)
parNetParmCbDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCbDelay.setStatus("current")
if mibBuilder.loadTexts:
    parNetParmCbDelay.setUnits("milliseconds")


class _ParNetParmCbOffset_Type(Integer32):
    """Custom type parNetParmCbOffset based on Integer32"""
    defaultValue = 10


_ParNetParmCbOffset_Object = MibScalar
parNetParmCbOffset = _ParNetParmCbOffset_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 4),
    _ParNetParmCbOffset_Type()
)
parNetParmCbOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCbOffset.setStatus("current")


class _ParNetParmMsgTimeout_Type(Integer32):
    """Custom type parNetParmMsgTimeout based on Integer32"""
    defaultValue = 1700


_ParNetParmMsgTimeout_Object = MibScalar
parNetParmMsgTimeout = _ParNetParmMsgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 5),
    _ParNetParmMsgTimeout_Type()
)
parNetParmMsgTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmMsgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    parNetParmMsgTimeout.setUnits("milliseconds")


class _ParNetParmMsgMaxTimeout_Type(Integer32):
    """Custom type parNetParmMsgMaxTimeout based on Integer32"""
    defaultValue = 7


_ParNetParmMsgMaxTimeout_Object = MibScalar
parNetParmMsgMaxTimeout = _ParNetParmMsgMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 6),
    _ParNetParmMsgMaxTimeout_Type()
)
parNetParmMsgMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmMsgMaxTimeout.setStatus("current")


class _ParNetParmMsgMaxTimeoutSat_Type(Integer32):
    """Custom type parNetParmMsgMaxTimeoutSat based on Integer32"""
    defaultValue = 6


_ParNetParmMsgMaxTimeoutSat_Object = MibScalar
parNetParmMsgMaxTimeoutSat = _ParNetParmMsgMaxTimeoutSat_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 7),
    _ParNetParmMsgMaxTimeoutSat_Type()
)
parNetParmMsgMaxTimeoutSat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmMsgMaxTimeoutSat.setStatus("current")


class _ParNetParmBlindMaxTimeout_Type(Integer32):
    """Custom type parNetParmBlindMaxTimeout based on Integer32"""
    defaultValue = 4


_ParNetParmBlindMaxTimeout_Object = MibScalar
parNetParmBlindMaxTimeout = _ParNetParmBlindMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 8),
    _ParNetParmBlindMaxTimeout_Type()
)
parNetParmBlindMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmBlindMaxTimeout.setStatus("current")


class _ParNetParmCbMaxTimeout_Type(Integer32):
    """Custom type parNetParmCbMaxTimeout based on Integer32"""
    defaultValue = 5


_ParNetParmCbMaxTimeout_Object = MibScalar
parNetParmCbMaxTimeout = _ParNetParmCbMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 9),
    _ParNetParmCbMaxTimeout_Type()
)
parNetParmCbMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCbMaxTimeout.setStatus("current")


class _ParNetParmCfTestInterval_Type(Integer32):
    """Custom type parNetParmCfTestInterval based on Integer32"""
    defaultValue = 10000


_ParNetParmCfTestInterval_Object = MibScalar
parNetParmCfTestInterval = _ParNetParmCfTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 10),
    _ParNetParmCfTestInterval_Type()
)
parNetParmCfTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCfTestInterval.setStatus("current")


class _ParNetParmCfTestMultiplier_Type(Integer32):
    """Custom type parNetParmCfTestMultiplier based on Integer32"""
    defaultValue = 3


_ParNetParmCfTestMultiplier_Object = MibScalar
parNetParmCfTestMultiplier = _ParNetParmCfTestMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 11),
    _ParNetParmCfTestMultiplier_Type()
)
parNetParmCfTestMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCfTestMultiplier.setStatus("current")


class _ParNetParmNetwWindowSz_Type(Integer32):
    """Custom type parNetParmNetwWindowSz based on Integer32"""
    defaultValue = 1


_ParNetParmNetwWindowSz_Object = MibScalar
parNetParmNetwWindowSz = _ParNetParmNetwWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 12),
    _ParNetParmNetwWindowSz_Type()
)
parNetParmNetwWindowSz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmNetwWindowSz.setStatus("current")


class _ParNetParmNetwLetWait_Type(Integer32):
    """Custom type parNetParmNetwLetWait based on Integer32"""
    defaultValue = 50


_ParNetParmNetwLetWait_Object = MibScalar
parNetParmNetwLetWait = _ParNetParmNetwLetWait_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 13),
    _ParNetParmNetwLetWait_Type()
)
parNetParmNetwLetWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmNetwLetWait.setStatus("current")
if mibBuilder.loadTexts:
    parNetParmNetwLetWait.setUnits("milliseconds")


class _ParNetParmCfDelay_Type(Integer32):
    """Custom type parNetParmCfDelay based on Integer32"""
    defaultValue = 60


_ParNetParmCfDelay_Object = MibScalar
parNetParmCfDelay = _ParNetParmCfDelay_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 14),
    _ParNetParmCfDelay_Type()
)
parNetParmCfDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmCfDelay.setStatus("current")


class _ParNetParmHighTxRate_Type(Integer32):
    """Custom type parNetParmHighTxRate based on Integer32"""
    defaultValue = 2500


_ParNetParmHighTxRate_Object = MibScalar
parNetParmHighTxRate = _ParNetParmHighTxRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 15),
    _ParNetParmHighTxRate_Type()
)
parNetParmHighTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmHighTxRate.setStatus("current")


class _ParNetParmLowTxRate_Type(Integer32):
    """Custom type parNetParmLowTxRate based on Integer32"""
    defaultValue = 500


_ParNetParmLowTxRate_Object = MibScalar
parNetParmLowTxRate = _ParNetParmLowTxRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 16),
    _ParNetParmLowTxRate_Type()
)
parNetParmLowTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmLowTxRate.setStatus("current")


class _ParNetParmMaxNodeBlks_Type(Integer32):
    """Custom type parNetParmMaxNodeBlks based on Integer32"""
    defaultValue = 3000


_ParNetParmMaxNodeBlks_Object = MibScalar
parNetParmMaxNodeBlks = _ParNetParmMaxNodeBlks_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 17),
    _ParNetParmMaxNodeBlks_Type()
)
parNetParmMaxNodeBlks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmMaxNodeBlks.setStatus("current")


class _ParNetParmTopoMsgSegSz_Type(Integer32):
    """Custom type parNetParmTopoMsgSegSz based on Integer32"""
    defaultValue = 3570


_ParNetParmTopoMsgSegSz_Object = MibScalar
parNetParmTopoMsgSegSz = _ParNetParmTopoMsgSegSz_Object(
    (1, 3, 6, 1, 4, 1, 351, 130, 5, 7, 18),
    _ParNetParmTopoMsgSegSz_Type()
)
parNetParmTopoMsgSegSz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    parNetParmTopoMsgSegSz.setStatus("current")
if mibBuilder.loadTexts:
    parNetParmTopoMsgSegSz.setUnits("bytes")
_CwParMIBConformance_ObjectIdentity = ObjectIdentity
cwParMIBConformance = _CwParMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2)
)
_CwParMIBGroups_ObjectIdentity = ObjectIdentity
cwParMIBGroups = _CwParMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1)
)
_CwParMIBCompliances_ObjectIdentity = ObjectIdentity
cwParMIBCompliances = _CwParMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 2)
)

# Managed Objects groups

cwParCmParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 1)
)
cwParCmParamsGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parCmParmsMaxRoutingBundle"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsRerouteTimer"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsResetTimer"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsDnUpPerPass"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsDnUpTimer"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsRrtErrsPerCycle"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsRrtCycleInterval"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsMaxRrtCycles"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsRrtPauseTime"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsMaxUpdates"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsRerouteGroups"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsMinRrGroupSize"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsRrGroupInc"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsCostBased"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsUseCache"),
        ("CISCO-WAN-PAR-MIB", "parCmParmsUseDelay"),
        ("CISCO-WAN-PAR-MIB", "parCmParmMaxViaCons"))
)
if mibBuilder.loadTexts:
    cwParCmParamsGroup.setStatus("current")

cwParCmParamsUpdateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 2)
)
cwParCmParamsUpdateGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parMnUpdtInterval"),
        ("CISCO-WAN-PAR-MIB", "parMnUpdtNodesPerInt"),
        ("CISCO-WAN-PAR-MIB", "parMnUpdtBatchSend"))
)
if mibBuilder.loadTexts:
    cwParCmParamsUpdateGroup.setStatus("current")

cwParGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 3)
)
cwParGeneralGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parSwFuncAbrVsvd"),
        ("CISCO-WAN-PAR-MIB", "parSwFuncNodeType"),
        ("CISCO-WAN-PAR-MIB", "parOnOffBackgroundUpdt"),
        ("CISCO-WAN-PAR-MIB", "parOnOffDynamicBwAlloc"),
        ("CISCO-WAN-PAR-MIB", "parOnOffCmUpdts"),
        ("CISCO-WAN-PAR-MIB", "parOnOffRouting"),
        ("CISCO-WAN-PAR-MIB", "parOnOffCommFailTest"),
        ("CISCO-WAN-PAR-MIB", "parOnOffDrtDelay"),
        ("CISCO-WAN-PAR-MIB", "parOnOffRenumRec"),
        ("CISCO-WAN-PAR-MIB", "parOnOffCommBreak"))
)
if mibBuilder.loadTexts:
    cwParGeneralGroup.setStatus("current")

cwParSysParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 4)
)
cwParSysParamsGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parSysParmsTsPacketAge"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsConnFail"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsVcPollRate"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxVDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxCDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxDDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxADelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxHsdDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsDeEnable"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsFrStandard"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsDrtDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsInvLogAlarmThres"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxCdpVDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxCdpCDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxCdpDDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxCdpADelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxCdpHsdDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxIpcdpVDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxIpcdpCDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxIpcdpDDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxIpcdpADelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxIpcdpHsdDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsMaxIphsdDelay"),
        ("CISCO-WAN-PAR-MIB", "parSysParmsFpdDeJitter"))
)
if mibBuilder.loadTexts:
    cwParSysParamsGroup.setStatus("current")

cwParNetParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 5)
)
cwParNetParamsGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parNetParmCondInitialStgr"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCondPerNodeInterval"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCbDelay"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCbOffset"),
        ("CISCO-WAN-PAR-MIB", "parNetParmMsgTimeout"),
        ("CISCO-WAN-PAR-MIB", "parNetParmMsgMaxTimeout"),
        ("CISCO-WAN-PAR-MIB", "parNetParmMsgMaxTimeoutSat"),
        ("CISCO-WAN-PAR-MIB", "parNetParmBlindMaxTimeout"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCbMaxTimeout"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCfTestInterval"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCfTestMultiplier"),
        ("CISCO-WAN-PAR-MIB", "parNetParmNetwWindowSz"),
        ("CISCO-WAN-PAR-MIB", "parNetParmNetwLetWait"),
        ("CISCO-WAN-PAR-MIB", "parNetParmCfDelay"),
        ("CISCO-WAN-PAR-MIB", "parNetParmHighTxRate"),
        ("CISCO-WAN-PAR-MIB", "parNetParmLowTxRate"),
        ("CISCO-WAN-PAR-MIB", "parNetParmMaxNodeBlks"),
        ("CISCO-WAN-PAR-MIB", "parNetParmTopoMsgSegSz"))
)
if mibBuilder.loadTexts:
    cwParNetParamsGroup.setStatus("current")

cwParNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 6)
)
cwParNodeGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parSnNodeId"),
        ("CISCO-WAN-PAR-MIB", "parSnNodeIP"),
        ("CISCO-WAN-PAR-MIB", "parSnNodeName"),
        ("CISCO-WAN-PAR-MIB", "parSnRevision"),
        ("CISCO-WAN-PAR-MIB", "parSnNodeAlarmStatus"),
        ("CISCO-WAN-PAR-MIB", "parSnNumberOfTrunks"))
)
if mibBuilder.loadTexts:
    cwParNodeGroup.setStatus("current")

cwParInterfaceConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 7)
)
cwParInterfaceConfGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parIfLogicalInterface"),
        ("CISCO-WAN-PAR-MIB", "parIfType"),
        ("CISCO-WAN-PAR-MIB", "parIfOperStatus"),
        ("CISCO-WAN-PAR-MIB", "parIfTxBw"),
        ("CISCO-WAN-PAR-MIB", "parIfRxBw"),
        ("CISCO-WAN-PAR-MIB", "parIfMaxConn"),
        ("CISCO-WAN-PAR-MIB", "parIfHiAddrMin"),
        ("CISCO-WAN-PAR-MIB", "parIfHiAddrMax"),
        ("CISCO-WAN-PAR-MIB", "parIfLoAddrMin"),
        ("CISCO-WAN-PAR-MIB", "parIfLoAddrMax"))
)
if mibBuilder.loadTexts:
    cwParInterfaceConfGroup.setStatus("current")

cwParTrunkConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 8)
)
cwParTrunkConfGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parTrkId"),
        ("CISCO-WAN-PAR-MIB", "parTrkStatReserve"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgCcRestrict"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgLineType"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgPassSync"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgDerouteDelay"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassFst"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassFr"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassNts"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassTs"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassVoice"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassCbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassVbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgTrafficClassAbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgAdminStatus"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgRoutingCost"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgVpcConids"),
        ("CISCO-WAN-PAR-MIB", "parTrkCnfgVccConids"),
        ("CISCO-WAN-PAR-MIB", "parTrkLocalSlotNumber"),
        ("CISCO-WAN-PAR-MIB", "parTrkLocalPortNumber"),
        ("CISCO-WAN-PAR-MIB", "parTrkLocalVTrunkId"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteNodeId"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteTrunkId"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteSlotNumber"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemotePortNumber"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteVTrunkId"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteNodeIP"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteNodeType"),
        ("CISCO-WAN-PAR-MIB", "parTrkRemoteNodeName"),
        ("CISCO-WAN-PAR-MIB", "parTrkAlarmStatus"),
        ("CISCO-WAN-PAR-MIB", "parTrkAlarmType"),
        ("CISCO-WAN-PAR-MIB", "parTrkLineLoad"),
        ("CISCO-WAN-PAR-MIB", "parTrkBwCapacity"))
)
if mibBuilder.loadTexts:
    cwParTrunkConfGroup.setStatus("current")

cwParTrunkLoadConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 9)
)
cwParTrunkLoadConfGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedCbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedCbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedVbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedVbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedAbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedAbr"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedNts"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedNts"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedTs"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedTs"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedVoice"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedVoice"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedBdataA"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedBdataA"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadXmtUsedBdataB"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadRcvUsedBdataB"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadVccConidsUsed"),
        ("CISCO-WAN-PAR-MIB", "parTrkLoadVpcConidsUsed"))
)
if mibBuilder.loadTexts:
    cwParTrunkLoadConfGroup.setStatus("current")

cwParConnConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 10)
)
cwParConnConfGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parConnLocalSlot"),
        ("CISCO-WAN-PAR-MIB", "parConnLocalPort"),
        ("CISCO-WAN-PAR-MIB", "parConnLocalVpi"),
        ("CISCO-WAN-PAR-MIB", "parConnLocalVci"),
        ("CISCO-WAN-PAR-MIB", "parConnMasterShip"),
        ("CISCO-WAN-PAR-MIB", "parConnLocalVcIndx"),
        ("CISCO-WAN-PAR-MIB", "parConnLocalEndpt"),
        ("CISCO-WAN-PAR-MIB", "parConnRemoteNodeName"),
        ("CISCO-WAN-PAR-MIB", "parConnRemoteSlot"),
        ("CISCO-WAN-PAR-MIB", "parConnRemotePort"),
        ("CISCO-WAN-PAR-MIB", "parConnRemoteVpi"),
        ("CISCO-WAN-PAR-MIB", "parConnRemoteVci"),
        ("CISCO-WAN-PAR-MIB", "parConnRemoteVcIndx"),
        ("CISCO-WAN-PAR-MIB", "parConnRemoteEndpt"),
        ("CISCO-WAN-PAR-MIB", "parConnOperStatus"),
        ("CISCO-WAN-PAR-MIB", "parConnAdminStatus"),
        ("CISCO-WAN-PAR-MIB", "parConnRoute"),
        ("CISCO-WAN-PAR-MIB", "parPrefRoute"),
        ("CISCO-WAN-PAR-MIB", "parConnFailRsn"),
        ("CISCO-WAN-PAR-MIB", "parRrtFailRsn"),
        ("CISCO-WAN-PAR-MIB", "parConnRstrTyp"),
        ("CISCO-WAN-PAR-MIB", "parConnRstrZcs"),
        ("CISCO-WAN-PAR-MIB", "parConnCos"))
)
if mibBuilder.loadTexts:
    cwParConnConfGroup.setStatus("current")

cwParClockConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 1, 11)
)
cwParClockConfGroup.setObjects(
      *(("CISCO-WAN-PAR-MIB", "parClockIndex"),
        ("CISCO-WAN-PAR-MIB", "parClockType"),
        ("CISCO-WAN-PAR-MIB", "parClockCurSource"),
        ("CISCO-WAN-PAR-MIB", "parClockSource"),
        ("CISCO-WAN-PAR-MIB", "parClockSourceId"),
        ("CISCO-WAN-PAR-MIB", "parClockPath"))
)
if mibBuilder.loadTexts:
    cwParClockConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwParCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 63, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwParCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-PAR-MIB",
    **{"parSelfNode": parSelfNode,
       "parSnNodeId": parSnNodeId,
       "parSnNodeIP": parSnNodeIP,
       "parSnNodeName": parSnNodeName,
       "parSnRevision": parSnRevision,
       "parSnNodeAlarmStatus": parSnNodeAlarmStatus,
       "parSnNumberOfTrunks": parSnNumberOfTrunks,
       "parInterfaces": parInterfaces,
       "parIfTable": parIfTable,
       "parIfEntry": parIfEntry,
       "parIfLogicalInterface": parIfLogicalInterface,
       "parIfType": parIfType,
       "parIfOperStatus": parIfOperStatus,
       "parIfTxBw": parIfTxBw,
       "parIfRxBw": parIfRxBw,
       "parIfMaxConn": parIfMaxConn,
       "parIfHiAddrMin": parIfHiAddrMin,
       "parIfHiAddrMax": parIfHiAddrMax,
       "parIfLoAddrMin": parIfLoAddrMin,
       "parIfLoAddrMax": parIfLoAddrMax,
       "parTrkTable": parTrkTable,
       "parTrkEntry": parTrkEntry,
       "parTrkId": parTrkId,
       "parTrkStatReserve": parTrkStatReserve,
       "parTrkCnfgCcRestrict": parTrkCnfgCcRestrict,
       "parTrkCnfgLineType": parTrkCnfgLineType,
       "parTrkCnfgPassSync": parTrkCnfgPassSync,
       "parTrkCnfgDerouteDelay": parTrkCnfgDerouteDelay,
       "parTrkCnfgTrafficClassFst": parTrkCnfgTrafficClassFst,
       "parTrkCnfgTrafficClassFr": parTrkCnfgTrafficClassFr,
       "parTrkCnfgTrafficClassNts": parTrkCnfgTrafficClassNts,
       "parTrkCnfgTrafficClassTs": parTrkCnfgTrafficClassTs,
       "parTrkCnfgTrafficClassVoice": parTrkCnfgTrafficClassVoice,
       "parTrkCnfgTrafficClassCbr": parTrkCnfgTrafficClassCbr,
       "parTrkCnfgTrafficClassVbr": parTrkCnfgTrafficClassVbr,
       "parTrkCnfgTrafficClassAbr": parTrkCnfgTrafficClassAbr,
       "parTrkCnfgAdminStatus": parTrkCnfgAdminStatus,
       "parTrkCnfgRoutingCost": parTrkCnfgRoutingCost,
       "parTrkCnfgVccConids": parTrkCnfgVccConids,
       "parTrkCnfgVpcConids": parTrkCnfgVpcConids,
       "parTrkLocalSlotNumber": parTrkLocalSlotNumber,
       "parTrkLocalPortNumber": parTrkLocalPortNumber,
       "parTrkLocalVTrunkId": parTrkLocalVTrunkId,
       "parTrkRemoteNodeId": parTrkRemoteNodeId,
       "parTrkRemoteTrunkId": parTrkRemoteTrunkId,
       "parTrkRemoteSlotNumber": parTrkRemoteSlotNumber,
       "parTrkRemotePortNumber": parTrkRemotePortNumber,
       "parTrkRemoteVTrunkId": parTrkRemoteVTrunkId,
       "parTrkRemoteNodeIP": parTrkRemoteNodeIP,
       "parTrkRemoteNodeType": parTrkRemoteNodeType,
       "parTrkRemoteNodeName": parTrkRemoteNodeName,
       "parTrkAlarmStatus": parTrkAlarmStatus,
       "parTrkAlarmType": parTrkAlarmType,
       "parTrkBwCapacity": parTrkBwCapacity,
       "parTrkLineLoad": parTrkLineLoad,
       "parTrkLoadTable": parTrkLoadTable,
       "parTrkLoadEntry": parTrkLoadEntry,
       "parTrkLoadXmtUsedCbr": parTrkLoadXmtUsedCbr,
       "parTrkLoadRcvUsedCbr": parTrkLoadRcvUsedCbr,
       "parTrkLoadXmtUsedVbr": parTrkLoadXmtUsedVbr,
       "parTrkLoadRcvUsedVbr": parTrkLoadRcvUsedVbr,
       "parTrkLoadXmtUsedAbr": parTrkLoadXmtUsedAbr,
       "parTrkLoadRcvUsedAbr": parTrkLoadRcvUsedAbr,
       "parTrkLoadXmtUsedNts": parTrkLoadXmtUsedNts,
       "parTrkLoadRcvUsedNts": parTrkLoadRcvUsedNts,
       "parTrkLoadXmtUsedTs": parTrkLoadXmtUsedTs,
       "parTrkLoadRcvUsedTs": parTrkLoadRcvUsedTs,
       "parTrkLoadXmtUsedVoice": parTrkLoadXmtUsedVoice,
       "parTrkLoadRcvUsedVoice": parTrkLoadRcvUsedVoice,
       "parTrkLoadXmtUsedBdataA": parTrkLoadXmtUsedBdataA,
       "parTrkLoadRcvUsedBdataA": parTrkLoadRcvUsedBdataA,
       "parTrkLoadXmtUsedBdataB": parTrkLoadXmtUsedBdataB,
       "parTrkLoadRcvUsedBdataB": parTrkLoadRcvUsedBdataB,
       "parTrkLoadVccConidsUsed": parTrkLoadVccConidsUsed,
       "parTrkLoadVpcConidsUsed": parTrkLoadVpcConidsUsed,
       "parConnection": parConnection,
       "parConnectionTable": parConnectionTable,
       "parConnectionEntry": parConnectionEntry,
       "parConnLocalSlot": parConnLocalSlot,
       "parConnLocalPort": parConnLocalPort,
       "parConnLocalVpi": parConnLocalVpi,
       "parConnLocalVci": parConnLocalVci,
       "parConnMasterShip": parConnMasterShip,
       "parConnLocalVcIndx": parConnLocalVcIndx,
       "parConnLocalEndpt": parConnLocalEndpt,
       "parConnRemoteNodeName": parConnRemoteNodeName,
       "parConnRemoteSlot": parConnRemoteSlot,
       "parConnRemotePort": parConnRemotePort,
       "parConnRemoteVpi": parConnRemoteVpi,
       "parConnRemoteVci": parConnRemoteVci,
       "parConnRemoteVcIndx": parConnRemoteVcIndx,
       "parConnOperStatus": parConnOperStatus,
       "parConnAdminStatus": parConnAdminStatus,
       "parConnRoute": parConnRoute,
       "parConnRemoteEndpt": parConnRemoteEndpt,
       "parPrefRoute": parPrefRoute,
       "parConnFailRsn": parConnFailRsn,
       "parRrtFailRsn": parRrtFailRsn,
       "parConnRstrTyp": parConnRstrTyp,
       "parConnRstrZcs": parConnRstrZcs,
       "parConnCos": parConnCos,
       "parNetworkClock": parNetworkClock,
       "parClockTable": parClockTable,
       "parClockEntry": parClockEntry,
       "parClockIndex": parClockIndex,
       "parClockType": parClockType,
       "parClockSource": parClockSource,
       "parClockCurSource": parClockCurSource,
       "parClockSourceId": parClockSourceId,
       "parClockPath": parClockPath,
       "parConfigParms": parConfigParms,
       "parVsiConfigParms": parVsiConfigParms,
       "parCmParms": parCmParms,
       "parCmParmsMaxRoutingBundle": parCmParmsMaxRoutingBundle,
       "parCmParmsRerouteTimer": parCmParmsRerouteTimer,
       "parCmParmsResetTimer": parCmParmsResetTimer,
       "parCmParmsDnUpPerPass": parCmParmsDnUpPerPass,
       "parCmParmsDnUpTimer": parCmParmsDnUpTimer,
       "parCmParmsRrtErrsPerCycle": parCmParmsRrtErrsPerCycle,
       "parCmParmsRrtCycleInterval": parCmParmsRrtCycleInterval,
       "parCmParmsMaxRrtCycles": parCmParmsMaxRrtCycles,
       "parCmParmsRrtPauseTime": parCmParmsRrtPauseTime,
       "parCmParmsMaxUpdates": parCmParmsMaxUpdates,
       "parCmParmsRerouteGroups": parCmParmsRerouteGroups,
       "parCmParmsMinRrGroupSize": parCmParmsMinRrGroupSize,
       "parCmParmsRrGroupInc": parCmParmsRrGroupInc,
       "parCmParmsCostBased": parCmParmsCostBased,
       "parCmParmsUseCache": parCmParmsUseCache,
       "parCmParmsUseDelay": parCmParmsUseDelay,
       "parCmParmMaxViaCons": parCmParmMaxViaCons,
       "parMnUpdt": parMnUpdt,
       "parMnUpdtInterval": parMnUpdtInterval,
       "parMnUpdtNodesPerInt": parMnUpdtNodesPerInt,
       "parMnUpdtBatchSend": parMnUpdtBatchSend,
       "parSwFunc": parSwFunc,
       "parSwFuncAbrVsvd": parSwFuncAbrVsvd,
       "parSwFuncNodeType": parSwFuncNodeType,
       "parOnOff": parOnOff,
       "parOnOffBackgroundUpdt": parOnOffBackgroundUpdt,
       "parOnOffDynamicBwAlloc": parOnOffDynamicBwAlloc,
       "parOnOffCmUpdts": parOnOffCmUpdts,
       "parOnOffRouting": parOnOffRouting,
       "parOnOffCommFailTest": parOnOffCommFailTest,
       "parOnOffDrtDelay": parOnOffDrtDelay,
       "parOnOffRenumRec": parOnOffRenumRec,
       "parOnOffCommBreak": parOnOffCommBreak,
       "parSysParms": parSysParms,
       "parSysParmsTsPacketAge": parSysParmsTsPacketAge,
       "parSysParmsConnFail": parSysParmsConnFail,
       "parSysParmsVcPollRate": parSysParmsVcPollRate,
       "parSysParmsMaxVDelay": parSysParmsMaxVDelay,
       "parSysParmsMaxCDelay": parSysParmsMaxCDelay,
       "parSysParmsMaxDDelay": parSysParmsMaxDDelay,
       "parSysParmsMaxADelay": parSysParmsMaxADelay,
       "parSysParmsMaxHsdDelay": parSysParmsMaxHsdDelay,
       "parSysParmsDeEnable": parSysParmsDeEnable,
       "parSysParmsFrStandard": parSysParmsFrStandard,
       "parSysParmsDrtDelay": parSysParmsDrtDelay,
       "parSysParmsInvLogAlarmThres": parSysParmsInvLogAlarmThres,
       "parSysParmsMaxCdpVDelay": parSysParmsMaxCdpVDelay,
       "parSysParmsMaxCdpCDelay": parSysParmsMaxCdpCDelay,
       "parSysParmsMaxCdpDDelay": parSysParmsMaxCdpDDelay,
       "parSysParmsMaxCdpADelay": parSysParmsMaxCdpADelay,
       "parSysParmsMaxCdpHsdDelay": parSysParmsMaxCdpHsdDelay,
       "parSysParmsMaxIpcdpVDelay": parSysParmsMaxIpcdpVDelay,
       "parSysParmsMaxIpcdpCDelay": parSysParmsMaxIpcdpCDelay,
       "parSysParmsMaxIpcdpDDelay": parSysParmsMaxIpcdpDDelay,
       "parSysParmsMaxIpcdpADelay": parSysParmsMaxIpcdpADelay,
       "parSysParmsMaxIpcdpHsdDelay": parSysParmsMaxIpcdpHsdDelay,
       "parSysParmsMaxIphsdDelay": parSysParmsMaxIphsdDelay,
       "parSysParmsFpdDeJitter": parSysParmsFpdDeJitter,
       "parNetworkingParms": parNetworkingParms,
       "parNetParmCondInitialStgr": parNetParmCondInitialStgr,
       "parNetParmCondPerNodeInterval": parNetParmCondPerNodeInterval,
       "parNetParmCbDelay": parNetParmCbDelay,
       "parNetParmCbOffset": parNetParmCbOffset,
       "parNetParmMsgTimeout": parNetParmMsgTimeout,
       "parNetParmMsgMaxTimeout": parNetParmMsgMaxTimeout,
       "parNetParmMsgMaxTimeoutSat": parNetParmMsgMaxTimeoutSat,
       "parNetParmBlindMaxTimeout": parNetParmBlindMaxTimeout,
       "parNetParmCbMaxTimeout": parNetParmCbMaxTimeout,
       "parNetParmCfTestInterval": parNetParmCfTestInterval,
       "parNetParmCfTestMultiplier": parNetParmCfTestMultiplier,
       "parNetParmNetwWindowSz": parNetParmNetwWindowSz,
       "parNetParmNetwLetWait": parNetParmNetwLetWait,
       "parNetParmCfDelay": parNetParmCfDelay,
       "parNetParmHighTxRate": parNetParmHighTxRate,
       "parNetParmLowTxRate": parNetParmLowTxRate,
       "parNetParmMaxNodeBlks": parNetParmMaxNodeBlks,
       "parNetParmTopoMsgSegSz": parNetParmTopoMsgSegSz,
       "ciscoWanParMIB": ciscoWanParMIB,
       "cwParMIBConformance": cwParMIBConformance,
       "cwParMIBGroups": cwParMIBGroups,
       "cwParCmParamsGroup": cwParCmParamsGroup,
       "cwParCmParamsUpdateGroup": cwParCmParamsUpdateGroup,
       "cwParGeneralGroup": cwParGeneralGroup,
       "cwParSysParamsGroup": cwParSysParamsGroup,
       "cwParNetParamsGroup": cwParNetParamsGroup,
       "cwParNodeGroup": cwParNodeGroup,
       "cwParInterfaceConfGroup": cwParInterfaceConfGroup,
       "cwParTrunkConfGroup": cwParTrunkConfGroup,
       "cwParTrunkLoadConfGroup": cwParTrunkLoadConfGroup,
       "cwParConnConfGroup": cwParConnConfGroup,
       "cwParClockConfGroup": cwParClockConfGroup,
       "cwParMIBCompliances": cwParMIBCompliances,
       "cwParCompliance": cwParCompliance}
)
