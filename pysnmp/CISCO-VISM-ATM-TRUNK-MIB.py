# SNMP MIB module (CISCO-VISM-ATM-TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-ATM-TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:45 2024
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

(vismChanGrp,
 voice) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "vismChanGrp",
    "voice")

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

ciscoVismAtmTrunkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 87)
)
ciscoVismAtmTrunkMIB.setRevisions(
        ("2004-04-14 00:00",
         "2004-02-05 00:00",
         "2003-12-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VismAal2CidGrp_ObjectIdentity = ObjectIdentity
vismAal2CidGrp = _VismAal2CidGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4)
)
_VismAal2CidCnfTable_Object = MibTable
vismAal2CidCnfTable = _VismAal2CidCnfTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1)
)
if mibBuilder.loadTexts:
    vismAal2CidCnfTable.setStatus("current")
_VismAal2CidEntry_Object = MibTableRow
vismAal2CidEntry = _VismAal2CidEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1)
)
vismAal2CidEntry.setIndexNames(
    (0, "CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidLcn"),
    (0, "CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidNum"),
)
if mibBuilder.loadTexts:
    vismAal2CidEntry.setStatus("current")


class _VismAal2CidNum_Type(Integer32):
    """Custom type vismAal2CidNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_VismAal2CidNum_Type.__name__ = "Integer32"
_VismAal2CidNum_Object = MibTableColumn
vismAal2CidNum = _VismAal2CidNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 1),
    _VismAal2CidNum_Type()
)
vismAal2CidNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismAal2CidNum.setStatus("current")


class _VismAal2CidLcn_Type(Integer32):
    """Custom type vismAal2CidLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_VismAal2CidLcn_Type.__name__ = "Integer32"
_VismAal2CidLcn_Object = MibTableColumn
vismAal2CidLcn = _VismAal2CidLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 2),
    _VismAal2CidLcn_Type()
)
vismAal2CidLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismAal2CidLcn.setStatus("current")


class _VismAal2EndptNum_Type(Integer32):
    """Custom type vismAal2EndptNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VismAal2EndptNum_Type.__name__ = "Integer32"
_VismAal2EndptNum_Object = MibTableColumn
vismAal2EndptNum = _VismAal2EndptNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 3),
    _VismAal2EndptNum_Type()
)
vismAal2EndptNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2EndptNum.setStatus("current")


class _VismAal2CidRowStatus_Type(Integer32):
    """Custom type vismAal2CidRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_VismAal2CidRowStatus_Type.__name__ = "Integer32"
_VismAal2CidRowStatus_Object = MibTableColumn
vismAal2CidRowStatus = _VismAal2CidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 4),
    _VismAal2CidRowStatus_Type()
)
vismAal2CidRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidRowStatus.setStatus("current")
_VismAal2CidType3Redundancy_Type = TruthValue
_VismAal2CidType3Redundancy_Object = MibTableColumn
vismAal2CidType3Redundancy = _VismAal2CidType3Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 5),
    _VismAal2CidType3Redundancy_Type()
)
vismAal2CidType3Redundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidType3Redundancy.setStatus("current")


class _VismAal2CidVad_Type(TruthValue):
    """Custom type vismAal2CidVad based on TruthValue"""


_VismAal2CidVad_Object = MibTableColumn
vismAal2CidVad = _VismAal2CidVad_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 6),
    _VismAal2CidVad_Type()
)
vismAal2CidVad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidVad.setStatus("current")


class _VismAal2CidProfileType_Type(Integer32):
    """Custom type vismAal2CidProfileType based on Integer32"""
    defaultValue = 3

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
        *(("atm", 2),
          ("custom", 3),
          ("itu", 1),
          ("none", 4))
    )


_VismAal2CidProfileType_Type.__name__ = "Integer32"
_VismAal2CidProfileType_Object = MibTableColumn
vismAal2CidProfileType = _VismAal2CidProfileType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 7),
    _VismAal2CidProfileType_Type()
)
vismAal2CidProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidProfileType.setStatus("current")


