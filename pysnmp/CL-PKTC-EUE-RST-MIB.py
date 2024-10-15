# SNMP MIB module (CL-PKTC-EUE-RST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CL-PKTC-EUE-RST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:33 2024
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

(pktcEUEDevOpIndex,) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-DEV-MIB",
    "pktcEUEDevOpIndex")

(PktcEUETCActStatus,
 PktcEUETCActStatusInfo) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-TC-MIB",
    "PktcEUETCActStatus",
    "PktcEUETCActStatusInfo")

(pktcApplicationMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcApplicationMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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


# MODULE-IDENTITY

pktcEUERSTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcRSTTCTONEANNC(OctetString, TextualConvention):
    status = "current"


class PktcRSTTCFeatID(Integer32, TextualConvention):
    status = "current"
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("announcement", 4),
          ("autoCallback", 20),
          ("autoRecall", 19),
          ("basicCall", 3),
          ("busyLineVerify", 21),
          ("callForwarding", 11),
          ("callHold", 13),
          ("callTransfer", 14),
          ("callWaiting", 12),
          ("callerId", 7),
          ("callerIdBlocking", 9),
          ("callerIdDelivery", 10),
          ("callerIdDisplay", 8),
          ("digitMap", 2),
          ("doNotDisturb", 16),
          ("emergencySvc", 22),
          ("msgWaitIndicator", 18),
          ("noAnsTimeout", 6),
          ("other", 1),
          ("scf", 23),
          ("statusChange", 5),
          ("subscriberPIN", 17),
          ("threeWayCalling", 15))
    )



class PktcEUETCRSTAppPrfIndexType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class PktcEUETCRSTAppFeatIndexType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



# MIB Managed Objects in the order of their OIDs

_PktcEUERSTNotifications_ObjectIdentity = ObjectIdentity
pktcEUERSTNotifications = _PktcEUERSTNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 0)
)
_PktcEUERSTObjects_ObjectIdentity = ObjectIdentity
pktcEUERSTObjects = _PktcEUERSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1)
)
_PktcEUERSTProfile_ObjectIdentity = ObjectIdentity
pktcEUERSTProfile = _PktcEUERSTProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1)
)


class _PktcEUERSTProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEUERSTProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUERSTProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEUERSTProfileVersion_Object = MibScalar
pktcEUERSTProfileVersion = _PktcEUERSTProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 1),
    _PktcEUERSTProfileVersion_Type()
)
pktcEUERSTProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTProfileVersion.setStatus("current")
_PktcEUERSTAppProfileToFeatTable_Object = MibTable
pktcEUERSTAppProfileToFeatTable = _PktcEUERSTAppProfileToFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileToFeatTable.setStatus("current")
_PktcEUERSTAppProfileToFeatEntry_Object = MibTableRow
pktcEUERSTAppProfileToFeatEntry = _PktcEUERSTAppProfileToFeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1)
)
pktcEUERSTAppProfileToFeatEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppProfileIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppFeatIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileToFeatEntry.setStatus("current")
_PktcEUERSTAppProfileIndex_Type = PktcEUETCRSTAppPrfIndexType
_PktcEUERSTAppProfileIndex_Object = MibTableColumn
pktcEUERSTAppProfileIndex = _PktcEUERSTAppProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 1),
    _PktcEUERSTAppProfileIndex_Type()
)
pktcEUERSTAppProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileIndex.setStatus("current")
_PktcEUERSTAppFeatIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTAppFeatIndex_Object = MibTableColumn
pktcEUERSTAppFeatIndex = _PktcEUERSTAppFeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 2),
    _PktcEUERSTAppFeatIndex_Type()
)
pktcEUERSTAppFeatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTAppFeatIndex.setStatus("current")
_PktcEUERSTAppFeatID_Type = PktcRSTTCFeatID
_PktcEUERSTAppFeatID_Object = MibTableColumn
pktcEUERSTAppFeatID = _PktcEUERSTAppFeatID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 3),
    _PktcEUERSTAppFeatID_Type()
)
pktcEUERSTAppFeatID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppFeatID.setStatus("current")
_PktcEUERSTAppFeatIndexRef_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTAppFeatIndexRef_Object = MibTableColumn
pktcEUERSTAppFeatIndexRef = _PktcEUERSTAppFeatIndexRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 4),
    _PktcEUERSTAppFeatIndexRef_Type()
)
pktcEUERSTAppFeatIndexRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppFeatIndexRef.setStatus("current")
_PktcEUERSTAppNwActStat_Type = PktcEUETCActStatus
_PktcEUERSTAppNwActStat_Object = MibTableColumn
pktcEUERSTAppNwActStat = _PktcEUERSTAppNwActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 5),
    _PktcEUERSTAppNwActStat_Type()
)
pktcEUERSTAppNwActStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppNwActStat.setStatus("current")
_PktcEUERSTAppNwActStatInfo_Type = PktcEUETCActStatusInfo
_PktcEUERSTAppNwActStatInfo_Object = MibTableColumn
pktcEUERSTAppNwActStatInfo = _PktcEUERSTAppNwActStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 6),
    _PktcEUERSTAppNwActStatInfo_Type()
)
pktcEUERSTAppNwActStatInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUERSTAppNwActStatInfo.setStatus("current")
_PktcEUERSTAppEUEActStat_Type = PktcEUETCActStatus
_PktcEUERSTAppEUEActStat_Object = MibTableColumn
pktcEUERSTAppEUEActStat = _PktcEUERSTAppEUEActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 7),
    _PktcEUERSTAppEUEActStat_Type()
)
pktcEUERSTAppEUEActStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTAppEUEActStat.setStatus("current")
_PktcEUERSTAppEUEActStatInfo_Type = PktcEUETCActStatusInfo
_PktcEUERSTAppEUEActStatInfo_Object = MibTableColumn
pktcEUERSTAppEUEActStatInfo = _PktcEUERSTAppEUEActStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 8),
    _PktcEUERSTAppEUEActStatInfo_Type()
)
pktcEUERSTAppEUEActStatInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTAppEUEActStatInfo.setStatus("current")
_PktcEUERSTAppRowActStatus_Type = RowStatus
_PktcEUERSTAppRowActStatus_Object = MibTableColumn
pktcEUERSTAppRowActStatus = _PktcEUERSTAppRowActStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 2, 1, 9),
    _PktcEUERSTAppRowActStatus_Type()
)
pktcEUERSTAppRowActStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTAppRowActStatus.setStatus("current")
_PktcEUERSTDigitMapFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTDigitMapFeat = _PktcEUERSTDigitMapFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3)
)
_PktcEUERSTDMTimerT_Type = Unsigned32
_PktcEUERSTDMTimerT_Object = MibScalar
pktcEUERSTDMTimerT = _PktcEUERSTDMTimerT_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 1),
    _PktcEUERSTDMTimerT_Type()
)
pktcEUERSTDMTimerT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTDMTimerT.setStatus("current")
_PktcEUERSTDMTimerS_Type = Unsigned32
_PktcEUERSTDMTimerS_Object = MibScalar
pktcEUERSTDMTimerS = _PktcEUERSTDMTimerS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 2),
    _PktcEUERSTDMTimerS_Type()
)
pktcEUERSTDMTimerS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTDMTimerS.setStatus("current")
_PktcEUERSTDMTimerL_Type = Unsigned32
_PktcEUERSTDMTimerL_Object = MibScalar
pktcEUERSTDMTimerL = _PktcEUERSTDMTimerL_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 3),
    _PktcEUERSTDMTimerL_Type()
)
pktcEUERSTDMTimerL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTDMTimerL.setStatus("current")
_PktcEUERSTDMTimerZ_Type = Unsigned32
_PktcEUERSTDMTimerZ_Object = MibScalar
pktcEUERSTDMTimerZ = _PktcEUERSTDMTimerZ_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 4),
    _PktcEUERSTDMTimerZ_Type()
)
pktcEUERSTDMTimerZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTDMTimerZ.setStatus("current")
_PktcEUERSTDigitMapProfileTable_Object = MibTable
pktcEUERSTDigitMapProfileTable = _PktcEUERSTDigitMapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapProfileTable.setStatus("current")
_PktcEUERSTDigitMapProfileEntry_Object = MibTableRow
pktcEUERSTDigitMapProfileEntry = _PktcEUERSTDigitMapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 5, 1)
)
pktcEUERSTDigitMapProfileEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapProfileEntry.setStatus("current")
_PktcEUERSTDMIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTDMIndex_Object = MibTableColumn
pktcEUERSTDMIndex = _PktcEUERSTDMIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 5, 1, 1),
    _PktcEUERSTDMIndex_Type()
)
pktcEUERSTDMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTDMIndex.setStatus("current")


