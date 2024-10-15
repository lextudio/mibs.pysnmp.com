# SNMP MIB module (TMU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TMU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:27 2024
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
 internet,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "internet",
    "iso",
    "mgmt")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Tmu_ObjectIdentity = ObjectIdentity
tmu = _Tmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60)
)
_TmuSystem_ObjectIdentity = ObjectIdentity
tmuSystem = _TmuSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 1)
)
_FibTmuNumEventErrs_Type = Counter32
_FibTmuNumEventErrs_Object = MibScalar
fibTmuNumEventErrs = _FibTmuNumEventErrs_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 1),
    _FibTmuNumEventErrs_Type()
)
fibTmuNumEventErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumEventErrs.setStatus("mandatory")
_FibTmuArpAgeTime_Type = TimeTicks
_FibTmuArpAgeTime_Object = MibScalar
fibTmuArpAgeTime = _FibTmuArpAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 2),
    _FibTmuArpAgeTime_Type()
)
fibTmuArpAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuArpAgeTime.setStatus("mandatory")
_FibTmuNumRarpUpdate_Type = Counter32
_FibTmuNumRarpUpdate_Object = MibScalar
fibTmuNumRarpUpdate = _FibTmuNumRarpUpdate_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 3),
    _FibTmuNumRarpUpdate_Type()
)
fibTmuNumRarpUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRarpUpdate.setStatus("mandatory")
_FibTmuMainSwVersion_Type = Integer32
_FibTmuMainSwVersion_Object = MibScalar
fibTmuMainSwVersion = _FibTmuMainSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 4),
    _FibTmuMainSwVersion_Type()
)
fibTmuMainSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMainSwVersion.setStatus("mandatory")
_FibTmuEepromVersion_Type = Integer32
_FibTmuEepromVersion_Object = MibScalar
fibTmuEepromVersion = _FibTmuEepromVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 5),
    _FibTmuEepromVersion_Type()
)
fibTmuEepromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuEepromVersion.setStatus("mandatory")
_FibTmuEepromDeffective_Type = Integer32
_FibTmuEepromDeffective_Object = MibScalar
fibTmuEepromDeffective = _FibTmuEepromDeffective_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 6),
    _FibTmuEepromDeffective_Type()
)
fibTmuEepromDeffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuEepromDeffective.setStatus("mandatory")
_FibTmuLastSysIfIndex_Type = Integer32
_FibTmuLastSysIfIndex_Object = MibScalar
fibTmuLastSysIfIndex = _FibTmuLastSysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 7),
    _FibTmuLastSysIfIndex_Type()
)
fibTmuLastSysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuLastSysIfIndex.setStatus("mandatory")
_FibTmuTrDrvVersion_Type = Integer32
_FibTmuTrDrvVersion_Object = MibScalar
fibTmuTrDrvVersion = _FibTmuTrDrvVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 8),
    _FibTmuTrDrvVersion_Type()
)
fibTmuTrDrvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuTrDrvVersion.setStatus("mandatory")
_FibTmuSccDrvVersion_Type = Integer32
_FibTmuSccDrvVersion_Object = MibScalar
fibTmuSccDrvVersion = _FibTmuSccDrvVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 9),
    _FibTmuSccDrvVersion_Type()
)
fibTmuSccDrvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuSccDrvVersion.setStatus("mandatory")
_FibTmuSnmpUsrVersion_Type = Integer32
_FibTmuSnmpUsrVersion_Object = MibScalar
fibTmuSnmpUsrVersion = _FibTmuSnmpUsrVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 10),
    _FibTmuSnmpUsrVersion_Type()
)
fibTmuSnmpUsrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuSnmpUsrVersion.setStatus("mandatory")


class _FibTmuDisplayDebugMode_Type(Integer32):
    """Custom type fibTmuDisplayDebugMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular-mode", 1),
          ("special-debug-mode", 2))
    )


_FibTmuDisplayDebugMode_Type.__name__ = "Integer32"
_FibTmuDisplayDebugMode_Object = MibScalar
fibTmuDisplayDebugMode = _FibTmuDisplayDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 11),
    _FibTmuDisplayDebugMode_Type()
)
fibTmuDisplayDebugMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuDisplayDebugMode.setStatus("mandatory")


class _FibTmuEeFaultsFormat_Type(Integer32):
    """Custom type fibTmuEeFaultsFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concise-mode", 2),
          ("full-mode", 1))
    )


_FibTmuEeFaultsFormat_Type.__name__ = "Integer32"
_FibTmuEeFaultsFormat_Object = MibScalar
fibTmuEeFaultsFormat = _FibTmuEeFaultsFormat_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 12),
    _FibTmuEeFaultsFormat_Type()
)
fibTmuEeFaultsFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuEeFaultsFormat.setStatus("mandatory")


class _FibTmuRunFaultsFormat_Type(Integer32):
    """Custom type fibTmuRunFaultsFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concise-mode", 2),
          ("full-mode", 1))
    )


_FibTmuRunFaultsFormat_Type.__name__ = "Integer32"
_FibTmuRunFaultsFormat_Object = MibScalar
fibTmuRunFaultsFormat = _FibTmuRunFaultsFormat_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 13),
    _FibTmuRunFaultsFormat_Type()
)
fibTmuRunFaultsFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuRunFaultsFormat.setStatus("mandatory")
_FibTmuFunctionalityVersion_Type = Integer32
_FibTmuFunctionalityVersion_Object = MibScalar
fibTmuFunctionalityVersion = _FibTmuFunctionalityVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 14),
    _FibTmuFunctionalityVersion_Type()
)
fibTmuFunctionalityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctionalityVersion.setStatus("mandatory")
_FibTmuUtilitiesVersion_Type = Integer32
_FibTmuUtilitiesVersion_Object = MibScalar
fibTmuUtilitiesVersion = _FibTmuUtilitiesVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 15),
    _FibTmuUtilitiesVersion_Type()
)
fibTmuUtilitiesVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuUtilitiesVersion.setStatus("mandatory")


class _FibTmuWrapIn_Type(Integer32):
    """Custom type fibTmuWrapIn based on Integer32"""
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
        *(("no-wrap", 1),
          ("wrap-set-by-Tmu", 3),
          ("wrap-set-by-both", 4),
          ("wrap-set-by-manager", 2))
    )


_FibTmuWrapIn_Type.__name__ = "Integer32"
_FibTmuWrapIn_Object = MibScalar
fibTmuWrapIn = _FibTmuWrapIn_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 16),
    _FibTmuWrapIn_Type()
)
fibTmuWrapIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuWrapIn.setStatus("mandatory")


class _FibTmuWrapOut_Type(Integer32):
    """Custom type fibTmuWrapOut based on Integer32"""
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
        *(("no-wrap", 1),
          ("wrap-set-by-Tmu", 3),
          ("wrap-set-by-both", 4),
          ("wrap-set-by-manager", 2))
    )


_FibTmuWrapOut_Type.__name__ = "Integer32"
_FibTmuWrapOut_Object = MibScalar
fibTmuWrapOut = _FibTmuWrapOut_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 17),
    _FibTmuWrapOut_Type()
)
fibTmuWrapOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuWrapOut.setStatus("mandatory")


class _FibTmuLoadEeDefaults_Type(Integer32):
    """Custom type fibTmuLoadEeDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-load-default", 1),
          ("load-defaults", 2))
    )


_FibTmuLoadEeDefaults_Type.__name__ = "Integer32"
_FibTmuLoadEeDefaults_Object = MibScalar
fibTmuLoadEeDefaults = _FibTmuLoadEeDefaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 18),
    _FibTmuLoadEeDefaults_Type()
)
fibTmuLoadEeDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuLoadEeDefaults.setStatus("mandatory")


class _FibTmuDontResetFatal_Type(Integer32):
    """Custom type fibTmuDontResetFatal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-reset-fatal", 2),
          ("reset-fatal", 1))
    )


_FibTmuDontResetFatal_Type.__name__ = "Integer32"
_FibTmuDontResetFatal_Object = MibScalar
fibTmuDontResetFatal = _FibTmuDontResetFatal_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 19),
    _FibTmuDontResetFatal_Type()
)
fibTmuDontResetFatal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuDontResetFatal.setStatus("mandatory")


class _FibTmuRIConnection_Type(Integer32):
    """Custom type fibTmuRIConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("none", 0))
    )


_FibTmuRIConnection_Type.__name__ = "Integer32"
_FibTmuRIConnection_Object = MibScalar
fibTmuRIConnection = _FibTmuRIConnection_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 20),
    _FibTmuRIConnection_Type()
)
fibTmuRIConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuRIConnection.setStatus("mandatory")


class _FibTmuROConnection_Type(Integer32):
    """Custom type fibTmuROConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("none", 0))
    )


_FibTmuROConnection_Type.__name__ = "Integer32"
_FibTmuROConnection_Object = MibScalar
fibTmuROConnection = _FibTmuROConnection_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 21),
    _FibTmuROConnection_Type()
)
fibTmuROConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuROConnection.setStatus("mandatory")


class _FibTmuRealTimeClock_Type(DisplayString):
    """Custom type fibTmuRealTimeClock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(23, 23),
    )


_FibTmuRealTimeClock_Type.__name__ = "DisplayString"
_FibTmuRealTimeClock_Object = MibScalar
fibTmuRealTimeClock = _FibTmuRealTimeClock_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 1, 22),
    _FibTmuRealTimeClock_Type()
)
fibTmuRealTimeClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuRealTimeClock.setStatus("mandatory")
_TmuIntrfc_ObjectIdentity = ObjectIdentity
tmuIntrfc = _TmuIntrfc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 2)
)
_FibTmuIntrfcTable_Object = MibTable
fibTmuIntrfcTable = _FibTmuIntrfcTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1)
)
if mibBuilder.loadTexts:
    fibTmuIntrfcTable.setStatus("mandatory")
_FibTmuIntrfcEntry_Object = MibTableRow
fibTmuIntrfcEntry = _FibTmuIntrfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1)
)
fibTmuIntrfcEntry.setIndexNames(
    (0, "TMU-MIB", "fibTmuIntrfcIndex"),
)
if mibBuilder.loadTexts:
    fibTmuIntrfcEntry.setStatus("mandatory")