class _VismAal2CidProfileNum_Type(Integer32):
    """Custom type vismAal2CidProfileNum based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismAal2CidProfileNum_Type.__name__ = "Integer32"
_VismAal2CidProfileNum_Object = MibTableColumn
vismAal2CidProfileNum = _VismAal2CidProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 8),
    _VismAal2CidProfileNum_Type()
)
vismAal2CidProfileNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidProfileNum.setStatus("current")


class _VismAal2CidCodecType_Type(Integer32):
    """Custom type vismAal2CidCodecType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 6),
          ("g711a", 2),
          ("g711u", 1),
          ("g723ah", 12),
          ("g723al", 14),
          ("g723h", 11),
          ("g723l", 13),
          ("g726r16000", 7),
          ("g726r24000", 8),
          ("g726r32000", 3),
          ("g726r40000", 9),
          ("g729a", 4),
          ("g729ab", 5),
          ("lossless", 15))
    )


_VismAal2CidCodecType_Type.__name__ = "Integer32"
_VismAal2CidCodecType_Object = MibTableColumn
vismAal2CidCodecType = _VismAal2CidCodecType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 9),
    _VismAal2CidCodecType_Type()
)
vismAal2CidCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidCodecType.setStatus("current")


class _VismAal2CidDtmfTransport_Type(TruthValue):
    """Custom type vismAal2CidDtmfTransport based on TruthValue"""


_VismAal2CidDtmfTransport_Object = MibTableColumn
vismAal2CidDtmfTransport = _VismAal2CidDtmfTransport_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 10),
    _VismAal2CidDtmfTransport_Type()
)
vismAal2CidDtmfTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidDtmfTransport.setStatus("current")
_VismAal2CidCasTransport_Type = TruthValue
_VismAal2CidCasTransport_Object = MibTableColumn
vismAal2CidCasTransport = _VismAal2CidCasTransport_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 11),
    _VismAal2CidCasTransport_Type()
)
vismAal2CidCasTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidCasTransport.setStatus("current")


class _VismAal2CidEcanEnable_Type(TruthValue):
    """Custom type vismAal2CidEcanEnable based on TruthValue"""


_VismAal2CidEcanEnable_Object = MibTableColumn
vismAal2CidEcanEnable = _VismAal2CidEcanEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 12),
    _VismAal2CidEcanEnable_Type()
)
vismAal2CidEcanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidEcanEnable.setStatus("current")


class _VismAal2InitVadTimer_Type(Integer32):
    """Custom type vismAal2InitVadTimer based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 65535),
    )


_VismAal2InitVadTimer_Type.__name__ = "Integer32"
_VismAal2InitVadTimer_Object = MibTableColumn
vismAal2InitVadTimer = _VismAal2InitVadTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 13),
    _VismAal2InitVadTimer_Type()
)
vismAal2InitVadTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2InitVadTimer.setStatus("current")
if mibBuilder.loadTexts:
    vismAal2InitVadTimer.setUnits("milliseconds")


class _VismAal2CnfPktPeriod_Type(Integer32):
    """Custom type vismAal2CnfPktPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              20,
              30,
              40)
        )
    )
    namedValues = NamedValues(
        *(("five", 5),
          ("fourty", 40),
          ("ten", 10),
          ("thirty", 30),
          ("twenty", 20))
    )


_VismAal2CnfPktPeriod_Type.__name__ = "Integer32"
_VismAal2CnfPktPeriod_Object = MibTableColumn
vismAal2CnfPktPeriod = _VismAal2CnfPktPeriod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 14),
    _VismAal2CnfPktPeriod_Type()
)
vismAal2CnfPktPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CnfPktPeriod.setStatus("current")


class _VismAal2CidICSEnable_Type(TruthValue):
    """Custom type vismAal2CidICSEnable based on TruthValue"""