class _PktcEUERSTDMValue_Type(OctetString):
    """Custom type pktcEUERSTDMValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )


_PktcEUERSTDMValue_Type.__name__ = "OctetString"
_PktcEUERSTDMValue_Object = MibTableColumn
pktcEUERSTDMValue = _PktcEUERSTDMValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 1, 3, 5, 1, 2),
    _PktcEUERSTDMValue_Type()
)
pktcEUERSTDMValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUERSTDMValue.setStatus("current")
_PktcEUERSTFeatures_ObjectIdentity = ObjectIdentity
pktcEUERSTFeatures = _PktcEUERSTFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2)
)
_PktcEUERSTBasicCallFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTBasicCallFeat = _PktcEUERSTBasicCallFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1)
)
_PktcEUERSTBasicCallTable_Object = MibTable
pktcEUERSTBasicCallTable = _PktcEUERSTBasicCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTBasicCallTable.setStatus("current")
_PktcEUERSTBasicCallEntry_Object = MibTableRow
pktcEUERSTBasicCallEntry = _PktcEUERSTBasicCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1)
)
pktcEUERSTBasicCallEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTBCallIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTBasicCallEntry.setStatus("current")
_PktcEUERSTBCallIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTBCallIndex_Object = MibTableColumn
pktcEUERSTBCallIndex = _PktcEUERSTBCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1, 1),
    _PktcEUERSTBCallIndex_Type()
)
pktcEUERSTBCallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTBCallIndex.setStatus("current")
_PktcEUERSTBCallSDP_Type = SnmpAdminString
_PktcEUERSTBCallSDP_Object = MibTableColumn
pktcEUERSTBCallSDP = _PktcEUERSTBCallSDP_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 1, 1, 2),
    _PktcEUERSTBCallSDP_Type()
)
pktcEUERSTBCallSDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTBCallSDP.setStatus("current")
_PktcEUERSTNfBasicCallTable_Object = MibTable
pktcEUERSTNfBasicCallTable = _PktcEUERSTNfBasicCallTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBasicCallTable.setStatus("current")
_PktcEUERSTNfBasicCallEntry_Object = MibTableRow
pktcEUERSTNfBasicCallEntry = _PktcEUERSTNfBasicCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1)
)
pktcEUERSTNfBasicCallEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBasicCallEntry.setStatus("current")
_PktcEUERSTNfBCallByeDelay_Type = Unsigned32
_PktcEUERSTNfBCallByeDelay_Object = MibTableColumn
pktcEUERSTNfBCallByeDelay = _PktcEUERSTNfBCallByeDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 1),
    _PktcEUERSTNfBCallByeDelay_Type()
)
pktcEUERSTNfBCallByeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallByeDelay.setStatus("current")
_PktcEUERSTNfBCallOrigDTTimer_Type = Unsigned32
_PktcEUERSTNfBCallOrigDTTimer_Object = MibTableColumn
pktcEUERSTNfBCallOrigDTTimer = _PktcEUERSTNfBCallOrigDTTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 2),
    _PktcEUERSTNfBCallOrigDTTimer_Type()
)
pktcEUERSTNfBCallOrigDTTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallOrigDTTimer.setStatus("current")
_PktcEUERSTNfBCallTermOHErrSig_Type = PktcRSTTCTONEANNC
_PktcEUERSTNfBCallTermOHErrSig_Object = MibTableColumn
pktcEUERSTNfBCallTermOHErrSig = _PktcEUERSTNfBCallTermOHErrSig_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 3),
    _PktcEUERSTNfBCallTermOHErrSig_Type()
)
pktcEUERSTNfBCallTermOHErrSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallTermOHErrSig.setStatus("current")
_PktcEUERSTNfBCallTermErrSigTimer_Type = Unsigned32
_PktcEUERSTNfBCallTermErrSigTimer_Object = MibTableColumn
pktcEUERSTNfBCallTermErrSigTimer = _PktcEUERSTNfBCallTermErrSigTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 4),
    _PktcEUERSTNfBCallTermErrSigTimer_Type()
)
pktcEUERSTNfBCallTermErrSigTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallTermErrSigTimer.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone1_Type = PktcRSTTCTONEANNC
_PktcEUERSTNfBCallPermSeqTone1_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone1 = _PktcEUERSTNfBCallPermSeqTone1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 5),
    _PktcEUERSTNfBCallPermSeqTone1_Type()
)
pktcEUERSTNfBCallPermSeqTone1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone1.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer1_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer1_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer1 = _PktcEUERSTNfBCallPermSeqTimer1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 6),
    _PktcEUERSTNfBCallPermSeqTimer1_Type()
)
pktcEUERSTNfBCallPermSeqTimer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer1.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone2_Type = PktcRSTTCTONEANNC
_PktcEUERSTNfBCallPermSeqTone2_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone2 = _PktcEUERSTNfBCallPermSeqTone2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 7),
    _PktcEUERSTNfBCallPermSeqTone2_Type()
)
pktcEUERSTNfBCallPermSeqTone2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone2.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer2_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer2_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer2 = _PktcEUERSTNfBCallPermSeqTimer2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 8),
    _PktcEUERSTNfBCallPermSeqTimer2_Type()
)
pktcEUERSTNfBCallPermSeqTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer2.setStatus("current")
_PktcEUERSTNfBCallPermSeqTone3_Type = PktcRSTTCTONEANNC
_PktcEUERSTNfBCallPermSeqTone3_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTone3 = _PktcEUERSTNfBCallPermSeqTone3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 9),
    _PktcEUERSTNfBCallPermSeqTone3_Type()
)
pktcEUERSTNfBCallPermSeqTone3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTone3.setStatus("current")
_PktcEUERSTNfBCallPermSeqTimer3_Type = Unsigned32
_PktcEUERSTNfBCallPermSeqTimer3_Object = MibTableColumn
pktcEUERSTNfBCallPermSeqTimer3 = _PktcEUERSTNfBCallPermSeqTimer3_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 10),
    _PktcEUERSTNfBCallPermSeqTimer3_Type()
)
pktcEUERSTNfBCallPermSeqTimer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallPermSeqTimer3.setStatus("current")
_PktcEUERSTNfBCallLORTimer_Type = Unsigned32
_PktcEUERSTNfBCallLORTimer_Object = MibTableColumn
pktcEUERSTNfBCallLORTimer = _PktcEUERSTNfBCallLORTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 11),
    _PktcEUERSTNfBCallLORTimer_Type()
)
pktcEUERSTNfBCallLORTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallLORTimer.setStatus("current")


class _PktcEUERSTNfBCallNEMDSCPValue_Type(Unsigned32):
    """Custom type pktcEUERSTNfBCallNEMDSCPValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTNfBCallNEMDSCPValue_Type.__name__ = "Unsigned32"
_PktcEUERSTNfBCallNEMDSCPValue_Object = MibTableColumn
pktcEUERSTNfBCallNEMDSCPValue = _PktcEUERSTNfBCallNEMDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 1, 2, 1, 12),
    _PktcEUERSTNfBCallNEMDSCPValue_Type()
)
pktcEUERSTNfBCallNEMDSCPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBCallNEMDSCPValue.setStatus("current")
_PktcEUERSTAncFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTAncFeat = _PktcEUERSTAncFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2)
)
_PktcEUERSTAncTable_Object = MibTable
pktcEUERSTAncTable = _PktcEUERSTAncTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTAncTable.setStatus("current")
_PktcEUERSTAncEntry_Object = MibTableRow
pktcEUERSTAncEntry = _PktcEUERSTAncEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1)
)
pktcEUERSTAncEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTAncIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAncEntry.setStatus("current")
_PktcEUERSTAncIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTAncIndex_Object = MibTableColumn
pktcEUERSTAncIndex = _PktcEUERSTAncIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1, 1),
    _PktcEUERSTAncIndex_Type()
)
pktcEUERSTAncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTAncIndex.setStatus("current")
_PktcEUERSTAncPrefLang_Type = SnmpAdminString
_PktcEUERSTAncPrefLang_Object = MibTableColumn
pktcEUERSTAncPrefLang = _PktcEUERSTAncPrefLang_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 1, 1, 2),
    _PktcEUERSTAncPrefLang_Type()
)
pktcEUERSTAncPrefLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTAncPrefLang.setStatus("current")
_PktcEUERSTNfAncTable_Object = MibTable
pktcEUERSTNfAncTable = _PktcEUERSTNfAncTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncTable.setStatus("current")
_PktcEUERSTNfAncEntry_Object = MibTableRow
pktcEUERSTNfAncEntry = _PktcEUERSTNfAncEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1)
)
pktcEUERSTNfAncEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncEntry.setStatus("current")
_PktcEUERSTNfAncRes_Type = SnmpAdminString
_PktcEUERSTNfAncRes_Object = MibTableColumn
pktcEUERSTNfAncRes = _PktcEUERSTNfAncRes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 1),
    _PktcEUERSTNfAncRes_Type()
)
pktcEUERSTNfAncRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncRes.setStatus("current")
_PktcEUERSTNfAncDomain_Type = SnmpAdminString
_PktcEUERSTNfAncDomain_Object = MibTableColumn
pktcEUERSTNfAncDomain = _PktcEUERSTNfAncDomain_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 2),
    _PktcEUERSTNfAncDomain_Type()
)
pktcEUERSTNfAncDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncDomain.setStatus("current")
_PktcEUERSTNfAncPath_Type = SnmpAdminString
_PktcEUERSTNfAncPath_Object = MibTableColumn
pktcEUERSTNfAncPath = _PktcEUERSTNfAncPath_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 3),
    _PktcEUERSTNfAncPath_Type()
)
pktcEUERSTNfAncPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncPath.setStatus("current")
_PktcEUERSTNfAncMIMEType_Type = SnmpAdminString
_PktcEUERSTNfAncMIMEType_Object = MibTableColumn
pktcEUERSTNfAncMIMEType = _PktcEUERSTNfAncMIMEType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 2, 1, 4),
    _PktcEUERSTNfAncMIMEType_Type()
)
pktcEUERSTNfAncMIMEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMIMEType.setStatus("current")
_PktcEUERSTNfAncMapTable_Object = MibTable
pktcEUERSTNfAncMapTable = _PktcEUERSTNfAncMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapTable.setStatus("current")
_PktcEUERSTNfAncMapEntry_Object = MibTableRow
pktcEUERSTNfAncMapEntry = _PktcEUERSTNfAncMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1)
)
pktcEUERSTNfAncMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncRspCode"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMapEntry.setStatus("current")