_FibTmuIntrfcIndex_Type = Integer32
_FibTmuIntrfcIndex_Object = MibTableColumn
fibTmuIntrfcIndex = _FibTmuIntrfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 1),
    _FibTmuIntrfcIndex_Type()
)
fibTmuIntrfcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuIntrfcIndex.setStatus("mandatory")
_FibTmuNumRarpRcvd_Type = Counter32
_FibTmuNumRarpRcvd_Object = MibTableColumn
fibTmuNumRarpRcvd = _FibTmuNumRarpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 2),
    _FibTmuNumRarpRcvd_Type()
)
fibTmuNumRarpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRarpRcvd.setStatus("mandatory")
_FibTmuNumRxRjctMem_Type = Counter32
_FibTmuNumRxRjctMem_Object = MibTableColumn
fibTmuNumRxRjctMem = _FibTmuNumRxRjctMem_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 3),
    _FibTmuNumRxRjctMem_Type()
)
fibTmuNumRxRjctMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRxRjctMem.setStatus("mandatory")
_FibTmuNumRxAccepted_Type = Counter32
_FibTmuNumRxAccepted_Object = MibTableColumn
fibTmuNumRxAccepted = _FibTmuNumRxAccepted_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 4),
    _FibTmuNumRxAccepted_Type()
)
fibTmuNumRxAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRxAccepted.setStatus("mandatory")
_FibTmuNumRxBdcst_Type = Counter32
_FibTmuNumRxBdcst_Object = MibTableColumn
fibTmuNumRxBdcst = _FibTmuNumRxBdcst_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 5),
    _FibTmuNumRxBdcst_Type()
)
fibTmuNumRxBdcst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRxBdcst.setStatus("mandatory")
_FibTmuNumRxSpecific_Type = Counter32
_FibTmuNumRxSpecific_Object = MibTableColumn
fibTmuNumRxSpecific = _FibTmuNumRxSpecific_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 6),
    _FibTmuNumRxSpecific_Type()
)
fibTmuNumRxSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRxSpecific.setStatus("mandatory")
_FibTmuNumRifIncluded_Type = Counter32
_FibTmuNumRifIncluded_Object = MibTableColumn
fibTmuNumRifIncluded = _FibTmuNumRifIncluded_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 7),
    _FibTmuNumRifIncluded_Type()
)
fibTmuNumRifIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRifIncluded.setStatus("mandatory")
_FibTmuNumNoRif_Type = Counter32
_FibTmuNumNoRif_Object = MibTableColumn
fibTmuNumNoRif = _FibTmuNumNoRif_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 8),
    _FibTmuNumNoRif_Type()
)
fibTmuNumNoRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumNoRif.setStatus("mandatory")
_FibTmuNumNonSnap_Type = Counter32
_FibTmuNumNonSnap_Object = MibTableColumn
fibTmuNumNonSnap = _FibTmuNumNonSnap_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 9),
    _FibTmuNumNonSnap_Type()
)
fibTmuNumNonSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumNonSnap.setStatus("mandatory")
_FibTmuNumUnknownType_Type = Counter32
_FibTmuNumUnknownType_Object = MibTableColumn
fibTmuNumUnknownType = _FibTmuNumUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 10),
    _FibTmuNumUnknownType_Type()
)
fibTmuNumUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumUnknownType.setStatus("mandatory")
_FibTmuNumRifLong_Type = Counter32
_FibTmuNumRifLong_Object = MibTableColumn
fibTmuNumRifLong = _FibTmuNumRifLong_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 11),
    _FibTmuNumRifLong_Type()
)
fibTmuNumRifLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRifLong.setStatus("mandatory")
_FibTmuNumRrpRjctIp_Type = Counter32
_FibTmuNumRrpRjctIp_Object = MibTableColumn
fibTmuNumRrpRjctIp = _FibTmuNumRrpRjctIp_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 12),
    _FibTmuNumRrpRjctIp_Type()
)
fibTmuNumRrpRjctIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRrpRjctIp.setStatus("mandatory")
_FibTmuNumArpRcvd_Type = Counter32
_FibTmuNumArpRcvd_Object = MibTableColumn
fibTmuNumArpRcvd = _FibTmuNumArpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 13),
    _FibTmuNumArpRcvd_Type()
)
fibTmuNumArpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumArpRcvd.setStatus("mandatory")
_FibTmuNumIpRcvd_Type = Counter32
_FibTmuNumIpRcvd_Object = MibTableColumn
fibTmuNumIpRcvd = _FibTmuNumIpRcvd_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 14),
    _FibTmuNumIpRcvd_Type()
)
fibTmuNumIpRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumIpRcvd.setStatus("mandatory")
_FibTmuNumIfDown_Type = Counter32
_FibTmuNumIfDown_Object = MibTableColumn
fibTmuNumIfDown = _FibTmuNumIfDown_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 15),
    _FibTmuNumIfDown_Type()
)
fibTmuNumIfDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumIfDown.setStatus("mandatory")
_FibTmuNumOwnBrdcst_Type = Counter32
_FibTmuNumOwnBrdcst_Object = MibTableColumn
fibTmuNumOwnBrdcst = _FibTmuNumOwnBrdcst_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 16),
    _FibTmuNumOwnBrdcst_Type()
)
fibTmuNumOwnBrdcst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumOwnBrdcst.setStatus("mandatory")
_FibTmuAc00Cntr_Type = Counter32
_FibTmuAc00Cntr_Object = MibTableColumn
fibTmuAc00Cntr = _FibTmuAc00Cntr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 17),
    _FibTmuAc00Cntr_Type()
)
fibTmuAc00Cntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuAc00Cntr.setStatus("mandatory")
_FibTmuAc01Cntr_Type = Counter32
_FibTmuAc01Cntr_Object = MibTableColumn
fibTmuAc01Cntr = _FibTmuAc01Cntr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 18),
    _FibTmuAc01Cntr_Type()
)
fibTmuAc01Cntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuAc01Cntr.setStatus("mandatory")
_FibTmuAc10Cntr_Type = Counter32
_FibTmuAc10Cntr_Object = MibTableColumn
fibTmuAc10Cntr = _FibTmuAc10Cntr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 19),
    _FibTmuAc10Cntr_Type()
)
fibTmuAc10Cntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuAc10Cntr.setStatus("mandatory")
_FibTmuAc11Cntr_Type = Counter32
_FibTmuAc11Cntr_Object = MibTableColumn
fibTmuAc11Cntr = _FibTmuAc11Cntr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 20),
    _FibTmuAc11Cntr_Type()
)
fibTmuAc11Cntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuAc11Cntr.setStatus("mandatory")
_FibTmuParityEc_Type = Counter32
_FibTmuParityEc_Object = MibTableColumn
fibTmuParityEc = _FibTmuParityEc_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 21),
    _FibTmuParityEc_Type()
)
fibTmuParityEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuParityEc.setStatus("mandatory")
_FibTmuFrameEc_Type = Counter32
_FibTmuFrameEc_Object = MibTableColumn
fibTmuFrameEc = _FibTmuFrameEc_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 22),
    _FibTmuFrameEc_Type()
)
fibTmuFrameEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFrameEc.setStatus("mandatory")
_FibTmuRxNoiseEc_Type = Counter32
_FibTmuRxNoiseEc_Object = MibTableColumn
fibTmuRxNoiseEc = _FibTmuRxNoiseEc_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 23),
    _FibTmuRxNoiseEc_Type()
)
fibTmuRxNoiseEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuRxNoiseEc.setStatus("mandatory")
_FibTmuBreakEc_Type = Counter32
_FibTmuBreakEc_Object = MibTableColumn
fibTmuBreakEc = _FibTmuBreakEc_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 24),
    _FibTmuBreakEc_Type()
)
fibTmuBreakEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuBreakEc.setStatus("mandatory")
_FibTmuNumConfigNotValid_Type = Counter32
_FibTmuNumConfigNotValid_Object = MibTableColumn
fibTmuNumConfigNotValid = _FibTmuNumConfigNotValid_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 25),
    _FibTmuNumConfigNotValid_Type()
)
fibTmuNumConfigNotValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumConfigNotValid.setStatus("mandatory")
_FibTmuNumAddrNotFound_Type = Counter32
_FibTmuNumAddrNotFound_Object = MibTableColumn
fibTmuNumAddrNotFound = _FibTmuNumAddrNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 26),
    _FibTmuNumAddrNotFound_Type()
)
fibTmuNumAddrNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumAddrNotFound.setStatus("mandatory")
_FibTmuNumProcessDisabled_Type = Counter32
_FibTmuNumProcessDisabled_Object = MibTableColumn
fibTmuNumProcessDisabled = _FibTmuNumProcessDisabled_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 27),
    _FibTmuNumProcessDisabled_Type()
)
fibTmuNumProcessDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumProcessDisabled.setStatus("mandatory")
_FibTmuNumBeaconsRcvd_Type = Counter32
_FibTmuNumBeaconsRcvd_Object = MibTableColumn
fibTmuNumBeaconsRcvd = _FibTmuNumBeaconsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 28),
    _FibTmuNumBeaconsRcvd_Type()
)
fibTmuNumBeaconsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumBeaconsRcvd.setStatus("mandatory")
_FibTmuLastBeaconTime_Type = TimeTicks
_FibTmuLastBeaconTime_Object = MibTableColumn
fibTmuLastBeaconTime = _FibTmuLastBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 29),
    _FibTmuLastBeaconTime_Type()
)
fibTmuLastBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuLastBeaconTime.setStatus("mandatory")
_FibTmuLastBeaconType_Type = Integer32
_FibTmuLastBeaconType_Object = MibTableColumn
fibTmuLastBeaconType = _FibTmuLastBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 30),
    _FibTmuLastBeaconType_Type()
)
fibTmuLastBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuLastBeaconType.setStatus("mandatory")
_FibTmuLastBeaconAddr_Type = MacAddress
_FibTmuLastBeaconAddr_Object = MibTableColumn
fibTmuLastBeaconAddr = _FibTmuLastBeaconAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 31),
    _FibTmuLastBeaconAddr_Type()
)
fibTmuLastBeaconAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuLastBeaconAddr.setStatus("mandatory")
_FibTmuLastBeaconNaun_Type = MacAddress
_FibTmuLastBeaconNaun_Object = MibTableColumn
fibTmuLastBeaconNaun = _FibTmuLastBeaconNaun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 32),
    _FibTmuLastBeaconNaun_Type()
)
fibTmuLastBeaconNaun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuLastBeaconNaun.setStatus("mandatory")
_FibTmuNumRxGroup_Type = Counter32
_FibTmuNumRxGroup_Object = MibTableColumn
fibTmuNumRxGroup = _FibTmuNumRxGroup_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 33),
    _FibTmuNumRxGroup_Type()
)
fibTmuNumRxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRxGroup.setStatus("mandatory")
_FibTmuNumRxFunctional_Type = Counter32
_FibTmuNumRxFunctional_Object = MibTableColumn
fibTmuNumRxFunctional = _FibTmuNumRxFunctional_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 2, 1, 1, 34),
    _FibTmuNumRxFunctional_Type()
)
fibTmuNumRxFunctional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumRxFunctional.setStatus("mandatory")
_TmuMatch_ObjectIdentity = ObjectIdentity
tmuMatch = _TmuMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 3)
)
_FibTmuMatchUpdateTime_Type = TimeTicks
_FibTmuMatchUpdateTime_Object = MibScalar
fibTmuMatchUpdateTime = _FibTmuMatchUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 1),
    _FibTmuMatchUpdateTime_Type()
)
fibTmuMatchUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchUpdateTime.setStatus("mandatory")
_FibTmuMatchNumEntries_Type = Integer32
_FibTmuMatchNumEntries_Object = MibScalar
fibTmuMatchNumEntries = _FibTmuMatchNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 2),
    _FibTmuMatchNumEntries_Type()
)
fibTmuMatchNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchNumEntries.setStatus("mandatory")
_FibTmuMatchNumTmuEntries_Type = Integer32
_FibTmuMatchNumTmuEntries_Object = MibScalar
fibTmuMatchNumTmuEntries = _FibTmuMatchNumTmuEntries_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 3),
    _FibTmuMatchNumTmuEntries_Type()
)
fibTmuMatchNumTmuEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchNumTmuEntries.setStatus("mandatory")
_FibTmuMatchFirstChipIndex_Type = Integer32
_FibTmuMatchFirstChipIndex_Object = MibScalar
fibTmuMatchFirstChipIndex = _FibTmuMatchFirstChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 4),
    _FibTmuMatchFirstChipIndex_Type()
)
fibTmuMatchFirstChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchFirstChipIndex.setStatus("mandatory")
_FibTmuMatchSecondChipIndex_Type = Integer32
_FibTmuMatchSecondChipIndex_Object = MibScalar
fibTmuMatchSecondChipIndex = _FibTmuMatchSecondChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 5),
    _FibTmuMatchSecondChipIndex_Type()
)
fibTmuMatchSecondChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchSecondChipIndex.setStatus("mandatory")
_FibTmuMatchActMonIndex_Type = Integer32
_FibTmuMatchActMonIndex_Object = MibScalar
fibTmuMatchActMonIndex = _FibTmuMatchActMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 6),
    _FibTmuMatchActMonIndex_Type()
)
fibTmuMatchActMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchActMonIndex.setStatus("mandatory")
_FibTmuMatchConfigChipIndex_Type = Integer32
_FibTmuMatchConfigChipIndex_Object = MibScalar
fibTmuMatchConfigChipIndex = _FibTmuMatchConfigChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 7),
    _FibTmuMatchConfigChipIndex_Type()
)
fibTmuMatchConfigChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchConfigChipIndex.setStatus("mandatory")


class _FibTmuMatchListValid_Type(Integer32):
    """Custom type fibTmuMatchListValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", -1),
          ("valid", 2))
    )


_FibTmuMatchListValid_Type.__name__ = "Integer32"
_FibTmuMatchListValid_Object = MibScalar
fibTmuMatchListValid = _FibTmuMatchListValid_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 8),
    _FibTmuMatchListValid_Type()
)
fibTmuMatchListValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchListValid.setStatus("mandatory")


class _FibTmuMatchUpToDate_Type(Integer32):
    """Custom type fibTmuMatchUpToDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-up-to-date", 1),
          ("up-to-date", 2))
    )


_FibTmuMatchUpToDate_Type.__name__ = "Integer32"
_FibTmuMatchUpToDate_Object = MibScalar
fibTmuMatchUpToDate = _FibTmuMatchUpToDate_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 9),
    _FibTmuMatchUpToDate_Type()
)
fibTmuMatchUpToDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchUpToDate.setStatus("mandatory")