_VismAal2CidICSEnable_Object = MibTableColumn
vismAal2CidICSEnable = _VismAal2CidICSEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 15),
    _VismAal2CidICSEnable_Type()
)
vismAal2CidICSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidICSEnable.setStatus("current")


class _VismAal2CidState_Type(Integer32):
    """Custom type vismAal2CidState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cidStateActive", 1),
          ("cidStateFailed", 2))
    )


_VismAal2CidState_Type.__name__ = "Integer32"
_VismAal2CidState_Object = MibTableColumn
vismAal2CidState = _VismAal2CidState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 16),
    _VismAal2CidState_Type()
)
vismAal2CidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismAal2CidState.setStatus("current")


class _VismAal2CidFailReason_Type(Integer32):
    """Custom type vismAal2CidFailReason based on Integer32"""
    defaultValue = 4

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
        *(("both", 3),
          ("highLevel", 2),
          ("notFail", 4),
          ("self", 1))
    )


_VismAal2CidFailReason_Type.__name__ = "Integer32"
_VismAal2CidFailReason_Object = MibTableColumn
vismAal2CidFailReason = _VismAal2CidFailReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 17),
    _VismAal2CidFailReason_Type()
)
vismAal2CidFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismAal2CidFailReason.setStatus("current")


class _VismAal2CidAdminState_Type(Integer32):
    """Custom type vismAal2CidAdminState based on Integer32"""
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
        *(("cidCommandedOutOfService", 3),
          ("cidInService", 2),
          ("cidPendingInService", 1),
          ("cidPendingOutOfService", 4),
          ("cidUnknownState", 5))
    )


_VismAal2CidAdminState_Type.__name__ = "Integer32"
_VismAal2CidAdminState_Object = MibTableColumn
vismAal2CidAdminState = _VismAal2CidAdminState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 3, 4, 1, 1, 18),
    _VismAal2CidAdminState_Type()
)
vismAal2CidAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismAal2CidAdminState.setStatus("current")
_BearerConnGrp_ObjectIdentity = ObjectIdentity
bearerConnGrp = _BearerConnGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9)
)
_BearerConnTable_Object = MibTable
bearerConnTable = _BearerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1)
)
if mibBuilder.loadTexts:
    bearerConnTable.setStatus("current")
_BearerConnEntry_Object = MibTableRow
bearerConnEntry = _BearerConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1)
)
bearerConnEntry.setIndexNames(
    (0, "CISCO-VISM-ATM-TRUNK-MIB", "bearerEndptNum"),
)
if mibBuilder.loadTexts:
    bearerConnEntry.setStatus("current")


class _BearerEndptNum_Type(Integer32):
    """Custom type bearerEndptNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BearerEndptNum_Type.__name__ = "Integer32"
_BearerEndptNum_Object = MibTableColumn
bearerEndptNum = _BearerEndptNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 1),
    _BearerEndptNum_Type()
)
bearerEndptNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerEndptNum.setStatus("current")
_BearerCid_Type = Integer32
_BearerCid_Object = MibTableColumn
bearerCid = _BearerCid_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 2),
    _BearerCid_Type()
)
bearerCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCid.setStatus("current")