class _PktcEUERSTNfAncRspCode_Type(Unsigned32):
    """Custom type pktcEUERSTNfAncRspCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_PktcEUERSTNfAncRspCode_Type.__name__ = "Unsigned32"
_PktcEUERSTNfAncRspCode_Object = MibTableColumn
pktcEUERSTNfAncRspCode = _PktcEUERSTNfAncRspCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1, 1),
    _PktcEUERSTNfAncRspCode_Type()
)
pktcEUERSTNfAncRspCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncRspCode.setStatus("current")
_PktcEUERSTNfAncURI_Type = SnmpAdminString
_PktcEUERSTNfAncURI_Object = MibTableColumn
pktcEUERSTNfAncURI = _PktcEUERSTNfAncURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 3, 1, 2),
    _PktcEUERSTNfAncURI_Type()
)
pktcEUERSTNfAncURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncURI.setStatus("current")
_PktcEUERSTNfAncMediaMapTable_Object = MibTable
pktcEUERSTNfAncMediaMapTable = _PktcEUERSTNfAncMediaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaMapTable.setStatus("current")
_PktcEUERSTNfAncMediaMapEntry_Object = MibTableRow
pktcEUERSTNfAncMediaMapEntry = _PktcEUERSTNfAncMediaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1)
)
pktcEUERSTNfAncMediaMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaId"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaMapEntry.setStatus("current")
_PktcEUERSTNfAncMediaId_Type = SnmpAdminString
_PktcEUERSTNfAncMediaId_Object = MibTableColumn
pktcEUERSTNfAncMediaId = _PktcEUERSTNfAncMediaId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 1),
    _PktcEUERSTNfAncMediaId_Type()
)
pktcEUERSTNfAncMediaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaId.setStatus("current")
_PktcEUERSTNfAncMediaURI_Type = SnmpAdminString
_PktcEUERSTNfAncMediaURI_Object = MibTableColumn
pktcEUERSTNfAncMediaURI = _PktcEUERSTNfAncMediaURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 2),
    _PktcEUERSTNfAncMediaURI_Type()
)
pktcEUERSTNfAncMediaURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaURI.setStatus("current")
_PktcEUERSTNfAncMediaCachMaxAge_Type = Unsigned32
_PktcEUERSTNfAncMediaCachMaxAge_Object = MibTableColumn
pktcEUERSTNfAncMediaCachMaxAge = _PktcEUERSTNfAncMediaCachMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 4, 1, 3),
    _PktcEUERSTNfAncMediaCachMaxAge_Type()
)
pktcEUERSTNfAncMediaCachMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncMediaCachMaxAge.setStatus("current")
_PktcEUERSTNfAncLocalMediaTable_Object = MibTable
pktcEUERSTNfAncLocalMediaTable = _PktcEUERSTNfAncLocalMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLocalMediaTable.setStatus("current")
_PktcEUERSTNfAncLocalMediaEntry_Object = MibTableRow
pktcEUERSTNfAncLocalMediaEntry = _PktcEUERSTNfAncLocalMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1)
)
pktcEUERSTNfAncLocalMediaEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaURI"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLocalMediaEntry.setStatus("current")
_PktcEUERSTNfAncLclMediaURI_Type = SnmpAdminString
_PktcEUERSTNfAncLclMediaURI_Object = MibTableColumn
pktcEUERSTNfAncLclMediaURI = _PktcEUERSTNfAncLclMediaURI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 1),
    _PktcEUERSTNfAncLclMediaURI_Type()
)
pktcEUERSTNfAncLclMediaURI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaURI.setStatus("current")
_PktcEUERSTNfAncLclMediaType_Type = SnmpAdminString
_PktcEUERSTNfAncLclMediaType_Object = MibTableColumn
pktcEUERSTNfAncLclMediaType = _PktcEUERSTNfAncLclMediaType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 2),
    _PktcEUERSTNfAncLclMediaType_Type()
)
pktcEUERSTNfAncLclMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaType.setStatus("current")
_PktcEUERSTNfAncLclMediaData_Type = SnmpAdminString
_PktcEUERSTNfAncLclMediaData_Object = MibTableColumn
pktcEUERSTNfAncLclMediaData = _PktcEUERSTNfAncLclMediaData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 2, 5, 1, 3),
    _PktcEUERSTNfAncLclMediaData_Type()
)
pktcEUERSTNfAncLclMediaData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfAncLclMediaData.setStatus("current")
_PktcEUERSTUEActStatChgFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTUEActStatChgFeat = _PktcEUERSTUEActStatChgFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3)
)
_PktcEUERSTUEActStatChgTable_Object = MibTable
pktcEUERSTUEActStatChgTable = _PktcEUERSTUEActStatChgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgTable.setStatus("current")
_PktcEUERSTUEActStatChgEntry_Object = MibTableRow
pktcEUERSTUEActStatChgEntry = _PktcEUERSTUEActStatChgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1)
)
pktcEUERSTUEActStatChgEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTUEActStatChgIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgEntry.setStatus("current")
_PktcEUERSTUEActStatChgIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTUEActStatChgIndex_Object = MibTableColumn
pktcEUERSTUEActStatChgIndex = _PktcEUERSTUEActStatChgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1, 1),
    _PktcEUERSTUEActStatChgIndex_Type()
)
pktcEUERSTUEActStatChgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgIndex.setStatus("current")
_PktcEUERSTUEActStatChgRegExp_Type = Unsigned32
_PktcEUERSTUEActStatChgRegExp_Object = MibTableColumn
pktcEUERSTUEActStatChgRegExp = _PktcEUERSTUEActStatChgRegExp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 3, 1, 1, 2),
    _PktcEUERSTUEActStatChgRegExp_Type()
)
pktcEUERSTUEActStatChgRegExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTUEActStatChgRegExp.setStatus("current")
_PktcEUERSTNoAnsTimeoutFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTNoAnsTimeoutFeat = _PktcEUERSTNoAnsTimeoutFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4)
)
_PktcEUERSTNoAnsTimeoutTable_Object = MibTable
pktcEUERSTNoAnsTimeoutTable = _PktcEUERSTNoAnsTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTimeoutTable.setStatus("current")
_PktcEUERSTNoAnsTimeoutEntry_Object = MibTableRow
pktcEUERSTNoAnsTimeoutEntry = _PktcEUERSTNoAnsTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1)
)
pktcEUERSTNoAnsTimeoutEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTNoAnsTOIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTimeoutEntry.setStatus("current")
_PktcEUERSTNoAnsTOIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTNoAnsTOIndex_Object = MibTableColumn
pktcEUERSTNoAnsTOIndex = _PktcEUERSTNoAnsTOIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1, 1),
    _PktcEUERSTNoAnsTOIndex_Type()
)
pktcEUERSTNoAnsTOIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTOIndex.setStatus("current")
_PktcEUERSTNoAnsTODuration_Type = Unsigned32
_PktcEUERSTNoAnsTODuration_Object = MibTableColumn
pktcEUERSTNoAnsTODuration = _PktcEUERSTNoAnsTODuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 4, 1, 1, 2),
    _PktcEUERSTNoAnsTODuration_Type()
)
pktcEUERSTNoAnsTODuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsTODuration.setStatus("current")
_PktcEUERSTCallerIdFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallerIdFeat = _PktcEUERSTCallerIdFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5)
)
_PktcEUERSTCIDTable_Object = MibTable
pktcEUERSTCIDTable = _PktcEUERSTCIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDTable.setStatus("current")
_PktcEUERSTCIDEntry_Object = MibTableRow
pktcEUERSTCIDEntry = _PktcEUERSTCIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1)
)
pktcEUERSTCIDEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDEntry.setStatus("current")
_PktcEUERSTCIDIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDIndex_Object = MibTableColumn
pktcEUERSTCIDIndex = _PktcEUERSTCIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1, 1),
    _PktcEUERSTCIDIndex_Type()
)
pktcEUERSTCIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDIndex.setStatus("current")


class _PktcEUERSTCIDPPS_Type(Integer32):
    """Custom type pktcEUERSTCIDPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anonymous", 1),
          ("public", 2))
    )