class _FibTmuMatchNoMatchReason_Type(Integer32):
    """Custom type fibTmuMatchNoMatchReason based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("empty-reason", 1),
          ("first-not-found", 8),
          ("found-twice", 10),
          ("inconsistency", 5),
          ("malloc-fail", 2),
          ("no-chip-on-list", 4),
          ("no-tr-list", 14),
          ("ports-gt-stations", 12),
          ("second-not-found", 9),
          ("segment-unstable", 3),
          ("soft-01", 6),
          ("soft-02", 7),
          ("soft-03", 11),
          ("stations-gt-ports", 13))
    )


_FibTmuMatchNoMatchReason_Type.__name__ = "Integer32"
_FibTmuMatchNoMatchReason_Object = MibScalar
fibTmuMatchNoMatchReason = _FibTmuMatchNoMatchReason_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 10),
    _FibTmuMatchNoMatchReason_Type()
)
fibTmuMatchNoMatchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchNoMatchReason.setStatus("mandatory")
_FibTmuMatchTable_Object = MibTable
fibTmuMatchTable = _FibTmuMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20)
)
if mibBuilder.loadTexts:
    fibTmuMatchTable.setStatus("mandatory")
_FibTmuMatchEntry_Object = MibTableRow
fibTmuMatchEntry = _FibTmuMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20, 1)
)
fibTmuMatchEntry.setIndexNames(
    (0, "TMU-MIB", "fibTmuMatchIndex"),
)
if mibBuilder.loadTexts:
    fibTmuMatchEntry.setStatus("mandatory")
_FibTmuMatchIndex_Type = Integer32
_FibTmuMatchIndex_Object = MibTableColumn
fibTmuMatchIndex = _FibTmuMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20, 1, 1),
    _FibTmuMatchIndex_Type()
)
fibTmuMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchIndex.setStatus("mandatory")
_FibTmuMatchTauId_Type = Integer32
_FibTmuMatchTauId_Object = MibTableColumn
fibTmuMatchTauId = _FibTmuMatchTauId_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20, 1, 2),
    _FibTmuMatchTauId_Type()
)
fibTmuMatchTauId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchTauId.setStatus("mandatory")
_FibTmuMatchPortId_Type = Integer32
_FibTmuMatchPortId_Object = MibTableColumn
fibTmuMatchPortId = _FibTmuMatchPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20, 1, 3),
    _FibTmuMatchPortId_Type()
)
fibTmuMatchPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchPortId.setStatus("mandatory")
_FibTmuMatchPhysAddr_Type = MacAddress
_FibTmuMatchPhysAddr_Object = MibTableColumn
fibTmuMatchPhysAddr = _FibTmuMatchPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20, 1, 4),
    _FibTmuMatchPhysAddr_Type()
)
fibTmuMatchPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchPhysAddr.setStatus("mandatory")
_FibTmuMatchStationInfo_Type = Integer32
_FibTmuMatchStationInfo_Object = MibTableColumn
fibTmuMatchStationInfo = _FibTmuMatchStationInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 3, 20, 1, 5),
    _FibTmuMatchStationInfo_Type()
)
fibTmuMatchStationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchStationInfo.setStatus("mandatory")
_TmuStations_ObjectIdentity = ObjectIdentity
tmuStations = _TmuStations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 4)
)
_FibTmuStationsUpdateTime_Type = TimeTicks
_FibTmuStationsUpdateTime_Object = MibScalar
fibTmuStationsUpdateTime = _FibTmuStationsUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 1),
    _FibTmuStationsUpdateTime_Type()
)
fibTmuStationsUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsUpdateTime.setStatus("mandatory")
_FibTmuStationsNumEntries_Type = Integer32
_FibTmuStationsNumEntries_Object = MibScalar
fibTmuStationsNumEntries = _FibTmuStationsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 2),
    _FibTmuStationsNumEntries_Type()
)
fibTmuStationsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsNumEntries.setStatus("mandatory")
_FibTmuStationsNumTmuEntries_Type = Integer32
_FibTmuStationsNumTmuEntries_Object = MibScalar
fibTmuStationsNumTmuEntries = _FibTmuStationsNumTmuEntries_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 3),
    _FibTmuStationsNumTmuEntries_Type()
)
fibTmuStationsNumTmuEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsNumTmuEntries.setStatus("mandatory")
_FibTmuStationsFirstChipIndex_Type = Integer32
_FibTmuStationsFirstChipIndex_Object = MibScalar
fibTmuStationsFirstChipIndex = _FibTmuStationsFirstChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 4),
    _FibTmuStationsFirstChipIndex_Type()
)
fibTmuStationsFirstChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsFirstChipIndex.setStatus("mandatory")
_FibTmuStationsSecondChipIndex_Type = Integer32
_FibTmuStationsSecondChipIndex_Object = MibScalar
fibTmuStationsSecondChipIndex = _FibTmuStationsSecondChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 5),
    _FibTmuStationsSecondChipIndex_Type()
)
fibTmuStationsSecondChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsSecondChipIndex.setStatus("mandatory")
_FibTmuStationsActMonIndex_Type = Integer32
_FibTmuStationsActMonIndex_Object = MibScalar
fibTmuStationsActMonIndex = _FibTmuStationsActMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 6),
    _FibTmuStationsActMonIndex_Type()
)
fibTmuStationsActMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsActMonIndex.setStatus("mandatory")
_FibTmuStationsConfigChipIndex_Type = Integer32
_FibTmuStationsConfigChipIndex_Object = MibScalar
fibTmuStationsConfigChipIndex = _FibTmuStationsConfigChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 7),
    _FibTmuStationsConfigChipIndex_Type()
)
fibTmuStationsConfigChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsConfigChipIndex.setStatus("mandatory")


class _FibTmuStationsStationsListValid_Type(Integer32):
    """Custom type fibTmuStationsStationsListValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-valid", -1),
          ("valid", 2))
    )


_FibTmuStationsStationsListValid_Type.__name__ = "Integer32"
_FibTmuStationsStationsListValid_Object = MibScalar
fibTmuStationsStationsListValid = _FibTmuStationsStationsListValid_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 8),
    _FibTmuStationsStationsListValid_Type()
)
fibTmuStationsStationsListValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsStationsListValid.setStatus("mandatory")


class _FibTmuStationsUpToDate_Type(Integer32):
    """Custom type fibTmuStationsUpToDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-up-to-date", 1),
          ("up-to-date", 2))
    )


_FibTmuStationsUpToDate_Type.__name__ = "Integer32"
_FibTmuStationsUpToDate_Object = MibScalar
fibTmuStationsUpToDate = _FibTmuStationsUpToDate_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 9),
    _FibTmuStationsUpToDate_Type()
)
fibTmuStationsUpToDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsUpToDate.setStatus("mandatory")


class _FibTmuMatchNoStationsListReason_Type(Integer32):
    """Custom type fibTmuMatchNoStationsListReason based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("empty-reason", 1),
          ("first-not-found", 8),
          ("found-twice", 10),
          ("inconsistency", 5),
          ("malloc-fail", 2),
          ("no-chip-on-list", 4),
          ("no-tr-list", 14),
          ("second-not-found", 9),
          ("segment-unstable", 3),
          ("soft-01", 6),
          ("soft-02", 7))
    )


_FibTmuMatchNoStationsListReason_Type.__name__ = "Integer32"
_FibTmuMatchNoStationsListReason_Object = MibScalar
fibTmuMatchNoStationsListReason = _FibTmuMatchNoStationsListReason_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 10),
    _FibTmuMatchNoStationsListReason_Type()
)
fibTmuMatchNoStationsListReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuMatchNoStationsListReason.setStatus("mandatory")
_FibTmuStationsTable_Object = MibTable
fibTmuStationsTable = _FibTmuStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 20)
)
if mibBuilder.loadTexts:
    fibTmuStationsTable.setStatus("mandatory")
_FibTmuStationsEntry_Object = MibTableRow
fibTmuStationsEntry = _FibTmuStationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 20, 1)
)
fibTmuStationsEntry.setIndexNames(
    (0, "TMU-MIB", "fibTmuStationsIndex"),
)
if mibBuilder.loadTexts:
    fibTmuStationsEntry.setStatus("mandatory")
_FibTmuStationsIndex_Type = Integer32
_FibTmuStationsIndex_Object = MibTableColumn
fibTmuStationsIndex = _FibTmuStationsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 20, 1, 1),
    _FibTmuStationsIndex_Type()
)
fibTmuStationsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsIndex.setStatus("mandatory")
_FibTmuStationsPhysAddr_Type = MacAddress
_FibTmuStationsPhysAddr_Object = MibTableColumn
fibTmuStationsPhysAddr = _FibTmuStationsPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 20, 1, 2),
    _FibTmuStationsPhysAddr_Type()
)
fibTmuStationsPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsPhysAddr.setStatus("mandatory")
_FibTmuStationsStationInfo_Type = Integer32
_FibTmuStationsStationInfo_Object = MibTableColumn
fibTmuStationsStationInfo = _FibTmuStationsStationInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 4, 20, 1, 3),
    _FibTmuStationsStationInfo_Type()
)
fibTmuStationsStationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuStationsStationInfo.setStatus("mandatory")
_TmuPorts_ObjectIdentity = ObjectIdentity
tmuPorts = _TmuPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 5)
)
_FibTmuPortsNumRelayOpen_Type = Integer32
_FibTmuPortsNumRelayOpen_Object = MibScalar
fibTmuPortsNumRelayOpen = _FibTmuPortsNumRelayOpen_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 1),
    _FibTmuPortsNumRelayOpen_Type()
)
fibTmuPortsNumRelayOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumRelayOpen.setStatus("mandatory")
_FibTmuPortsNumPhantomPresent_Type = Integer32
_FibTmuPortsNumPhantomPresent_Object = MibScalar
fibTmuPortsNumPhantomPresent = _FibTmuPortsNumPhantomPresent_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 2),
    _FibTmuPortsNumPhantomPresent_Type()
)
fibTmuPortsNumPhantomPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumPhantomPresent.setStatus("mandatory")
_FibTmuPortsNumPortsPerTmu_Type = Integer32
_FibTmuPortsNumPortsPerTmu_Object = MibScalar
fibTmuPortsNumPortsPerTmu = _FibTmuPortsNumPortsPerTmu_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 3),
    _FibTmuPortsNumPortsPerTmu_Type()
)
fibTmuPortsNumPortsPerTmu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumPortsPerTmu.setStatus("mandatory")
_FibTmuPortsNumTausPerTmu_Type = Integer32
_FibTmuPortsNumTausPerTmu_Object = MibScalar
fibTmuPortsNumTausPerTmu = _FibTmuPortsNumTausPerTmu_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 4),
    _FibTmuPortsNumTausPerTmu_Type()
)
fibTmuPortsNumTausPerTmu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumTausPerTmu.setStatus("mandatory")
_FibTmuPortsNumPortsPerTau_Type = Integer32
_FibTmuPortsNumPortsPerTau_Object = MibScalar
fibTmuPortsNumPortsPerTau = _FibTmuPortsNumPortsPerTau_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 5),
    _FibTmuPortsNumPortsPerTau_Type()
)
fibTmuPortsNumPortsPerTau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumPortsPerTau.setStatus("mandatory")
_FibTmuPortsMaxNumTauErrs_Type = Integer32
_FibTmuPortsMaxNumTauErrs_Object = MibScalar
fibTmuPortsMaxNumTauErrs = _FibTmuPortsMaxNumTauErrs_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 6),
    _FibTmuPortsMaxNumTauErrs_Type()
)
fibTmuPortsMaxNumTauErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsMaxNumTauErrs.setStatus("mandatory")
_FibTmuPortsMaxFirstTimeout_Type = Integer32
_FibTmuPortsMaxFirstTimeout_Object = MibScalar
fibTmuPortsMaxFirstTimeout = _FibTmuPortsMaxFirstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 7),
    _FibTmuPortsMaxFirstTimeout_Type()
)
fibTmuPortsMaxFirstTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsMaxFirstTimeout.setStatus("mandatory")
_FibTmuPortsTauTable_Object = MibTable
fibTmuPortsTauTable = _FibTmuPortsTauTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29)
)
if mibBuilder.loadTexts:
    fibTmuPortsTauTable.setStatus("mandatory")
_FibTmuPortsTauEntry_Object = MibTableRow
fibTmuPortsTauEntry = _FibTmuPortsTauEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1)
)
fibTmuPortsTauEntry.setIndexNames(
    (0, "TMU-MIB", "fibTmuPortsTmuPort"),
)
if mibBuilder.loadTexts:
    fibTmuPortsTauEntry.setStatus("mandatory")
_FibTmuPortsTmuPort_Type = Integer32
_FibTmuPortsTmuPort_Object = MibTableColumn
fibTmuPortsTmuPort = _FibTmuPortsTmuPort_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 1),
    _FibTmuPortsTmuPort_Type()
)
fibTmuPortsTmuPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsTmuPort.setStatus("mandatory")


class _FibTmuPortsPortType_Type(Integer32):
    """Custom type fibTmuPortsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("station-only", 2),
          ("station-or-Tau", 1))
    )


_FibTmuPortsPortType_Type.__name__ = "Integer32"
_FibTmuPortsPortType_Object = MibTableColumn
fibTmuPortsPortType = _FibTmuPortsPortType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 2),
    _FibTmuPortsPortType_Type()
)
fibTmuPortsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsPortType.setStatus("mandatory")


class _FibTmuPortsEndConnection_Type(Integer32):
    """Custom type fibTmuPortsEndConnection based on Integer32"""
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
        *(("passive-connected", 4),
          ("single-connected", 3),
          ("tau-connected", 2),
          ("undefined", 1))
    )


_FibTmuPortsEndConnection_Type.__name__ = "Integer32"
_FibTmuPortsEndConnection_Object = MibTableColumn
fibTmuPortsEndConnection = _FibTmuPortsEndConnection_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 3),
    _FibTmuPortsEndConnection_Type()
)
fibTmuPortsEndConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsEndConnection.setStatus("mandatory")
_FibTmuPortsPortStatus_Type = Integer32
_FibTmuPortsPortStatus_Object = MibTableColumn
fibTmuPortsPortStatus = _FibTmuPortsPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 4),
    _FibTmuPortsPortStatus_Type()
)
fibTmuPortsPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsPortStatus.setStatus("mandatory")


class _FibTmuPortsManagerCloseRun_Type(Integer32):
    """Custom type fibTmuPortsManagerCloseRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_FibTmuPortsManagerCloseRun_Type.__name__ = "Integer32"
_FibTmuPortsManagerCloseRun_Object = MibTableColumn
fibTmuPortsManagerCloseRun = _FibTmuPortsManagerCloseRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 5),
    _FibTmuPortsManagerCloseRun_Type()
)
fibTmuPortsManagerCloseRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsManagerCloseRun.setStatus("mandatory")


