# SNMP MIB module (JUNIPER-TIMING-NOTFNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-TIMING-NOTFNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:19 2024
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
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifOperStatus")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(jnxTimingNotfnsMIBRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxTimingNotfnsMIBRoot")

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

jnxTimingNotfnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1)
)
jnxTimingNotfnsMIB.setRevisions(
        ("2015-10-14 00:00",
         "2013-03-15 15:41")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPtpClockIdTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JnxPtpPhaseOffsetTC(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-9"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_JnxTimingFaults_ObjectIdentity = ObjectIdentity
jnxTimingFaults = _JnxTimingFaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1)
)
_JnxTimingEvents_ObjectIdentity = ObjectIdentity
jnxTimingEvents = _JnxTimingEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2)
)
_JnxTimingNotfObjects_ObjectIdentity = ObjectIdentity
jnxTimingNotfObjects = _JnxTimingNotfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3)
)


class _JnxClksyncState_Type(Integer32):
    """Custom type jnxClksyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_JnxClksyncState_Type.__name__ = "Integer32"
_JnxClksyncState_Object = MibScalar
jnxClksyncState = _JnxClksyncState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 1),
    _JnxClksyncState_Type()
)
jnxClksyncState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncState.setStatus("current")
_JnxClksyncIfIndex_Type = InterfaceIndex
_JnxClksyncIfIndex_Object = MibScalar
jnxClksyncIfIndex = _JnxClksyncIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 2),
    _JnxClksyncIfIndex_Type()
)
jnxClksyncIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncIfIndex.setStatus("current")
_JnxClksyncIntfName_Type = DisplayString
_JnxClksyncIntfName_Object = MibScalar
jnxClksyncIntfName = _JnxClksyncIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 3),
    _JnxClksyncIntfName_Type()
)
jnxClksyncIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncIntfName.setStatus("current")
_JnxAcbFpgaRevMajor_Type = Integer32
_JnxAcbFpgaRevMajor_Object = MibScalar
jnxAcbFpgaRevMajor = _JnxAcbFpgaRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 4),
    _JnxAcbFpgaRevMajor_Type()
)
jnxAcbFpgaRevMajor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxAcbFpgaRevMajor.setStatus("current")
_JnxAcbFpgaRevMinor_Type = Integer32
_JnxAcbFpgaRevMinor_Object = MibScalar
jnxAcbFpgaRevMinor = _JnxAcbFpgaRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 5),
    _JnxAcbFpgaRevMinor_Type()
)
jnxAcbFpgaRevMinor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxAcbFpgaRevMinor.setStatus("current")
_JnxBootCpldFpgaRevMajor_Type = Integer32
_JnxBootCpldFpgaRevMajor_Object = MibScalar
jnxBootCpldFpgaRevMajor = _JnxBootCpldFpgaRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 6),
    _JnxBootCpldFpgaRevMajor_Type()
)
jnxBootCpldFpgaRevMajor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxBootCpldFpgaRevMajor.setStatus("current")
_JnxBootCpldFpgaRevMinor_Type = Integer32
_JnxBootCpldFpgaRevMinor_Object = MibScalar
jnxBootCpldFpgaRevMinor = _JnxBootCpldFpgaRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 7),
    _JnxBootCpldFpgaRevMinor_Type()
)
jnxBootCpldFpgaRevMinor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxBootCpldFpgaRevMinor.setStatus("current")


class _JnxClksyncQualityCode_Type(Integer32):
    """Custom type jnxClksyncQualityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("dnu", 15),
          ("dus", 17),
          ("prc", 2),
          ("prs", 1),
          ("sec", 11),
          ("smc", 12),
          ("ssu-a", 4),
          ("ssu-b", 8),
          ("st2", 7),
          ("st3", 10),
          ("st3e", 13),
          ("st4", 14),
          ("stu", 0),
          ("tnc", 16))
    )


_JnxClksyncQualityCode_Type.__name__ = "Integer32"
_JnxClksyncQualityCode_Object = MibScalar
jnxClksyncQualityCode = _JnxClksyncQualityCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 8),
    _JnxClksyncQualityCode_Type()
)
jnxClksyncQualityCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncQualityCode.setStatus("current")