class _BearerLcn_Type(Integer32):
    """Custom type bearerLcn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(131, 510),
    )


_BearerLcn_Type.__name__ = "Integer32"
_BearerLcn_Object = MibTableColumn
bearerLcn = _BearerLcn_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 3),
    _BearerLcn_Type()
)
bearerLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerLcn.setStatus("current")
_BearerSentPkts_Type = Counter32
_BearerSentPkts_Object = MibTableColumn
bearerSentPkts = _BearerSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 4),
    _BearerSentPkts_Type()
)
bearerSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerSentPkts.setStatus("current")
_BearerRcvdPkts_Type = Counter32
_BearerRcvdPkts_Object = MibTableColumn
bearerRcvdPkts = _BearerRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 5),
    _BearerRcvdPkts_Type()
)
bearerRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerRcvdPkts.setStatus("current")
_BearerSentOctets_Type = Counter32
_BearerSentOctets_Object = MibTableColumn
bearerSentOctets = _BearerSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 6),
    _BearerSentOctets_Type()
)
bearerSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerSentOctets.setStatus("current")
_BearerRcvdOctets_Type = Counter32
_BearerRcvdOctets_Object = MibTableColumn
bearerRcvdOctets = _BearerRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 7),
    _BearerRcvdOctets_Type()
)
bearerRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerRcvdOctets.setStatus("current")
_BearerLostPkts_Type = Counter32
_BearerLostPkts_Object = MibTableColumn
bearerLostPkts = _BearerLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 8),
    _BearerLostPkts_Type()
)
bearerLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerLostPkts.setStatus("current")
_BearerJitter_Type = Integer32
_BearerJitter_Object = MibTableColumn
bearerJitter = _BearerJitter_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 9),
    _BearerJitter_Type()
)
bearerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerJitter.setStatus("current")
if mibBuilder.loadTexts:
    bearerJitter.setUnits("milliseconds")
_BearerLatency_Type = Integer32
_BearerLatency_Object = MibTableColumn
bearerLatency = _BearerLatency_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 10),
    _BearerLatency_Type()
)
bearerLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerLatency.setStatus("current")
if mibBuilder.loadTexts:
    bearerLatency.setUnits("milliseconds")
_BearerAal2ExtAISCnts_Type = Counter32
_BearerAal2ExtAISCnts_Object = MibTableColumn
bearerAal2ExtAISCnts = _BearerAal2ExtAISCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 11),
    _BearerAal2ExtAISCnts_Type()
)
bearerAal2ExtAISCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerAal2ExtAISCnts.setStatus("current")
_BearerAal2ExtRAICnts_Type = Counter32
_BearerAal2ExtRAICnts_Object = MibTableColumn
bearerAal2ExtRAICnts = _BearerAal2ExtRAICnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 12),
    _BearerAal2ExtRAICnts_Type()
)
bearerAal2ExtRAICnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerAal2ExtRAICnts.setStatus("current")
_BearerAal2ConnAISCnts_Type = Counter32
_BearerAal2ConnAISCnts_Object = MibTableColumn
bearerAal2ConnAISCnts = _BearerAal2ConnAISCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 13),
    _BearerAal2ConnAISCnts_Type()
)
bearerAal2ConnAISCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerAal2ConnAISCnts.setStatus("current")
_BearerAal2ConnRDICnts_Type = Counter32
_BearerAal2ConnRDICnts_Object = MibTableColumn
bearerAal2ConnRDICnts = _BearerAal2ConnRDICnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 14),
    _BearerAal2ConnRDICnts_Type()
)
bearerAal2ConnRDICnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerAal2ConnRDICnts.setStatus("current")


class _BearerCntClrButton_Type(Integer32):
    """Custom type bearerCntClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_BearerCntClrButton_Type.__name__ = "Integer32"
_BearerCntClrButton_Object = MibTableColumn
bearerCntClrButton = _BearerCntClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 15),
    _BearerCntClrButton_Type()
)
bearerCntClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bearerCntClrButton.setStatus("current")


class _BearerPeakXmtCellRate_Type(Unsigned32):
    """Custom type bearerPeakXmtCellRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BearerPeakXmtCellRate_Type.__name__ = "Unsigned32"
_BearerPeakXmtCellRate_Object = MibTableColumn
bearerPeakXmtCellRate = _BearerPeakXmtCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 16),
    _BearerPeakXmtCellRate_Type()
)
bearerPeakXmtCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerPeakXmtCellRate.setStatus("current")
if mibBuilder.loadTexts:
    bearerPeakXmtCellRate.setUnits("cells-per-second")


class _BearerCurrentXmtCellRate_Type(Unsigned32):
    """Custom type bearerCurrentXmtCellRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BearerCurrentXmtCellRate_Type.__name__ = "Unsigned32"