class _FibTmuPortsManagerClosePerm_Type(Integer32):
    """Custom type fibTmuPortsManagerClosePerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_FibTmuPortsManagerClosePerm_Type.__name__ = "Integer32"
_FibTmuPortsManagerClosePerm_Object = MibTableColumn
fibTmuPortsManagerClosePerm = _FibTmuPortsManagerClosePerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 6),
    _FibTmuPortsManagerClosePerm_Type()
)
fibTmuPortsManagerClosePerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsManagerClosePerm.setStatus("mandatory")
_FibTmuPortsNumConsequentErrs_Type = Integer32
_FibTmuPortsNumConsequentErrs_Object = MibTableColumn
fibTmuPortsNumConsequentErrs = _FibTmuPortsNumConsequentErrs_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 10),
    _FibTmuPortsNumConsequentErrs_Type()
)
fibTmuPortsNumConsequentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumConsequentErrs.setStatus("mandatory")
_FibTmuPortsNumTimeout_Type = Counter32
_FibTmuPortsNumTimeout_Object = MibTableColumn
fibTmuPortsNumTimeout = _FibTmuPortsNumTimeout_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 11),
    _FibTmuPortsNumTimeout_Type()
)
fibTmuPortsNumTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumTimeout.setStatus("mandatory")


class _FibTmuPortsTauPortState_Type(Integer32):
    """Custom type fibTmuPortsTauPortState based on Integer32"""
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
        *(("active-connection", 3),
          ("getting-config", 4),
          ("initializing", 5),
          ("no-connection", 1),
          ("pre-active", 6),
          ("waiting-to-open", 2))
    )


_FibTmuPortsTauPortState_Type.__name__ = "Integer32"
_FibTmuPortsTauPortState_Object = MibTableColumn
fibTmuPortsTauPortState = _FibTmuPortsTauPortState_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 12),
    _FibTmuPortsTauPortState_Type()
)
fibTmuPortsTauPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsTauPortState.setStatus("mandatory")
_FibTmuPortsNumPorts_Type = Integer32
_FibTmuPortsNumPorts_Object = MibTableColumn
fibTmuPortsNumPorts = _FibTmuPortsNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 13),
    _FibTmuPortsNumPorts_Type()
)
fibTmuPortsNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumPorts.setStatus("mandatory")
_FibTmuPortsNumAttached_Type = Integer32
_FibTmuPortsNumAttached_Object = MibTableColumn
fibTmuPortsNumAttached = _FibTmuPortsNumAttached_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 14),
    _FibTmuPortsNumAttached_Type()
)
fibTmuPortsNumAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumAttached.setStatus("mandatory")
_FibTmuPortsNumPhantomUp_Type = Integer32
_FibTmuPortsNumPhantomUp_Object = MibTableColumn
fibTmuPortsNumPhantomUp = _FibTmuPortsNumPhantomUp_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 15),
    _FibTmuPortsNumPhantomUp_Type()
)
fibTmuPortsNumPhantomUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumPhantomUp.setStatus("mandatory")
_FibTmuPortsTauRevision_Type = Integer32
_FibTmuPortsTauRevision_Object = MibTableColumn
fibTmuPortsTauRevision = _FibTmuPortsTauRevision_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 16),
    _FibTmuPortsTauRevision_Type()
)
fibTmuPortsTauRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsTauRevision.setStatus("mandatory")


class _FibTmuPortsModuleId_Type(OctetString):
    """Custom type fibTmuPortsModuleId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FibTmuPortsModuleId_Type.__name__ = "OctetString"
_FibTmuPortsModuleId_Object = MibTableColumn
fibTmuPortsModuleId = _FibTmuPortsModuleId_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 17),
    _FibTmuPortsModuleId_Type()
)
fibTmuPortsModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsModuleId.setStatus("mandatory")
_FibTmuPortsNumModules_Type = Integer32
_FibTmuPortsNumModules_Object = MibTableColumn
fibTmuPortsNumModules = _FibTmuPortsNumModules_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 18),
    _FibTmuPortsNumModules_Type()
)
fibTmuPortsNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsNumModules.setStatus("mandatory")
_FibTmuPortsTauMode_Type = Integer32
_FibTmuPortsTauMode_Object = MibTableColumn
fibTmuPortsTauMode = _FibTmuPortsTauMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 19),
    _FibTmuPortsTauMode_Type()
)
fibTmuPortsTauMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsTauMode.setStatus("mandatory")


class _FibTmuPortsLedState_Type(Integer32):
    """Custom type fibTmuPortsLedState based on Integer32"""
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
        *(("fast-rate", 2),
          ("fixed-off", 4),
          ("fixed-on", 3),
          ("slow-rate", 1))
    )


_FibTmuPortsLedState_Type.__name__ = "Integer32"
_FibTmuPortsLedState_Object = MibTableColumn
fibTmuPortsLedState = _FibTmuPortsLedState_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 20),
    _FibTmuPortsLedState_Type()
)
fibTmuPortsLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsLedState.setStatus("mandatory")


class _FibTmuPortsRequestType_Type(Integer32):
    """Custom type fibTmuPortsRequestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              33,
              49,
              65,
              81,
              97,
              113,
              129,
              145,
              161)
        )
    )
    namedValues = NamedValues(
        *(("attach-detach-msg", 65),
          ("get-all-msg", 113),
          ("get-changes-msg", 129),
          ("get-configuration-msg", 17),
          ("get-phantom-msg", 33),
          ("get-relay-msg", 49),
          ("no-Tau-msg", 1),
          ("reset-Tau-msg", 145),
          ("self-test-Tau-msg", 161),
          ("set-active-msg", 97),
          ("set-beacon-msg", 81))
    )


_FibTmuPortsRequestType_Type.__name__ = "Integer32"
_FibTmuPortsRequestType_Object = MibTableColumn
fibTmuPortsRequestType = _FibTmuPortsRequestType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 21),
    _FibTmuPortsRequestType_Type()
)
fibTmuPortsRequestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsRequestType.setStatus("mandatory")
_FibTmuPortsLastTxTime_Type = TimeTicks
_FibTmuPortsLastTxTime_Object = MibTableColumn
fibTmuPortsLastTxTime = _FibTmuPortsLastTxTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 22),
    _FibTmuPortsLastTxTime_Type()
)
fibTmuPortsLastTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsLastTxTime.setStatus("mandatory")
_FibTmuPortsLastPollTime_Type = TimeTicks
_FibTmuPortsLastPollTime_Object = MibTableColumn
fibTmuPortsLastPollTime = _FibTmuPortsLastPollTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 23),
    _FibTmuPortsLastPollTime_Type()
)
fibTmuPortsLastPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsLastPollTime.setStatus("mandatory")
_FibTmuPortsUpdateTime_Type = TimeTicks
_FibTmuPortsUpdateTime_Object = MibTableColumn
fibTmuPortsUpdateTime = _FibTmuPortsUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 24),
    _FibTmuPortsUpdateTime_Type()
)
fibTmuPortsUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsUpdateTime.setStatus("mandatory")
_FibTmuPortsAllowedAddr_Type = MacAddress
_FibTmuPortsAllowedAddr_Object = MibTableColumn
fibTmuPortsAllowedAddr = _FibTmuPortsAllowedAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 25),
    _FibTmuPortsAllowedAddr_Type()
)
fibTmuPortsAllowedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsAllowedAddr.setStatus("mandatory")


class _FibTmuPortsAllowedAddrLoaded_Type(Integer32):
    """Custom type fibTmuPortsAllowedAddrLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addr-not-loaded", 1),
          ("loaded-and-active", 3),
          ("loaded-not-active", 2))
    )


_FibTmuPortsAllowedAddrLoaded_Type.__name__ = "Integer32"
_FibTmuPortsAllowedAddrLoaded_Object = MibTableColumn
fibTmuPortsAllowedAddrLoaded = _FibTmuPortsAllowedAddrLoaded_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 29, 1, 26),
    _FibTmuPortsAllowedAddrLoaded_Type()
)
fibTmuPortsAllowedAddrLoaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsAllowedAddrLoaded.setStatus("mandatory")
_FibTmuPortsAllTable_Object = MibTable
fibTmuPortsAllTable = _FibTmuPortsAllTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30)
)
if mibBuilder.loadTexts:
    fibTmuPortsAllTable.setStatus("mandatory")
_FibTmuPortsAllEntry_Object = MibTableRow
fibTmuPortsAllEntry = _FibTmuPortsAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1)
)
fibTmuPortsAllEntry.setIndexNames(
    (0, "TMU-MIB", "fibTmuPortsTmuPortIndex"),
    (0, "TMU-MIB", "fibTmuPortsTauPortIndex"),
)
if mibBuilder.loadTexts:
    fibTmuPortsAllEntry.setStatus("mandatory")
_FibTmuPortsTmuPortIndex_Type = Integer32
_FibTmuPortsTmuPortIndex_Object = MibTableColumn
fibTmuPortsTmuPortIndex = _FibTmuPortsTmuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 1),
    _FibTmuPortsTmuPortIndex_Type()
)
fibTmuPortsTmuPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsTmuPortIndex.setStatus("mandatory")
_FibTmuPortsTauPortIndex_Type = Integer32
_FibTmuPortsTauPortIndex_Object = MibTableColumn
fibTmuPortsTauPortIndex = _FibTmuPortsTauPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 2),
    _FibTmuPortsTauPortIndex_Type()
)
fibTmuPortsTauPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsTauPortIndex.setStatus("mandatory")
_FibTmuPortsPortState_Type = Integer32
_FibTmuPortsPortState_Object = MibTableColumn
fibTmuPortsPortState = _FibTmuPortsPortState_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 3),
    _FibTmuPortsPortState_Type()
)
fibTmuPortsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsPortState.setStatus("mandatory")


class _FibTmuPortsGenCloseRun_Type(Integer32):
    """Custom type fibTmuPortsGenCloseRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_FibTmuPortsGenCloseRun_Type.__name__ = "Integer32"
_FibTmuPortsGenCloseRun_Object = MibTableColumn
fibTmuPortsGenCloseRun = _FibTmuPortsGenCloseRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 4),
    _FibTmuPortsGenCloseRun_Type()
)
fibTmuPortsGenCloseRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsGenCloseRun.setStatus("mandatory")


class _FibTmuPortsGenClosePerm_Type(Integer32):
    """Custom type fibTmuPortsGenClosePerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_FibTmuPortsGenClosePerm_Type.__name__ = "Integer32"
_FibTmuPortsGenClosePerm_Object = MibTableColumn
fibTmuPortsGenClosePerm = _FibTmuPortsGenClosePerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 5),
    _FibTmuPortsGenClosePerm_Type()
)
fibTmuPortsGenClosePerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsGenClosePerm.setStatus("mandatory")
_FibTmuPortsPhysAddr_Type = MacAddress
_FibTmuPortsPhysAddr_Object = MibTableColumn
fibTmuPortsPhysAddr = _FibTmuPortsPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 6),
    _FibTmuPortsPhysAddr_Type()
)
fibTmuPortsPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsPhysAddr.setStatus("mandatory")
_FibTmuPortsStationInfo_Type = Integer32
_FibTmuPortsStationInfo_Object = MibTableColumn
fibTmuPortsStationInfo = _FibTmuPortsStationInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 7),
    _FibTmuPortsStationInfo_Type()
)
fibTmuPortsStationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuPortsStationInfo.setStatus("mandatory")
_FibTmuPortsTauAllowedAddr_Type = MacAddress
_FibTmuPortsTauAllowedAddr_Object = MibTableColumn
fibTmuPortsTauAllowedAddr = _FibTmuPortsTauAllowedAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 8),
    _FibTmuPortsTauAllowedAddr_Type()
)
fibTmuPortsTauAllowedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsTauAllowedAddr.setStatus("mandatory")


class _FibTmuPortsTauAllowedAddrLoaded_Type(Integer32):
    """Custom type fibTmuPortsTauAllowedAddrLoaded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("addr-not-loaded", 1),
          ("loaded-and-active", 3),
          ("loaded-not-active", 2))
    )


_FibTmuPortsTauAllowedAddrLoaded_Type.__name__ = "Integer32"
_FibTmuPortsTauAllowedAddrLoaded_Object = MibTableColumn
fibTmuPortsTauAllowedAddrLoaded = _FibTmuPortsTauAllowedAddrLoaded_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 5, 30, 1, 9),
    _FibTmuPortsTauAllowedAddrLoaded_Type()
)
fibTmuPortsTauAllowedAddrLoaded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuPortsTauAllowedAddrLoaded.setStatus("mandatory")
_TmuProduction_ObjectIdentity = ObjectIdentity
tmuProduction = _TmuProduction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 6)
)
_FibTmuProductionAddr48No1_Type = MacAddress
_FibTmuProductionAddr48No1_Object = MibScalar
fibTmuProductionAddr48No1 = _FibTmuProductionAddr48No1_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 1),
    _FibTmuProductionAddr48No1_Type()
)
fibTmuProductionAddr48No1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionAddr48No1.setStatus("mandatory")
_FibTmuProductionAddr48No2_Type = MacAddress
_FibTmuProductionAddr48No2_Object = MibScalar
fibTmuProductionAddr48No2 = _FibTmuProductionAddr48No2_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 2),
    _FibTmuProductionAddr48No2_Type()
)
fibTmuProductionAddr48No2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionAddr48No2.setStatus("mandatory")
_FibTmuProductionAddr48No3_Type = MacAddress
_FibTmuProductionAddr48No3_Object = MibScalar
fibTmuProductionAddr48No3 = _FibTmuProductionAddr48No3_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 3),
    _FibTmuProductionAddr48No3_Type()
)
fibTmuProductionAddr48No3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionAddr48No3.setStatus("mandatory")


class _FibTmuProductionRomType_Type(Integer32):
    """Custom type fibTmuProductionRomType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rom-27c020", 2),
          ("rom-27c040", 3),
          ("unknown", 1))
    )