class _JnxClksyncDpllState_Type(Integer32):
    """Custom type jnxClksyncDpllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 3),
          ("holder", 2),
          ("lock-acq", 0),
          ("locked", 1),
          ("unknown", -1))
    )


_JnxClksyncDpllState_Type.__name__ = "Integer32"
_JnxClksyncDpllState_Object = MibScalar
jnxClksyncDpllState = _JnxClksyncDpllState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 9),
    _JnxClksyncDpllState_Type()
)
jnxClksyncDpllState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncDpllState.setStatus("current")


class _JnxPtpServoState_Type(Integer32):
    """Custom type jnxPtpServoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acquiring", 3),
          ("free-run", 1),
          ("freq-locked", 4),
          ("holdover", 2),
          ("init", 0),
          ("phase-aligned", 5))
    )


_JnxPtpServoState_Type.__name__ = "Integer32"
_JnxPtpServoState_Object = MibScalar
jnxPtpServoState = _JnxPtpServoState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 10),
    _JnxPtpServoState_Type()
)
jnxPtpServoState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpServoState.setStatus("current")
_JnxPtpClass_Type = Integer32
_JnxPtpClass_Object = MibScalar
jnxPtpClass = _JnxPtpClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 11),
    _JnxPtpClass_Type()
)
jnxPtpClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpClass.setStatus("current")
_JnxPtpAccuracy_Type = Integer32
_JnxPtpAccuracy_Object = MibScalar
jnxPtpAccuracy = _JnxPtpAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 12),
    _JnxPtpAccuracy_Type()
)
jnxPtpAccuracy.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpAccuracy.setStatus("current")
_JnxPtpGmId_Type = JnxPtpClockIdTC
_JnxPtpGmId_Object = MibScalar
jnxPtpGmId = _JnxPtpGmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 13),
    _JnxPtpGmId_Type()
)
jnxPtpGmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpGmId.setStatus("current")
_JnxPtpGmIpAddr_Type = InetAddress
_JnxPtpGmIpAddr_Object = MibScalar
jnxPtpGmIpAddr = _JnxPtpGmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 14),
    _JnxPtpGmIpAddr_Type()
)
jnxPtpGmIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpGmIpAddr.setStatus("current")
_JnxClkStreamHandle_Type = Integer32
_JnxClkStreamHandle_Object = MibScalar
jnxClkStreamHandle = _JnxClkStreamHandle_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 15),
    _JnxClkStreamHandle_Type()
)
jnxClkStreamHandle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClkStreamHandle.setStatus("current")
_JnxRemoteIpAddr_Type = InetAddress
_JnxRemoteIpAddr_Object = MibScalar
jnxRemoteIpAddr = _JnxRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 16),
    _JnxRemoteIpAddr_Type()
)
jnxRemoteIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxRemoteIpAddr.setStatus("current")