_BearerCurrentXmtCellRate_Object = MibTableColumn
bearerCurrentXmtCellRate = _BearerCurrentXmtCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 17),
    _BearerCurrentXmtCellRate_Type()
)
bearerCurrentXmtCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentXmtCellRate.setStatus("current")
if mibBuilder.loadTexts:
    bearerCurrentXmtCellRate.setUnits("cells-per-second")


class _BearerPeakRcvCellRate_Type(Unsigned32):
    """Custom type bearerPeakRcvCellRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BearerPeakRcvCellRate_Type.__name__ = "Unsigned32"
_BearerPeakRcvCellRate_Object = MibTableColumn
bearerPeakRcvCellRate = _BearerPeakRcvCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 18),
    _BearerPeakRcvCellRate_Type()
)
bearerPeakRcvCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerPeakRcvCellRate.setStatus("current")
if mibBuilder.loadTexts:
    bearerPeakRcvCellRate.setUnits("cells-per-second")


class _BearerCurrentRcvCellRate_Type(Unsigned32):
    """Custom type bearerCurrentRcvCellRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BearerCurrentRcvCellRate_Type.__name__ = "Unsigned32"
_BearerCurrentRcvCellRate_Object = MibTableColumn
bearerCurrentRcvCellRate = _BearerCurrentRcvCellRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 19),
    _BearerCurrentRcvCellRate_Type()
)
bearerCurrentRcvCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentRcvCellRate.setStatus("current")
if mibBuilder.loadTexts:
    bearerCurrentRcvCellRate.setUnits("cells-per-second")
_BearerCurrentExtAISRcvCnts_Type = Counter32
_BearerCurrentExtAISRcvCnts_Object = MibTableColumn
bearerCurrentExtAISRcvCnts = _BearerCurrentExtAISRcvCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 20),
    _BearerCurrentExtAISRcvCnts_Type()
)
bearerCurrentExtAISRcvCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentExtAISRcvCnts.setStatus("current")
_BearerCurrentExtRAIRcvCnts_Type = Counter32
_BearerCurrentExtRAIRcvCnts_Object = MibTableColumn
bearerCurrentExtRAIRcvCnts = _BearerCurrentExtRAIRcvCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 21),
    _BearerCurrentExtRAIRcvCnts_Type()
)
bearerCurrentExtRAIRcvCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentExtRAIRcvCnts.setStatus("current")
_BearerCurrentConnAISCnts_Type = Counter32
_BearerCurrentConnAISCnts_Object = MibTableColumn
bearerCurrentConnAISCnts = _BearerCurrentConnAISCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 22),
    _BearerCurrentConnAISCnts_Type()
)
bearerCurrentConnAISCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentConnAISCnts.setStatus("current")
_BearerCurrentConnRDICnts_Type = Counter32
_BearerCurrentConnRDICnts_Object = MibTableColumn
bearerCurrentConnRDICnts = _BearerCurrentConnRDICnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 23),
    _BearerCurrentConnRDICnts_Type()
)
bearerCurrentConnRDICnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentConnRDICnts.setStatus("current")
_BearerCurrentExtAISXmtCnts_Type = Counter32
_BearerCurrentExtAISXmtCnts_Object = MibTableColumn
bearerCurrentExtAISXmtCnts = _BearerCurrentExtAISXmtCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 24),
    _BearerCurrentExtAISXmtCnts_Type()
)
bearerCurrentExtAISXmtCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentExtAISXmtCnts.setStatus("current")
_BearerCurrentExtRAIXmtCnts_Type = Counter32
_BearerCurrentExtRAIXmtCnts_Object = MibTableColumn
bearerCurrentExtRAIXmtCnts = _BearerCurrentExtRAIXmtCnts_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 5, 9, 1, 1, 25),
    _BearerCurrentExtRAIXmtCnts_Type()
)
bearerCurrentExtRAIXmtCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bearerCurrentExtRAIXmtCnts.setStatus("current")
_CvismAtmTrunkMIBConformance_ObjectIdentity = ObjectIdentity
cvismAtmTrunkMIBConformance = _CvismAtmTrunkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2)
)
_CvismAtmTrunkMIBGroups_ObjectIdentity = ObjectIdentity
cvismAtmTrunkMIBGroups = _CvismAtmTrunkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 1)
)
_CvismAtmTrunkMIBCompliances_ObjectIdentity = ObjectIdentity
cvismAtmTrunkMIBCompliances = _CvismAtmTrunkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 2)
)