_FibTmuProductionRomType_Type.__name__ = "Integer32"
_FibTmuProductionRomType_Object = MibScalar
fibTmuProductionRomType = _FibTmuProductionRomType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 4),
    _FibTmuProductionRomType_Type()
)
fibTmuProductionRomType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionRomType.setStatus("mandatory")


class _FibTmuProductionRamType_Type(Integer32):
    """Custom type fibTmuProductionRamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ram-128k8", 2),
          ("unknown", 1))
    )


_FibTmuProductionRamType_Type.__name__ = "Integer32"
_FibTmuProductionRamType_Object = MibScalar
fibTmuProductionRamType = _FibTmuProductionRamType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 5),
    _FibTmuProductionRamType_Type()
)
fibTmuProductionRamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionRamType.setStatus("mandatory")


class _FibTmuProductionFlashType_Type(Integer32):
    """Custom type fibTmuProductionFlashType based on Integer32"""
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
        *(("flash-28f010", 2),
          ("flash-28f020", 3),
          ("flash-29f010", 4),
          ("flash-29f040", 5),
          ("unknown", 1))
    )


_FibTmuProductionFlashType_Type.__name__ = "Integer32"
_FibTmuProductionFlashType_Object = MibScalar
fibTmuProductionFlashType = _FibTmuProductionFlashType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 6),
    _FibTmuProductionFlashType_Type()
)
fibTmuProductionFlashType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionFlashType.setStatus("mandatory")


class _FibTmuProductionEepromType_Type(Integer32):
    """Custom type fibTmuProductionEepromType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("with-page-mode", 2),
          ("without-page-mode", 3))
    )


_FibTmuProductionEepromType_Type.__name__ = "Integer32"
_FibTmuProductionEepromType_Object = MibScalar
fibTmuProductionEepromType = _FibTmuProductionEepromType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 7),
    _FibTmuProductionEepromType_Type()
)
fibTmuProductionEepromType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionEepromType.setStatus("mandatory")


class _FibTmuProductionSerialNum_Type(OctetString):
    """Custom type fibTmuProductionSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_FibTmuProductionSerialNum_Type.__name__ = "OctetString"
_FibTmuProductionSerialNum_Object = MibScalar
fibTmuProductionSerialNum = _FibTmuProductionSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 8),
    _FibTmuProductionSerialNum_Type()
)
fibTmuProductionSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionSerialNum.setStatus("mandatory")


class _FibTmuProductionRamSize_Type(Integer32):
    """Custom type fibTmuProductionRamSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 64),
    )


_FibTmuProductionRamSize_Type.__name__ = "Integer32"
_FibTmuProductionRamSize_Object = MibScalar
fibTmuProductionRamSize = _FibTmuProductionRamSize_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 9),
    _FibTmuProductionRamSize_Type()
)
fibTmuProductionRamSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionRamSize.setStatus("mandatory")


class _FibTmuProductionFlash0Size_Type(Integer32):
    """Custom type fibTmuProductionFlash0Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 64),
    )


_FibTmuProductionFlash0Size_Type.__name__ = "Integer32"
_FibTmuProductionFlash0Size_Object = MibScalar
fibTmuProductionFlash0Size = _FibTmuProductionFlash0Size_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 10),
    _FibTmuProductionFlash0Size_Type()
)
fibTmuProductionFlash0Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionFlash0Size.setStatus("mandatory")


class _FibTmuProductionFlash1Size_Type(Integer32):
    """Custom type fibTmuProductionFlash1Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 64),
    )


_FibTmuProductionFlash1Size_Type.__name__ = "Integer32"
_FibTmuProductionFlash1Size_Object = MibScalar
fibTmuProductionFlash1Size = _FibTmuProductionFlash1Size_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 11),
    _FibTmuProductionFlash1Size_Type()
)
fibTmuProductionFlash1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionFlash1Size.setStatus("mandatory")


class _FibTmuProductionEepromSize_Type(Integer32):
    """Custom type fibTmuProductionEepromSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 64),
    )


_FibTmuProductionEepromSize_Type.__name__ = "Integer32"
_FibTmuProductionEepromSize_Object = MibScalar
fibTmuProductionEepromSize = _FibTmuProductionEepromSize_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 12),
    _FibTmuProductionEepromSize_Type()
)
fibTmuProductionEepromSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionEepromSize.setStatus("mandatory")


class _FibTmuProductionHwInfo_Type(OctetString):
    """Custom type fibTmuProductionHwInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FibTmuProductionHwInfo_Type.__name__ = "OctetString"
_FibTmuProductionHwInfo_Object = MibScalar
fibTmuProductionHwInfo = _FibTmuProductionHwInfo_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 13),
    _FibTmuProductionHwInfo_Type()
)
fibTmuProductionHwInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuProductionHwInfo.setStatus("mandatory")


class _FibTmuProductionBoardType_Type(Integer32):
    """Custom type fibTmuProductionBoardType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("board-9230", 2),
          ("board-9230-16", 3),
          ("board-9230-16F", 5),
          ("board-9230-32", 4),
          ("board-9230-32F", 6),
          ("board-9232-16", 7),
          ("board-9232-32", 8),
          ("unknown", 1))
    )


_FibTmuProductionBoardType_Type.__name__ = "Integer32"
_FibTmuProductionBoardType_Object = MibScalar
fibTmuProductionBoardType = _FibTmuProductionBoardType_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 6, 14),
    _FibTmuProductionBoardType_Type()
)
fibTmuProductionBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuProductionBoardType.setStatus("mandatory")
_TmuSecurity_ObjectIdentity = ObjectIdentity
tmuSecurity = _TmuSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 7)
)
_FibTmuSecurityModeRun_Type = Integer32
_FibTmuSecurityModeRun_Object = MibScalar
fibTmuSecurityModeRun = _FibTmuSecurityModeRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 7, 1),
    _FibTmuSecurityModeRun_Type()
)
fibTmuSecurityModeRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuSecurityModeRun.setStatus("mandatory")
_FibTmuSecurityModePerm_Type = Integer32
_FibTmuSecurityModePerm_Object = MibScalar
fibTmuSecurityModePerm = _FibTmuSecurityModePerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 7, 2),
    _FibTmuSecurityModePerm_Type()
)
fibTmuSecurityModePerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuSecurityModePerm.setStatus("mandatory")
_FibTmuNumStationSecurity_Type = Integer32
_FibTmuNumStationSecurity_Object = MibScalar
fibTmuNumStationSecurity = _FibTmuNumStationSecurity_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 7, 3),
    _FibTmuNumStationSecurity_Type()
)
fibTmuNumStationSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumStationSecurity.setStatus("mandatory")
_FibTmuNumStationLeft_Type = Integer32
_FibTmuNumStationLeft_Object = MibScalar
fibTmuNumStationLeft = _FibTmuNumStationLeft_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 7, 4),
    _FibTmuNumStationLeft_Type()
)
fibTmuNumStationLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuNumStationLeft.setStatus("mandatory")
_TmuFunction_ObjectIdentity = ObjectIdentity
tmuFunction = _TmuFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 8)
)
_FibTmuFunctRtpGrpVrsRun_ObjectIdentity = ObjectIdentity
fibTmuFunctRtpGrpVrsRun = _FibTmuFunctRtpGrpVrsRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1)
)


class _FibTmuFunctBeacon2AutotestRun_Type(Integer32):
    """Custom type fibTmuFunctBeacon2AutotestRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 200),
    )


_FibTmuFunctBeacon2AutotestRun_Type.__name__ = "Integer32"
_FibTmuFunctBeacon2AutotestRun_Object = MibScalar
fibTmuFunctBeacon2AutotestRun = _FibTmuFunctBeacon2AutotestRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 1),
    _FibTmuFunctBeacon2AutotestRun_Type()
)
fibTmuFunctBeacon2AutotestRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctBeacon2AutotestRun.setStatus("mandatory")


class _FibTmuFunctBeacon2OkRun_Type(Integer32):
    """Custom type fibTmuFunctBeacon2OkRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 200),
    )


_FibTmuFunctBeacon2OkRun_Type.__name__ = "Integer32"
_FibTmuFunctBeacon2OkRun_Object = MibScalar
fibTmuFunctBeacon2OkRun = _FibTmuFunctBeacon2OkRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 2),
    _FibTmuFunctBeacon2OkRun_Type()
)
fibTmuFunctBeacon2OkRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctBeacon2OkRun.setStatus("mandatory")


class _FibTmuFunctOk2BeaconRun_Type(Integer32):
    """Custom type fibTmuFunctOk2BeaconRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1100, 2500),
    )


_FibTmuFunctOk2BeaconRun_Type.__name__ = "Integer32"
_FibTmuFunctOk2BeaconRun_Object = MibScalar
fibTmuFunctOk2BeaconRun = _FibTmuFunctOk2BeaconRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 3),
    _FibTmuFunctOk2BeaconRun_Type()
)
fibTmuFunctOk2BeaconRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctOk2BeaconRun.setStatus("mandatory")


class _FibTmuFunctWrapCwtRun_Type(Integer32):
    """Custom type fibTmuFunctWrapCwtRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FibTmuFunctWrapCwtRun_Type.__name__ = "Integer32"
_FibTmuFunctWrapCwtRun_Object = MibScalar
fibTmuFunctWrapCwtRun = _FibTmuFunctWrapCwtRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 4),
    _FibTmuFunctWrapCwtRun_Type()
)
fibTmuFunctWrapCwtRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctWrapCwtRun.setStatus("mandatory")


class _FibTmuFunctWrapWnrRun_Type(Integer32):
    """Custom type fibTmuFunctWrapWnrRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wnr-dont-release-cpu", 1),
          ("wnr-release-cpu", 2))
    )


_FibTmuFunctWrapWnrRun_Type.__name__ = "Integer32"
_FibTmuFunctWrapWnrRun_Object = MibScalar
fibTmuFunctWrapWnrRun = _FibTmuFunctWrapWnrRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 5),
    _FibTmuFunctWrapWnrRun_Type()
)
fibTmuFunctWrapWnrRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctWrapWnrRun.setStatus("mandatory")


class _FibTmuFunctRingIstRun_Type(Integer32):
    """Custom type fibTmuFunctRingIstRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FibTmuFunctRingIstRun_Type.__name__ = "Integer32"
_FibTmuFunctRingIstRun_Object = MibScalar
fibTmuFunctRingIstRun = _FibTmuFunctRingIstRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 6),
    _FibTmuFunctRingIstRun_Type()
)
fibTmuFunctRingIstRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctRingIstRun.setStatus("mandatory")


class _FibTmuFunctRingIstnrRun_Type(Integer32):
    """Custom type fibTmuFunctRingIstnrRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("istnr-dont-release-cpu", 1),
          ("istnr-release-cpu", 2))
    )


_FibTmuFunctRingIstnrRun_Type.__name__ = "Integer32"
_FibTmuFunctRingIstnrRun_Object = MibScalar
fibTmuFunctRingIstnrRun = _FibTmuFunctRingIstnrRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 7),
    _FibTmuFunctRingIstnrRun_Type()
)
fibTmuFunctRingIstnrRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctRingIstnrRun.setStatus("mandatory")


class _FibTmuFunctCheckAogTauRun_Type(Integer32):
    """Custom type fibTmuFunctCheckAogTauRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check-ring", 2),
          ("dont-check-ring", 1))
    )


_FibTmuFunctCheckAogTauRun_Type.__name__ = "Integer32"
_FibTmuFunctCheckAogTauRun_Object = MibScalar
fibTmuFunctCheckAogTauRun = _FibTmuFunctCheckAogTauRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 8),
    _FibTmuFunctCheckAogTauRun_Type()
)
fibTmuFunctCheckAogTauRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctCheckAogTauRun.setStatus("mandatory")


class _FibTmuFunctMaxNoiRun_Type(Integer32):
    """Custom type fibTmuFunctMaxNoiRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_FibTmuFunctMaxNoiRun_Type.__name__ = "Integer32"
_FibTmuFunctMaxNoiRun_Object = MibScalar
fibTmuFunctMaxNoiRun = _FibTmuFunctMaxNoiRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 9),
    _FibTmuFunctMaxNoiRun_Type()
)
fibTmuFunctMaxNoiRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctMaxNoiRun.setStatus("mandatory")


class _FibTmuFunctLinkPtifRun_Type(Integer32):
    """Custom type fibTmuFunctLinkPtifRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-link-to-last", 1),
          ("link-to-last", 2))
    )


_FibTmuFunctLinkPtifRun_Type.__name__ = "Integer32"
_FibTmuFunctLinkPtifRun_Object = MibScalar
fibTmuFunctLinkPtifRun = _FibTmuFunctLinkPtifRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 10),
    _FibTmuFunctLinkPtifRun_Type()
)
fibTmuFunctLinkPtifRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctLinkPtifRun.setStatus("mandatory")


class _FibTmuFunctInsPatRun_Type(Integer32):
    """Custom type fibTmuFunctInsPatRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 4000),
    )