class _JnxClksyncHybridState_Type(Integer32):
    """Custom type jnxClksyncHybridState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("freq-acq", 1),
          ("freq-phase-lck", 5),
          ("freqLck-phaseAcq1", 2),
          ("freqLck-phaseAcq2", 3),
          ("freqLck-phaseAcq3", 4),
          ("init", 0))
    )


_JnxClksyncHybridState_Type.__name__ = "Integer32"
_JnxClksyncHybridState_Object = MibScalar
jnxClksyncHybridState = _JnxClksyncHybridState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 17),
    _JnxClksyncHybridState_Type()
)
jnxClksyncHybridState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncHybridState.setStatus("current")
_JnxPtpPhaseOffset_Type = JnxPtpPhaseOffsetTC
_JnxPtpPhaseOffset_Object = MibScalar
jnxPtpPhaseOffset = _JnxPtpPhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 18),
    _JnxPtpPhaseOffset_Type()
)
jnxPtpPhaseOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpPhaseOffset.setStatus("current")
_JnxClksyncQualityCodeStr_Type = DisplayString
_JnxClksyncQualityCodeStr_Object = MibScalar
jnxClksyncQualityCodeStr = _JnxClksyncQualityCodeStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 19),
    _JnxClksyncQualityCodeStr_Type()
)
jnxClksyncQualityCodeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncQualityCodeStr.setStatus("current")
_JnxClksyncDpllStateStr_Type = DisplayString
_JnxClksyncDpllStateStr_Object = MibScalar
jnxClksyncDpllStateStr = _JnxClksyncDpllStateStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 20),
    _JnxClksyncDpllStateStr_Type()
)
jnxClksyncDpllStateStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncDpllStateStr.setStatus("current")
_JnxPtpServoStateStr_Type = DisplayString
_JnxPtpServoStateStr_Object = MibScalar
jnxPtpServoStateStr = _JnxPtpServoStateStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 21),
    _JnxPtpServoStateStr_Type()
)
jnxPtpServoStateStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxPtpServoStateStr.setStatus("current")
_JnxClksyncHybridStateStr_Type = DisplayString
_JnxClksyncHybridStateStr_Object = MibScalar
jnxClksyncHybridStateStr = _JnxClksyncHybridStateStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 22),
    _JnxClksyncHybridStateStr_Type()
)
jnxClksyncHybridStateStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncHybridStateStr.setStatus("current")
_JnxClksyncColorStr_Type = DisplayString
_JnxClksyncColorStr_Object = MibScalar
jnxClksyncColorStr = _JnxClksyncColorStr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 3, 23),
    _JnxClksyncColorStr_Type()
)
jnxClksyncColorStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxClksyncColorStr.setStatus("current")
_JnxTimingConformance_ObjectIdentity = ObjectIdentity
jnxTimingConformance = _JnxTimingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4)
)
_JnxTimingCompliances_ObjectIdentity = ObjectIdentity
jnxTimingCompliances = _JnxTimingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 1)
)
_JnxTimingGroups_ObjectIdentity = ObjectIdentity
jnxTimingGroups = _JnxTimingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2)
)

# Managed Objects groups

jnxTimingObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2, 1)
)
jnxTimingObjectsGroup.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMinor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMinor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCode"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpClass"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpAccuracy"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmIpAddr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClkStreamHandle"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxRemoteIpAddr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpPhaseOffset"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCodeStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoStateStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridStateStr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncColorStr"))
)
if mibBuilder.loadTexts:
    jnxTimingObjectsGroup.setStatus("current")


# Notification objects

jnxTimingFaultLOSSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 1)
)
jnxTimingFaultLOSSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOSSet.setStatus(
        "current"
    )

jnxTimingFaultLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 2)
)
jnxTimingFaultLOSClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOSClear.setStatus(
        "current"
    )

jnxTimingFaultEFDSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 3)
)
jnxTimingFaultEFDSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultEFDSet.setStatus(
        "current"
    )

jnxTimingFaultEFDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 4)
)
jnxTimingFaultEFDClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultEFDClear.setStatus(
        "current"
    )

jnxTimingFaultLOESMCSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 5)
)
jnxTimingFaultLOESMCSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOESMCSet.setStatus(
        "current"
    )

jnxTimingFaultLOESMCClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 6)
)
jnxTimingFaultLOESMCClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLOESMCClear.setStatus(
        "current"
    )

jnxTimingFaultQLFailSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 7)
)
jnxTimingFaultQLFailSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultQLFailSet.setStatus(
        "current"
    )

jnxTimingFaultQLFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 8)
)
jnxTimingFaultQLFailClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultQLFailClear.setStatus(
        "current"
    )

jnxTimingFaultLTISet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 9)
)
jnxTimingFaultLTISet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLTISet.setStatus(
        "current"
    )

jnxTimingFaultLTIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 10)
)
jnxTimingFaultLTIClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultLTIClear.setStatus(
        "current"
    )

jnxTimingFaultAcbcFpgaVerNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 11)
)
jnxTimingFaultAcbcFpgaVerNotCompatible.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxAcbFpgaRevMinor"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultAcbcFpgaVerNotCompatible.setStatus(
        "current"
    )

jnxTimingFaultBootCpldVerNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 12)
)
jnxTimingFaultBootCpldVerNotCompatible.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMajor"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxBootCpldFpgaRevMinor"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultBootCpldVerNotCompatible.setStatus(
        "current"
    )

jnxTimingFaultPriSrcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 13)
)
jnxTimingFaultPriSrcFailed.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultPriSrcFailed.setStatus(
        "current"
    )

jnxTimingFaultSecSrcFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 14)
)
jnxTimingFaultSecSrcFailed.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultSecSrcFailed.setStatus(
        "current"
    )

jnxTimingFaultPtpUniNegRateRejectSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 15)
)
jnxTimingFaultPtpUniNegRateRejectSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClkStreamHandle"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxRemoteIpAddr"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultPtpUniNegRateRejectSet.setStatus(
        "current"
    )

jnxTimingFaultPtpUniNegRateRejectClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 16)
)
jnxTimingFaultPtpUniNegRateRejectClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClkStreamHandle"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxRemoteIpAddr"))
)
if mibBuilder.loadTexts:
    jnxTimingFaultPtpUniNegRateRejectClear.setStatus(
        "current"
    )

jnxTimingEventSquelchSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 17)
)
jnxTimingEventSquelchSet.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSquelchSet.setStatus(
        "current"
    )

jnxTimingEventSquelchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 1, 18)
)
jnxTimingEventSquelchClear.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSquelchClear.setStatus(
        "current"
    )

jnxTimingEventPriSrcRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 1)
)
jnxTimingEventPriSrcRecovered.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPriSrcRecovered.setStatus(
        "current"
    )

jnxTimingEventSecSrcRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 2)
)
jnxTimingEventSecSrcRecovered.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSecSrcRecovered.setStatus(
        "current"
    )

jnxTimingEventPriRefChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 3)
)
jnxTimingEventPriRefChanged.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPriRefChanged.setStatus(
        "current"
    )

jnxTimingEventSecRefChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 4)
)
jnxTimingEventSecRefChanged.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSecRefChanged.setStatus(
        "current"
    )

jnxTimingEventQLChangedRx = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 5)
)
jnxTimingEventQLChangedRx.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCode"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCodeStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventQLChangedRx.setStatus(
        "current"
    )

jnxTimingEventQLChangedTx = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 6)
)
jnxTimingEventQLChangedTx.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCode"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncQualityCodeStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventQLChangedTx.setStatus(
        "current"
    )

jnxTimingEventSynceHldovrToLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 7)
)
jnxTimingEventSynceHldovrToLck.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSynceHldovrToLck.setStatus(
        "current"
    )

jnxTimingEventSynceLckToHldovr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 8)
)
jnxTimingEventSynceLckToHldovr.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSynceLckToHldovr.setStatus(
        "current"
    )

jnxTimingEventDpllStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 9)
)
jnxTimingEventDpllStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventDpllStatus.setStatus(
        "current"
    )

jnxTimingEventSynceDpllStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 10)
)
jnxTimingEventSynceDpllStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventSynceDpllStatus.setStatus(
        "current"
    )

jnxTimingEventBitsDpllStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 11)
)
jnxTimingEventBitsDpllStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncDpllStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventBitsDpllStatus.setStatus(
        "current"
    )

jnxTimingEventPtpServoStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 12)
)
jnxTimingEventPtpServoStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpServoStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpServoStatus.setStatus(
        "current"
    )

jnxTimingEventPtpGMClockClassChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 13)
)
jnxTimingEventPtpGMClockClassChange.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpClass"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpGMClockClassChange.setStatus(
        "current"
    )

jnxTimingEventPtpGMClockAccuracyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 14)
)
jnxTimingEventPtpGMClockAccuracyChange.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpAccuracy"))
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpGMClockAccuracyChange.setStatus(
        "current"
    )

jnxTimingEventPtpGMChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 15)
)
jnxTimingEventPtpGMChange.setObjects(
    ("JUNIPER-TIMING-NOTFNS-MIB", "jnxPtpGmId")
)
if mibBuilder.loadTexts:
    jnxTimingEventPtpGMChange.setStatus(
        "current"
    )

jnxTimingEventHybridStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 16)
)
jnxTimingEventHybridStatus.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridState"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncHybridStateStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventHybridStatus.setStatus(
        "current"
    )

jnxTimingEventLedColorChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 2, 19)
)
jnxTimingEventLedColorChange.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIfIndex"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncIntfName"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxClksyncColorStr"))
)
if mibBuilder.loadTexts:
    jnxTimingEventLedColorChange.setStatus(
        "current"
    )


# Notifications groups

jnxTimingNotfnFaultsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2, 2)
)
jnxTimingNotfnFaultsGroup.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOSSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOSClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultEFDSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultEFDClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOESMCSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLOESMCClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultQLFailSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultQLFailClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLTISet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultLTIClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultAcbcFpgaVerNotCompatible"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultBootCpldVerNotCompatible"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultPriSrcFailed"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultSecSrcFailed"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultPtpUniNegRateRejectSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingFaultPtpUniNegRateRejectClear"))
)
if mibBuilder.loadTexts:
    jnxTimingNotfnFaultsGroup.setStatus(
        "current"
    )

jnxTimingNotfnEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 2, 3)
)
jnxTimingNotfnEventsGroup.setObjects(
      *(("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPriSrcRecovered"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSecSrcRecovered"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPriRefChanged"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSecRefChanged"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventQLChangedRx"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventQLChangedTx"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSynceHldovrToLck"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSynceLckToHldovr"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventDpllStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSynceDpllStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventBitsDpllStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpServoStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpGMClockClassChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpGMClockAccuracyChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventPtpGMChange"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventHybridStatus"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSquelchSet"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventSquelchClear"),
        ("JUNIPER-TIMING-NOTFNS-MIB", "jnxTimingEventLedColorChange"))
)
if mibBuilder.loadTexts:
    jnxTimingNotfnEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

jnxTimingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2636, 3, 75, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jnxTimingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-TIMING-NOTFNS-MIB",
    **{"JnxPtpClockIdTC": JnxPtpClockIdTC,
       "JnxPtpPhaseOffsetTC": JnxPtpPhaseOffsetTC,
       "jnxTimingNotfnsMIB": jnxTimingNotfnsMIB,
       "jnxTimingFaults": jnxTimingFaults,
       "jnxTimingFaultLOSSet": jnxTimingFaultLOSSet,
       "jnxTimingFaultLOSClear": jnxTimingFaultLOSClear,
       "jnxTimingFaultEFDSet": jnxTimingFaultEFDSet,
       "jnxTimingFaultEFDClear": jnxTimingFaultEFDClear,
       "jnxTimingFaultLOESMCSet": jnxTimingFaultLOESMCSet,
       "jnxTimingFaultLOESMCClear": jnxTimingFaultLOESMCClear,
       "jnxTimingFaultQLFailSet": jnxTimingFaultQLFailSet,
       "jnxTimingFaultQLFailClear": jnxTimingFaultQLFailClear,
       "jnxTimingFaultLTISet": jnxTimingFaultLTISet,
       "jnxTimingFaultLTIClear": jnxTimingFaultLTIClear,
       "jnxTimingFaultAcbcFpgaVerNotCompatible": jnxTimingFaultAcbcFpgaVerNotCompatible,
       "jnxTimingFaultBootCpldVerNotCompatible": jnxTimingFaultBootCpldVerNotCompatible,
       "jnxTimingFaultPriSrcFailed": jnxTimingFaultPriSrcFailed,
       "jnxTimingFaultSecSrcFailed": jnxTimingFaultSecSrcFailed,
       "jnxTimingFaultPtpUniNegRateRejectSet": jnxTimingFaultPtpUniNegRateRejectSet,
       "jnxTimingFaultPtpUniNegRateRejectClear": jnxTimingFaultPtpUniNegRateRejectClear,
       "jnxTimingEventSquelchSet": jnxTimingEventSquelchSet,
       "jnxTimingEventSquelchClear": jnxTimingEventSquelchClear,
       "jnxTimingEvents": jnxTimingEvents,
       "jnxTimingEventPriSrcRecovered": jnxTimingEventPriSrcRecovered,
       "jnxTimingEventSecSrcRecovered": jnxTimingEventSecSrcRecovered,
       "jnxTimingEventPriRefChanged": jnxTimingEventPriRefChanged,
       "jnxTimingEventSecRefChanged": jnxTimingEventSecRefChanged,
       "jnxTimingEventQLChangedRx": jnxTimingEventQLChangedRx,
       "jnxTimingEventQLChangedTx": jnxTimingEventQLChangedTx,
       "jnxTimingEventSynceHldovrToLck": jnxTimingEventSynceHldovrToLck,
       "jnxTimingEventSynceLckToHldovr": jnxTimingEventSynceLckToHldovr,
       "jnxTimingEventDpllStatus": jnxTimingEventDpllStatus,
       "jnxTimingEventSynceDpllStatus": jnxTimingEventSynceDpllStatus,
       "jnxTimingEventBitsDpllStatus": jnxTimingEventBitsDpllStatus,
       "jnxTimingEventPtpServoStatus": jnxTimingEventPtpServoStatus,
       "jnxTimingEventPtpGMClockClassChange": jnxTimingEventPtpGMClockClassChange,
       "jnxTimingEventPtpGMClockAccuracyChange": jnxTimingEventPtpGMClockAccuracyChange,
       "jnxTimingEventPtpGMChange": jnxTimingEventPtpGMChange,
       "jnxTimingEventHybridStatus": jnxTimingEventHybridStatus,
       "jnxTimingEventLedColorChange": jnxTimingEventLedColorChange,
       "jnxTimingNotfObjects": jnxTimingNotfObjects,
       "jnxClksyncState": jnxClksyncState,
       "jnxClksyncIfIndex": jnxClksyncIfIndex,
       "jnxClksyncIntfName": jnxClksyncIntfName,
       "jnxAcbFpgaRevMajor": jnxAcbFpgaRevMajor,
       "jnxAcbFpgaRevMinor": jnxAcbFpgaRevMinor,
       "jnxBootCpldFpgaRevMajor": jnxBootCpldFpgaRevMajor,
       "jnxBootCpldFpgaRevMinor": jnxBootCpldFpgaRevMinor,
       "jnxClksyncQualityCode": jnxClksyncQualityCode,
       "jnxClksyncDpllState": jnxClksyncDpllState,
       "jnxPtpServoState": jnxPtpServoState,
       "jnxPtpClass": jnxPtpClass,
       "jnxPtpAccuracy": jnxPtpAccuracy,
       "jnxPtpGmId": jnxPtpGmId,
       "jnxPtpGmIpAddr": jnxPtpGmIpAddr,
       "jnxClkStreamHandle": jnxClkStreamHandle,
       "jnxRemoteIpAddr": jnxRemoteIpAddr,
       "jnxClksyncHybridState": jnxClksyncHybridState,
       "jnxPtpPhaseOffset": jnxPtpPhaseOffset,
       "jnxClksyncQualityCodeStr": jnxClksyncQualityCodeStr,
       "jnxClksyncDpllStateStr": jnxClksyncDpllStateStr,
       "jnxPtpServoStateStr": jnxPtpServoStateStr,
       "jnxClksyncHybridStateStr": jnxClksyncHybridStateStr,
       "jnxClksyncColorStr": jnxClksyncColorStr,
       "jnxTimingConformance": jnxTimingConformance,
       "jnxTimingCompliances": jnxTimingCompliances,
       "jnxTimingCompliance": jnxTimingCompliance,
       "jnxTimingGroups": jnxTimingGroups,
       "jnxTimingObjectsGroup": jnxTimingObjectsGroup,
       "jnxTimingNotfnFaultsGroup": jnxTimingNotfnFaultsGroup,
       "jnxTimingNotfnEventsGroup": jnxTimingNotfnEventsGroup}
)