_PktcEUERSTCIDPPS_Type.__name__ = "Integer32"
_PktcEUERSTCIDPPS_Object = MibTableColumn
pktcEUERSTCIDPPS = _PktcEUERSTCIDPPS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 5, 1, 1, 2),
    _PktcEUERSTCIDPPS_Type()
)
pktcEUERSTCIDPPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDPPS.setStatus("current")
_PktcEUERSTCIDDisFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCIDDisFeat = _PktcEUERSTCIDDisFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6)
)
_PktcEUERSTCIDDisTable_Object = MibTable
pktcEUERSTCIDDisTable = _PktcEUERSTCIDDisTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisTable.setStatus("current")
_PktcEUERSTCIDDisEntry_Object = MibTableRow
pktcEUERSTCIDDisEntry = _PktcEUERSTCIDDisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1)
)
pktcEUERSTCIDDisEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisEntry.setStatus("current")
_PktcEUERSTCIDDisIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDDisIndex_Object = MibTableColumn
pktcEUERSTCIDDisIndex = _PktcEUERSTCIDDisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 1),
    _PktcEUERSTCIDDisIndex_Type()
)
pktcEUERSTCIDDisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisIndex.setStatus("current")
_PktcEUERSTCIDDisCNDActActStat_Type = TruthValue
_PktcEUERSTCIDDisCNDActActStat_Object = MibTableColumn
pktcEUERSTCIDDisCNDActActStat = _PktcEUERSTCIDDisCNDActActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 2),
    _PktcEUERSTCIDDisCNDActActStat_Type()
)
pktcEUERSTCIDDisCNDActActStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisCNDActActStat.setStatus("current")
_PktcEUERSTCIDDisCNAMDActActStat_Type = TruthValue
_PktcEUERSTCIDDisCNAMDActActStat_Object = MibTableColumn
pktcEUERSTCIDDisCNAMDActActStat = _PktcEUERSTCIDDisCNAMDActActStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 3),
    _PktcEUERSTCIDDisCNAMDActActStat_Type()
)
pktcEUERSTCIDDisCNAMDActActStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisCNAMDActActStat.setStatus("current")
_PktcEUERSTCIDDisDefCountry_Type = SnmpAdminString
_PktcEUERSTCIDDisDefCountry_Object = MibTableColumn
pktcEUERSTCIDDisDefCountry = _PktcEUERSTCIDDisDefCountry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 1, 1, 4),
    _PktcEUERSTCIDDisDefCountry_Type()
)
pktcEUERSTCIDDisDefCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisDefCountry.setStatus("current")
_PktcEUERSTCIDDisTimeAdj_Type = SnmpAdminString
_PktcEUERSTCIDDisTimeAdj_Object = MibScalar
pktcEUERSTCIDDisTimeAdj = _PktcEUERSTCIDDisTimeAdj_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 6, 2),
    _PktcEUERSTCIDDisTimeAdj_Type()
)
pktcEUERSTCIDDisTimeAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDisTimeAdj.setStatus("current")
_PktcEUERSTCIDCallBlkFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCIDCallBlkFeat = _PktcEUERSTCIDCallBlkFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7)
)
_PktcEUERSTCallBlkTable_Object = MibTable
pktcEUERSTCallBlkTable = _PktcEUERSTCallBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallBlkTable.setStatus("current")
_PktcEUERSTCallBlkEntry_Object = MibTableRow
pktcEUERSTCallBlkEntry = _PktcEUERSTCallBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1)
)
pktcEUERSTCallBlkEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDBlkIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallBlkEntry.setStatus("current")
_PktcEUERSTCIDBlkIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDBlkIndex_Object = MibTableColumn
pktcEUERSTCIDBlkIndex = _PktcEUERSTCIDBlkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 1),
    _PktcEUERSTCIDBlkIndex_Type()
)
pktcEUERSTCIDBlkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDBlkIndex.setStatus("current")
_PktcEUERSTCIDCBlkConfTone_Type = PktcRSTTCTONEANNC
_PktcEUERSTCIDCBlkConfTone_Object = MibTableColumn
pktcEUERSTCIDCBlkConfTone = _PktcEUERSTCIDCBlkConfTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 2),
    _PktcEUERSTCIDCBlkConfTone_Type()
)
pktcEUERSTCIDCBlkConfTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDCBlkConfTone.setStatus("current")
_PktcEUERSTCIDCBlkErrTone_Type = PktcRSTTCTONEANNC
_PktcEUERSTCIDCBlkErrTone_Object = MibTableColumn
pktcEUERSTCIDCBlkErrTone = _PktcEUERSTCIDCBlkErrTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 7, 1, 1, 3),
    _PktcEUERSTCIDCBlkErrTone_Type()
)
pktcEUERSTCIDCBlkErrTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDCBlkErrTone.setStatus("current")
_PktcEUERSTCIDCallDelFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCIDCallDelFeat = _PktcEUERSTCIDCallDelFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8)
)
_PktcEUERSTCallDelTable_Object = MibTable
pktcEUERSTCallDelTable = _PktcEUERSTCallDelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallDelTable.setStatus("current")
_PktcEUERSTCallDelEntry_Object = MibTableRow
pktcEUERSTCallDelEntry = _PktcEUERSTCallDelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1)
)
pktcEUERSTCallDelEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallDelEntry.setStatus("current")
_PktcEUERSTCIDDelIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCIDDelIndex_Object = MibTableColumn
pktcEUERSTCIDDelIndex = _PktcEUERSTCIDDelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 1),
    _PktcEUERSTCIDDelIndex_Type()
)
pktcEUERSTCIDDelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelIndex.setStatus("current")
_PktcEUERSTCIDDelConfTone_Type = PktcRSTTCTONEANNC
_PktcEUERSTCIDDelConfTone_Object = MibTableColumn
pktcEUERSTCIDDelConfTone = _PktcEUERSTCIDDelConfTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 2),
    _PktcEUERSTCIDDelConfTone_Type()
)
pktcEUERSTCIDDelConfTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelConfTone.setStatus("current")
_PktcEUERSTCIDDelErrTone_Type = PktcRSTTCTONEANNC
_PktcEUERSTCIDDelErrTone_Object = MibTableColumn
pktcEUERSTCIDDelErrTone = _PktcEUERSTCIDDelErrTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 8, 1, 1, 3),
    _PktcEUERSTCIDDelErrTone_Type()
)
pktcEUERSTCIDDelErrTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCIDDelErrTone.setStatus("current")
_PktcEUERSTCFwdFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCFwdFeat = _PktcEUERSTCFwdFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9)
)
_PktcEUERSTCallFwdTable_Object = MibTable
pktcEUERSTCallFwdTable = _PktcEUERSTCallFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdTable.setStatus("current")
_PktcEUERSTCallFwdEntry_Object = MibTableRow
pktcEUERSTCallFwdEntry = _PktcEUERSTCallFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1)
)
pktcEUERSTCallFwdEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdEntry.setStatus("current")
_PktcEUERSTCallFwdIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCallFwdIndex_Object = MibTableColumn
pktcEUERSTCallFwdIndex = _PktcEUERSTCallFwdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 1),
    _PktcEUERSTCallFwdIndex_Type()
)
pktcEUERSTCallFwdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdIndex.setStatus("current")
_PktcEUERSTCallFwdRingReminder_Type = TruthValue
_PktcEUERSTCallFwdRingReminder_Object = MibTableColumn
pktcEUERSTCallFwdRingReminder = _PktcEUERSTCallFwdRingReminder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 2),
    _PktcEUERSTCallFwdRingReminder_Type()
)
pktcEUERSTCallFwdRingReminder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdRingReminder.setStatus("current")
_PktcEUERSTCallFwdSubDuration_Type = Unsigned32
_PktcEUERSTCallFwdSubDuration_Object = MibTableColumn
pktcEUERSTCallFwdSubDuration = _PktcEUERSTCallFwdSubDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 1, 1, 3),
    _PktcEUERSTCallFwdSubDuration_Type()
)
pktcEUERSTCallFwdSubDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdSubDuration.setStatus("current")
_PktcEUERSTNfCallFwdTable_Object = MibTable
pktcEUERSTNfCallFwdTable = _PktcEUERSTNfCallFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdTable.setStatus("current")
_PktcEUERSTNfCallFwdEntry_Object = MibTableRow
pktcEUERSTNfCallFwdEntry = _PktcEUERSTNfCallFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2, 1)
)
pktcEUERSTNfCallFwdEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdEntry.setStatus("current")
_PktcEUERSTNfCallFwdSpDialTone_Type = TruthValue
_PktcEUERSTNfCallFwdSpDialTone_Object = MibTableColumn
pktcEUERSTNfCallFwdSpDialTone = _PktcEUERSTNfCallFwdSpDialTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 9, 2, 1, 1),
    _PktcEUERSTNfCallFwdSpDialTone_Type()
)
pktcEUERSTNfCallFwdSpDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfCallFwdSpDialTone.setStatus("current")
_PktcEUERSTCallWaitFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallWaitFeat = _PktcEUERSTCallWaitFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10)
)
_PktcEUERSTCallWaitTable_Object = MibTable
pktcEUERSTCallWaitTable = _PktcEUERSTCallWaitTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitTable.setStatus("current")
_PktcEUERSTCallWaitEntry_Object = MibTableRow
pktcEUERSTCallWaitEntry = _PktcEUERSTCallWaitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1)
)
pktcEUERSTCallWaitEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCWIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitEntry.setStatus("current")
_PktcEUERSTCWIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCWIndex_Object = MibTableColumn
pktcEUERSTCWIndex = _PktcEUERSTCWIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1, 1),
    _PktcEUERSTCWIndex_Type()
)
pktcEUERSTCWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCWIndex.setStatus("current")
_PktcEUERSTCWDisStarCode_Type = SnmpAdminString
_PktcEUERSTCWDisStarCode_Object = MibTableColumn
pktcEUERSTCWDisStarCode = _PktcEUERSTCWDisStarCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 10, 1, 1, 2),
    _PktcEUERSTCWDisStarCode_Type()
)
pktcEUERSTCWDisStarCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCWDisStarCode.setStatus("current")
_PktcEUERSTCallHoldFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallHoldFeat = _PktcEUERSTCallHoldFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11)
)
_PktcEUERSTCallHoldTable_Object = MibTable
pktcEUERSTCallHoldTable = _PktcEUERSTCallHoldTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallHoldTable.setStatus("current")
_PktcEUERSTCallHoldEntry_Object = MibTableRow
pktcEUERSTCallHoldEntry = _PktcEUERSTCallHoldEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1)
)
pktcEUERSTCallHoldEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCHIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallHoldEntry.setStatus("current")
_PktcEUERSTCHIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCHIndex_Object = MibTableColumn
pktcEUERSTCHIndex = _PktcEUERSTCHIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1, 1),
    _PktcEUERSTCHIndex_Type()
)
pktcEUERSTCHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCHIndex.setStatus("current")
_PktcEUERSTCHFeatCode_Type = SnmpAdminString
_PktcEUERSTCHFeatCode_Object = MibTableColumn
pktcEUERSTCHFeatCode = _PktcEUERSTCHFeatCode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1, 2),
    _PktcEUERSTCHFeatCode_Type()
)
pktcEUERSTCHFeatCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCHFeatCode.setStatus("current")
_PktcEUERSTCHFeatConfirm_Type = PktcRSTTCTONEANNC
_PktcEUERSTCHFeatConfirm_Object = MibTableColumn
pktcEUERSTCHFeatConfirm = _PktcEUERSTCHFeatConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 11, 1, 1, 3),
    _PktcEUERSTCHFeatConfirm_Type()
)
pktcEUERSTCHFeatConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCHFeatConfirm.setStatus("current")
_PktcEUERSTCallXfrFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTCallXfrFeat = _PktcEUERSTCallXfrFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12)
)
_PktcEUERSTCallXfrTable_Object = MibTable
pktcEUERSTCallXfrTable = _PktcEUERSTCallXfrTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTCallXfrTable.setStatus("current")
_PktcEUERSTCallXfrEntry_Object = MibTableRow
pktcEUERSTCallXfrEntry = _PktcEUERSTCallXfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1)
)
pktcEUERSTCallXfrEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTCallXfrEntry.setStatus("current")
_PktcEUERSTCXIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTCXIndex_Object = MibTableColumn
pktcEUERSTCXIndex = _PktcEUERSTCXIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 1),
    _PktcEUERSTCXIndex_Type()
)
pktcEUERSTCXIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTCXIndex.setStatus("current")
_PktcEUERSTCXNtfyTimeout_Type = Unsigned32
_PktcEUERSTCXNtfyTimeout_Object = MibTableColumn
pktcEUERSTCXNtfyTimeout = _PktcEUERSTCXNtfyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 12, 1, 1, 2),
    _PktcEUERSTCXNtfyTimeout_Type()
)
pktcEUERSTCXNtfyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTCXNtfyTimeout.setStatus("current")
_PktcEUERSTDnDFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTDnDFeat = _PktcEUERSTDnDFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13)
)
_PktcEUERSTDnDTable_Object = MibTable
pktcEUERSTDnDTable = _PktcEUERSTDnDTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTDnDTable.setStatus("current")
_PktcEUERSTDnDEntry_Object = MibTableRow
pktcEUERSTDnDEntry = _PktcEUERSTDnDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1)
)
pktcEUERSTDnDEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTDnDEntry.setStatus("current")
_PktcEUERSTDnDIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTDnDIndex_Object = MibTableColumn
pktcEUERSTDnDIndex = _PktcEUERSTDnDIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 1),
    _PktcEUERSTDnDIndex_Type()
)
pktcEUERSTDnDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTDnDIndex.setStatus("current")
_PktcEUERSTDnDActConfirm_Type = PktcRSTTCTONEANNC
_PktcEUERSTDnDActConfirm_Object = MibTableColumn
pktcEUERSTDnDActConfirm = _PktcEUERSTDnDActConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 2),
    _PktcEUERSTDnDActConfirm_Type()
)
pktcEUERSTDnDActConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTDnDActConfirm.setStatus("current")
_PktcEUERSTDnDDeActConfirm_Type = PktcRSTTCTONEANNC
_PktcEUERSTDnDDeActConfirm_Object = MibTableColumn
pktcEUERSTDnDDeActConfirm = _PktcEUERSTDnDDeActConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 13, 1, 1, 3),
    _PktcEUERSTDnDDeActConfirm_Type()
)
pktcEUERSTDnDDeActConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTDnDDeActConfirm.setStatus("current")
_PktcEUERSTMWIFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTMWIFeat = _PktcEUERSTMWIFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14)
)
_PktcEUERSTNfMWITable_Object = MibTable
pktcEUERSTNfMWITable = _PktcEUERSTNfMWITable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfMWITable.setStatus("current")
_PktcEUERSTNfMWIEntry_Object = MibTableRow
pktcEUERSTNfMWIEntry = _PktcEUERSTNfMWIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1, 1)
)
pktcEUERSTNfMWIEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfMWIEntry.setStatus("current")
_PktcEUERSTNfMWISubDuration_Type = Unsigned32
_PktcEUERSTNfMWISubDuration_Object = MibTableColumn
pktcEUERSTNfMWISubDuration = _PktcEUERSTNfMWISubDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 14, 1, 1, 1),
    _PktcEUERSTNfMWISubDuration_Type()
)
pktcEUERSTNfMWISubDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfMWISubDuration.setStatus("current")
_PktcEUERSTAutoRclFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTAutoRclFeat = _PktcEUERSTAutoRclFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15)
)
_PktcEUERSTAutoRclTable_Object = MibTable
pktcEUERSTAutoRclTable = _PktcEUERSTAutoRclTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoRclTable.setStatus("current")
_PktcEUERSTAutoRclEntry_Object = MibTableRow
pktcEUERSTAutoRclEntry = _PktcEUERSTAutoRclEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1)
)
pktcEUERSTAutoRclEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTARIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoRclEntry.setStatus("current")
_PktcEUERSTARIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTARIndex_Object = MibTableColumn
pktcEUERSTARIndex = _PktcEUERSTARIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 1),
    _PktcEUERSTARIndex_Type()
)
pktcEUERSTARIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTARIndex.setStatus("current")