_FibTmuFunctInsPatRun_Type.__name__ = "Integer32"
_FibTmuFunctInsPatRun_Object = MibScalar
fibTmuFunctInsPatRun = _FibTmuFunctInsPatRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 11),
    _FibTmuFunctInsPatRun_Type()
)
fibTmuFunctInsPatRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctInsPatRun.setStatus("mandatory")


class _FibTmuFunctUseMismatchRun_Type(Integer32):
    """Custom type fibTmuFunctUseMismatchRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-use-mismatch", 1),
          ("use-mismatch", 2))
    )


_FibTmuFunctUseMismatchRun_Type.__name__ = "Integer32"
_FibTmuFunctUseMismatchRun_Object = MibScalar
fibTmuFunctUseMismatchRun = _FibTmuFunctUseMismatchRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 12),
    _FibTmuFunctUseMismatchRun_Type()
)
fibTmuFunctUseMismatchRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctUseMismatchRun.setStatus("mandatory")


class _FibTmuFunctChkRingInsRun_Type(Integer32):
    """Custom type fibTmuFunctChkRingInsRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check-ring", 2),
          ("dont-check-ring", 1))
    )


_FibTmuFunctChkRingInsRun_Type.__name__ = "Integer32"
_FibTmuFunctChkRingInsRun_Object = MibScalar
fibTmuFunctChkRingInsRun = _FibTmuFunctChkRingInsRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 13),
    _FibTmuFunctChkRingInsRun_Type()
)
fibTmuFunctChkRingInsRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctChkRingInsRun.setStatus("mandatory")


class _FibTmuFunctChkRingPerRun_Type(Integer32):
    """Custom type fibTmuFunctChkRingPerRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 4000),
    )


_FibTmuFunctChkRingPerRun_Type.__name__ = "Integer32"
_FibTmuFunctChkRingPerRun_Object = MibScalar
fibTmuFunctChkRingPerRun = _FibTmuFunctChkRingPerRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 14),
    _FibTmuFunctChkRingPerRun_Type()
)
fibTmuFunctChkRingPerRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctChkRingPerRun.setStatus("mandatory")


class _FibTmuFunctClaimTimeOutRun_Type(Integer32):
    """Custom type fibTmuFunctClaimTimeOutRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 500),
    )


_FibTmuFunctClaimTimeOutRun_Type.__name__ = "Integer32"
_FibTmuFunctClaimTimeOutRun_Object = MibScalar
fibTmuFunctClaimTimeOutRun = _FibTmuFunctClaimTimeOutRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 15),
    _FibTmuFunctClaimTimeOutRun_Type()
)
fibTmuFunctClaimTimeOutRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctClaimTimeOutRun.setStatus("mandatory")


class _FibTmuFunctAnotherCheckRun_Type(Integer32):
    """Custom type fibTmuFunctAnotherCheckRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("another-check", 2),
          ("no-another-check", 1))
    )


_FibTmuFunctAnotherCheckRun_Type.__name__ = "Integer32"
_FibTmuFunctAnotherCheckRun_Object = MibScalar
fibTmuFunctAnotherCheckRun = _FibTmuFunctAnotherCheckRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 16),
    _FibTmuFunctAnotherCheckRun_Type()
)
fibTmuFunctAnotherCheckRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctAnotherCheckRun.setStatus("mandatory")


class _FibTmuFunctTmsOnOutRun_Type(Integer32):
    """Custom type fibTmuFunctTmsOnOutRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FibTmuFunctTmsOnOutRun_Type.__name__ = "Integer32"
_FibTmuFunctTmsOnOutRun_Object = MibScalar
fibTmuFunctTmsOnOutRun = _FibTmuFunctTmsOnOutRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 17),
    _FibTmuFunctTmsOnOutRun_Type()
)
fibTmuFunctTmsOnOutRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctTmsOnOutRun.setStatus("mandatory")


class _FibTmuFunctUseJitterRun_Type(Integer32):
    """Custom type fibTmuFunctUseJitterRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-jitter-buster", 1),
          ("use-jitter-buster", 2))
    )


_FibTmuFunctUseJitterRun_Type.__name__ = "Integer32"
_FibTmuFunctUseJitterRun_Object = MibScalar
fibTmuFunctUseJitterRun = _FibTmuFunctUseJitterRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 18),
    _FibTmuFunctUseJitterRun_Type()
)
fibTmuFunctUseJitterRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctUseJitterRun.setStatus("mandatory")


class _FibTmuFunctForceStpRiRun_Type(Integer32):
    """Custom type fibTmuFunctForceStpRiRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-force-ri-stp", 1),
          ("force-ri-stp", 2))
    )


_FibTmuFunctForceStpRiRun_Type.__name__ = "Integer32"
_FibTmuFunctForceStpRiRun_Object = MibScalar
fibTmuFunctForceStpRiRun = _FibTmuFunctForceStpRiRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 21),
    _FibTmuFunctForceStpRiRun_Type()
)
fibTmuFunctForceStpRiRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctForceStpRiRun.setStatus("mandatory")


class _FibTmuFunctForceStpRoRun_Type(Integer32):
    """Custom type fibTmuFunctForceStpRoRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-force-ro-stp", 1),
          ("force-ro-stp", 2))
    )


_FibTmuFunctForceStpRoRun_Type.__name__ = "Integer32"
_FibTmuFunctForceStpRoRun_Object = MibScalar
fibTmuFunctForceStpRoRun = _FibTmuFunctForceStpRoRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 22),
    _FibTmuFunctForceStpRoRun_Type()
)
fibTmuFunctForceStpRoRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctForceStpRoRun.setStatus("mandatory")


class _FibTmuFunctMaxSavRecRun_Type(Integer32):
    """Custom type fibTmuFunctMaxSavRecRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_FibTmuFunctMaxSavRecRun_Type.__name__ = "Integer32"
_FibTmuFunctMaxSavRecRun_Object = MibScalar
fibTmuFunctMaxSavRecRun = _FibTmuFunctMaxSavRecRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 23),
    _FibTmuFunctMaxSavRecRun_Type()
)
fibTmuFunctMaxSavRecRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctMaxSavRecRun.setStatus("mandatory")


class _FibTmuFunctReadPerRun_Type(Integer32):
    """Custom type fibTmuFunctReadPerRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FibTmuFunctReadPerRun_Type.__name__ = "Integer32"
_FibTmuFunctReadPerRun_Object = MibScalar
fibTmuFunctReadPerRun = _FibTmuFunctReadPerRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 24),
    _FibTmuFunctReadPerRun_Type()
)
fibTmuFunctReadPerRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctReadPerRun.setStatus("mandatory")


class _FibTmuFunctDmaThreshRun_Type(Integer32):
    """Custom type fibTmuFunctDmaThreshRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_FibTmuFunctDmaThreshRun_Type.__name__ = "Integer32"
_FibTmuFunctDmaThreshRun_Object = MibScalar
fibTmuFunctDmaThreshRun = _FibTmuFunctDmaThreshRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 25),
    _FibTmuFunctDmaThreshRun_Type()
)
fibTmuFunctDmaThreshRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctDmaThreshRun.setStatus("mandatory")


class _FibTmuFunctRemWrapTypeRun_Type(Integer32):
    """Custom type fibTmuFunctRemWrapTypeRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FibTmuFunctRemWrapTypeRun_Type.__name__ = "Integer32"
_FibTmuFunctRemWrapTypeRun_Object = MibScalar
fibTmuFunctRemWrapTypeRun = _FibTmuFunctRemWrapTypeRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 26),
    _FibTmuFunctRemWrapTypeRun_Type()
)
fibTmuFunctRemWrapTypeRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctRemWrapTypeRun.setStatus("mandatory")


class _FibTmuFunctRemWrapLenRun_Type(Integer32):
    """Custom type fibTmuFunctRemWrapLenRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_FibTmuFunctRemWrapLenRun_Type.__name__ = "Integer32"
_FibTmuFunctRemWrapLenRun_Object = MibScalar
fibTmuFunctRemWrapLenRun = _FibTmuFunctRemWrapLenRun_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 1, 27),
    _FibTmuFunctRemWrapLenRun_Type()
)
fibTmuFunctRemWrapLenRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibTmuFunctRemWrapLenRun.setStatus("mandatory")
_FibTmuFunctRtpGrpVrsPerm_ObjectIdentity = ObjectIdentity
fibTmuFunctRtpGrpVrsPerm = _FibTmuFunctRtpGrpVrsPerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2)
)


class _FibTmuFunctBeacon2AutotestPerm_Type(Integer32):
    """Custom type fibTmuFunctBeacon2AutotestPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 200),
    )


_FibTmuFunctBeacon2AutotestPerm_Type.__name__ = "Integer32"
_FibTmuFunctBeacon2AutotestPerm_Object = MibScalar
fibTmuFunctBeacon2AutotestPerm = _FibTmuFunctBeacon2AutotestPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 1),
    _FibTmuFunctBeacon2AutotestPerm_Type()
)
fibTmuFunctBeacon2AutotestPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctBeacon2AutotestPerm.setStatus("mandatory")


class _FibTmuFunctBeacon2OkPerm_Type(Integer32):
    """Custom type fibTmuFunctBeacon2OkPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 200),
    )


_FibTmuFunctBeacon2OkPerm_Type.__name__ = "Integer32"
_FibTmuFunctBeacon2OkPerm_Object = MibScalar
fibTmuFunctBeacon2OkPerm = _FibTmuFunctBeacon2OkPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 2),
    _FibTmuFunctBeacon2OkPerm_Type()
)
fibTmuFunctBeacon2OkPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctBeacon2OkPerm.setStatus("mandatory")


class _FibTmuFunctOk2BeaconPerm_Type(Integer32):
    """Custom type fibTmuFunctOk2BeaconPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1100, 2500),
    )


_FibTmuFunctOk2BeaconPerm_Type.__name__ = "Integer32"
_FibTmuFunctOk2BeaconPerm_Object = MibScalar
fibTmuFunctOk2BeaconPerm = _FibTmuFunctOk2BeaconPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 3),
    _FibTmuFunctOk2BeaconPerm_Type()
)
fibTmuFunctOk2BeaconPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctOk2BeaconPerm.setStatus("mandatory")


class _FibTmuFunctWrapCwtPerm_Type(Integer32):
    """Custom type fibTmuFunctWrapCwtPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FibTmuFunctWrapCwtPerm_Type.__name__ = "Integer32"
_FibTmuFunctWrapCwtPerm_Object = MibScalar
fibTmuFunctWrapCwtPerm = _FibTmuFunctWrapCwtPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 4),
    _FibTmuFunctWrapCwtPerm_Type()
)
fibTmuFunctWrapCwtPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctWrapCwtPerm.setStatus("mandatory")


class _FibTmuFunctWrapWnrPerm_Type(Integer32):
    """Custom type fibTmuFunctWrapWnrPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-release-cpu", 1),
          ("release-cpu", 2))
    )


_FibTmuFunctWrapWnrPerm_Type.__name__ = "Integer32"
_FibTmuFunctWrapWnrPerm_Object = MibScalar
fibTmuFunctWrapWnrPerm = _FibTmuFunctWrapWnrPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 5),
    _FibTmuFunctWrapWnrPerm_Type()
)
fibTmuFunctWrapWnrPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctWrapWnrPerm.setStatus("mandatory")


class _FibTmuFunctRingIstPerm_Type(Integer32):
    """Custom type fibTmuFunctRingIstPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FibTmuFunctRingIstPerm_Type.__name__ = "Integer32"
_FibTmuFunctRingIstPerm_Object = MibScalar
fibTmuFunctRingIstPerm = _FibTmuFunctRingIstPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 6),
    _FibTmuFunctRingIstPerm_Type()
)
fibTmuFunctRingIstPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctRingIstPerm.setStatus("mandatory")


class _FibTmuFunctRingIstnrPerm_Type(Integer32):
    """Custom type fibTmuFunctRingIstnrPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("istnr-dont-release-cpu", 1),
          ("istnr-release-cpu", 2))
    )


_FibTmuFunctRingIstnrPerm_Type.__name__ = "Integer32"
_FibTmuFunctRingIstnrPerm_Object = MibScalar
fibTmuFunctRingIstnrPerm = _FibTmuFunctRingIstnrPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 7),
    _FibTmuFunctRingIstnrPerm_Type()
)
fibTmuFunctRingIstnrPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctRingIstnrPerm.setStatus("mandatory")


class _FibTmuFunctCheckAogTauPerm_Type(Integer32):
    """Custom type fibTmuFunctCheckAogTauPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check-ring", 2),
          ("dont-check-ring", 1))
    )


_FibTmuFunctCheckAogTauPerm_Type.__name__ = "Integer32"
_FibTmuFunctCheckAogTauPerm_Object = MibScalar
fibTmuFunctCheckAogTauPerm = _FibTmuFunctCheckAogTauPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 8),
    _FibTmuFunctCheckAogTauPerm_Type()
)
fibTmuFunctCheckAogTauPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctCheckAogTauPerm.setStatus("mandatory")