# Managed Objects groups

ciscoVismBearerConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 1, 1)
)
ciscoVismBearerConnGroup.setObjects(
      *(("CISCO-VISM-ATM-TRUNK-MIB", "bearerEndptNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCid"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerLcn"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerSentPkts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerRcvdPkts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerSentOctets"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerRcvdOctets"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerLostPkts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerJitter"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerLatency"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ExtAISCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ExtRAICnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ConnAISCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ConnRDICnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCntClrButton"))
)
if mibBuilder.loadTexts:
    ciscoVismBearerConnGroup.setStatus("deprecated")

ciscoVismAAl2CidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 1, 2)
)
ciscoVismAAl2CidGroup.setObjects(
      *(("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidLcn"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2EndptNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidRowStatus"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidType3Redundancy"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidVad"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidProfileType"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidProfileNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidCodecType"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidDtmfTransport"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidCasTransport"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidEcanEnable"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2InitVadTimer"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CnfPktPeriod"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidICSEnable"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidState"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidFailReason"))
)
if mibBuilder.loadTexts:
    ciscoVismAAl2CidGroup.setStatus("deprecated")

ciscoVismAAl2CidGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 1, 3)
)
ciscoVismAAl2CidGroupRev1.setObjects(
      *(("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidLcn"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2EndptNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidRowStatus"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidType3Redundancy"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidVad"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidProfileType"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidProfileNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidCodecType"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidDtmfTransport"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidCasTransport"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidEcanEnable"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2InitVadTimer"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CnfPktPeriod"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidICSEnable"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidState"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidFailReason"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "vismAal2CidAdminState"))
)
if mibBuilder.loadTexts:
    ciscoVismAAl2CidGroupRev1.setStatus("current")

ciscoVismBearerConnGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 1, 4)
)
ciscoVismBearerConnGroupRev1.setObjects(
      *(("CISCO-VISM-ATM-TRUNK-MIB", "bearerEndptNum"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCid"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerLcn"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerSentPkts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerRcvdPkts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerSentOctets"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerRcvdOctets"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerLostPkts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerJitter"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerLatency"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ExtAISCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ExtRAICnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ConnAISCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerAal2ConnRDICnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCntClrButton"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerPeakXmtCellRate"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentXmtCellRate"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerPeakRcvCellRate"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentRcvCellRate"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentExtAISRcvCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentExtRAIRcvCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentConnAISCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentConnRDICnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentExtAISXmtCnts"),
        ("CISCO-VISM-ATM-TRUNK-MIB", "bearerCurrentExtRAIXmtCnts"))
)
if mibBuilder.loadTexts:
    ciscoVismBearerConnGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvismAtmTrunkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cvismAtmTrunkCompliance.setStatus(
        "deprecated"
    )

cvismAtmTrunkComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cvismAtmTrunkComplianceRev1.setStatus(
        "deprecated"
    )

cvismAtmTrunkComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 87, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cvismAtmTrunkComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-ATM-TRUNK-MIB",
    **{"vismAal2CidGrp": vismAal2CidGrp,
       "vismAal2CidCnfTable": vismAal2CidCnfTable,
       "vismAal2CidEntry": vismAal2CidEntry,
       "vismAal2CidNum": vismAal2CidNum,
       "vismAal2CidLcn": vismAal2CidLcn,
       "vismAal2EndptNum": vismAal2EndptNum,
       "vismAal2CidRowStatus": vismAal2CidRowStatus,
       "vismAal2CidType3Redundancy": vismAal2CidType3Redundancy,
       "vismAal2CidVad": vismAal2CidVad,
       "vismAal2CidProfileType": vismAal2CidProfileType,
       "vismAal2CidProfileNum": vismAal2CidProfileNum,
       "vismAal2CidCodecType": vismAal2CidCodecType,
       "vismAal2CidDtmfTransport": vismAal2CidDtmfTransport,
       "vismAal2CidCasTransport": vismAal2CidCasTransport,
       "vismAal2CidEcanEnable": vismAal2CidEcanEnable,
       "vismAal2InitVadTimer": vismAal2InitVadTimer,
       "vismAal2CnfPktPeriod": vismAal2CnfPktPeriod,
       "vismAal2CidICSEnable": vismAal2CidICSEnable,
       "vismAal2CidState": vismAal2CidState,
       "vismAal2CidFailReason": vismAal2CidFailReason,
       "vismAal2CidAdminState": vismAal2CidAdminState,
       "bearerConnGrp": bearerConnGrp,
       "bearerConnTable": bearerConnTable,
       "bearerConnEntry": bearerConnEntry,
       "bearerEndptNum": bearerEndptNum,
       "bearerCid": bearerCid,
       "bearerLcn": bearerLcn,
       "bearerSentPkts": bearerSentPkts,
       "bearerRcvdPkts": bearerRcvdPkts,
       "bearerSentOctets": bearerSentOctets,
       "bearerRcvdOctets": bearerRcvdOctets,
       "bearerLostPkts": bearerLostPkts,
       "bearerJitter": bearerJitter,
       "bearerLatency": bearerLatency,
       "bearerAal2ExtAISCnts": bearerAal2ExtAISCnts,
       "bearerAal2ExtRAICnts": bearerAal2ExtRAICnts,
       "bearerAal2ConnAISCnts": bearerAal2ConnAISCnts,
       "bearerAal2ConnRDICnts": bearerAal2ConnRDICnts,
       "bearerCntClrButton": bearerCntClrButton,
       "bearerPeakXmtCellRate": bearerPeakXmtCellRate,
       "bearerCurrentXmtCellRate": bearerCurrentXmtCellRate,
       "bearerPeakRcvCellRate": bearerPeakRcvCellRate,
       "bearerCurrentRcvCellRate": bearerCurrentRcvCellRate,
       "bearerCurrentExtAISRcvCnts": bearerCurrentExtAISRcvCnts,
       "bearerCurrentExtRAIRcvCnts": bearerCurrentExtRAIRcvCnts,
       "bearerCurrentConnAISCnts": bearerCurrentConnAISCnts,
       "bearerCurrentConnRDICnts": bearerCurrentConnRDICnts,
       "bearerCurrentExtAISXmtCnts": bearerCurrentExtAISXmtCnts,
       "bearerCurrentExtRAIXmtCnts": bearerCurrentExtRAIXmtCnts,
       "ciscoVismAtmTrunkMIB": ciscoVismAtmTrunkMIB,
       "cvismAtmTrunkMIBConformance": cvismAtmTrunkMIBConformance,
       "cvismAtmTrunkMIBGroups": cvismAtmTrunkMIBGroups,
       "ciscoVismBearerConnGroup": ciscoVismBearerConnGroup,
       "ciscoVismAAl2CidGroup": ciscoVismAAl2CidGroup,
       "ciscoVismAAl2CidGroupRev1": ciscoVismAAl2CidGroupRev1,
       "ciscoVismBearerConnGroupRev1": ciscoVismBearerConnGroupRev1,
       "cvismAtmTrunkMIBCompliances": cvismAtmTrunkMIBCompliances,
       "cvismAtmTrunkCompliance": cvismAtmTrunkCompliance,
       "cvismAtmTrunkComplianceRev1": cvismAtmTrunkComplianceRev1,
       "cvismAtmTrunkComplianceRev2": cvismAtmTrunkComplianceRev2}
)