class _PktcEUERSTARTimer_Type(Unsigned32):
    """Custom type pktcEUERSTARTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PktcEUERSTARTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTARTimer_Object = MibTableColumn
pktcEUERSTARTimer = _PktcEUERSTARTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 2),
    _PktcEUERSTARTimer_Type()
)
pktcEUERSTARTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTARTimer.setStatus("current")
_PktcEUERSTARSpRngDuration_Type = Unsigned32
_PktcEUERSTARSpRngDuration_Object = MibTableColumn
pktcEUERSTARSpRngDuration = _PktcEUERSTARSpRngDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 3),
    _PktcEUERSTARSpRngDuration_Type()
)
pktcEUERSTARSpRngDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTARSpRngDuration.setStatus("current")
_PktcEUERSTARSpRngRetryTime_Type = Unsigned32
_PktcEUERSTARSpRngRetryTime_Object = MibTableColumn
pktcEUERSTARSpRngRetryTime = _PktcEUERSTARSpRngRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 4),
    _PktcEUERSTARSpRngRetryTime_Type()
)
pktcEUERSTARSpRngRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTARSpRngRetryTime.setStatus("current")
_PktcEUERSTARSpRngRetries_Type = Unsigned32
_PktcEUERSTARSpRngRetries_Object = MibTableColumn
pktcEUERSTARSpRngRetries = _PktcEUERSTARSpRngRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 5),
    _PktcEUERSTARSpRngRetries_Type()
)
pktcEUERSTARSpRngRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTARSpRngRetries.setStatus("current")
_PktcEUERSTARMaxSubSend_Type = Unsigned32
_PktcEUERSTARMaxSubSend_Object = MibTableColumn
pktcEUERSTARMaxSubSend = _PktcEUERSTARMaxSubSend_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 6),
    _PktcEUERSTARMaxSubSend_Type()
)
pktcEUERSTARMaxSubSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTARMaxSubSend.setStatus("current")
_PktcEUERSTARMaxSubRec_Type = Unsigned32
_PktcEUERSTARMaxSubRec_Object = MibTableColumn
pktcEUERSTARMaxSubRec = _PktcEUERSTARMaxSubRec_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 15, 1, 1, 7),
    _PktcEUERSTARMaxSubRec_Type()
)
pktcEUERSTARMaxSubRec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTARMaxSubRec.setStatus("current")
_PktcEUERSTAutoCbFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTAutoCbFeat = _PktcEUERSTAutoCbFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16)
)
_PktcEUERSTAutoCbTable_Object = MibTable
pktcEUERSTAutoCbTable = _PktcEUERSTAutoCbTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoCbTable.setStatus("current")
_PktcEUERSTAutoCbEntry_Object = MibTableRow
pktcEUERSTAutoCbEntry = _PktcEUERSTAutoCbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1)
)
pktcEUERSTAutoCbEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoCbEntry.setStatus("current")
_PktcEUERSTACbIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTACbIndex_Object = MibTableColumn
pktcEUERSTACbIndex = _PktcEUERSTACbIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 1),
    _PktcEUERSTACbIndex_Type()
)
pktcEUERSTACbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTACbIndex.setStatus("current")


class _PktcEUERSTACbTimer_Type(Unsigned32):
    """Custom type pktcEUERSTACbTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PktcEUERSTACbTimer_Type.__name__ = "Unsigned32"