class _FibTmuFunctMaxNoiPerm_Type(Integer32):
    """Custom type fibTmuFunctMaxNoiPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_FibTmuFunctMaxNoiPerm_Type.__name__ = "Integer32"
_FibTmuFunctMaxNoiPerm_Object = MibScalar
fibTmuFunctMaxNoiPerm = _FibTmuFunctMaxNoiPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 9),
    _FibTmuFunctMaxNoiPerm_Type()
)
fibTmuFunctMaxNoiPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctMaxNoiPerm.setStatus("mandatory")


class _FibTmuFunctLinkPtifPerm_Type(Integer32):
    """Custom type fibTmuFunctLinkPtifPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-link-to-last", 1),
          ("link-to-last", 2))
    )


_FibTmuFunctLinkPtifPerm_Type.__name__ = "Integer32"
_FibTmuFunctLinkPtifPerm_Object = MibScalar
fibTmuFunctLinkPtifPerm = _FibTmuFunctLinkPtifPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 10),
    _FibTmuFunctLinkPtifPerm_Type()
)
fibTmuFunctLinkPtifPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctLinkPtifPerm.setStatus("mandatory")


class _FibTmuFunctInsPatPerm_Type(Integer32):
    """Custom type fibTmuFunctInsPatPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 4000),
    )


_FibTmuFunctInsPatPerm_Type.__name__ = "Integer32"
_FibTmuFunctInsPatPerm_Object = MibScalar
fibTmuFunctInsPatPerm = _FibTmuFunctInsPatPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 11),
    _FibTmuFunctInsPatPerm_Type()
)
fibTmuFunctInsPatPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctInsPatPerm.setStatus("mandatory")


class _FibTmuFunctUseMismatchPerm_Type(Integer32):
    """Custom type fibTmuFunctUseMismatchPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-use-mismatch", 1),
          ("use-mismatch", 2))
    )


_FibTmuFunctUseMismatchPerm_Type.__name__ = "Integer32"
_FibTmuFunctUseMismatchPerm_Object = MibScalar
fibTmuFunctUseMismatchPerm = _FibTmuFunctUseMismatchPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 12),
    _FibTmuFunctUseMismatchPerm_Type()
)
fibTmuFunctUseMismatchPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctUseMismatchPerm.setStatus("mandatory")


class _FibTmuFunctChkRingInsPerm_Type(Integer32):
    """Custom type fibTmuFunctChkRingInsPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("check-ring", 2),
          ("dont-check-ring", 1))
    )


_FibTmuFunctChkRingInsPerm_Type.__name__ = "Integer32"
_FibTmuFunctChkRingInsPerm_Object = MibScalar
fibTmuFunctChkRingInsPerm = _FibTmuFunctChkRingInsPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 13),
    _FibTmuFunctChkRingInsPerm_Type()
)
fibTmuFunctChkRingInsPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctChkRingInsPerm.setStatus("mandatory")


class _FibTmuFunctChkRingPerPerm_Type(Integer32):
    """Custom type fibTmuFunctChkRingPerPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 4000),
    )


_FibTmuFunctChkRingPerPerm_Type.__name__ = "Integer32"
_FibTmuFunctChkRingPerPerm_Object = MibScalar
fibTmuFunctChkRingPerPerm = _FibTmuFunctChkRingPerPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 14),
    _FibTmuFunctChkRingPerPerm_Type()
)
fibTmuFunctChkRingPerPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctChkRingPerPerm.setStatus("mandatory")


class _FibTmuFunctClaimTimeOutPerm_Type(Integer32):
    """Custom type fibTmuFunctClaimTimeOutPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 500),
    )


_FibTmuFunctClaimTimeOutPerm_Type.__name__ = "Integer32"
_FibTmuFunctClaimTimeOutPerm_Object = MibScalar
fibTmuFunctClaimTimeOutPerm = _FibTmuFunctClaimTimeOutPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 15),
    _FibTmuFunctClaimTimeOutPerm_Type()
)
fibTmuFunctClaimTimeOutPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctClaimTimeOutPerm.setStatus("mandatory")


class _FibTmuFunctAnotherCheckPerm_Type(Integer32):
    """Custom type fibTmuFunctAnotherCheckPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("another-check", 2),
          ("no-another-check", 1))
    )


_FibTmuFunctAnotherCheckPerm_Type.__name__ = "Integer32"
_FibTmuFunctAnotherCheckPerm_Object = MibScalar
fibTmuFunctAnotherCheckPerm = _FibTmuFunctAnotherCheckPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 16),
    _FibTmuFunctAnotherCheckPerm_Type()
)
fibTmuFunctAnotherCheckPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctAnotherCheckPerm.setStatus("mandatory")


class _FibTmuFunctTmsOnOutPerm_Type(Integer32):
    """Custom type fibTmuFunctTmsOnOutPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FibTmuFunctTmsOnOutPerm_Type.__name__ = "Integer32"
_FibTmuFunctTmsOnOutPerm_Object = MibScalar
fibTmuFunctTmsOnOutPerm = _FibTmuFunctTmsOnOutPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 17),
    _FibTmuFunctTmsOnOutPerm_Type()
)
fibTmuFunctTmsOnOutPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctTmsOnOutPerm.setStatus("mandatory")


class _FibTmuFunctUseJitterPerm_Type(Integer32):
    """Custom type fibTmuFunctUseJitterPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-jitter-buster", 1),
          ("use-jitter-buster", 2))
    )


_FibTmuFunctUseJitterPerm_Type.__name__ = "Integer32"
_FibTmuFunctUseJitterPerm_Object = MibScalar
fibTmuFunctUseJitterPerm = _FibTmuFunctUseJitterPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 18),
    _FibTmuFunctUseJitterPerm_Type()
)
fibTmuFunctUseJitterPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctUseJitterPerm.setStatus("mandatory")


class _FibTmuFunctForceStpRiPerm_Type(Integer32):
    """Custom type fibTmuFunctForceStpRiPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-force-ri-stp", 1),
          ("force-ri-stp", 2))
    )


_FibTmuFunctForceStpRiPerm_Type.__name__ = "Integer32"
_FibTmuFunctForceStpRiPerm_Object = MibScalar
fibTmuFunctForceStpRiPerm = _FibTmuFunctForceStpRiPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 21),
    _FibTmuFunctForceStpRiPerm_Type()
)
fibTmuFunctForceStpRiPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctForceStpRiPerm.setStatus("mandatory")


class _FibTmuFunctForceStpRoPerm_Type(Integer32):
    """Custom type fibTmuFunctForceStpRoPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-not-force-ro-stp", 1),
          ("force-ro-stp", 2))
    )


_FibTmuFunctForceStpRoPerm_Type.__name__ = "Integer32"
_FibTmuFunctForceStpRoPerm_Object = MibScalar
fibTmuFunctForceStpRoPerm = _FibTmuFunctForceStpRoPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 22),
    _FibTmuFunctForceStpRoPerm_Type()
)
fibTmuFunctForceStpRoPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctForceStpRoPerm.setStatus("mandatory")


class _FibTmuFunctMaxSavRecPerm_Type(Integer32):
    """Custom type fibTmuFunctMaxSavRecPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 20),
    )


_FibTmuFunctMaxSavRecPerm_Type.__name__ = "Integer32"
_FibTmuFunctMaxSavRecPerm_Object = MibScalar
fibTmuFunctMaxSavRecPerm = _FibTmuFunctMaxSavRecPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 23),
    _FibTmuFunctMaxSavRecPerm_Type()
)
fibTmuFunctMaxSavRecPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctMaxSavRecPerm.setStatus("mandatory")


class _FibTmuFunctReadPerPerm_Type(Integer32):
    """Custom type fibTmuFunctReadPerPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FibTmuFunctReadPerPerm_Type.__name__ = "Integer32"
_FibTmuFunctReadPerPerm_Object = MibScalar
fibTmuFunctReadPerPerm = _FibTmuFunctReadPerPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 24),
    _FibTmuFunctReadPerPerm_Type()
)
fibTmuFunctReadPerPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctReadPerPerm.setStatus("mandatory")


class _FibTmuFunctDmaThreshPerm_Type(Integer32):
    """Custom type fibTmuFunctDmaThreshPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_FibTmuFunctDmaThreshPerm_Type.__name__ = "Integer32"
_FibTmuFunctDmaThreshPerm_Object = MibScalar
fibTmuFunctDmaThreshPerm = _FibTmuFunctDmaThreshPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 25),
    _FibTmuFunctDmaThreshPerm_Type()
)
fibTmuFunctDmaThreshPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctDmaThreshPerm.setStatus("mandatory")


class _FibTmuFunctRemWrapTypePerm_Type(Integer32):
    """Custom type fibTmuFunctRemWrapTypePerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FibTmuFunctRemWrapTypePerm_Type.__name__ = "Integer32"
_FibTmuFunctRemWrapTypePerm_Object = MibScalar
fibTmuFunctRemWrapTypePerm = _FibTmuFunctRemWrapTypePerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 26),
    _FibTmuFunctRemWrapTypePerm_Type()
)
fibTmuFunctRemWrapTypePerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctRemWrapTypePerm.setStatus("mandatory")