_PktcEUERSTACbTimer_Object = MibTableColumn
pktcEUERSTACbTimer = _PktcEUERSTACbTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 2),
    _PktcEUERSTACbTimer_Type()
)
pktcEUERSTACbTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTACbTimer.setStatus("current")
_PktcEUERSTACbSpRngDuration_Type = Unsigned32
_PktcEUERSTACbSpRngDuration_Object = MibTableColumn
pktcEUERSTACbSpRngDuration = _PktcEUERSTACbSpRngDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 3),
    _PktcEUERSTACbSpRngDuration_Type()
)
pktcEUERSTACbSpRngDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTACbSpRngDuration.setStatus("current")
_PktcEUERSTACbSpRngRetryTime_Type = Unsigned32
_PktcEUERSTACbSpRngRetryTime_Object = MibTableColumn
pktcEUERSTACbSpRngRetryTime = _PktcEUERSTACbSpRngRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 4),
    _PktcEUERSTACbSpRngRetryTime_Type()
)
pktcEUERSTACbSpRngRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTACbSpRngRetryTime.setStatus("current")
_PktcEUERSTACbSpRngRetries_Type = Unsigned32
_PktcEUERSTACbSpRngRetries_Object = MibTableColumn
pktcEUERSTACbSpRngRetries = _PktcEUERSTACbSpRngRetries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 5),
    _PktcEUERSTACbSpRngRetries_Type()
)
pktcEUERSTACbSpRngRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTACbSpRngRetries.setStatus("current")
_PktcEUERSTACbMaxSubSend_Type = Unsigned32
_PktcEUERSTACbMaxSubSend_Object = MibTableColumn
pktcEUERSTACbMaxSubSend = _PktcEUERSTACbMaxSubSend_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 6),
    _PktcEUERSTACbMaxSubSend_Type()
)
pktcEUERSTACbMaxSubSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTACbMaxSubSend.setStatus("current")
_PktcEUERSTACbMaxSubRec_Type = Unsigned32
_PktcEUERSTACbMaxSubRec_Object = MibTableColumn
pktcEUERSTACbMaxSubRec = _PktcEUERSTACbMaxSubRec_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 16, 1, 1, 7),
    _PktcEUERSTACbMaxSubRec_Type()
)
pktcEUERSTACbMaxSubRec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTACbMaxSubRec.setStatus("current")
_PktcEUERSTBusyLineVFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTBusyLineVFeat = _PktcEUERSTBusyLineVFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17)
)
_PktcEUERSTNfBusyLineVTable_Object = MibTable
pktcEUERSTNfBusyLineVTable = _PktcEUERSTNfBusyLineVTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBusyLineVTable.setStatus("current")
_PktcEUERSTNfBusyLineVEntry_Object = MibTableRow
pktcEUERSTNfBusyLineVEntry = _PktcEUERSTNfBusyLineVEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1, 1)
)
pktcEUERSTNfBusyLineVEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfBusyLineVEntry.setStatus("current")
_PktcEUERSTNfBLVOperId_Type = SnmpAdminString
_PktcEUERSTNfBLVOperId_Object = MibTableColumn
pktcEUERSTNfBLVOperId = _PktcEUERSTNfBLVOperId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 17, 1, 1, 1),
    _PktcEUERSTNfBLVOperId_Type()
)
pktcEUERSTNfBLVOperId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfBLVOperId.setStatus("current")
_PktcEUERSTEmSvcFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTEmSvcFeat = _PktcEUERSTEmSvcFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18)
)
_PktcEUERSTNfEmSvcTable_Object = MibTable
pktcEUERSTNfEmSvcTable = _PktcEUERSTNfEmSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcTable.setStatus("current")
_PktcEUERSTNfEmSvcEntry_Object = MibTableRow
pktcEUERSTNfEmSvcEntry = _PktcEUERSTNfEmSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1)
)
pktcEUERSTNfEmSvcEntry.setIndexNames(
    (0, "CL-PKTC-EUE-DEV-MIB", "pktcEUEDevOpIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcEntry.setStatus("current")


class _PktcEUERSTNfEmSvcNwHoldTimer_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcNwHoldTimer based on Unsigned32"""
    defaultValue = 45


_PktcEUERSTNfEmSvcNwHoldTimer_Object = MibTableColumn
pktcEUERSTNfEmSvcNwHoldTimer = _PktcEUERSTNfEmSvcNwHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 1),
    _PktcEUERSTNfEmSvcNwHoldTimer_Type()
)
pktcEUERSTNfEmSvcNwHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcNwHoldTimer.setStatus("current")


class _PktcEUERSTNfEmSvcHowlTimer_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcHowlTimer based on Unsigned32"""
    defaultValue = 3


_PktcEUERSTNfEmSvcHowlTimer_Object = MibTableColumn
pktcEUERSTNfEmSvcHowlTimer = _PktcEUERSTNfEmSvcHowlTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 2),
    _PktcEUERSTNfEmSvcHowlTimer_Type()
)
pktcEUERSTNfEmSvcHowlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcHowlTimer.setStatus("current")