class _FibTmuFunctRemWrapLenPerm_Type(Integer32):
    """Custom type fibTmuFunctRemWrapLenPerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_FibTmuFunctRemWrapLenPerm_Type.__name__ = "Integer32"
_FibTmuFunctRemWrapLenPerm_Object = MibScalar
fibTmuFunctRemWrapLenPerm = _FibTmuFunctRemWrapLenPerm_Object(
    (1, 3, 6, 1, 4, 1, 22, 60, 8, 2, 27),
    _FibTmuFunctRemWrapLenPerm_Type()
)
fibTmuFunctRemWrapLenPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibTmuFunctRemWrapLenPerm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TMU-MIB",
    **{"mgmt": mgmt,
       "private": private,
       "enterprises": enterprises,
       "fibronics": fibronics,
       "tmu": tmu,
       "tmuSystem": tmuSystem,
       "fibTmuNumEventErrs": fibTmuNumEventErrs,
       "fibTmuArpAgeTime": fibTmuArpAgeTime,
       "fibTmuNumRarpUpdate": fibTmuNumRarpUpdate,
       "fibTmuMainSwVersion": fibTmuMainSwVersion,
       "fibTmuEepromVersion": fibTmuEepromVersion,
       "fibTmuEepromDeffective": fibTmuEepromDeffective,
       "fibTmuLastSysIfIndex": fibTmuLastSysIfIndex,
       "fibTmuTrDrvVersion": fibTmuTrDrvVersion,
       "fibTmuSccDrvVersion": fibTmuSccDrvVersion,
       "fibTmuSnmpUsrVersion": fibTmuSnmpUsrVersion,
       "fibTmuDisplayDebugMode": fibTmuDisplayDebugMode,
       "fibTmuEeFaultsFormat": fibTmuEeFaultsFormat,
       "fibTmuRunFaultsFormat": fibTmuRunFaultsFormat,
       "fibTmuFunctionalityVersion": fibTmuFunctionalityVersion,
       "fibTmuUtilitiesVersion": fibTmuUtilitiesVersion,
       "fibTmuWrapIn": fibTmuWrapIn,
       "fibTmuWrapOut": fibTmuWrapOut,
       "fibTmuLoadEeDefaults": fibTmuLoadEeDefaults,
       "fibTmuDontResetFatal": fibTmuDontResetFatal,
       "fibTmuRIConnection": fibTmuRIConnection,
       "fibTmuROConnection": fibTmuROConnection,
       "fibTmuRealTimeClock": fibTmuRealTimeClock,
       "tmuIntrfc": tmuIntrfc,
       "fibTmuIntrfcTable": fibTmuIntrfcTable,
       "fibTmuIntrfcEntry": fibTmuIntrfcEntry,
       "fibTmuIntrfcIndex": fibTmuIntrfcIndex,
       "fibTmuNumRarpRcvd": fibTmuNumRarpRcvd,
       "fibTmuNumRxRjctMem": fibTmuNumRxRjctMem,
       "fibTmuNumRxAccepted": fibTmuNumRxAccepted,
       "fibTmuNumRxBdcst": fibTmuNumRxBdcst,
       "fibTmuNumRxSpecific": fibTmuNumRxSpecific,
       "fibTmuNumRifIncluded": fibTmuNumRifIncluded,
       "fibTmuNumNoRif": fibTmuNumNoRif,
       "fibTmuNumNonSnap": fibTmuNumNonSnap,
       "fibTmuNumUnknownType": fibTmuNumUnknownType,
       "fibTmuNumRifLong": fibTmuNumRifLong,
       "fibTmuNumRrpRjctIp": fibTmuNumRrpRjctIp,
       "fibTmuNumArpRcvd": fibTmuNumArpRcvd,
       "fibTmuNumIpRcvd": fibTmuNumIpRcvd,
       "fibTmuNumIfDown": fibTmuNumIfDown,
       "fibTmuNumOwnBrdcst": fibTmuNumOwnBrdcst,
       "fibTmuAc00Cntr": fibTmuAc00Cntr,
       "fibTmuAc01Cntr": fibTmuAc01Cntr,
       "fibTmuAc10Cntr": fibTmuAc10Cntr,
       "fibTmuAc11Cntr": fibTmuAc11Cntr,
       "fibTmuParityEc": fibTmuParityEc,
       "fibTmuFrameEc": fibTmuFrameEc,
       "fibTmuRxNoiseEc": fibTmuRxNoiseEc,
       "fibTmuBreakEc": fibTmuBreakEc,
       "fibTmuNumConfigNotValid": fibTmuNumConfigNotValid,
       "fibTmuNumAddrNotFound": fibTmuNumAddrNotFound,
       "fibTmuNumProcessDisabled": fibTmuNumProcessDisabled,
       "fibTmuNumBeaconsRcvd": fibTmuNumBeaconsRcvd,
       "fibTmuLastBeaconTime": fibTmuLastBeaconTime,
       "fibTmuLastBeaconType": fibTmuLastBeaconType,
       "fibTmuLastBeaconAddr": fibTmuLastBeaconAddr,
       "fibTmuLastBeaconNaun": fibTmuLastBeaconNaun,
       "fibTmuNumRxGroup": fibTmuNumRxGroup,
       "fibTmuNumRxFunctional": fibTmuNumRxFunctional,
       "tmuMatch": tmuMatch,
       "fibTmuMatchUpdateTime": fibTmuMatchUpdateTime,
       "fibTmuMatchNumEntries": fibTmuMatchNumEntries,
       "fibTmuMatchNumTmuEntries": fibTmuMatchNumTmuEntries,
       "fibTmuMatchFirstChipIndex": fibTmuMatchFirstChipIndex,
       "fibTmuMatchSecondChipIndex": fibTmuMatchSecondChipIndex,
       "fibTmuMatchActMonIndex": fibTmuMatchActMonIndex,
       "fibTmuMatchConfigChipIndex": fibTmuMatchConfigChipIndex,
       "fibTmuMatchListValid": fibTmuMatchListValid,
       "fibTmuMatchUpToDate": fibTmuMatchUpToDate,
       "fibTmuMatchNoMatchReason": fibTmuMatchNoMatchReason,
       "fibTmuMatchTable": fibTmuMatchTable,
       "fibTmuMatchEntry": fibTmuMatchEntry,
       "fibTmuMatchIndex": fibTmuMatchIndex,
       "fibTmuMatchTauId": fibTmuMatchTauId,
       "fibTmuMatchPortId": fibTmuMatchPortId,
       "fibTmuMatchPhysAddr": fibTmuMatchPhysAddr,
       "fibTmuMatchStationInfo": fibTmuMatchStationInfo,
       "tmuStations": tmuStations,
       "fibTmuStationsUpdateTime": fibTmuStationsUpdateTime,
       "fibTmuStationsNumEntries": fibTmuStationsNumEntries,
       "fibTmuStationsNumTmuEntries": fibTmuStationsNumTmuEntries,
       "fibTmuStationsFirstChipIndex": fibTmuStationsFirstChipIndex,
       "fibTmuStationsSecondChipIndex": fibTmuStationsSecondChipIndex,
       "fibTmuStationsActMonIndex": fibTmuStationsActMonIndex,
       "fibTmuStationsConfigChipIndex": fibTmuStationsConfigChipIndex,
       "fibTmuStationsStationsListValid": fibTmuStationsStationsListValid,
       "fibTmuStationsUpToDate": fibTmuStationsUpToDate,
       "fibTmuMatchNoStationsListReason": fibTmuMatchNoStationsListReason,
       "fibTmuStationsTable": fibTmuStationsTable,
       "fibTmuStationsEntry": fibTmuStationsEntry,
       "fibTmuStationsIndex": fibTmuStationsIndex,
       "fibTmuStationsPhysAddr": fibTmuStationsPhysAddr,
       "fibTmuStationsStationInfo": fibTmuStationsStationInfo,
       "tmuPorts": tmuPorts,
       "fibTmuPortsNumRelayOpen": fibTmuPortsNumRelayOpen,
       "fibTmuPortsNumPhantomPresent": fibTmuPortsNumPhantomPresent,
       "fibTmuPortsNumPortsPerTmu": fibTmuPortsNumPortsPerTmu,
       "fibTmuPortsNumTausPerTmu": fibTmuPortsNumTausPerTmu,
       "fibTmuPortsNumPortsPerTau": fibTmuPortsNumPortsPerTau,
       "fibTmuPortsMaxNumTauErrs": fibTmuPortsMaxNumTauErrs,
       "fibTmuPortsMaxFirstTimeout": fibTmuPortsMaxFirstTimeout,
       "fibTmuPortsTauTable": fibTmuPortsTauTable,
       "fibTmuPortsTauEntry": fibTmuPortsTauEntry,
       "fibTmuPortsTmuPort": fibTmuPortsTmuPort,
       "fibTmuPortsPortType": fibTmuPortsPortType,
       "fibTmuPortsEndConnection": fibTmuPortsEndConnection,
       "fibTmuPortsPortStatus": fibTmuPortsPortStatus,
       "fibTmuPortsManagerCloseRun": fibTmuPortsManagerCloseRun,
       "fibTmuPortsManagerClosePerm": fibTmuPortsManagerClosePerm,
       "fibTmuPortsNumConsequentErrs": fibTmuPortsNumConsequentErrs,
       "fibTmuPortsNumTimeout": fibTmuPortsNumTimeout,
       "fibTmuPortsTauPortState": fibTmuPortsTauPortState,
       "fibTmuPortsNumPorts": fibTmuPortsNumPorts,
       "fibTmuPortsNumAttached": fibTmuPortsNumAttached,
       "fibTmuPortsNumPhantomUp": fibTmuPortsNumPhantomUp,
       "fibTmuPortsTauRevision": fibTmuPortsTauRevision,
       "fibTmuPortsModuleId": fibTmuPortsModuleId,
       "fibTmuPortsNumModules": fibTmuPortsNumModules,
       "fibTmuPortsTauMode": fibTmuPortsTauMode,
       "fibTmuPortsLedState": fibTmuPortsLedState,
       "fibTmuPortsRequestType": fibTmuPortsRequestType,
       "fibTmuPortsLastTxTime": fibTmuPortsLastTxTime,
       "fibTmuPortsLastPollTime": fibTmuPortsLastPollTime,
       "fibTmuPortsUpdateTime": fibTmuPortsUpdateTime,
       "fibTmuPortsAllowedAddr": fibTmuPortsAllowedAddr,
       "fibTmuPortsAllowedAddrLoaded": fibTmuPortsAllowedAddrLoaded,
       "fibTmuPortsAllTable": fibTmuPortsAllTable,
       "fibTmuPortsAllEntry": fibTmuPortsAllEntry,
       "fibTmuPortsTmuPortIndex": fibTmuPortsTmuPortIndex,
       "fibTmuPortsTauPortIndex": fibTmuPortsTauPortIndex,
       "fibTmuPortsPortState": fibTmuPortsPortState,
       "fibTmuPortsGenCloseRun": fibTmuPortsGenCloseRun,
       "fibTmuPortsGenClosePerm": fibTmuPortsGenClosePerm,
       "fibTmuPortsPhysAddr": fibTmuPortsPhysAddr,
       "fibTmuPortsStationInfo": fibTmuPortsStationInfo,
       "fibTmuPortsTauAllowedAddr": fibTmuPortsTauAllowedAddr,
       "fibTmuPortsTauAllowedAddrLoaded": fibTmuPortsTauAllowedAddrLoaded,
       "tmuProduction": tmuProduction,
       "fibTmuProductionAddr48No1": fibTmuProductionAddr48No1,
       "fibTmuProductionAddr48No2": fibTmuProductionAddr48No2,
       "fibTmuProductionAddr48No3": fibTmuProductionAddr48No3,
       "fibTmuProductionRomType": fibTmuProductionRomType,
       "fibTmuProductionRamType": fibTmuProductionRamType,
       "fibTmuProductionFlashType": fibTmuProductionFlashType,
       "fibTmuProductionEepromType": fibTmuProductionEepromType,
       "fibTmuProductionSerialNum": fibTmuProductionSerialNum,
       "fibTmuProductionRamSize": fibTmuProductionRamSize,
       "fibTmuProductionFlash0Size": fibTmuProductionFlash0Size,
       "fibTmuProductionFlash1Size": fibTmuProductionFlash1Size,
       "fibTmuProductionEepromSize": fibTmuProductionEepromSize,
       "fibTmuProductionHwInfo": fibTmuProductionHwInfo,
       "fibTmuProductionBoardType": fibTmuProductionBoardType,
       "tmuSecurity": tmuSecurity,
       "fibTmuSecurityModeRun": fibTmuSecurityModeRun,
       "fibTmuSecurityModePerm": fibTmuSecurityModePerm,
       "fibTmuNumStationSecurity": fibTmuNumStationSecurity,
       "fibTmuNumStationLeft": fibTmuNumStationLeft,
       "tmuFunction": tmuFunction,
       "fibTmuFunctRtpGrpVrsRun": fibTmuFunctRtpGrpVrsRun,
       "fibTmuFunctBeacon2AutotestRun": fibTmuFunctBeacon2AutotestRun,
       "fibTmuFunctBeacon2OkRun": fibTmuFunctBeacon2OkRun,
       "fibTmuFunctOk2BeaconRun": fibTmuFunctOk2BeaconRun,
       "fibTmuFunctWrapCwtRun": fibTmuFunctWrapCwtRun,
       "fibTmuFunctWrapWnrRun": fibTmuFunctWrapWnrRun,
       "fibTmuFunctRingIstRun": fibTmuFunctRingIstRun,
       "fibTmuFunctRingIstnrRun": fibTmuFunctRingIstnrRun,
       "fibTmuFunctCheckAogTauRun": fibTmuFunctCheckAogTauRun,
       "fibTmuFunctMaxNoiRun": fibTmuFunctMaxNoiRun,
       "fibTmuFunctLinkPtifRun": fibTmuFunctLinkPtifRun,
       "fibTmuFunctInsPatRun": fibTmuFunctInsPatRun,
       "fibTmuFunctUseMismatchRun": fibTmuFunctUseMismatchRun,
       "fibTmuFunctChkRingInsRun": fibTmuFunctChkRingInsRun,
       "fibTmuFunctChkRingPerRun": fibTmuFunctChkRingPerRun,
       "fibTmuFunctClaimTimeOutRun": fibTmuFunctClaimTimeOutRun,
       "fibTmuFunctAnotherCheckRun": fibTmuFunctAnotherCheckRun,
       "fibTmuFunctTmsOnOutRun": fibTmuFunctTmsOnOutRun,
       "fibTmuFunctUseJitterRun": fibTmuFunctUseJitterRun,
       "fibTmuFunctForceStpRiRun": fibTmuFunctForceStpRiRun,
       "fibTmuFunctForceStpRoRun": fibTmuFunctForceStpRoRun,
       "fibTmuFunctMaxSavRecRun": fibTmuFunctMaxSavRecRun,
       "fibTmuFunctReadPerRun": fibTmuFunctReadPerRun,
       "fibTmuFunctDmaThreshRun": fibTmuFunctDmaThreshRun,
       "fibTmuFunctRemWrapTypeRun": fibTmuFunctRemWrapTypeRun,
       "fibTmuFunctRemWrapLenRun": fibTmuFunctRemWrapLenRun,
       "fibTmuFunctRtpGrpVrsPerm": fibTmuFunctRtpGrpVrsPerm,
       "fibTmuFunctBeacon2AutotestPerm": fibTmuFunctBeacon2AutotestPerm,
       "fibTmuFunctBeacon2OkPerm": fibTmuFunctBeacon2OkPerm,
       "fibTmuFunctOk2BeaconPerm": fibTmuFunctOk2BeaconPerm,
       "fibTmuFunctWrapCwtPerm": fibTmuFunctWrapCwtPerm,
       "fibTmuFunctWrapWnrPerm": fibTmuFunctWrapWnrPerm,
       "fibTmuFunctRingIstPerm": fibTmuFunctRingIstPerm,
       "fibTmuFunctRingIstnrPerm": fibTmuFunctRingIstnrPerm,
       "fibTmuFunctCheckAogTauPerm": fibTmuFunctCheckAogTauPerm,
       "fibTmuFunctMaxNoiPerm": fibTmuFunctMaxNoiPerm,
       "fibTmuFunctLinkPtifPerm": fibTmuFunctLinkPtifPerm,
       "fibTmuFunctInsPatPerm": fibTmuFunctInsPatPerm,
       "fibTmuFunctUseMismatchPerm": fibTmuFunctUseMismatchPerm,
       "fibTmuFunctChkRingInsPerm": fibTmuFunctChkRingInsPerm,
       "fibTmuFunctChkRingPerPerm": fibTmuFunctChkRingPerPerm,
       "fibTmuFunctClaimTimeOutPerm": fibTmuFunctClaimTimeOutPerm,
       "fibTmuFunctAnotherCheckPerm": fibTmuFunctAnotherCheckPerm,
       "fibTmuFunctTmsOnOutPerm": fibTmuFunctTmsOnOutPerm,
       "fibTmuFunctUseJitterPerm": fibTmuFunctUseJitterPerm,
       "fibTmuFunctForceStpRiPerm": fibTmuFunctForceStpRiPerm,
       "fibTmuFunctForceStpRoPerm": fibTmuFunctForceStpRoPerm,
       "fibTmuFunctMaxSavRecPerm": fibTmuFunctMaxSavRecPerm,
       "fibTmuFunctReadPerPerm": fibTmuFunctReadPerPerm,
       "fibTmuFunctDmaThreshPerm": fibTmuFunctDmaThreshPerm,
       "fibTmuFunctRemWrapTypePerm": fibTmuFunctRemWrapTypePerm,
       "fibTmuFunctRemWrapLenPerm": fibTmuFunctRemWrapLenPerm}
)