class _PktcEUERSTNfEmSvcMediaDSCPVal_Type(Unsigned32):
    """Custom type pktcEUERSTNfEmSvcMediaDSCPVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PktcEUERSTNfEmSvcMediaDSCPVal_Type.__name__ = "Unsigned32"
_PktcEUERSTNfEmSvcMediaDSCPVal_Object = MibTableColumn
pktcEUERSTNfEmSvcMediaDSCPVal = _PktcEUERSTNfEmSvcMediaDSCPVal_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 18, 1, 1, 3),
    _PktcEUERSTNfEmSvcMediaDSCPVal_Type()
)
pktcEUERSTNfEmSvcMediaDSCPVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTNfEmSvcMediaDSCPVal.setStatus("current")
_PktcEUERSTSCFFeat_ObjectIdentity = ObjectIdentity
pktcEUERSTSCFFeat = _PktcEUERSTSCFFeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19)
)
_PktcEUERSTSCFTable_Object = MibTable
pktcEUERSTSCFTable = _PktcEUERSTSCFTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTSCFTable.setStatus("current")
_PktcEUERSTSCFEntry_Object = MibTableRow
pktcEUERSTSCFEntry = _PktcEUERSTSCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1)
)
pktcEUERSTSCFEntry.setIndexNames(
    (0, "CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFIndex"),
)
if mibBuilder.loadTexts:
    pktcEUERSTSCFEntry.setStatus("current")
_PktcEUERSTSCFIndex_Type = PktcEUETCRSTAppFeatIndexType
_PktcEUERSTSCFIndex_Object = MibTableColumn
pktcEUERSTSCFIndex = _PktcEUERSTSCFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1, 1),
    _PktcEUERSTSCFIndex_Type()
)
pktcEUERSTSCFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUERSTSCFIndex.setStatus("current")
_PktcEUERSTSCFCFRingReminder_Type = TruthValue
_PktcEUERSTSCFCFRingReminder_Object = MibTableColumn
pktcEUERSTSCFCFRingReminder = _PktcEUERSTSCFCFRingReminder_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 1, 2, 19, 1, 1, 2),
    _PktcEUERSTSCFCFRingReminder_Type()
)
pktcEUERSTSCFCFRingReminder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUERSTSCFCFRingReminder.setStatus("current")
_PktcEUERSTConformance_ObjectIdentity = ObjectIdentity
pktcEUERSTConformance = _PktcEUERSTConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2)
)
_PktcEUERSTCompliances_ObjectIdentity = ObjectIdentity
pktcEUERSTCompliances = _PktcEUERSTCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 1)
)
_PktcEUERSTMIBCompliances_ObjectIdentity = ObjectIdentity
pktcEUERSTMIBCompliances = _PktcEUERSTMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 1)
)
_PktcEUERSTGroups_ObjectIdentity = ObjectIdentity
pktcEUERSTGroups = _PktcEUERSTGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2)
)
_PktcEUERSTMIBGroups_ObjectIdentity = ObjectIdentity
pktcEUERSTMIBGroups = _PktcEUERSTMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2)
)

# Managed Objects groups

pktcEUERSTProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 1)
)
pktcEUERSTProfileGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTProfileVersion")
)
if mibBuilder.loadTexts:
    pktcEUERSTProfileGroup.setStatus("current")

pktcEUERSTBasicCallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 2)
)
pktcEUERSTBasicCallGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTBCallSDP"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallByeDelay"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallOrigDTTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallTermOHErrSig"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallTermErrSigTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone1"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer1"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone2"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer2"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTone3"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallPermSeqTimer3"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallLORTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBCallNEMDSCPValue"))
)
if mibBuilder.loadTexts:
    pktcEUERSTBasicCallGroup.setStatus("current")

pktcEUERSTAncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 3)
)
pktcEUERSTAncGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAncPrefLang"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncRes"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncDomain"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncPath"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMIMEType"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncURI"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaURI"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncMediaCachMaxAge"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaData"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfAncLclMediaType"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAncGroup.setStatus("current")

pktcEUERSTUEStGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 4)
)
pktcEUERSTUEStGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTUEActStatChgRegExp")
)
if mibBuilder.loadTexts:
    pktcEUERSTUEStGroup.setStatus("current")

pktcEUERSTNoAnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 5)
)
pktcEUERSTNoAnsGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNoAnsTODuration")
)
if mibBuilder.loadTexts:
    pktcEUERSTNoAnsGroup.setStatus("current")

pktcEUERSTCallerIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 6)
)
pktcEUERSTCallerIDGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDPPS"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisTimeAdj"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisCNDActActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisCNAMDActActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDCBlkConfTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDCBlkErrTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelConfTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDelErrTone"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCIDDisDefCountry"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallerIDGroup.setStatus("current")

pktcEUERSTCallFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 7)
)
pktcEUERSTCallFwdGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdRingReminder"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCallFwdSubDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfCallFwdSpDialTone"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallFwdGroup.setStatus("current")

pktcEUERSTCallWaitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 8)
)
pktcEUERSTCallWaitGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCWDisStarCode")
)
if mibBuilder.loadTexts:
    pktcEUERSTCallWaitGroup.setStatus("current")

pktcEUERSTCallHoldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 9)
)
pktcEUERSTCallHoldGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCHFeatCode"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCHFeatConfirm"))
)
if mibBuilder.loadTexts:
    pktcEUERSTCallHoldGroup.setStatus("current")

pktcEUERSTCallTransGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 10)
)
pktcEUERSTCallTransGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTCXNtfyTimeout")
)
if mibBuilder.loadTexts:
    pktcEUERSTCallTransGroup.setStatus("current")

pktcEUERSTDNDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 11)
)
pktcEUERSTDNDGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDActConfirm"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDnDDeActConfirm"))
)
if mibBuilder.loadTexts:
    pktcEUERSTDNDGroup.setStatus("current")

pktcEUERSTMWIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 12)
)
pktcEUERSTMWIGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfMWISubDuration")
)
if mibBuilder.loadTexts:
    pktcEUERSTMWIGroup.setStatus("current")

pktcEUERSTAutoRecallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 13)
)
pktcEUERSTAutoRecallGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARSpRngDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARSpRngRetryTime"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARSpRngRetries"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARMaxSubSend"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTARMaxSubRec"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoRecallGroup.setStatus("current")

pktcEUERSTAutoCallbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 14)
)
pktcEUERSTAutoCallbackGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbSpRngDuration"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbSpRngRetryTime"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbSpRngRetries"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbMaxSubSend"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTACbMaxSubRec"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAutoCallbackGroup.setStatus("current")

pktcEUERSTBusyLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 15)
)
pktcEUERSTBusyLineGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfBLVOperId")
)
if mibBuilder.loadTexts:
    pktcEUERSTBusyLineGroup.setStatus("current")

pktcEUERSTEmerSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 16)
)
pktcEUERSTEmerSvcGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcNwHoldTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcHowlTimer"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTNfEmSvcMediaDSCPVal"))
)
if mibBuilder.loadTexts:
    pktcEUERSTEmerSvcGroup.setStatus("current")

pktcEUERSTDigitMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 17)
)
pktcEUERSTDigitMapGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMTimerT"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMTimerS"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMTimerL"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMTimerZ"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTDMValue"))
)
if mibBuilder.loadTexts:
    pktcEUERSTDigitMapGroup.setStatus("current")

pktcEUERSTAppProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 18)
)
pktcEUERSTAppProfileGroup.setObjects(
      *(("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppFeatID"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppFeatIndexRef"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppNwActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppNwActStatInfo"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppEUEActStat"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppEUEActStatInfo"),
        ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTAppRowActStatus"))
)
if mibBuilder.loadTexts:
    pktcEUERSTAppProfileGroup.setStatus("current")

pktcEUERSTSCFProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 2, 19)
)
pktcEUERSTSCFProfileGroup.setObjects(
    ("CL-PKTC-EUE-RST-MIB", "pktcEUERSTSCFCFRingReminder")
)
if mibBuilder.loadTexts:
    pktcEUERSTSCFProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUERSTMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEUERSTMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-RST-MIB",
    **{"PktcRSTTCTONEANNC": PktcRSTTCTONEANNC,
       "PktcRSTTCFeatID": PktcRSTTCFeatID,
       "PktcEUETCRSTAppPrfIndexType": PktcEUETCRSTAppPrfIndexType,
       "PktcEUETCRSTAppFeatIndexType": PktcEUETCRSTAppFeatIndexType,
       "pktcEUERSTMIB": pktcEUERSTMIB,
       "pktcEUERSTNotifications": pktcEUERSTNotifications,
       "pktcEUERSTObjects": pktcEUERSTObjects,
       "pktcEUERSTProfile": pktcEUERSTProfile,
       "pktcEUERSTProfileVersion": pktcEUERSTProfileVersion,
       "pktcEUERSTAppProfileToFeatTable": pktcEUERSTAppProfileToFeatTable,
       "pktcEUERSTAppProfileToFeatEntry": pktcEUERSTAppProfileToFeatEntry,
       "pktcEUERSTAppProfileIndex": pktcEUERSTAppProfileIndex,
       "pktcEUERSTAppFeatIndex": pktcEUERSTAppFeatIndex,
       "pktcEUERSTAppFeatID": pktcEUERSTAppFeatID,
       "pktcEUERSTAppFeatIndexRef": pktcEUERSTAppFeatIndexRef,
       "pktcEUERSTAppNwActStat": pktcEUERSTAppNwActStat,
       "pktcEUERSTAppNwActStatInfo": pktcEUERSTAppNwActStatInfo,
       "pktcEUERSTAppEUEActStat": pktcEUERSTAppEUEActStat,
       "pktcEUERSTAppEUEActStatInfo": pktcEUERSTAppEUEActStatInfo,
       "pktcEUERSTAppRowActStatus": pktcEUERSTAppRowActStatus,
       "pktcEUERSTDigitMapFeat": pktcEUERSTDigitMapFeat,
       "pktcEUERSTDMTimerT": pktcEUERSTDMTimerT,
       "pktcEUERSTDMTimerS": pktcEUERSTDMTimerS,
       "pktcEUERSTDMTimerL": pktcEUERSTDMTimerL,
       "pktcEUERSTDMTimerZ": pktcEUERSTDMTimerZ,
       "pktcEUERSTDigitMapProfileTable": pktcEUERSTDigitMapProfileTable,
       "pktcEUERSTDigitMapProfileEntry": pktcEUERSTDigitMapProfileEntry,
       "pktcEUERSTDMIndex": pktcEUERSTDMIndex,
       "pktcEUERSTDMValue": pktcEUERSTDMValue,
       "pktcEUERSTFeatures": pktcEUERSTFeatures,
       "pktcEUERSTBasicCallFeat": pktcEUERSTBasicCallFeat,
       "pktcEUERSTBasicCallTable": pktcEUERSTBasicCallTable,
       "pktcEUERSTBasicCallEntry": pktcEUERSTBasicCallEntry,
       "pktcEUERSTBCallIndex": pktcEUERSTBCallIndex,
       "pktcEUERSTBCallSDP": pktcEUERSTBCallSDP,
       "pktcEUERSTNfBasicCallTable": pktcEUERSTNfBasicCallTable,
       "pktcEUERSTNfBasicCallEntry": pktcEUERSTNfBasicCallEntry,
       "pktcEUERSTNfBCallByeDelay": pktcEUERSTNfBCallByeDelay,
       "pktcEUERSTNfBCallOrigDTTimer": pktcEUERSTNfBCallOrigDTTimer,
       "pktcEUERSTNfBCallTermOHErrSig": pktcEUERSTNfBCallTermOHErrSig,
       "pktcEUERSTNfBCallTermErrSigTimer": pktcEUERSTNfBCallTermErrSigTimer,
       "pktcEUERSTNfBCallPermSeqTone1": pktcEUERSTNfBCallPermSeqTone1,
       "pktcEUERSTNfBCallPermSeqTimer1": pktcEUERSTNfBCallPermSeqTimer1,
       "pktcEUERSTNfBCallPermSeqTone2": pktcEUERSTNfBCallPermSeqTone2,
       "pktcEUERSTNfBCallPermSeqTimer2": pktcEUERSTNfBCallPermSeqTimer2,
       "pktcEUERSTNfBCallPermSeqTone3": pktcEUERSTNfBCallPermSeqTone3,
       "pktcEUERSTNfBCallPermSeqTimer3": pktcEUERSTNfBCallPermSeqTimer3,
       "pktcEUERSTNfBCallLORTimer": pktcEUERSTNfBCallLORTimer,
       "pktcEUERSTNfBCallNEMDSCPValue": pktcEUERSTNfBCallNEMDSCPValue,
       "pktcEUERSTAncFeat": pktcEUERSTAncFeat,
       "pktcEUERSTAncTable": pktcEUERSTAncTable,
       "pktcEUERSTAncEntry": pktcEUERSTAncEntry,
       "pktcEUERSTAncIndex": pktcEUERSTAncIndex,
       "pktcEUERSTAncPrefLang": pktcEUERSTAncPrefLang,
       "pktcEUERSTNfAncTable": pktcEUERSTNfAncTable,
       "pktcEUERSTNfAncEntry": pktcEUERSTNfAncEntry,
       "pktcEUERSTNfAncRes": pktcEUERSTNfAncRes,
       "pktcEUERSTNfAncDomain": pktcEUERSTNfAncDomain,
       "pktcEUERSTNfAncPath": pktcEUERSTNfAncPath,
       "pktcEUERSTNfAncMIMEType": pktcEUERSTNfAncMIMEType,
       "pktcEUERSTNfAncMapTable": pktcEUERSTNfAncMapTable,
       "pktcEUERSTNfAncMapEntry": pktcEUERSTNfAncMapEntry,
       "pktcEUERSTNfAncRspCode": pktcEUERSTNfAncRspCode,
       "pktcEUERSTNfAncURI": pktcEUERSTNfAncURI,
       "pktcEUERSTNfAncMediaMapTable": pktcEUERSTNfAncMediaMapTable,
       "pktcEUERSTNfAncMediaMapEntry": pktcEUERSTNfAncMediaMapEntry,
       "pktcEUERSTNfAncMediaId": pktcEUERSTNfAncMediaId,
       "pktcEUERSTNfAncMediaURI": pktcEUERSTNfAncMediaURI,
       "pktcEUERSTNfAncMediaCachMaxAge": pktcEUERSTNfAncMediaCachMaxAge,
       "pktcEUERSTNfAncLocalMediaTable": pktcEUERSTNfAncLocalMediaTable,
       "pktcEUERSTNfAncLocalMediaEntry": pktcEUERSTNfAncLocalMediaEntry,
       "pktcEUERSTNfAncLclMediaURI": pktcEUERSTNfAncLclMediaURI,
       "pktcEUERSTNfAncLclMediaType": pktcEUERSTNfAncLclMediaType,
       "pktcEUERSTNfAncLclMediaData": pktcEUERSTNfAncLclMediaData,
       "pktcEUERSTUEActStatChgFeat": pktcEUERSTUEActStatChgFeat,
       "pktcEUERSTUEActStatChgTable": pktcEUERSTUEActStatChgTable,
       "pktcEUERSTUEActStatChgEntry": pktcEUERSTUEActStatChgEntry,
       "pktcEUERSTUEActStatChgIndex": pktcEUERSTUEActStatChgIndex,
       "pktcEUERSTUEActStatChgRegExp": pktcEUERSTUEActStatChgRegExp,
       "pktcEUERSTNoAnsTimeoutFeat": pktcEUERSTNoAnsTimeoutFeat,
       "pktcEUERSTNoAnsTimeoutTable": pktcEUERSTNoAnsTimeoutTable,
       "pktcEUERSTNoAnsTimeoutEntry": pktcEUERSTNoAnsTimeoutEntry,
       "pktcEUERSTNoAnsTOIndex": pktcEUERSTNoAnsTOIndex,
       "pktcEUERSTNoAnsTODuration": pktcEUERSTNoAnsTODuration,
       "pktcEUERSTCallerIdFeat": pktcEUERSTCallerIdFeat,
       "pktcEUERSTCIDTable": pktcEUERSTCIDTable,
       "pktcEUERSTCIDEntry": pktcEUERSTCIDEntry,
       "pktcEUERSTCIDIndex": pktcEUERSTCIDIndex,
       "pktcEUERSTCIDPPS": pktcEUERSTCIDPPS,
       "pktcEUERSTCIDDisFeat": pktcEUERSTCIDDisFeat,
       "pktcEUERSTCIDDisTable": pktcEUERSTCIDDisTable,
       "pktcEUERSTCIDDisEntry": pktcEUERSTCIDDisEntry,
       "pktcEUERSTCIDDisIndex": pktcEUERSTCIDDisIndex,
       "pktcEUERSTCIDDisCNDActActStat": pktcEUERSTCIDDisCNDActActStat,
       "pktcEUERSTCIDDisCNAMDActActStat": pktcEUERSTCIDDisCNAMDActActStat,
       "pktcEUERSTCIDDisDefCountry": pktcEUERSTCIDDisDefCountry,
       "pktcEUERSTCIDDisTimeAdj": pktcEUERSTCIDDisTimeAdj,
       "pktcEUERSTCIDCallBlkFeat": pktcEUERSTCIDCallBlkFeat,
       "pktcEUERSTCallBlkTable": pktcEUERSTCallBlkTable,
       "pktcEUERSTCallBlkEntry": pktcEUERSTCallBlkEntry,
       "pktcEUERSTCIDBlkIndex": pktcEUERSTCIDBlkIndex,
       "pktcEUERSTCIDCBlkConfTone": pktcEUERSTCIDCBlkConfTone,
       "pktcEUERSTCIDCBlkErrTone": pktcEUERSTCIDCBlkErrTone,
       "pktcEUERSTCIDCallDelFeat": pktcEUERSTCIDCallDelFeat,
       "pktcEUERSTCallDelTable": pktcEUERSTCallDelTable,
       "pktcEUERSTCallDelEntry": pktcEUERSTCallDelEntry,
       "pktcEUERSTCIDDelIndex": pktcEUERSTCIDDelIndex,
       "pktcEUERSTCIDDelConfTone": pktcEUERSTCIDDelConfTone,
       "pktcEUERSTCIDDelErrTone": pktcEUERSTCIDDelErrTone,
       "pktcEUERSTCFwdFeat": pktcEUERSTCFwdFeat,
       "pktcEUERSTCallFwdTable": pktcEUERSTCallFwdTable,
       "pktcEUERSTCallFwdEntry": pktcEUERSTCallFwdEntry,
       "pktcEUERSTCallFwdIndex": pktcEUERSTCallFwdIndex,
       "pktcEUERSTCallFwdRingReminder": pktcEUERSTCallFwdRingReminder,
       "pktcEUERSTCallFwdSubDuration": pktcEUERSTCallFwdSubDuration,
       "pktcEUERSTNfCallFwdTable": pktcEUERSTNfCallFwdTable,
       "pktcEUERSTNfCallFwdEntry": pktcEUERSTNfCallFwdEntry,
       "pktcEUERSTNfCallFwdSpDialTone": pktcEUERSTNfCallFwdSpDialTone,
       "pktcEUERSTCallWaitFeat": pktcEUERSTCallWaitFeat,
       "pktcEUERSTCallWaitTable": pktcEUERSTCallWaitTable,
       "pktcEUERSTCallWaitEntry": pktcEUERSTCallWaitEntry,
       "pktcEUERSTCWIndex": pktcEUERSTCWIndex,
       "pktcEUERSTCWDisStarCode": pktcEUERSTCWDisStarCode,
       "pktcEUERSTCallHoldFeat": pktcEUERSTCallHoldFeat,
       "pktcEUERSTCallHoldTable": pktcEUERSTCallHoldTable,
       "pktcEUERSTCallHoldEntry": pktcEUERSTCallHoldEntry,
       "pktcEUERSTCHIndex": pktcEUERSTCHIndex,
       "pktcEUERSTCHFeatCode": pktcEUERSTCHFeatCode,
       "pktcEUERSTCHFeatConfirm": pktcEUERSTCHFeatConfirm,
       "pktcEUERSTCallXfrFeat": pktcEUERSTCallXfrFeat,
       "pktcEUERSTCallXfrTable": pktcEUERSTCallXfrTable,
       "pktcEUERSTCallXfrEntry": pktcEUERSTCallXfrEntry,
       "pktcEUERSTCXIndex": pktcEUERSTCXIndex,
       "pktcEUERSTCXNtfyTimeout": pktcEUERSTCXNtfyTimeout,
       "pktcEUERSTDnDFeat": pktcEUERSTDnDFeat,
       "pktcEUERSTDnDTable": pktcEUERSTDnDTable,
       "pktcEUERSTDnDEntry": pktcEUERSTDnDEntry,
       "pktcEUERSTDnDIndex": pktcEUERSTDnDIndex,
       "pktcEUERSTDnDActConfirm": pktcEUERSTDnDActConfirm,
       "pktcEUERSTDnDDeActConfirm": pktcEUERSTDnDDeActConfirm,
       "pktcEUERSTMWIFeat": pktcEUERSTMWIFeat,
       "pktcEUERSTNfMWITable": pktcEUERSTNfMWITable,
       "pktcEUERSTNfMWIEntry": pktcEUERSTNfMWIEntry,
       "pktcEUERSTNfMWISubDuration": pktcEUERSTNfMWISubDuration,
       "pktcEUERSTAutoRclFeat": pktcEUERSTAutoRclFeat,
       "pktcEUERSTAutoRclTable": pktcEUERSTAutoRclTable,
       "pktcEUERSTAutoRclEntry": pktcEUERSTAutoRclEntry,
       "pktcEUERSTARIndex": pktcEUERSTARIndex,
       "pktcEUERSTARTimer": pktcEUERSTARTimer,
       "pktcEUERSTARSpRngDuration": pktcEUERSTARSpRngDuration,
       "pktcEUERSTARSpRngRetryTime": pktcEUERSTARSpRngRetryTime,
       "pktcEUERSTARSpRngRetries": pktcEUERSTARSpRngRetries,
       "pktcEUERSTARMaxSubSend": pktcEUERSTARMaxSubSend,
       "pktcEUERSTARMaxSubRec": pktcEUERSTARMaxSubRec,
       "pktcEUERSTAutoCbFeat": pktcEUERSTAutoCbFeat,
       "pktcEUERSTAutoCbTable": pktcEUERSTAutoCbTable,
       "pktcEUERSTAutoCbEntry": pktcEUERSTAutoCbEntry,
       "pktcEUERSTACbIndex": pktcEUERSTACbIndex,
       "pktcEUERSTACbTimer": pktcEUERSTACbTimer,
       "pktcEUERSTACbSpRngDuration": pktcEUERSTACbSpRngDuration,
       "pktcEUERSTACbSpRngRetryTime": pktcEUERSTACbSpRngRetryTime,
       "pktcEUERSTACbSpRngRetries": pktcEUERSTACbSpRngRetries,
       "pktcEUERSTACbMaxSubSend": pktcEUERSTACbMaxSubSend,
       "pktcEUERSTACbMaxSubRec": pktcEUERSTACbMaxSubRec,
       "pktcEUERSTBusyLineVFeat": pktcEUERSTBusyLineVFeat,
       "pktcEUERSTNfBusyLineVTable": pktcEUERSTNfBusyLineVTable,
       "pktcEUERSTNfBusyLineVEntry": pktcEUERSTNfBusyLineVEntry,
       "pktcEUERSTNfBLVOperId": pktcEUERSTNfBLVOperId,
       "pktcEUERSTEmSvcFeat": pktcEUERSTEmSvcFeat,
       "pktcEUERSTNfEmSvcTable": pktcEUERSTNfEmSvcTable,
       "pktcEUERSTNfEmSvcEntry": pktcEUERSTNfEmSvcEntry,
       "pktcEUERSTNfEmSvcNwHoldTimer": pktcEUERSTNfEmSvcNwHoldTimer,
       "pktcEUERSTNfEmSvcHowlTimer": pktcEUERSTNfEmSvcHowlTimer,
       "pktcEUERSTNfEmSvcMediaDSCPVal": pktcEUERSTNfEmSvcMediaDSCPVal,
       "pktcEUERSTSCFFeat": pktcEUERSTSCFFeat,
       "pktcEUERSTSCFTable": pktcEUERSTSCFTable,
       "pktcEUERSTSCFEntry": pktcEUERSTSCFEntry,
       "pktcEUERSTSCFIndex": pktcEUERSTSCFIndex,
       "pktcEUERSTSCFCFRingReminder": pktcEUERSTSCFCFRingReminder,
       "pktcEUERSTConformance": pktcEUERSTConformance,
       "pktcEUERSTCompliances": pktcEUERSTCompliances,
       "pktcEUERSTMIBCompliances": pktcEUERSTMIBCompliances,
       "pktcEUERSTMIBCompliance": pktcEUERSTMIBCompliance,
       "pktcEUERSTGroups": pktcEUERSTGroups,
       "pktcEUERSTMIBGroups": pktcEUERSTMIBGroups,
       "pktcEUERSTProfileGroup": pktcEUERSTProfileGroup,
       "pktcEUERSTBasicCallGroup": pktcEUERSTBasicCallGroup,
       "pktcEUERSTAncGroup": pktcEUERSTAncGroup,
       "pktcEUERSTUEStGroup": pktcEUERSTUEStGroup,
       "pktcEUERSTNoAnsGroup": pktcEUERSTNoAnsGroup,
       "pktcEUERSTCallerIDGroup": pktcEUERSTCallerIDGroup,
       "pktcEUERSTCallFwdGroup": pktcEUERSTCallFwdGroup,
       "pktcEUERSTCallWaitGroup": pktcEUERSTCallWaitGroup,
       "pktcEUERSTCallHoldGroup": pktcEUERSTCallHoldGroup,
       "pktcEUERSTCallTransGroup": pktcEUERSTCallTransGroup,
       "pktcEUERSTDNDGroup": pktcEUERSTDNDGroup,
       "pktcEUERSTMWIGroup": pktcEUERSTMWIGroup,
       "pktcEUERSTAutoRecallGroup": pktcEUERSTAutoRecallGroup,
       "pktcEUERSTAutoCallbackGroup": pktcEUERSTAutoCallbackGroup,
       "pktcEUERSTBusyLineGroup": pktcEUERSTBusyLineGroup,
       "pktcEUERSTEmerSvcGroup": pktcEUERSTEmerSvcGroup,
       "pktcEUERSTDigitMapGroup": pktcEUERSTDigitMapGroup,
       "pktcEUERSTAppProfileGroup": pktcEUERSTAppProfileGroup,
       "pktcEUERSTSCFProfileGroup": pktcEUERSTSCFProfileGroup}
)
