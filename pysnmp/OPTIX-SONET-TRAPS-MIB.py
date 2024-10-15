# SNMP MIB module (OPTIX-SONET-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:34 2024
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

(optixCommonSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixCommonSonet")

(AlarmEventType,
 AlmDataNtfcnCdeType,
 AlmDataSrvEffType,
 DirectionType,
 LocationType,
 MOD2Type,
 PerformanceEventType,
 ValidflagType) = mibBuilder.importSymbols(
    "OPTIX-SONET-TC-MIB",
    "AlarmEventType",
    "AlmDataNtfcnCdeType",
    "AlmDataSrvEffType",
    "DirectionType",
    "LocationType",
    "MOD2Type",
    "PerformanceEventType",
    "ValidflagType")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

optixSonetTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40)
)
optixSonetTraps.setRevisions(
        ("2006-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OptixTrapsAlarm_ObjectIdentity = ObjectIdentity
optixTrapsAlarm = _OptixTrapsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10)
)
_OptixTrapsEvent_ObjectIdentity = ObjectIdentity
optixTrapsEvent = _OptixTrapsEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20)
)
_OptixTrapsEnvironment_ObjectIdentity = ObjectIdentity
optixTrapsEnvironment = _OptixTrapsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30)
)
_OptixTrapsPerformance_ObjectIdentity = ObjectIdentity
optixTrapsPerformance = _OptixTrapsPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40)
)
_OptixTrapsCommon_ObjectIdentity = ObjectIdentity
optixTrapsCommon = _OptixTrapsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50)
)
_RptAlmName_Type = AlarmEventType
_RptAlmName_Object = MibScalar
rptAlmName = _RptAlmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 10),
    _RptAlmName_Type()
)
rptAlmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptAlmName.setStatus("current")
_RptEvtMOD2_Type = MOD2Type
_RptEvtMOD2_Object = MibScalar
rptEvtMOD2 = _RptEvtMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 20),
    _RptEvtMOD2_Type()
)
rptEvtMOD2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtMOD2.setStatus("current")
_RptEvtSlot_Type = Unsigned32
_RptEvtSlot_Object = MibScalar
rptEvtSlot = _RptEvtSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 30),
    _RptEvtSlot_Type()
)
rptEvtSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtSlot.setStatus("current")
_RptEvtPort_Type = Unsigned32
_RptEvtPort_Object = MibScalar
rptEvtPort = _RptEvtPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 40),
    _RptEvtPort_Type()
)
rptEvtPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtPort.setStatus("current")
_RptEvtPath_Type = Unsigned32
_RptEvtPath_Object = MibScalar
rptEvtPath = _RptEvtPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 50),
    _RptEvtPath_Type()
)
rptEvtPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtPath.setStatus("current")
_RptEvtVT_Type = Unsigned32
_RptEvtVT_Object = MibScalar
rptEvtVT = _RptEvtVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 70),
    _RptEvtVT_Type()
)
rptEvtVT.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtVT.setStatus("current")
_RptEvtDateTime_Type = DateAndTime
_RptEvtDateTime_Object = MibScalar
rptEvtDateTime = _RptEvtDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 80),
    _RptEvtDateTime_Type()
)
rptEvtDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtDateTime.setStatus("current")
_RptEvtSrvEff_Type = AlmDataSrvEffType
_RptEvtSrvEff_Object = MibScalar
rptEvtSrvEff = _RptEvtSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 90),
    _RptEvtSrvEff_Type()
)
rptEvtSrvEff.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtSrvEff.setStatus("current")
_RptEvtNtfcnCde_Type = AlmDataNtfcnCdeType
_RptEvtNtfcnCde_Object = MibScalar
rptEvtNtfcnCde = _RptEvtNtfcnCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 100),
    _RptEvtNtfcnCde_Type()
)
rptEvtNtfcnCde.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtNtfcnCde.setStatus("current")
_RptEvtLocation_Type = LocationType
_RptEvtLocation_Object = MibScalar
rptEvtLocation = _RptEvtLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 110),
    _RptEvtLocation_Type()
)
rptEvtLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtLocation.setStatus("current")
_RptEvtDirection_Type = DirectionType
_RptEvtDirection_Object = MibScalar
rptEvtDirection = _RptEvtDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 120),
    _RptEvtDirection_Type()
)
rptEvtDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtDirection.setStatus("current")
_RptEvtMonValue_Type = Integer32
_RptEvtMonValue_Object = MibScalar
rptEvtMonValue = _RptEvtMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 130),
    _RptEvtMonValue_Type()
)
rptEvtMonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtMonValue.setStatus("current")
_RptEvtThValue_Type = Unsigned32
_RptEvtThValue_Object = MibScalar
rptEvtThValue = _RptEvtThValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 140),
    _RptEvtThValue_Type()
)
rptEvtThValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtThValue.setStatus("current")
_RptEvtDescription_Type = DisplayString
_RptEvtDescription_Object = MibScalar
rptEvtDescription = _RptEvtDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 150),
    _RptEvtDescription_Type()
)
rptEvtDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtDescription.setStatus("current")
_RptEvtNumber_Type = Unsigned32
_RptEvtNumber_Object = MibScalar
rptEvtNumber = _RptEvtNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 160),
    _RptEvtNumber_Type()
)
rptEvtNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtNumber.setStatus("current")


class _RptEvtPeriod_Type(Integer32):
    """Custom type rptEvtPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("period15m", 1),
          ("period1day", 2))
    )


_RptEvtPeriod_Type.__name__ = "Integer32"
_RptEvtPeriod_Object = MibScalar
rptEvtPeriod = _RptEvtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 170),
    _RptEvtPeriod_Type()
)
rptEvtPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtPeriod.setStatus("current")
_RptEvtVldty_Type = ValidflagType
_RptEvtVldty_Object = MibScalar
rptEvtVldty = _RptEvtVldty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 180),
    _RptEvtVldty_Type()
)
rptEvtVldty.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtVldty.setStatus("current")


class _RptEvtEffect_Type(Integer32):
    """Custom type rptEvtEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cl", 8),
          ("sc", 7),
          ("tc", 6))
    )


_RptEvtEffect_Type.__name__ = "Integer32"
_RptEvtEffect_Object = MibScalar
rptEvtEffect = _RptEvtEffect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 190),
    _RptEvtEffect_Type()
)
rptEvtEffect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtEffect.setStatus("current")


class _RptEvtState_Type(Integer32):
    """Custom type rptEvtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("start", 1))
    )


_RptEvtState_Type.__name__ = "Integer32"
_RptEvtState_Object = MibScalar
rptEvtState = _RptEvtState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 200),
    _RptEvtState_Type()
)
rptEvtState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtState.setStatus("current")
_RptEvtAiddet_Type = Unsigned32
_RptEvtAiddet_Object = MibScalar
rptEvtAiddet = _RptEvtAiddet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 210),
    _RptEvtAiddet_Type()
)
rptEvtAiddet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtAiddet.setStatus("current")
_RptEvtSeqNumber_Type = Unsigned32
_RptEvtSeqNumber_Object = MibScalar
rptEvtSeqNumber = _RptEvtSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 220),
    _RptEvtSeqNumber_Type()
)
rptEvtSeqNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptEvtSeqNumber.setStatus("current")
_RptPmName_Type = PerformanceEventType
_RptPmName_Object = MibScalar
rptPmName = _RptPmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 50, 230),
    _RptPmName_Type()
)
rptPmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rptPmName.setStatus("current")
_OptixSonetTrapsConformance_ObjectIdentity = ObjectIdentity
optixSonetTrapsConformance = _OptixSonetTrapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 60)
)
_OptixSonetTrapsGroups_ObjectIdentity = ObjectIdentity
optixSonetTrapsGroups = _OptixSonetTrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 60, 1)
)
_OptixSonetTrapsCompliances_ObjectIdentity = ObjectIdentity
optixSonetTrapsCompliances = _OptixSonetTrapsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 60, 2)
)

# Managed Objects groups

optixSonetTrapsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 60, 1, 1)
)
optixSonetTrapsObjectGroup.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptAlmName"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptPmName"))
)
if mibBuilder.loadTexts:
    optixSonetTrapsObjectGroup.setStatus("current")


# Notification objects

almLossOfClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 3)
)
almLossOfClock.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLossOfClock.setStatus(
        "current"
    )

almFileLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 6)
)
almFileLost.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFileLost.setStatus(
        "current"
    )

almREILine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 37)
)
almREILine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almREILine.setStatus(
        "current"
    )

almBiasTemperatureOfPumpHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 69)
)
almBiasTemperatureOfPumpHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBiasTemperatureOfPumpHigh.setStatus(
        "current"
    )

almTimSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 87)
)
almTimSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTimSection.setStatus(
        "current"
    )

almLossOfAllSynchronousSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 100)
)
almLossOfAllSynchronousSource.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLossOfAllSynchronousSource.setStatus(
        "current"
    )

almSynchronousSourceDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 101)
)
almSynchronousSourceDegrade.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSynchronousSourceDegrade.setStatus(
        "current"
    )

almSyncLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 111)
)
almSyncLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSyncLOS.setStatus(
        "current"
    )

almProtectionSwitching = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 120)
)
almProtectionSwitching.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almProtectionSwitching.setStatus(
        "current"
    )

almDbmsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 185)
)
almDbmsError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDbmsError.setStatus(
        "current"
    )

almLossOfMultiplexSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 186)
)
almLossOfMultiplexSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLossOfMultiplexSignal.setStatus(
        "current"
    )

almLossOfSingleWavelengthSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 187)
)
almLossOfSingleWavelengthSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLossOfSingleWavelengthSignal.setStatus(
        "current"
    )

almAdditionOfSingleWavelengthSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 188)
)
almAdditionOfSingleWavelengthSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAdditionOfSingleWavelengthSignal.setStatus(
        "current"
    )

almLaserDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 189)
)
almLaserDegraded.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserDegraded.setStatus(
        "current"
    )

almPumpDiodeCoolingCurrentHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 192)
)
almPumpDiodeCoolingCurrentHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPumpDiodeCoolingCurrentHigh.setStatus(
        "current"
    )

almS1ModeSynChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 193)
)
almS1ModeSynChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almS1ModeSynChange.setStatus(
        "current"
    )

almDbmsIsInProtectMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 198)
)
almDbmsIsInProtectMode.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDbmsIsInProtectMode.setStatus(
        "current"
    )

almSecuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 200)
)
almSecuAlarm.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSecuAlarm.setStatus(
        "current"
    )

almForwardErrorCorrectionLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 212)
)
almForwardErrorCorrectionLossOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almForwardErrorCorrectionLossOfFrame.setStatus(
        "current"
    )

almForwardErrorCorrectionOutOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 213)
)
almForwardErrorCorrectionOutOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almForwardErrorCorrectionOutOfFrame.setStatus(
        "current"
    )

almRateOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 223)
)
almRateOver.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRateOver.setStatus(
        "current"
    )

almCardConfigurationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 232)
)
almCardConfigurationFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almCardConfigurationFail.setStatus(
        "current"
    )

almLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 240)
)
almLoopback.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopback.setStatus(
        "current"
    )

almCoolingCurrentModeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 270)
)
almCoolingCurrentModeHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almCoolingCurrentModeHigh.setStatus(
        "current"
    )

almOTULossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 272)
)
almOTULossOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOTULossOfFrame.setStatus(
        "current"
    )

almOTUOutOfMultiFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 273)
)
almOTUOutOfMultiFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOTUOutOfMultiFrame.setStatus(
        "current"
    )

almSmTIM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 274)
)
almSmTIM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSmTIM.setStatus(
        "current"
    )

almPmTIM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 275)
)
almPmTIM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPmTIM.setStatus(
        "current"
    )

almSmBDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 276)
)
almSmBDI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSmBDI.setStatus(
        "current"
    )

almPmBDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 277)
)
almPmBDI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPmBDI.setStatus(
        "current"
    )

almSmBEI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 278)
)
almSmBEI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSmBEI.setStatus(
        "current"
    )

almPmBEI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 279)
)
almPmBEI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPmBEI.setStatus(
        "current"
    )

almSmIAE = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 280)
)
almSmIAE.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSmIAE.setStatus(
        "current"
    )

almSmBipExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 282)
)
almSmBipExcessive.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSmBipExcessive.setStatus(
        "current"
    )

almPmBipExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 283)
)
almPmBipExcessive.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPmBipExcessive.setStatus(
        "current"
    )

almSmBipSignalDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 284)
)
almSmBipSignalDefect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSmBipSignalDefect.setStatus(
        "current"
    )

almPmBipSignalDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 285)
)
almPmBipSignalDefect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPmBipSignalDefect.setStatus(
        "current"
    )

almOTUAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 286)
)
almOTUAlarmIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOTUAlarmIndicationSignal.setStatus(
        "current"
    )

almODUAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 287)
)
almODUAlarmIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almODUAlarmIndicationSignal.setStatus(
        "current"
    )

almODUOpenConnectionIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 288)
)
almODUOpenConnectionIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almODUOpenConnectionIndicationSignal.setStatus(
        "current"
    )

almODULockedIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 289)
)
almODULockedIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almODULockedIndicationSignal.setStatus(
        "current"
    )

almSumInputOpticalPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 323)
)
almSumInputOpticalPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSumInputOpticalPowerHigh.setStatus(
        "current"
    )

almSumInputOpticalPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 324)
)
almSumInputOpticalPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSumInputOpticalPowerLow.setStatus(
        "current"
    )

almSumOutOpticalPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 325)
)
almSumOutOpticalPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSumOutOpticalPowerHigh.setStatus(
        "current"
    )

almOutOpticalPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 326)
)
almOutOpticalPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOutOpticalPowerLow.setStatus(
        "current"
    )

almGainLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 327)
)
almGainLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almGainLow.setStatus(
        "current"
    )

almExcessiveErrorDefectBeforeFEC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 335)
)
almExcessiveErrorDefectBeforeFEC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExcessiveErrorDefectBeforeFEC.setStatus(
        "current"
    )

almDgeAdjustmentFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 433)
)
almDgeAdjustmentFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDgeAdjustmentFail.setStatus(
        "current"
    )

almWavelengthLockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 439)
)
almWavelengthLockFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almWavelengthLockFail.setStatus(
        "current"
    )

almHotSwitchControlUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 440)
)
almHotSwitchControlUnavail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almHotSwitchControlUnavail.setStatus(
        "current"
    )

almEsconCodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 570)
)
almEsconCodeError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEsconCodeError.setStatus(
        "current"
    )

almCommitTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 573)
)
almCommitTimeout.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almCommitTimeout.setStatus(
        "current"
    )

almSwdlNePackageCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 574)
)
almSwdlNePackageCheck.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwdlNePackageCheck.setStatus(
        "current"
    )

almSwdlChaGmngmMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 575)
)
almSwdlChaGmngmMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwdlChaGmngmMismatch.setStatus(
        "current"
    )

almDBSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 591)
)
almDBSyncFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDBSyncFail.setStatus(
        "current"
    )

almClientMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 604)
)
almClientMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almClientMismatch.setStatus(
        "current"
    )

almLaserModuleMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 606)
)
almLaserModuleMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserModuleMismatch.setStatus(
        "current"
    )

almDlagProtFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12288)
)
almDlagProtFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDlagProtFail.setStatus(
        "current"
    )

almOamRemoteLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12291)
)
almOamRemoteLoop.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOamRemoteLoop.setStatus(
        "current"
    )

almOamRemoteSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12292)
)
almOamRemoteSD.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOamRemoteSD.setStatus(
        "current"
    )

almOamRemoteSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12293)
)
almOamRemoteSF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOamRemoteSF.setStatus(
        "current"
    )

almOamFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12294)
)
almOamFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOamFail.setStatus(
        "current"
    )

almCcLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12298)
)
almCcLoss.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almCcLoss.setStatus(
        "current"
    )

almMpConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12299)
)
almMpConflict.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almMpConflict.setStatus(
        "current"
    )

almLptRfi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12300)
)
almLptRfi.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLptRfi.setStatus(
        "current"
    )

almOamSelfLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12767)
)
almOamSelfLoop.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOamSelfLoop.setStatus(
        "current"
    )

almLagPortFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12769)
)
almLagPortFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLagPortFail.setStatus(
        "current"
    )

almEthCfmMismerge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12823)
)
almEthCfmMismerge.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEthCfmMismerge.setStatus(
        "current"
    )

almEthCfmUnexperi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12824)
)
almEthCfmUnexperi.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEthCfmUnexperi.setStatus(
        "current"
    )

almEthCfmLoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12825)
)
almEthCfmLoc.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEthCfmLoc.setStatus(
        "current"
    )

almEthCfmRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 12826)
)
almEthCfmRdi.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEthCfmRdi.setStatus(
        "current"
    )

almEqptNoServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32768)
)
almEqptNoServiceAffecting.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEqptNoServiceAffecting.setStatus(
        "current"
    )

almEqptServiceAffectingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32769)
)
almEqptServiceAffectingFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEqptServiceAffectingFail.setStatus(
        "current"
    )

almApsByteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32774)
)
almApsByteFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almApsByteFailure.setStatus(
        "current"
    )

almFarEndProtectionLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32776)
)
almFarEndProtectionLineFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFarEndProtectionLineFailure.setStatus(
        "current"
    )

almApsChannelMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32777)
)
almApsChannelMismatchFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almApsChannelMismatchFailure.setStatus(
        "current"
    )

almApsModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32778)
)
almApsModeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almApsModeMismatch.setStatus(
        "current"
    )

almApsTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32779)
)
almApsTypeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almApsTypeMismatch.setStatus(
        "current"
    )

almHoldoverSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32791)
)
almHoldoverSync.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almHoldoverSync.setStatus(
        "current"
    )

almFreeRunSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32792)
)
almFreeRunSync.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFreeRunSync.setStatus(
        "current"
    )

almFastStartSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32794)
)
almFastStartSync.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFastStartSync.setStatus(
        "current"
    )

almManualSetSSM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32798)
)
almManualSetSSM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almManualSetSSM.setStatus(
        "current"
    )

almFanOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32802)
)
almFanOffline.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFanOffline.setStatus(
        "current"
    )

almSingleFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32803)
)
almSingleFanFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSingleFanFail.setStatus(
        "current"
    )

almMultiFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32804)
)
almMultiFanFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almMultiFanFail.setStatus(
        "current"
    )

almEquipmentTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32807)
)
almEquipmentTypeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEquipmentTypeMismatch.setStatus(
        "current"
    )

almEquipmentOfflineOrUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32808)
)
almEquipmentOfflineOrUninstalled.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEquipmentOfflineOrUninstalled.setStatus(
        "current"
    )

almTransmitterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32814)
)
almTransmitterFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTransmitterFailure.setStatus(
        "current"
    )

almSignalFailureSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32815)
)
almSignalFailureSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalFailureSection.setStatus(
        "current"
    )

almInputPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32816)
)
almInputPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInputPowerHigh.setStatus(
        "current"
    )

almInputPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32817)
)
almInputPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInputPowerLow.setStatus(
        "current"
    )

almSignalFailureLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32818)
)
almSignalFailureLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalFailureLine.setStatus(
        "current"
    )

almSignalDegradeLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32819)
)
almSignalDegradeLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalDegradeLine.setStatus(
        "current"
    )

almLaserApprochingEndOfLife = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32820)
)
almLaserApprochingEndOfLife.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserApprochingEndOfLife.setStatus(
        "current"
    )

almOutPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32821)
)
almOutPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOutPowerHigh.setStatus(
        "current"
    )

almOutPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32822)
)
almOutPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOutPowerLow.setStatus(
        "current"
    )

almSignalDegradeSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32823)
)
almSignalDegradeSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalDegradeSection.setStatus(
        "current"
    )

almAlarmIndicationSignalLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32824)
)
almAlarmIndicationSignalLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAlarmIndicationSignalLine.setStatus(
        "current"
    )

almRemoteFailureIindicationLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32825)
)
almRemoteFailureIindicationLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRemoteFailureIindicationLine.setStatus(
        "current"
    )

almAlarmIndicationSignalPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32826)
)
almAlarmIndicationSignalPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAlarmIndicationSignalPath.setStatus(
        "current"
    )

almLossOfPointerPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32827)
)
almLossOfPointerPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLossOfPointerPath.setStatus(
        "current"
    )

almTraceIdentifierMismatchPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32828)
)
almTraceIdentifierMismatchPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTraceIdentifierMismatchPath.setStatus(
        "current"
    )

almUnequippedPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32829)
)
almUnequippedPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almUnequippedPath.setStatus(
        "current"
    )

almSignalFailurePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32830)
)
almSignalFailurePath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalFailurePath.setStatus(
        "current"
    )

almSignalDegradePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32831)
)
almSignalDegradePath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalDegradePath.setStatus(
        "current"
    )

almRemoteFailureIindicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32832)
)
almRemoteFailureIindicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRemoteFailureIindicationPath.setStatus(
        "current"
    )

almALS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32833)
)
almALS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almALS.setStatus(
        "current"
    )

almLoopbackFacility = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32834)
)
almLoopbackFacility.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackFacility.setStatus(
        "current"
    )

almLoopbackTerminal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32835)
)
almLoopbackTerminal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackTerminal.setStatus(
        "current"
    )

almPayloadLabelMisatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32836)
)
almPayloadLabelMisatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPayloadLabelMisatch.setStatus(
        "current"
    )

almEnhancedRemotePalyloadFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32837)
)
almEnhancedRemotePalyloadFailureIndicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEnhancedRemotePalyloadFailureIndicationPath.setStatus(
        "current"
    )

almEnhancedRemoteServerFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32838)
)
almEnhancedRemoteServerFailureIndicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEnhancedRemoteServerFailureIndicationPath.setStatus(
        "current"
    )

almEnhancedRemoteConnectivityFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32839)
)
almEnhancedRemoteConnectivityFailureIndicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEnhancedRemoteConnectivityFailureIndicationPath.setStatus(
        "current"
    )

almPDIPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32840)
)
almPDIPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPDIPath.setStatus(
        "current"
    )

almPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32841)
)
almPowerFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPowerFail.setStatus(
        "current"
    )

almLossOfPointerVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32842)
)
almLossOfPointerVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLossOfPointerVT.setStatus(
        "current"
    )

almAlarmIndicationSignalVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32843)
)
almAlarmIndicationSignalVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAlarmIndicationSignalVT.setStatus(
        "current"
    )

almPayloadLabelMismatchVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32844)
)
almPayloadLabelMismatchVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPayloadLabelMismatchVT.setStatus(
        "current"
    )

almUnequippedVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32845)
)
almUnequippedVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almUnequippedVT.setStatus(
        "current"
    )

almRemoteFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32846)
)
almRemoteFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRemoteFailureIndicationVT.setStatus(
        "current"
    )

almRemoteServerFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32847)
)
almRemoteServerFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRemoteServerFailureIndicationVT.setStatus(
        "current"
    )

almEnhancedRemoteConnectivityFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32848)
)
almEnhancedRemoteConnectivityFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEnhancedRemoteConnectivityFailureIndicationVT.setStatus(
        "current"
    )

almEnhancedRemotePalyloadFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32849)
)
almEnhancedRemotePalyloadFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almEnhancedRemotePalyloadFailureIndicationVT.setStatus(
        "current"
    )

almInterFaceCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32876)
)
almInterFaceCardOffline.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInterFaceCardOffline.setStatus(
        "current"
    )

almSyncChangeSSM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32877)
)
almSyncChangeSSM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSyncChangeSSM.setStatus(
        "current"
    )

almTimeingModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32878)
)
almTimeingModeChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTimeingModeChange.setStatus(
        "current"
    )

almLockoutWorkingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32879)
)
almLockoutWorkingUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutWorkingUnit.setStatus(
        "current"
    )

almLockoutProtectionUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32880)
)
almLockoutProtectionUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutProtectionUnit.setStatus(
        "current"
    )

almForcedSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32881)
)
almForcedSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almForcedSwitch.setStatus(
        "current"
    )

almManualSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32882)
)
almManualSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almManualSwitch.setStatus(
        "current"
    )

almExerciseSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32883)
)
almExerciseSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExerciseSwitch.setStatus(
        "current"
    )

almWaitToRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32884)
)
almWaitToRestore.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almWaitToRestore.setStatus(
        "current"
    )

almSwitchToIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32886)
)
almSwitchToIdle.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwitchToIdle.setStatus(
        "current"
    )

almSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32887)
)
almSwitchFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwitchFail.setStatus(
        "current"
    )

almSyncSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32889)
)
almSyncSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSyncSwitch.setStatus(
        "current"
    )

almCommunicationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32890)
)
almCommunicationFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almCommunicationFail.setStatus(
        "current"
    )

almPowerAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32891)
)
almPowerAFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPowerAFail.setStatus(
        "current"
    )

almPowerBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32892)
)
almPowerBFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPowerBFail.setStatus(
        "current"
    )

almInterfaceLinkMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32899)
)
almInterfaceLinkMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInterfaceLinkMismatch.setStatus(
        "current"
    )

almInterfaceCardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32900)
)
almInterfaceCardFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInterfaceCardFail.setStatus(
        "current"
    )

almAIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32901)
)
almAIC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAIC.setStatus(
        "current"
    )

almDbmsCfgCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32903)
)
almDbmsCfgCorrupted.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDbmsCfgCorrupted.setStatus(
        "current"
    )

almDefaultKByteDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32904)
)
almDefaultKByteDefect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDefaultKByteDefect.setStatus(
        "current"
    )

almInconsistentApsCodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32905)
)
almInconsistentApsCodes.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInconsistentApsCodes.setStatus(
        "current"
    )

almImproperApsCodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32906)
)
almImproperApsCodes.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almImproperApsCodes.setStatus(
        "current"
    )

almExtraTrafficIsBeingSquelched = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32907)
)
almExtraTrafficIsBeingSquelched.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExtraTrafficIsBeingSquelched.setStatus(
        "current"
    )

almTopologyNeedsUpdatingOrIsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32908)
)
almTopologyNeedsUpdatingOrIsInvalid.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTopologyNeedsUpdatingOrIsInvalid.setStatus(
        "current"
    )

almSquelchTableNeedsUpdatingOrIsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32909)
)
almSquelchTableNeedsUpdatingOrIsInvalid.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSquelchTableNeedsUpdatingOrIsInvalid.setStatus(
        "current"
    )

almNodeIdDuplicatedOrMismatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32910)
)
almNodeIdDuplicatedOrMismatched.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almNodeIdDuplicatedOrMismatched.setStatus(
        "current"
    )

almXconMismatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32911)
)
almXconMismatched.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almXconMismatched.setStatus(
        "current"
    )

almRingModeMisatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32912)
)
almRingModeMisatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRingModeMisatch.setStatus(
        "current"
    )

almSquelchModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32913)
)
almSquelchModeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSquelchModeMismatch.setStatus(
        "current"
    )

almLockoutProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32915)
)
almLockoutProtectionSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutProtectionSpan.setStatus(
        "current"
    )

almLockoutWorkingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32916)
)
almLockoutWorkingRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutWorkingRing.setStatus(
        "current"
    )

almLockoutWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32917)
)
almLockoutWorkingSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutWorkingSpan.setStatus(
        "current"
    )

almForceSwitchOfRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32918)
)
almForceSwitchOfRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almForceSwitchOfRing.setStatus(
        "current"
    )

almForceSwitchOfSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32919)
)
almForceSwitchOfSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almForceSwitchOfSpan.setStatus(
        "current"
    )

almManualSwitchOfRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32920)
)
almManualSwitchOfRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almManualSwitchOfRing.setStatus(
        "current"
    )

almManualSwitchOfSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32921)
)
almManualSwitchOfSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almManualSwitchOfSpan.setStatus(
        "current"
    )

almExerciseSwitchRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32922)
)
almExerciseSwitchRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExerciseSwitchRing.setStatus(
        "current"
    )

almExerciseSwitchSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32923)
)
almExerciseSwitchSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExerciseSwitchSpan.setStatus(
        "current"
    )

almLockoutProtectionForAllSpans = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32924)
)
almLockoutProtectionForAllSpans.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutProtectionForAllSpans.setStatus(
        "current"
    )

almRingSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32925)
)
almRingSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRingSwitch.setStatus(
        "current"
    )

almSpanSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32926)
)
almSpanSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSpanSwitch.setStatus(
        "current"
    )

almSwitchToPassthru = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32927)
)
almSwitchToPassthru.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwitchToPassthru.setStatus(
        "current"
    )

almPersistentLineSquelching = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 32928)
)
almPersistentLineSquelching.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPersistentLineSquelching.setStatus(
        "current"
    )

almDbmsCfgBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33156)
)
almDbmsCfgBackupFailed.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDbmsCfgBackupFailed.setStatus(
        "current"
    )

almFanFailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33161)
)
almFanFailures.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFanFailures.setStatus(
        "current"
    )

almInvalidEQPT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33170)
)
almInvalidEQPT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almInvalidEQPT.setStatus(
        "current"
    )

almLaserApdBiasVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33171)
)
almLaserApdBiasVoltageHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserApdBiasVoltageHigh.setStatus(
        "current"
    )

almLaserApdBiasVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33172)
)
almLaserApdBiasVoltageLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserApdBiasVoltageLow.setStatus(
        "current"
    )

almLBCHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33174)
)
almLBCHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLBCHigh.setStatus(
        "current"
    )

almLBCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33175)
)
almLBCLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLBCLow.setStatus(
        "current"
    )

almLCCHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33176)
)
almLCCHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLCCHigh.setStatus(
        "current"
    )

almLCCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33177)
)
almLCCLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLCCLow.setStatus(
        "current"
    )

almLinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33280)
)
almLinkError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLinkError.setStatus(
        "current"
    )

almLOA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33281)
)
almLOA.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLOA.setStatus(
        "current"
    )

almLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33282)
)
almLOF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLOF.setStatus(
        "current"
    )

almLOMPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33283)
)
almLOMPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLOMPath.setStatus(
        "current"
    )

almLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33284)
)
almLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLOS.setStatus(
        "current"
    )

almLaserTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33286)
)
almLaserTemperatureHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserTemperatureHigh.setStatus(
        "current"
    )

almLaserTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33287)
)
almLaserTemperatureLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserTemperatureLow.setStatus(
        "current"
    )

almNeBdDataMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33289)
)
almNeBdDataMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almNeBdDataMismatch.setStatus(
        "current"
    )

almNoLaserParameter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33298)
)
almNoLaserParameter.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almNoLaserParameter.setStatus(
        "current"
    )

almSyncReferenceSourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33301)
)
almSyncReferenceSourceFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSyncReferenceSourceFailure.setStatus(
        "current"
    )

almSignalDegradeVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33304)
)
almSignalDegradeVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalDegradeVT.setStatus(
        "current"
    )

almSignalFailureVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33305)
)
almSignalFailureVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSignalFailureVT.setStatus(
        "current"
    )

almSequenceNumberMismatchedVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33312)
)
almSequenceNumberMismatchedVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSequenceNumberMismatchedVT.setStatus(
        "current"
    )

almSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33314)
)
almSoftwareVersionMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSoftwareVersionMismatch.setStatus(
        "current"
    )

almTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33315)
)
almTemperatureHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTemperatureHigh.setStatus(
        "current"
    )

almAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33316)
)
almAIS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAIS.setStatus(
        "current"
    )

almLoopbackInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33330)
)
almLoopbackInhibited.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackInhibited.setStatus(
        "current"
    )

almLockoutOfTheProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33331)
)
almLockoutOfTheProtocol.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLockoutOfTheProtocol.setStatus(
        "current"
    )

almLaserShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33332)
)
almLaserShutDown.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserShutDown.setStatus(
        "current"
    )

almLoopbackAllDS1FEAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33333)
)
almLoopbackAllDS1FEAC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackAllDS1FEAC.setStatus(
        "current"
    )

almLoopbackCrossConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33335)
)
almLoopbackCrossConnect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackCrossConnect.setStatus(
        "current"
    )

almLoopbackDS1FEAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33336)
)
almLoopbackDS1FEAC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackDS1FEAC.setStatus(
        "current"
    )

almLoopbackDS3FEAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33337)
)
almLoopbackDS3FEAC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackDS3FEAC.setStatus(
        "current"
    )

almLoopbackFacilityPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33345)
)
almLoopbackFacilityPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackFacilityPath.setStatus(
        "current"
    )

almLoopbackTerminalPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33347)
)
almLoopbackTerminalPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackTerminalPath.setStatus(
        "current"
    )

almPrimaryChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33348)
)
almPrimaryChannelChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPrimaryChannelChange.setStatus(
        "current"
    )

almRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33349)
)
almRAI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRAI.setStatus(
        "current"
    )

almSsmDQL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33350)
)
almSsmDQL.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSsmDQL.setStatus(
        "current"
    )

almSsmLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33351)
)
almSsmLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSsmLOS.setStatus(
        "current"
    )

almTestSessionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33361)
)
almTestSessionActive.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTestSessionActive.setStatus(
        "current"
    )

almNormalSyncMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33363)
)
almNormalSyncMode.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almNormalSyncMode.setStatus(
        "current"
    )

almSwitchProtectionToWorkingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33364)
)
almSwitchProtectionToWorkingUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwitchProtectionToWorkingUnit.setStatus(
        "current"
    )

almSwtichWokingToProtectingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33365)
)
almSwtichWokingToProtectingUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSwtichWokingToProtectingUnit.setStatus(
        "current"
    )

almATECardOfflineOrUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33368)
)
almATECardOfflineOrUninstalled.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almATECardOfflineOrUninstalled.setStatus(
        "current"
    )

almPIUCardOfflineOrUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33370)
)
almPIUCardOfflineOrUninstalled.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPIUCardOfflineOrUninstalled.setStatus(
        "current"
    )

almOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33372)
)
almOOF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almOOF.setStatus(
        "current"
    )

almExerciseSwitchSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33373)
)
almExerciseSwitchSuccess.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExerciseSwitchSuccess.setStatus(
        "current"
    )

almExerciseSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33374)
)
almExerciseSwitchFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almExerciseSwitchFail.setStatus(
        "current"
    )

almUpgradeInProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33375)
)
almUpgradeInProcess.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almUpgradeInProcess.setStatus(
        "current"
    )

almChassisMea = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 33377)
)
almChassisMea.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almChassisMea.setStatus(
        "current"
    )

almLaserNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36923)
)
almLaserNotExist.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLaserNotExist.setStatus(
        "current"
    )

almLCASBandwidthReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36924)
)
almLCASBandwidthReduced.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLCASBandwidthReduced.setStatus(
        "current"
    )

almGFPLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36925)
)
almGFPLossOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almGFPLossOfFrame.setStatus(
        "current"
    )

almFanIsOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36926)
)
almFanIsOpened.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFanIsOpened.setStatus(
        "current"
    )

almFanIsClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36927)
)
almFanIsClosed.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFanIsClosed.setStatus(
        "current"
    )

almPathLevelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36928)
)
almPathLevelMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPathLevelMismatch.setStatus(
        "current"
    )

almTcaCVLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36930)
)
almTcaCVLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaCVLine.setStatus(
        "current"
    )

almDCCFailureIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36936)
)
almDCCFailureIndication.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDCCFailureIndication.setStatus(
        "current"
    )

almLanLossOfCarrierSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36937)
)
almLanLossOfCarrierSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLanLossOfCarrierSignal.setStatus(
        "current"
    )

almTcaCVCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36938)
)
almTcaCVCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaCVCPPath.setStatus(
        "current"
    )

almTcaCVPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36939)
)
almTcaCVPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaCVPath.setStatus(
        "current"
    )

almTcaCVPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36940)
)
almTcaCVPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaCVPPath.setStatus(
        "current"
    )

almTcaCVSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36941)
)
almTcaCVSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaCVSection.setStatus(
        "current"
    )

almTcaCVVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36942)
)
almTcaCVVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaCVVT.setStatus(
        "current"
    )

almTcaESCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36943)
)
almTcaESCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaESCPPath.setStatus(
        "current"
    )

almTcaESLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36944)
)
almTcaESLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaESLine.setStatus(
        "current"
    )

almTcaESPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36945)
)
almTcaESPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaESPath.setStatus(
        "current"
    )

almTcaESPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36946)
)
almTcaESPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaESPPath.setStatus(
        "current"
    )

almTcaESSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36947)
)
almTcaESSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaESSection.setStatus(
        "current"
    )

almTcaESVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36948)
)
almTcaESVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaESVT.setStatus(
        "current"
    )

almTcaPjcsPdet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36949)
)
almTcaPjcsPdet.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaPjcsPdet.setStatus(
        "current"
    )

almTcaPjcsVdet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36950)
)
almTcaPjcsVdet.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaPjcsVdet.setStatus(
        "current"
    )

almTcaSESCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36951)
)
almTcaSESCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaSESCPPath.setStatus(
        "current"
    )

almTcaSESLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36952)
)
almTcaSESLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaSESLine.setStatus(
        "current"
    )

almTcaSESPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36953)
)
almTcaSESPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaSESPath.setStatus(
        "current"
    )

almTcaSESPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36954)
)
almTcaSESPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaSESPPath.setStatus(
        "current"
    )

almTcaSESSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36955)
)
almTcaSESSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaSESSection.setStatus(
        "current"
    )

almTcaSESVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36956)
)
almTcaSESVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaSESVT.setStatus(
        "current"
    )

almTcaUASCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36957)
)
almTcaUASCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaUASCPPath.setStatus(
        "current"
    )

almTcaUASLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36958)
)
almTcaUASLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaUASLine.setStatus(
        "current"
    )

almTcaUASPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36959)
)
almTcaUASPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaUASPath.setStatus(
        "current"
    )

almTcaUASPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36960)
)
almTcaUASPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaUASPPath.setStatus(
        "current"
    )

almTcaUASVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36961)
)
almTcaUASVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almTcaUASVT.setStatus(
        "current"
    )

almBitsAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36966)
)
almBitsAIS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBitsAIS.setStatus(
        "current"
    )

almBitsLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36967)
)
almBitsLOF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBitsLOF.setStatus(
        "current"
    )

almBitsLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36968)
)
almBitsLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBitsLOS.setStatus(
        "current"
    )

almBitsCodeViolationOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36969)
)
almBitsCodeViolationOver.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBitsCodeViolationOver.setStatus(
        "current"
    )

almBlsrSFofRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36970)
)
almBlsrSFofRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBlsrSFofRing.setStatus(
        "current"
    )

almBlsrSFofSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36971)
)
almBlsrSFofSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBlsrSFofSpan.setStatus(
        "current"
    )

almBlsrSDofRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36972)
)
almBlsrSDofRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBlsrSDofRing.setStatus(
        "current"
    )

almBlsrSDofSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36973)
)
almBlsrSDofSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBlsrSDofSpan.setStatus(
        "current"
    )

almBlsrNodeIsolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36974)
)
almBlsrNodeIsolate.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almBlsrNodeIsolate.setStatus(
        "current"
    )

almSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36975)
)
almSF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSF.setStatus(
        "current"
    )

almSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36976)
)
almSD.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSD.setStatus(
        "current"
    )

almAutoSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36977)
)
almAutoSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almAutoSwitch.setStatus(
        "current"
    )

almLcasPlct = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36978)
)
almLcasPlct.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLcasPlct.setStatus(
        "current"
    )

almLcasPlcr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36979)
)
almLcasPlcr.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLcasPlcr.setStatus(
        "current"
    )

almLcasTlct = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36980)
)
almLcasTlct.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLcasTlct.setStatus(
        "current"
    )

almLcasTlcr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36981)
)
almLcasTlcr.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLcasTlcr.setStatus(
        "current"
    )

almLcasFopt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36985)
)
almLcasFopt.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLcasFopt.setStatus(
        "current"
    )

almLcasFopr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 36986)
)
almLcasFopr.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLcasFopr.setStatus(
        "current"
    )

almLoopbackFAC2NI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40960)
)
almLoopbackFAC2NI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLoopbackFAC2NI.setStatus(
        "current"
    )

almGfpCsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40961)
)
almGfpCsf.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almGfpCsf.setStatus(
        "current"
    )

almRevertiveModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40970)
)
almRevertiveModeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRevertiveModeMismatch.setStatus(
        "current"
    )

almRingIDMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40971)
)
almRingIDMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRingIDMismatch.setStatus(
        "current"
    )

almIncorrectFiberConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40972)
)
almIncorrectFiberConnection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almIncorrectFiberConnection.setStatus(
        "current"
    )

almStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40973)
)
almStateChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almStateChange.setStatus(
        "current"
    )

almMtMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40974)
)
almMtMode.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almMtMode.setStatus(
        "current"
    )

almRmvToMt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40979)
)
almRmvToMt.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRmvToMt.setStatus(
        "current"
    )

almRstFromMt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40980)
)
almRstFromMt.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRstFromMt.setStatus(
        "current"
    )

almLpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40981)
)
almLpbk.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLpbk.setStatus(
        "current"
    )

almRlsLpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40982)
)
almRlsLpbk.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRlsLpbk.setStatus(
        "current"
    )

almSyncNotSyncnronized = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40983)
)
almSyncNotSyncnronized.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSyncNotSyncnronized.setStatus(
        "current"
    )

almPowerExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40984)
)
almPowerExceed.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPowerExceed.setStatus(
        "current"
    )

almPartialUnprotected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40985)
)
almPartialUnprotected.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPartialUnprotected.setStatus(
        "current"
    )

almFanMea = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 40986)
)
almFanMea.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFanMea.setStatus(
        "current"
    )

almRemoteClientSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 63604)
)
almRemoteClientSF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRemoteClientSF.setStatus(
        "current"
    )

almRemoteClientSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 63605)
)
almRemoteClientSD.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almRemoteClientSD.setStatus(
        "current"
    )

almPowerSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 63607)
)
almPowerSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPowerSwitch.setStatus(
        "current"
    )

almPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 63629)
)
almPortOffline.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almPortOffline.setStatus(
        "current"
    )

almDataLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 63630)
)
almDataLost.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almDataLost.setStatus(
        "current"
    )

almSqmVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 65409)
)
almSqmVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almSqmVT.setStatus(
        "current"
    )

almLomVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 65410)
)
almLomVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almLomVT.setStatus(
        "current"
    )

almFCSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 10, 65411)
)
almFCSError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtNtfcnCde"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSrvEff"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    almFCSError.setStatus(
        "current"
    )

evtLossOfClock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 3)
)
evtLossOfClock.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLossOfClock.setStatus(
        "current"
    )

evtFileLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 6)
)
evtFileLost.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFileLost.setStatus(
        "current"
    )

evtREILine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 37)
)
evtREILine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtREILine.setStatus(
        "current"
    )

evtBiasTemperatureOfPumpHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 69)
)
evtBiasTemperatureOfPumpHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBiasTemperatureOfPumpHigh.setStatus(
        "current"
    )

evtTimSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 87)
)
evtTimSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTimSection.setStatus(
        "current"
    )

evtLossOfAllSynchronousSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 100)
)
evtLossOfAllSynchronousSource.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLossOfAllSynchronousSource.setStatus(
        "current"
    )

evtSynchronousSourceDegrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 101)
)
evtSynchronousSourceDegrade.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSynchronousSourceDegrade.setStatus(
        "current"
    )

evtSyncLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 111)
)
evtSyncLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSyncLOS.setStatus(
        "current"
    )

evtProtectionSwitching = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 120)
)
evtProtectionSwitching.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtProtectionSwitching.setStatus(
        "current"
    )

evtDbmsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 185)
)
evtDbmsError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDbmsError.setStatus(
        "current"
    )

evtLossOfMultiplexSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 186)
)
evtLossOfMultiplexSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLossOfMultiplexSignal.setStatus(
        "current"
    )

evtLossOfSingleWavelengthSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 187)
)
evtLossOfSingleWavelengthSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLossOfSingleWavelengthSignal.setStatus(
        "current"
    )

evtAdditionOfSingleWavelengthSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 188)
)
evtAdditionOfSingleWavelengthSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAdditionOfSingleWavelengthSignal.setStatus(
        "current"
    )

evtLaserDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 189)
)
evtLaserDegraded.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserDegraded.setStatus(
        "current"
    )

evtPumpDiodeCoolingCurrentHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 192)
)
evtPumpDiodeCoolingCurrentHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPumpDiodeCoolingCurrentHigh.setStatus(
        "current"
    )

evtS1ModeSynChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 193)
)
evtS1ModeSynChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtS1ModeSynChange.setStatus(
        "current"
    )

evtDbmsIsInProtectMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 198)
)
evtDbmsIsInProtectMode.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDbmsIsInProtectMode.setStatus(
        "current"
    )

evtSecuAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 200)
)
evtSecuAlarm.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSecuAlarm.setStatus(
        "current"
    )

evtForwardErrorCorrectionLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 212)
)
evtForwardErrorCorrectionLossOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtForwardErrorCorrectionLossOfFrame.setStatus(
        "current"
    )

evtForwardErrorCorrectionOutOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 213)
)
evtForwardErrorCorrectionOutOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtForwardErrorCorrectionOutOfFrame.setStatus(
        "current"
    )

evtRateOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 223)
)
evtRateOver.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRateOver.setStatus(
        "current"
    )

evtCardConfigurationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 232)
)
evtCardConfigurationFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtCardConfigurationFail.setStatus(
        "current"
    )

evtLoopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 240)
)
evtLoopback.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopback.setStatus(
        "current"
    )

evtCoolingCurrentModeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 270)
)
evtCoolingCurrentModeHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtCoolingCurrentModeHigh.setStatus(
        "current"
    )

evtOTULossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 272)
)
evtOTULossOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOTULossOfFrame.setStatus(
        "current"
    )

evtOTUOutOfMultiFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 273)
)
evtOTUOutOfMultiFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOTUOutOfMultiFrame.setStatus(
        "current"
    )

evtSmTIM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 274)
)
evtSmTIM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSmTIM.setStatus(
        "current"
    )

evtPmTIM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 275)
)
evtPmTIM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPmTIM.setStatus(
        "current"
    )

evtSmBDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 276)
)
evtSmBDI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSmBDI.setStatus(
        "current"
    )

evtPmBDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 277)
)
evtPmBDI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPmBDI.setStatus(
        "current"
    )

evtSmBEI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 278)
)
evtSmBEI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSmBEI.setStatus(
        "current"
    )

evtPmBEI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 279)
)
evtPmBEI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPmBEI.setStatus(
        "current"
    )

evtSmIAE = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 280)
)
evtSmIAE.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSmIAE.setStatus(
        "current"
    )

evtSmBipExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 282)
)
evtSmBipExcessive.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSmBipExcessive.setStatus(
        "current"
    )

evtPmBipExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 283)
)
evtPmBipExcessive.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPmBipExcessive.setStatus(
        "current"
    )

evtSmBipSignalDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 284)
)
evtSmBipSignalDefect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSmBipSignalDefect.setStatus(
        "current"
    )

evtPmBipSignalDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 285)
)
evtPmBipSignalDefect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPmBipSignalDefect.setStatus(
        "current"
    )

evtOTUAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 286)
)
evtOTUAlarmIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOTUAlarmIndicationSignal.setStatus(
        "current"
    )

evtODUAlarmIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 287)
)
evtODUAlarmIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtODUAlarmIndicationSignal.setStatus(
        "current"
    )

evtODUOpenConnectionIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 288)
)
evtODUOpenConnectionIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtODUOpenConnectionIndicationSignal.setStatus(
        "current"
    )

evtODULockedIndicationSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 289)
)
evtODULockedIndicationSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtODULockedIndicationSignal.setStatus(
        "current"
    )

evtSumInputOpticalPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 323)
)
evtSumInputOpticalPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSumInputOpticalPowerHigh.setStatus(
        "current"
    )

evtSumInputOpticalPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 324)
)
evtSumInputOpticalPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSumInputOpticalPowerLow.setStatus(
        "current"
    )

evtSumOutOpticalPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 325)
)
evtSumOutOpticalPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSumOutOpticalPowerHigh.setStatus(
        "current"
    )

evtOutOpticalPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 326)
)
evtOutOpticalPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOutOpticalPowerLow.setStatus(
        "current"
    )

evtGainLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 327)
)
evtGainLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtGainLow.setStatus(
        "current"
    )

evtExcessiveErrorDefectBeforeFEC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 335)
)
evtExcessiveErrorDefectBeforeFEC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExcessiveErrorDefectBeforeFEC.setStatus(
        "current"
    )

evtDgeAdjustmentFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 433)
)
evtDgeAdjustmentFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDgeAdjustmentFail.setStatus(
        "current"
    )

evtWavelengthLockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 439)
)
evtWavelengthLockFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtWavelengthLockFail.setStatus(
        "current"
    )

evtHotSwitchControlUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 440)
)
evtHotSwitchControlUnavail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtHotSwitchControlUnavail.setStatus(
        "current"
    )

evtEsconCodeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 570)
)
evtEsconCodeError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEsconCodeError.setStatus(
        "current"
    )

evtCommitTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 573)
)
evtCommitTimeout.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtCommitTimeout.setStatus(
        "current"
    )

evtSwdlNePackageCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 574)
)
evtSwdlNePackageCheck.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwdlNePackageCheck.setStatus(
        "current"
    )

evtSwdlChaGmngmMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 575)
)
evtSwdlChaGmngmMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwdlChaGmngmMismatch.setStatus(
        "current"
    )

evtDBSyncFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 591)
)
evtDBSyncFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDBSyncFail.setStatus(
        "current"
    )

evtClientMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 604)
)
evtClientMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtClientMismatch.setStatus(
        "current"
    )

evtLaserModuleMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 606)
)
evtLaserModuleMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserModuleMismatch.setStatus(
        "current"
    )

evtLptRfi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 12300)
)
evtLptRfi.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLptRfi.setStatus(
        "current"
    )

evtEqptNoServiceAffecting = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32768)
)
evtEqptNoServiceAffecting.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEqptNoServiceAffecting.setStatus(
        "current"
    )

evtEqptServiceAffectingFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32769)
)
evtEqptServiceAffectingFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEqptServiceAffectingFail.setStatus(
        "current"
    )

evtApsByteFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32774)
)
evtApsByteFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtApsByteFailure.setStatus(
        "current"
    )

evtFarEndProtectionLineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32776)
)
evtFarEndProtectionLineFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFarEndProtectionLineFailure.setStatus(
        "current"
    )

evtApsChannelMismatchFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32777)
)
evtApsChannelMismatchFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtApsChannelMismatchFailure.setStatus(
        "current"
    )

evtApsModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32778)
)
evtApsModeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtApsModeMismatch.setStatus(
        "current"
    )

evtApsTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32779)
)
evtApsTypeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtApsTypeMismatch.setStatus(
        "current"
    )

evtHoldoverSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32791)
)
evtHoldoverSync.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtHoldoverSync.setStatus(
        "current"
    )

evtFreeRunSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32792)
)
evtFreeRunSync.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFreeRunSync.setStatus(
        "current"
    )

evtFastStartSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32794)
)
evtFastStartSync.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFastStartSync.setStatus(
        "current"
    )

evtManualSetSSM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32798)
)
evtManualSetSSM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtManualSetSSM.setStatus(
        "current"
    )

evtFanOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32802)
)
evtFanOffline.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFanOffline.setStatus(
        "current"
    )

evtSingleFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32803)
)
evtSingleFanFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSingleFanFail.setStatus(
        "current"
    )

evtMultiFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32804)
)
evtMultiFanFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtMultiFanFail.setStatus(
        "current"
    )

evtEquipmentTypeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32807)
)
evtEquipmentTypeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEquipmentTypeMismatch.setStatus(
        "current"
    )

evtEquipmentOfflineOrUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32808)
)
evtEquipmentOfflineOrUninstalled.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEquipmentOfflineOrUninstalled.setStatus(
        "current"
    )

evtTransmitterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32814)
)
evtTransmitterFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTransmitterFailure.setStatus(
        "current"
    )

evtSignalFailureSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32815)
)
evtSignalFailureSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalFailureSection.setStatus(
        "current"
    )

evtInputPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32816)
)
evtInputPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInputPowerHigh.setStatus(
        "current"
    )

evtInputPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32817)
)
evtInputPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInputPowerLow.setStatus(
        "current"
    )

evtSignalFailureLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32818)
)
evtSignalFailureLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalFailureLine.setStatus(
        "current"
    )

evtSignalDegradeLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32819)
)
evtSignalDegradeLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalDegradeLine.setStatus(
        "current"
    )

evtLaserApprochingEndOfLife = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32820)
)
evtLaserApprochingEndOfLife.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserApprochingEndOfLife.setStatus(
        "current"
    )

evtOutPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32821)
)
evtOutPowerHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOutPowerHigh.setStatus(
        "current"
    )

evtOutPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32822)
)
evtOutPowerLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOutPowerLow.setStatus(
        "current"
    )

evtSignalDegradeSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32823)
)
evtSignalDegradeSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalDegradeSection.setStatus(
        "current"
    )

evtAlarmIndicationSignalLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32824)
)
evtAlarmIndicationSignalLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAlarmIndicationSignalLine.setStatus(
        "current"
    )

evtRemoteFailureIindicationLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32825)
)
evtRemoteFailureIindicationLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRemoteFailureIindicationLine.setStatus(
        "current"
    )

evtAlarmIndicationSignalPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32826)
)
evtAlarmIndicationSignalPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAlarmIndicationSignalPath.setStatus(
        "current"
    )

evtLossOfPointerPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32827)
)
evtLossOfPointerPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLossOfPointerPath.setStatus(
        "current"
    )

evtTraceIdentifierMismatchPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32828)
)
evtTraceIdentifierMismatchPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTraceIdentifierMismatchPath.setStatus(
        "current"
    )

evtUnequippedPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32829)
)
evtUnequippedPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtUnequippedPath.setStatus(
        "current"
    )

evtSignalFailurePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32830)
)
evtSignalFailurePath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalFailurePath.setStatus(
        "current"
    )

evtSignalDegradePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32831)
)
evtSignalDegradePath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalDegradePath.setStatus(
        "current"
    )

evtRemoteFailureIindicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32832)
)
evtRemoteFailureIindicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRemoteFailureIindicationPath.setStatus(
        "current"
    )

evtALS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32833)
)
evtALS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtALS.setStatus(
        "current"
    )

evtLoopbackFacility = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32834)
)
evtLoopbackFacility.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackFacility.setStatus(
        "current"
    )

evtLoopbackTerminal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32835)
)
evtLoopbackTerminal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackTerminal.setStatus(
        "current"
    )

evtPayloadLabelMisatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32836)
)
evtPayloadLabelMisatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPayloadLabelMisatch.setStatus(
        "current"
    )

evtEnhancedRemotePalyloadFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32837)
)
evtEnhancedRemotePalyloadFailureIndicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEnhancedRemotePalyloadFailureIndicationPath.setStatus(
        "current"
    )

evtEnhancedRemoteServerFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32838)
)
evtEnhancedRemoteServerFailureIndicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEnhancedRemoteServerFailureIndicationPath.setStatus(
        "current"
    )

evtEnhancedRemoteConnectivityFailureIndicationPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32839)
)
evtEnhancedRemoteConnectivityFailureIndicationPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEnhancedRemoteConnectivityFailureIndicationPath.setStatus(
        "current"
    )

evtPDIPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32840)
)
evtPDIPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPDIPath.setStatus(
        "current"
    )

evtPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32841)
)
evtPowerFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPowerFail.setStatus(
        "current"
    )

evtLossOfPointerVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32842)
)
evtLossOfPointerVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLossOfPointerVT.setStatus(
        "current"
    )

evtAlarmIndicationSignalVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32843)
)
evtAlarmIndicationSignalVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAlarmIndicationSignalVT.setStatus(
        "current"
    )

evtPayloadLabelMismatchVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32844)
)
evtPayloadLabelMismatchVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPayloadLabelMismatchVT.setStatus(
        "current"
    )

evtUnequippedVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32845)
)
evtUnequippedVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtUnequippedVT.setStatus(
        "current"
    )

evtRemoteFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32846)
)
evtRemoteFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRemoteFailureIndicationVT.setStatus(
        "current"
    )

evtRemoteServerFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32847)
)
evtRemoteServerFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRemoteServerFailureIndicationVT.setStatus(
        "current"
    )

evtEnhancedRemoteConnectivityFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32848)
)
evtEnhancedRemoteConnectivityFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEnhancedRemoteConnectivityFailureIndicationVT.setStatus(
        "current"
    )

evtEnhancedRemotePalyloadFailureIndicationVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32849)
)
evtEnhancedRemotePalyloadFailureIndicationVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtEnhancedRemotePalyloadFailureIndicationVT.setStatus(
        "current"
    )

evtInterFaceCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32876)
)
evtInterFaceCardOffline.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInterFaceCardOffline.setStatus(
        "current"
    )

evtSyncChangeSSM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32877)
)
evtSyncChangeSSM.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSyncChangeSSM.setStatus(
        "current"
    )

evtTimeingModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32878)
)
evtTimeingModeChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTimeingModeChange.setStatus(
        "current"
    )

evtLockoutWorkingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32879)
)
evtLockoutWorkingUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutWorkingUnit.setStatus(
        "current"
    )

evtLockoutProtectionUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32880)
)
evtLockoutProtectionUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutProtectionUnit.setStatus(
        "current"
    )

evtForcedSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32881)
)
evtForcedSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtForcedSwitch.setStatus(
        "current"
    )

evtManualSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32882)
)
evtManualSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtManualSwitch.setStatus(
        "current"
    )

evtExerciseSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32883)
)
evtExerciseSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExerciseSwitch.setStatus(
        "current"
    )

evtWaitToRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32884)
)
evtWaitToRestore.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtWaitToRestore.setStatus(
        "current"
    )

evtSwitchToIdle = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32886)
)
evtSwitchToIdle.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwitchToIdle.setStatus(
        "current"
    )

evtSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32887)
)
evtSwitchFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwitchFail.setStatus(
        "current"
    )

evtSyncSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32889)
)
evtSyncSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSyncSwitch.setStatus(
        "current"
    )

evtCommunicationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32890)
)
evtCommunicationFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtCommunicationFail.setStatus(
        "current"
    )

evtPowerAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32891)
)
evtPowerAFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPowerAFail.setStatus(
        "current"
    )

evtPowerBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32892)
)
evtPowerBFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPowerBFail.setStatus(
        "current"
    )

evtInterfaceLinkMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32899)
)
evtInterfaceLinkMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInterfaceLinkMismatch.setStatus(
        "current"
    )

evtInterfaceCardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32900)
)
evtInterfaceCardFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInterfaceCardFail.setStatus(
        "current"
    )

evtAIC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32901)
)
evtAIC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAIC.setStatus(
        "current"
    )

evtDbmsCfgCorrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32903)
)
evtDbmsCfgCorrupted.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDbmsCfgCorrupted.setStatus(
        "current"
    )

evtDefaultKByteDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32904)
)
evtDefaultKByteDefect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDefaultKByteDefect.setStatus(
        "current"
    )

evtInconsistentApsCodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32905)
)
evtInconsistentApsCodes.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInconsistentApsCodes.setStatus(
        "current"
    )

evtImproperApsCodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32906)
)
evtImproperApsCodes.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtImproperApsCodes.setStatus(
        "current"
    )

evtExtraTrafficIsBeingSquelched = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32907)
)
evtExtraTrafficIsBeingSquelched.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExtraTrafficIsBeingSquelched.setStatus(
        "current"
    )

evtTopologyNeedsUpdatingOrIsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32908)
)
evtTopologyNeedsUpdatingOrIsInvalid.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTopologyNeedsUpdatingOrIsInvalid.setStatus(
        "current"
    )

evtSquelchTableNeedsUpdatingOrIsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32909)
)
evtSquelchTableNeedsUpdatingOrIsInvalid.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSquelchTableNeedsUpdatingOrIsInvalid.setStatus(
        "current"
    )

evtNodeIdDuplicatedOrMismatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32910)
)
evtNodeIdDuplicatedOrMismatched.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtNodeIdDuplicatedOrMismatched.setStatus(
        "current"
    )

evtXconMismatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32911)
)
evtXconMismatched.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtXconMismatched.setStatus(
        "current"
    )

evtRingModeMisatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32912)
)
evtRingModeMisatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRingModeMisatch.setStatus(
        "current"
    )

evtSquelchModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32913)
)
evtSquelchModeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSquelchModeMismatch.setStatus(
        "current"
    )

evtLockoutProtectionSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32915)
)
evtLockoutProtectionSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutProtectionSpan.setStatus(
        "current"
    )

evtLockoutWorkingRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32916)
)
evtLockoutWorkingRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutWorkingRing.setStatus(
        "current"
    )

evtLockoutWorkingSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32917)
)
evtLockoutWorkingSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutWorkingSpan.setStatus(
        "current"
    )

evtForceSwitchOfRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32918)
)
evtForceSwitchOfRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtForceSwitchOfRing.setStatus(
        "current"
    )

evtForceSwitchOfSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32919)
)
evtForceSwitchOfSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtForceSwitchOfSpan.setStatus(
        "current"
    )

evtManualSwitchOfRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32920)
)
evtManualSwitchOfRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtManualSwitchOfRing.setStatus(
        "current"
    )

evtManualSwitchOfSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32921)
)
evtManualSwitchOfSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtManualSwitchOfSpan.setStatus(
        "current"
    )

evtExerciseSwitchRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32922)
)
evtExerciseSwitchRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExerciseSwitchRing.setStatus(
        "current"
    )

evtExerciseSwitchSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32923)
)
evtExerciseSwitchSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExerciseSwitchSpan.setStatus(
        "current"
    )

evtLockoutProtectionForAllSpans = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32924)
)
evtLockoutProtectionForAllSpans.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutProtectionForAllSpans.setStatus(
        "current"
    )

evtRingSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32925)
)
evtRingSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRingSwitch.setStatus(
        "current"
    )

evtSpanSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32926)
)
evtSpanSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSpanSwitch.setStatus(
        "current"
    )

evtSwitchToPassthru = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32927)
)
evtSwitchToPassthru.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwitchToPassthru.setStatus(
        "current"
    )

evtPersistentLineSquelching = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 32928)
)
evtPersistentLineSquelching.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPersistentLineSquelching.setStatus(
        "current"
    )

evtDbmsCfgBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33156)
)
evtDbmsCfgBackupFailed.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDbmsCfgBackupFailed.setStatus(
        "current"
    )

evtFanFailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33161)
)
evtFanFailures.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFanFailures.setStatus(
        "current"
    )

evtInvalidEQPT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33170)
)
evtInvalidEQPT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtInvalidEQPT.setStatus(
        "current"
    )

evtLaserApdBiasVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33171)
)
evtLaserApdBiasVoltageHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserApdBiasVoltageHigh.setStatus(
        "current"
    )

evtLaserApdBiasVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33172)
)
evtLaserApdBiasVoltageLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserApdBiasVoltageLow.setStatus(
        "current"
    )

evtLBCHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33174)
)
evtLBCHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLBCHigh.setStatus(
        "current"
    )

evtLBCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33175)
)
evtLBCLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLBCLow.setStatus(
        "current"
    )

evtLCCHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33176)
)
evtLCCHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLCCHigh.setStatus(
        "current"
    )

evtLCCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33177)
)
evtLCCLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLCCLow.setStatus(
        "current"
    )

evtLinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33280)
)
evtLinkError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLinkError.setStatus(
        "current"
    )

evtLOA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33281)
)
evtLOA.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLOA.setStatus(
        "current"
    )

evtLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33282)
)
evtLOF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLOF.setStatus(
        "current"
    )

evtLOMPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33283)
)
evtLOMPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLOMPath.setStatus(
        "current"
    )

evtLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33284)
)
evtLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLOS.setStatus(
        "current"
    )

evtLaserTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33286)
)
evtLaserTemperatureHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserTemperatureHigh.setStatus(
        "current"
    )

evtLaserTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33287)
)
evtLaserTemperatureLow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserTemperatureLow.setStatus(
        "current"
    )

evtNeBdDataMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33289)
)
evtNeBdDataMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtNeBdDataMismatch.setStatus(
        "current"
    )

evtNoLaserParameter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33298)
)
evtNoLaserParameter.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtNoLaserParameter.setStatus(
        "current"
    )

evtSyncReferenceSourceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33301)
)
evtSyncReferenceSourceFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSyncReferenceSourceFailure.setStatus(
        "current"
    )

evtSignalDegradeVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33304)
)
evtSignalDegradeVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalDegradeVT.setStatus(
        "current"
    )

evtSignalFailureVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33305)
)
evtSignalFailureVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSignalFailureVT.setStatus(
        "current"
    )

evtSequenceNumberMismatchedVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33312)
)
evtSequenceNumberMismatchedVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSequenceNumberMismatchedVT.setStatus(
        "current"
    )

evtSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33314)
)
evtSoftwareVersionMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSoftwareVersionMismatch.setStatus(
        "current"
    )

evtTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33315)
)
evtTemperatureHigh.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTemperatureHigh.setStatus(
        "current"
    )

evtAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33316)
)
evtAIS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAIS.setStatus(
        "current"
    )

evtLoopbackInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33330)
)
evtLoopbackInhibited.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackInhibited.setStatus(
        "current"
    )

evtLockoutOfTheProtocol = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33331)
)
evtLockoutOfTheProtocol.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLockoutOfTheProtocol.setStatus(
        "current"
    )

evtLaserShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33332)
)
evtLaserShutDown.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserShutDown.setStatus(
        "current"
    )

evtLoopbackAllDS1FEAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33333)
)
evtLoopbackAllDS1FEAC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackAllDS1FEAC.setStatus(
        "current"
    )

evtLoopbackCrossConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33335)
)
evtLoopbackCrossConnect.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackCrossConnect.setStatus(
        "current"
    )

evtLoopbackDS1FEAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33336)
)
evtLoopbackDS1FEAC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackDS1FEAC.setStatus(
        "current"
    )

evtLoopbackDS3FEAC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33337)
)
evtLoopbackDS3FEAC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackDS3FEAC.setStatus(
        "current"
    )

evtLoopbackFacilityPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33345)
)
evtLoopbackFacilityPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackFacilityPath.setStatus(
        "current"
    )

evtLoopbackTerminalPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33347)
)
evtLoopbackTerminalPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackTerminalPath.setStatus(
        "current"
    )

evtPrimaryChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33348)
)
evtPrimaryChannelChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPrimaryChannelChange.setStatus(
        "current"
    )

evtRAI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33349)
)
evtRAI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRAI.setStatus(
        "current"
    )

evtSsmDQL = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33350)
)
evtSsmDQL.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSsmDQL.setStatus(
        "current"
    )

evtSsmLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33351)
)
evtSsmLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSsmLOS.setStatus(
        "current"
    )

evtTestSessionActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33361)
)
evtTestSessionActive.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTestSessionActive.setStatus(
        "current"
    )

evtNormalSyncMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33363)
)
evtNormalSyncMode.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtNormalSyncMode.setStatus(
        "current"
    )

evtSwitchProtectionToWorkingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33364)
)
evtSwitchProtectionToWorkingUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwitchProtectionToWorkingUnit.setStatus(
        "current"
    )

evtSwtichWokingToProtectingUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33365)
)
evtSwtichWokingToProtectingUnit.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSwtichWokingToProtectingUnit.setStatus(
        "current"
    )

evtATECardOfflineOrUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33368)
)
evtATECardOfflineOrUninstalled.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtATECardOfflineOrUninstalled.setStatus(
        "current"
    )

evtPIUCardOfflineOrUninstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33370)
)
evtPIUCardOfflineOrUninstalled.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPIUCardOfflineOrUninstalled.setStatus(
        "current"
    )

evtOOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33372)
)
evtOOF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtOOF.setStatus(
        "current"
    )

evtExerciseSwitchSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33373)
)
evtExerciseSwitchSuccess.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExerciseSwitchSuccess.setStatus(
        "current"
    )

evtExerciseSwitchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33374)
)
evtExerciseSwitchFail.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtExerciseSwitchFail.setStatus(
        "current"
    )

evtUpgradeInProcess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33375)
)
evtUpgradeInProcess.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtUpgradeInProcess.setStatus(
        "current"
    )

evtChassisMea = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 33377)
)
evtChassisMea.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtChassisMea.setStatus(
        "current"
    )

evtLaserNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36923)
)
evtLaserNotExist.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLaserNotExist.setStatus(
        "current"
    )

evtLCASBandwidthReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36924)
)
evtLCASBandwidthReduced.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLCASBandwidthReduced.setStatus(
        "current"
    )

evtGFPLossOfFrame = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36925)
)
evtGFPLossOfFrame.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtGFPLossOfFrame.setStatus(
        "current"
    )

evtFanIsOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36926)
)
evtFanIsOpened.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFanIsOpened.setStatus(
        "current"
    )

evtFanIsClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36927)
)
evtFanIsClosed.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFanIsClosed.setStatus(
        "current"
    )

evtPathLevelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36928)
)
evtPathLevelMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPathLevelMismatch.setStatus(
        "current"
    )

evtTcaCVLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36930)
)
evtTcaCVLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaCVLine.setStatus(
        "current"
    )

evtDCCFailureIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36936)
)
evtDCCFailureIndication.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDCCFailureIndication.setStatus(
        "current"
    )

evtLanLossOfCarrierSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36937)
)
evtLanLossOfCarrierSignal.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLanLossOfCarrierSignal.setStatus(
        "current"
    )

evtTcaCVCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36938)
)
evtTcaCVCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaCVCPPath.setStatus(
        "current"
    )

evtTcaCVPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36939)
)
evtTcaCVPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaCVPath.setStatus(
        "current"
    )

evtTcaCVPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36940)
)
evtTcaCVPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaCVPPath.setStatus(
        "current"
    )

evtTcaCVSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36941)
)
evtTcaCVSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaCVSection.setStatus(
        "current"
    )

evtTcaCVVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36942)
)
evtTcaCVVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaCVVT.setStatus(
        "current"
    )

evtTcaESCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36943)
)
evtTcaESCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaESCPPath.setStatus(
        "current"
    )

evtTcaESLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36944)
)
evtTcaESLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaESLine.setStatus(
        "current"
    )

evtTcaESPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36945)
)
evtTcaESPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaESPath.setStatus(
        "current"
    )

evtTcaESPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36946)
)
evtTcaESPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaESPPath.setStatus(
        "current"
    )

evtTcaESSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36947)
)
evtTcaESSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaESSection.setStatus(
        "current"
    )

evtTcaESVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36948)
)
evtTcaESVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaESVT.setStatus(
        "current"
    )

evtTcaPjcsPdet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36949)
)
evtTcaPjcsPdet.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaPjcsPdet.setStatus(
        "current"
    )

evtTcaPjcsVdet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36950)
)
evtTcaPjcsVdet.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaPjcsVdet.setStatus(
        "current"
    )

evtTcaSESCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36951)
)
evtTcaSESCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaSESCPPath.setStatus(
        "current"
    )

evtTcaSESLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36952)
)
evtTcaSESLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaSESLine.setStatus(
        "current"
    )

evtTcaSESPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36953)
)
evtTcaSESPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaSESPath.setStatus(
        "current"
    )

evtTcaSESPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36954)
)
evtTcaSESPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaSESPPath.setStatus(
        "current"
    )

evtTcaSESSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36955)
)
evtTcaSESSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaSESSection.setStatus(
        "current"
    )

evtTcaSESVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36956)
)
evtTcaSESVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaSESVT.setStatus(
        "current"
    )

evtTcaUASCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36957)
)
evtTcaUASCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaUASCPPath.setStatus(
        "current"
    )

evtTcaUASLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36958)
)
evtTcaUASLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaUASLine.setStatus(
        "current"
    )

evtTcaUASPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36959)
)
evtTcaUASPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaUASPath.setStatus(
        "current"
    )

evtTcaUASPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36960)
)
evtTcaUASPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaUASPPath.setStatus(
        "current"
    )

evtTcaUASVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36961)
)
evtTcaUASVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtTcaUASVT.setStatus(
        "current"
    )

evtBitsAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36966)
)
evtBitsAIS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBitsAIS.setStatus(
        "current"
    )

evtBitsLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36967)
)
evtBitsLOF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBitsLOF.setStatus(
        "current"
    )

evtBitsLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36968)
)
evtBitsLOS.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBitsLOS.setStatus(
        "current"
    )

evtBitsCodeViolationOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36969)
)
evtBitsCodeViolationOver.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBitsCodeViolationOver.setStatus(
        "current"
    )

evtBlsrSFofRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36970)
)
evtBlsrSFofRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBlsrSFofRing.setStatus(
        "current"
    )

evtBlsrSFofSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36971)
)
evtBlsrSFofSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBlsrSFofSpan.setStatus(
        "current"
    )

evtBlsrSDofRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36972)
)
evtBlsrSDofRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBlsrSDofRing.setStatus(
        "current"
    )

evtBlsrSDofSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36973)
)
evtBlsrSDofSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBlsrSDofSpan.setStatus(
        "current"
    )

evtBlsrNodeIsolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36974)
)
evtBlsrNodeIsolate.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtBlsrNodeIsolate.setStatus(
        "current"
    )

evtSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36975)
)
evtSF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSF.setStatus(
        "current"
    )

evtSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36976)
)
evtSD.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSD.setStatus(
        "current"
    )

evtAutoSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36977)
)
evtAutoSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtAutoSwitch.setStatus(
        "current"
    )

evtLcasPlct = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36978)
)
evtLcasPlct.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLcasPlct.setStatus(
        "current"
    )

evtLcasPlcr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36979)
)
evtLcasPlcr.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLcasPlcr.setStatus(
        "current"
    )

evtLcasTlct = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36980)
)
evtLcasTlct.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLcasTlct.setStatus(
        "current"
    )

evtLcasTlcr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36981)
)
evtLcasTlcr.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLcasTlcr.setStatus(
        "current"
    )

evtLcasFopt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36985)
)
evtLcasFopt.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLcasFopt.setStatus(
        "current"
    )

evtLcasFopr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 36986)
)
evtLcasFopr.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLcasFopr.setStatus(
        "current"
    )

evtLoopbackFAC2NI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40960)
)
evtLoopbackFAC2NI.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLoopbackFAC2NI.setStatus(
        "current"
    )

evtGfpCsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40961)
)
evtGfpCsf.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtGfpCsf.setStatus(
        "current"
    )

evtRevertiveModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40970)
)
evtRevertiveModeMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRevertiveModeMismatch.setStatus(
        "current"
    )

evtRingIDMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40971)
)
evtRingIDMismatch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRingIDMismatch.setStatus(
        "current"
    )

evtIncorrectFiberConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40972)
)
evtIncorrectFiberConnection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtIncorrectFiberConnection.setStatus(
        "current"
    )

evtStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40973)
)
evtStateChange.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtStateChange.setStatus(
        "current"
    )

evtMtMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40974)
)
evtMtMode.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtMtMode.setStatus(
        "current"
    )

evtRmvToMt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40979)
)
evtRmvToMt.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRmvToMt.setStatus(
        "current"
    )

evtRstFromMt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40980)
)
evtRstFromMt.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRstFromMt.setStatus(
        "current"
    )

evtLpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40981)
)
evtLpbk.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLpbk.setStatus(
        "current"
    )

evtRlsLpbk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40982)
)
evtRlsLpbk.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRlsLpbk.setStatus(
        "current"
    )

evtSyncNotSyncnronized = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40983)
)
evtSyncNotSyncnronized.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSyncNotSyncnronized.setStatus(
        "current"
    )

evtPowerExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40984)
)
evtPowerExceed.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPowerExceed.setStatus(
        "current"
    )

evtPartialUnprotected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40985)
)
evtPartialUnprotected.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPartialUnprotected.setStatus(
        "current"
    )

evtFanMea = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 40986)
)
evtFanMea.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFanMea.setStatus(
        "current"
    )

evtRemoteClientSF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 63604)
)
evtRemoteClientSF.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRemoteClientSF.setStatus(
        "current"
    )

evtRemoteClientSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 63605)
)
evtRemoteClientSD.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtRemoteClientSD.setStatus(
        "current"
    )

evtPowerSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 63607)
)
evtPowerSwitch.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPowerSwitch.setStatus(
        "current"
    )

evtPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 63629)
)
evtPortOffline.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtPortOffline.setStatus(
        "current"
    )

evtDataLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 63630)
)
evtDataLost.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtDataLost.setStatus(
        "current"
    )

evtSqmVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 65409)
)
evtSqmVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtSqmVT.setStatus(
        "current"
    )

evtLomVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 65410)
)
evtLomVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtLomVT.setStatus(
        "current"
    )

evtFCSError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 20, 65411)
)
evtFCSError.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtEffect"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtThValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtAiddet"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    evtFCSError.setStatus(
        "current"
    )

envAirCompressorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 502)
)
envAirCompressorFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envAirCompressorFailure.setStatus(
        "current"
    )

envAirConditioningFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 503)
)
envAirConditioningFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envAirConditioningFailure.setStatus(
        "current"
    )

envAirDryerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 504)
)
envAirDryerFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envAirDryerFailure.setStatus(
        "current"
    )

envBatteryDischarging = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 505)
)
envBatteryDischarging.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envBatteryDischarging.setStatus(
        "current"
    )

envBatteryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 506)
)
envBatteryFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envBatteryFailure.setStatus(
        "current"
    )

envCoolingFacFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 507)
)
envCoolingFacFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envCoolingFacFailure.setStatus(
        "current"
    )

envCPMAJOR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 508)
)
envCPMAJOR.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envCPMAJOR.setStatus(
        "current"
    )

envCPMINOR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 509)
)
envCPMINOR.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envCPMINOR.setStatus(
        "current"
    )

envEngineFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 510)
)
envEngineFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envEngineFailure.setStatus(
        "current"
    )

envEngineOperating = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 511)
)
envEngineOperating.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envEngineOperating.setStatus(
        "current"
    )

envExplosiveGas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 512)
)
envExplosiveGas.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envExplosiveGas.setStatus(
        "current"
    )

envFireDetectorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 513)
)
envFireDetectorFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envFireDetectorFailure.setStatus(
        "current"
    )

envFire = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 514)
)
envFire.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envFire.setStatus(
        "current"
    )

envFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 515)
)
envFlood.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envFlood.setStatus(
        "current"
    )

envFuseFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 516)
)
envFuseFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envFuseFailure.setStatus(
        "current"
    )

envGeneratorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 517)
)
envGeneratorFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envGeneratorFailure.setStatus(
        "current"
    )

envHighAirflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 518)
)
envHighAirflow.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envHighAirflow.setStatus(
        "current"
    )

envHighHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 519)
)
envHighHumidity.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envHighHumidity.setStatus(
        "current"
    )

envHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 520)
)
envHighTemperature.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envHighTemperature.setStatus(
        "current"
    )

envHighWater = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 521)
)
envHighWater.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envHighWater.setStatus(
        "current"
    )

envIntrusion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 522)
)
envIntrusion.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envIntrusion.setStatus(
        "current"
    )

envLowBatteryVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 523)
)
envLowBatteryVoltage.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envLowBatteryVoltage.setStatus(
        "current"
    )

envLowFuel = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 524)
)
envLowFuel.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envLowFuel.setStatus(
        "current"
    )

envLowHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 525)
)
envLowHumidity.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envLowHumidity.setStatus(
        "current"
    )

envLowCablePressure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 526)
)
envLowCablePressure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envLowCablePressure.setStatus(
        "current"
    )

envLowTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 527)
)
envLowTemperature.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envLowTemperature.setStatus(
        "current"
    )

envLowWater = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 528)
)
envLowWater.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envLowWater.setStatus(
        "current"
    )

envMiscellaneous = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 529)
)
envMiscellaneous.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envMiscellaneous.setStatus(
        "current"
    )

envOpenDoor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 530)
)
envOpenDoor.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envOpenDoor.setStatus(
        "current"
    )

envCommercialPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 531)
)
envCommercialPowerFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envCommercialPowerFailure.setStatus(
        "current"
    )

envPumpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 532)
)
envPumpFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envPumpFailure.setStatus(
        "current"
    )

env48VoltPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 536)
)
env48VoltPowerSupplyFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    env48VoltPowerSupplyFailure.setStatus(
        "current"
    )

envRectifierFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 537)
)
envRectifierFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envRectifierFailure.setStatus(
        "current"
    )

envRectifierHighVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 538)
)
envRectifierHighVoltage.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envRectifierHighVoltage.setStatus(
        "current"
    )

envRectiFierLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 539)
)
envRectiFierLowVoltage.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envRectiFierLowVoltage.setStatus(
        "current"
    )

envSmoke = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 540)
)
envSmoke.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envSmoke.setStatus(
        "current"
    )

envToxicGas = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 541)
)
envToxicGas.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envToxicGas.setStatus(
        "current"
    )

envVentilationSystemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 30, 542)
)
envVentilationSystemFailure.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtNumber"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtState"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDescription"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSeqNumber"))
)
if mibBuilder.loadTexts:
    envVentilationSystemFailure.setStatus(
        "current"
    )

pmSESSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32770)
)
pmSESSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmSESSection.setStatus(
        "current"
    )

pmCVLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32784)
)
pmCVLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmCVLine.setStatus(
        "current"
    )

pmESLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32785)
)
pmESLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmESLine.setStatus(
        "current"
    )

pmSESLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32786)
)
pmSESLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmSESLine.setStatus(
        "current"
    )

pmUASLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32789)
)
pmUASLine.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmUASLine.setStatus(
        "current"
    )

pmPSD = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32799)
)
pmPSD.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPSD.setStatus(
        "current"
    )

pmCVPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32800)
)
pmCVPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmCVPath.setStatus(
        "current"
    )

pmESPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32801)
)
pmESPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmESPath.setStatus(
        "current"
    )

pmPjcsVdet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32852)
)
pmPjcsVdet.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPjcsVdet.setStatus(
        "current"
    )

pmBdTempCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32992)
)
pmBdTempCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmBdTempCur.setStatus(
        "current"
    )

pmBdTempMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32993)
)
pmBdTempMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmBdTempMax.setStatus(
        "current"
    )

pmBdTempMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 32994)
)
pmBdTempMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmBdTempMin.setStatus(
        "current"
    )

pmPmuTempCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33000)
)
pmPmuTempCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPmuTempCur.setStatus(
        "current"
    )

pmPmuTempMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33001)
)
pmPmuTempMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPmuTempMax.setStatus(
        "current"
    )

pmPmuTempMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33002)
)
pmPmuTempMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPmuTempMin.setStatus(
        "current"
    )

pmLbcCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33008)
)
pmLbcCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLbcCur.setStatus(
        "current"
    )

pmLbcMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33009)
)
pmLbcMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLbcMax.setStatus(
        "current"
    )

pmLbcMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33010)
)
pmLbcMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLbcMin.setStatus(
        "current"
    )

pmOptCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33011)
)
pmOptCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmOptCur.setStatus(
        "current"
    )

pmOptMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33012)
)
pmOptMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmOptMax.setStatus(
        "current"
    )

pmOptMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33013)
)
pmOptMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmOptMin.setStatus(
        "current"
    )

pmOprCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33014)
)
pmOprCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmOprCur.setStatus(
        "current"
    )

pmOprMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33015)
)
pmOprMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmOprMax.setStatus(
        "current"
    )

pmOprMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33016)
)
pmOprMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmOprMin.setStatus(
        "current"
    )

pmCVPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33056)
)
pmCVPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmCVPPath.setStatus(
        "current"
    )

pmCVCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33057)
)
pmCVCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmCVCPPath.setStatus(
        "current"
    )

pmESPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33058)
)
pmESPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmESPPath.setStatus(
        "current"
    )

pmESCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33059)
)
pmESCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmESCPPath.setStatus(
        "current"
    )

pmSESPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33060)
)
pmSESPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmSESPPath.setStatus(
        "current"
    )

pmSESCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33061)
)
pmSESCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmSESCPPath.setStatus(
        "current"
    )

pmUASPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33064)
)
pmUASPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmUASPPath.setStatus(
        "current"
    )

pmUASCPPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33065)
)
pmUASCPPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmUASCPPath.setStatus(
        "current"
    )

pmPscProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33088)
)
pmPscProtection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPscProtection.setStatus(
        "current"
    )

pmPsdProtection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33089)
)
pmPsdProtection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPsdProtection.setStatus(
        "current"
    )

pmPscSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33090)
)
pmPscSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPscSpan.setStatus(
        "current"
    )

pmPsdSpan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33091)
)
pmPsdSpan.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPsdSpan.setStatus(
        "current"
    )

pmPscRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33092)
)
pmPscRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPscRing.setStatus(
        "current"
    )

pmPsdRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33093)
)
pmPsdRing.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPsdRing.setStatus(
        "current"
    )

pmPscWork = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33094)
)
pmPscWork.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPscWork.setStatus(
        "current"
    )

pmPsdWork = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 33095)
)
pmPsdWork.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPsdWork.setStatus(
        "current"
    )

pmLCCCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36864)
)
pmLCCCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLCCCur.setStatus(
        "current"
    )

pmLCCMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36865)
)
pmLCCMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLCCMax.setStatus(
        "current"
    )

pmLCCMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36866)
)
pmLCCMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLCCMin.setStatus(
        "current"
    )

pmLTEMPCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36867)
)
pmLTEMPCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLTEMPCur.setStatus(
        "current"
    )

pmLTEMPMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36868)
)
pmLTEMPMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLTEMPMax.setStatus(
        "current"
    )

pmLTEMPMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36869)
)
pmLTEMPMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLTEMPMin.setStatus(
        "current"
    )

pmLAPDBVCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36870)
)
pmLAPDBVCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLAPDBVCur.setStatus(
        "current"
    )

pmLAPDBVMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36871)
)
pmLAPDBVMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLAPDBVMax.setStatus(
        "current"
    )

pmLAPDBVMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36872)
)
pmLAPDBVMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmLAPDBVMin.setStatus(
        "current"
    )

pmPLBCCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36873)
)
pmPLBCCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPLBCCur.setStatus(
        "current"
    )

pmPLBCMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36874)
)
pmPLBCMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPLBCMax.setStatus(
        "current"
    )

pmPLBCMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36875)
)
pmPLBCMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPLBCMin.setStatus(
        "current"
    )

pmPLWCCur = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36876)
)
pmPLWCCur.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPLWCCur.setStatus(
        "current"
    )

pmPLWCMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36877)
)
pmPLWCMax.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPLWCMax.setStatus(
        "current"
    )

pmPLWCMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36878)
)
pmPLWCMin.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPLWCMin.setStatus(
        "current"
    )

pmCVSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36879)
)
pmCVSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmCVSection.setStatus(
        "current"
    )

pmESSection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36880)
)
pmESSection.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmESSection.setStatus(
        "current"
    )

pmSESPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36881)
)
pmSESPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmSESPath.setStatus(
        "current"
    )

pmUASPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36882)
)
pmUASPath.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmUASPath.setStatus(
        "current"
    )

pmCVVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36883)
)
pmCVVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmCVVT.setStatus(
        "current"
    )

pmESVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36884)
)
pmESVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmESVT.setStatus(
        "current"
    )

pmSESVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36885)
)
pmSESVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmSESVT.setStatus(
        "current"
    )

pmUASVT = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36886)
)
pmUASVT.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmUASVT.setStatus(
        "current"
    )

pmPSC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 36887)
)
pmPSC.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPSC.setStatus(
        "current"
    )

pmPjcsPdet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 40, 45065)
)
pmPjcsPdet.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "rptEvtMOD2"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtSlot"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPort"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPath"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVT"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtMonValue"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtVldty"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtLocation"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDirection"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtPeriod"),
        ("OPTIX-SONET-TRAPS-MIB", "rptEvtDateTime"))
)
if mibBuilder.loadTexts:
    pmPjcsPdet.setStatus(
        "current"
    )


# Notifications groups

optixSonetTrapsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 60, 1, 2)
)
optixSonetTrapsNotificationGroup.setObjects(
      *(("OPTIX-SONET-TRAPS-MIB", "almSignalDegradeVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalFailureVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLossOfClock"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFileLost"),
        ("OPTIX-SONET-TRAPS-MIB", "evtREILine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBiasTemperatureOfPumpHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTimSection"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLossOfAllSynchronousSource"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSynchronousSourceDegrade"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSyncLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtProtectionSwitching"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDbmsError"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLossOfMultiplexSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLossOfSingleWavelengthSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAdditionOfSingleWavelengthSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserDegraded"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPumpDiodeCoolingCurrentHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtS1ModeSynChange"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDbmsIsInProtectMode"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSecuAlarm"),
        ("OPTIX-SONET-TRAPS-MIB", "evtForwardErrorCorrectionLossOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "evtForwardErrorCorrectionOutOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRateOver"),
        ("OPTIX-SONET-TRAPS-MIB", "evtCardConfigurationFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopback"),
        ("OPTIX-SONET-TRAPS-MIB", "evtCoolingCurrentModeHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOTULossOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOTUOutOfMultiFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSmTIM"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPmTIM"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSmBDI"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPmBDI"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSmBEI"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPmBEI"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSmIAE"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSmBipExcessive"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPmBipExcessive"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSmBipSignalDefect"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPmBipSignalDefect"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOTUAlarmIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtODUAlarmIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtODUOpenConnectionIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtODULockedIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSumInputOpticalPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSumInputOpticalPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSumOutOpticalPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOutOpticalPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtGainLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExcessiveErrorDefectBeforeFEC"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDgeAdjustmentFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtWavelengthLockFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtHotSwitchControlUnavail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEsconCodeError"),
        ("OPTIX-SONET-TRAPS-MIB", "evtCommitTimeout"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwdlNePackageCheck"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwdlChaGmngmMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDBSyncFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtClientMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserModuleMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEqptNoServiceAffecting"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEqptServiceAffectingFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtApsByteFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFarEndProtectionLineFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "evtApsChannelMismatchFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "evtApsModeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtApsTypeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtHoldoverSync"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFreeRunSync"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFastStartSync"),
        ("OPTIX-SONET-TRAPS-MIB", "evtManualSetSSM"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFanOffline"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSingleFanFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtMultiFanFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEquipmentTypeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEquipmentOfflineOrUninstalled"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTransmitterFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalFailureSection"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInputPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInputPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalFailureLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalDegradeLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserApprochingEndOfLife"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOutPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOutPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalDegradeSection"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAlarmIndicationSignalLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRemoteFailureIindicationLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAlarmIndicationSignalPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLossOfPointerPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTraceIdentifierMismatchPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtUnequippedPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalFailurePath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalDegradePath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRemoteFailureIindicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtALS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackFacility"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackTerminal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPayloadLabelMisatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEnhancedRemotePalyloadFailureIndicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEnhancedRemoteServerFailureIndicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEnhancedRemoteConnectivityFailureIndicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPDIPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPowerFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLossOfPointerVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAlarmIndicationSignalVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPayloadLabelMismatchVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtUnequippedVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRemoteFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRemoteServerFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEnhancedRemoteConnectivityFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtEnhancedRemotePalyloadFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInterFaceCardOffline"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSyncChangeSSM"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTimeingModeChange"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutWorkingUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutProtectionUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "evtForcedSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtManualSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExerciseSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtWaitToRestore"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwitchToIdle"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwitchFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSyncSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtCommunicationFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPowerAFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPowerBFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInterfaceLinkMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInterfaceCardFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAIC"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDbmsCfgCorrupted"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDefaultKByteDefect"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInconsistentApsCodes"),
        ("OPTIX-SONET-TRAPS-MIB", "evtImproperApsCodes"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExtraTrafficIsBeingSquelched"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTopologyNeedsUpdatingOrIsInvalid"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSquelchTableNeedsUpdatingOrIsInvalid"),
        ("OPTIX-SONET-TRAPS-MIB", "evtNodeIdDuplicatedOrMismatched"),
        ("OPTIX-SONET-TRAPS-MIB", "evtXconMismatched"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRingModeMisatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSquelchModeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutProtectionSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutWorkingRing"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutWorkingSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtForceSwitchOfRing"),
        ("OPTIX-SONET-TRAPS-MIB", "evtForceSwitchOfSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtManualSwitchOfRing"),
        ("OPTIX-SONET-TRAPS-MIB", "evtManualSwitchOfSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExerciseSwitchRing"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExerciseSwitchSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutProtectionForAllSpans"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRingSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSpanSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwitchToPassthru"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPersistentLineSquelching"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDbmsCfgBackupFailed"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFanFailures"),
        ("OPTIX-SONET-TRAPS-MIB", "evtInvalidEQPT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserApdBiasVoltageHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserApdBiasVoltageLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLBCHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLBCLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLCCHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLCCLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLinkError"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLOA"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLOF"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLOMPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserTemperatureHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserTemperatureLow"),
        ("OPTIX-SONET-TRAPS-MIB", "evtNeBdDataMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtNoLaserParameter"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSyncReferenceSourceFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalDegradeVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSignalFailureVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSequenceNumberMismatchedVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSoftwareVersionMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTemperatureHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAIS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackInhibited"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLockoutOfTheProtocol"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserShutDown"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackAllDS1FEAC"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackCrossConnect"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackDS1FEAC"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackDS3FEAC"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackFacilityPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackTerminalPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPrimaryChannelChange"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRAI"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSsmDQL"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSsmLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTestSessionActive"),
        ("OPTIX-SONET-TRAPS-MIB", "evtNormalSyncMode"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwitchProtectionToWorkingUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSwtichWokingToProtectingUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "evtATECardOfflineOrUninstalled"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPIUCardOfflineOrUninstalled"),
        ("OPTIX-SONET-TRAPS-MIB", "evtOOF"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExerciseSwitchSuccess"),
        ("OPTIX-SONET-TRAPS-MIB", "evtExerciseSwitchFail"),
        ("OPTIX-SONET-TRAPS-MIB", "evtUpgradeInProcess"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLaserNotExist"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLCASBandwidthReduced"),
        ("OPTIX-SONET-TRAPS-MIB", "evtGFPLossOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFanIsOpened"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFanIsClosed"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPathLevelMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaCVLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDCCFailureIndication"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLanLossOfCarrierSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaCVCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaCVPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaCVPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaCVSection"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaCVVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaESCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaESLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaESPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaESPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaESSection"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaESVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaPjcsPdet"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaPjcsVdet"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaSESCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaSESLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaSESPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaSESPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaSESSection"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaSESVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaUASCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaUASLine"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaUASPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaUASPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "evtTcaUASVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBitsAIS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBitsLOF"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBitsLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBitsCodeViolationOver"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBlsrSFofRing"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBlsrSFofSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBlsrSDofRing"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBlsrSDofSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "evtBlsrNodeIsolate"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSF"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSD"),
        ("OPTIX-SONET-TRAPS-MIB", "evtAutoSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLoopbackFAC2NI"),
        ("OPTIX-SONET-TRAPS-MIB", "evtMtMode"),
        ("OPTIX-SONET-TRAPS-MIB", "evtStateChange"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRemoteClientSF"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRemoteClientSD"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPowerSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPortOffline"),
        ("OPTIX-SONET-TRAPS-MIB", "evtDataLost"),
        ("OPTIX-SONET-TRAPS-MIB", "evtSqmVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLomVT"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFCSError"),
        ("OPTIX-SONET-TRAPS-MIB", "almLossOfClock"),
        ("OPTIX-SONET-TRAPS-MIB", "almFileLost"),
        ("OPTIX-SONET-TRAPS-MIB", "almBiasTemperatureOfPumpHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almTimSection"),
        ("OPTIX-SONET-TRAPS-MIB", "almLossOfAllSynchronousSource"),
        ("OPTIX-SONET-TRAPS-MIB", "almSynchronousSourceDegrade"),
        ("OPTIX-SONET-TRAPS-MIB", "almProtectionSwitching"),
        ("OPTIX-SONET-TRAPS-MIB", "almDbmsError"),
        ("OPTIX-SONET-TRAPS-MIB", "almLossOfMultiplexSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almLossOfSingleWavelengthSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almAdditionOfSingleWavelengthSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserDegraded"),
        ("OPTIX-SONET-TRAPS-MIB", "almPumpDiodeCoolingCurrentHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almS1ModeSynChange"),
        ("OPTIX-SONET-TRAPS-MIB", "almDbmsIsInProtectMode"),
        ("OPTIX-SONET-TRAPS-MIB", "almForwardErrorCorrectionLossOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "almForwardErrorCorrectionOutOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "almRateOver"),
        ("OPTIX-SONET-TRAPS-MIB", "almCardConfigurationFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopback"),
        ("OPTIX-SONET-TRAPS-MIB", "almCoolingCurrentModeHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almOTULossOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "almOTUOutOfMultiFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "almSmTIM"),
        ("OPTIX-SONET-TRAPS-MIB", "almPmTIM"),
        ("OPTIX-SONET-TRAPS-MIB", "almSmBDI"),
        ("OPTIX-SONET-TRAPS-MIB", "almPmBDI"),
        ("OPTIX-SONET-TRAPS-MIB", "almSmBEI"),
        ("OPTIX-SONET-TRAPS-MIB", "almPmBEI"),
        ("OPTIX-SONET-TRAPS-MIB", "almSmIAE"),
        ("OPTIX-SONET-TRAPS-MIB", "almSmBipExcessive"),
        ("OPTIX-SONET-TRAPS-MIB", "almPmBipExcessive"),
        ("OPTIX-SONET-TRAPS-MIB", "almSmBipSignalDefect"),
        ("OPTIX-SONET-TRAPS-MIB", "almPmBipSignalDefect"),
        ("OPTIX-SONET-TRAPS-MIB", "almOTUAlarmIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almODUAlarmIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almODUOpenConnectionIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almODULockedIndicationSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almSumInputOpticalPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almSumInputOpticalPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almSumOutOpticalPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almOutOpticalPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almGainLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almDgeAdjustmentFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almWavelengthLockFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almHotSwitchControlUnavail"),
        ("OPTIX-SONET-TRAPS-MIB", "almEsconCodeError"),
        ("OPTIX-SONET-TRAPS-MIB", "almCommitTimeout"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwdlNePackageCheck"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwdlChaGmngmMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almDBSyncFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almClientMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserModuleMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almEqptNoServiceAffecting"),
        ("OPTIX-SONET-TRAPS-MIB", "almEqptServiceAffectingFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almApsByteFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "almFarEndProtectionLineFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "almApsChannelMismatchFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "almApsModeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almApsTypeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almFreeRunSync"),
        ("OPTIX-SONET-TRAPS-MIB", "almFanOffline"),
        ("OPTIX-SONET-TRAPS-MIB", "almSingleFanFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almMultiFanFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almEquipmentTypeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almEquipmentOfflineOrUninstalled"),
        ("OPTIX-SONET-TRAPS-MIB", "almTransmitterFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalFailureSection"),
        ("OPTIX-SONET-TRAPS-MIB", "almInputPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almInputPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalFailureLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalDegradeLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserApprochingEndOfLife"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalDegradeSection"),
        ("OPTIX-SONET-TRAPS-MIB", "almAlarmIndicationSignalLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almRemoteFailureIindicationLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almAlarmIndicationSignalPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almLossOfPointerPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTraceIdentifierMismatchPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almUnequippedPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalFailurePath"),
        ("OPTIX-SONET-TRAPS-MIB", "almSignalDegradePath"),
        ("OPTIX-SONET-TRAPS-MIB", "almRemoteFailureIindicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almPayloadLabelMisatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almEnhancedRemotePalyloadFailureIndicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almEnhancedRemoteServerFailureIndicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almEnhancedRemoteConnectivityFailureIndicationPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almPowerFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almLossOfPointerVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almAlarmIndicationSignalVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almPayloadLabelMismatchVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almUnequippedVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almRemoteFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almRemoteServerFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almEnhancedRemoteConnectivityFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almEnhancedRemotePalyloadFailureIndicationVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almInterFaceCardOffline"),
        ("OPTIX-SONET-TRAPS-MIB", "almCommunicationFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almPowerAFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almPowerBFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almInterfaceLinkMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almInterfaceCardFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almAIC"),
        ("OPTIX-SONET-TRAPS-MIB", "almDbmsCfgCorrupted"),
        ("OPTIX-SONET-TRAPS-MIB", "almDefaultKByteDefect"),
        ("OPTIX-SONET-TRAPS-MIB", "almInconsistentApsCodes"),
        ("OPTIX-SONET-TRAPS-MIB", "almImproperApsCodes"),
        ("OPTIX-SONET-TRAPS-MIB", "almExtraTrafficIsBeingSquelched"),
        ("OPTIX-SONET-TRAPS-MIB", "almTopologyNeedsUpdatingOrIsInvalid"),
        ("OPTIX-SONET-TRAPS-MIB", "almSquelchTableNeedsUpdatingOrIsInvalid"),
        ("OPTIX-SONET-TRAPS-MIB", "almNodeIdDuplicatedOrMismatched"),
        ("OPTIX-SONET-TRAPS-MIB", "almXconMismatched"),
        ("OPTIX-SONET-TRAPS-MIB", "almRingModeMisatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almSquelchModeMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almDbmsCfgBackupFailed"),
        ("OPTIX-SONET-TRAPS-MIB", "almFanFailures"),
        ("OPTIX-SONET-TRAPS-MIB", "almInvalidEQPT"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserApdBiasVoltageHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserApdBiasVoltageLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almLBCHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almLBCLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almLCCHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almLCCLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almLinkError"),
        ("OPTIX-SONET-TRAPS-MIB", "almLOA"),
        ("OPTIX-SONET-TRAPS-MIB", "almLOF"),
        ("OPTIX-SONET-TRAPS-MIB", "almLOMPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserTemperatureHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserTemperatureLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almNeBdDataMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almNoLaserParameter"),
        ("OPTIX-SONET-TRAPS-MIB", "almSyncReferenceSourceFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "almSequenceNumberMismatchedVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almSoftwareVersionMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almTemperatureHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almAIS"),
        ("OPTIX-SONET-TRAPS-MIB", "almPrimaryChannelChange"),
        ("OPTIX-SONET-TRAPS-MIB", "almRAI"),
        ("OPTIX-SONET-TRAPS-MIB", "almSsmDQL"),
        ("OPTIX-SONET-TRAPS-MIB", "almSsmLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "almATECardOfflineOrUninstalled"),
        ("OPTIX-SONET-TRAPS-MIB", "almPIUCardOfflineOrUninstalled"),
        ("OPTIX-SONET-TRAPS-MIB", "almOOF"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserNotExist"),
        ("OPTIX-SONET-TRAPS-MIB", "almGFPLossOfFrame"),
        ("OPTIX-SONET-TRAPS-MIB", "almPathLevelMismatch"),
        ("OPTIX-SONET-TRAPS-MIB", "almDCCFailureIndication"),
        ("OPTIX-SONET-TRAPS-MIB", "almLanLossOfCarrierSignal"),
        ("OPTIX-SONET-TRAPS-MIB", "almBitsAIS"),
        ("OPTIX-SONET-TRAPS-MIB", "almBitsLOF"),
        ("OPTIX-SONET-TRAPS-MIB", "almBitsLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "almBitsCodeViolationOver"),
        ("OPTIX-SONET-TRAPS-MIB", "almBlsrNodeIsolate"),
        ("OPTIX-SONET-TRAPS-MIB", "almRemoteClientSF"),
        ("OPTIX-SONET-TRAPS-MIB", "almRemoteClientSD"),
        ("OPTIX-SONET-TRAPS-MIB", "almPowerSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almPortOffline"),
        ("OPTIX-SONET-TRAPS-MIB", "almDataLost"),
        ("OPTIX-SONET-TRAPS-MIB", "almSqmVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almLomVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almFCSError"),
        ("OPTIX-SONET-TRAPS-MIB", "almREILine"),
        ("OPTIX-SONET-TRAPS-MIB", "almSyncLOS"),
        ("OPTIX-SONET-TRAPS-MIB", "almSecuAlarm"),
        ("OPTIX-SONET-TRAPS-MIB", "almExcessiveErrorDefectBeforeFEC"),
        ("OPTIX-SONET-TRAPS-MIB", "almHoldoverSync"),
        ("OPTIX-SONET-TRAPS-MIB", "almFastStartSync"),
        ("OPTIX-SONET-TRAPS-MIB", "almManualSetSSM"),
        ("OPTIX-SONET-TRAPS-MIB", "almOutPowerHigh"),
        ("OPTIX-SONET-TRAPS-MIB", "almOutPowerLow"),
        ("OPTIX-SONET-TRAPS-MIB", "almALS"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackFacility"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackTerminal"),
        ("OPTIX-SONET-TRAPS-MIB", "almPDIPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almSyncChangeSSM"),
        ("OPTIX-SONET-TRAPS-MIB", "almTimeingModeChange"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutWorkingUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutProtectionUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "almForcedSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almManualSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almExerciseSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almWaitToRestore"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwitchToIdle"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwitchFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almSyncSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutProtectionSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutWorkingRing"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutWorkingSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almForceSwitchOfRing"),
        ("OPTIX-SONET-TRAPS-MIB", "almForceSwitchOfSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almManualSwitchOfRing"),
        ("OPTIX-SONET-TRAPS-MIB", "almManualSwitchOfSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almExerciseSwitchRing"),
        ("OPTIX-SONET-TRAPS-MIB", "almExerciseSwitchSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutProtectionForAllSpans"),
        ("OPTIX-SONET-TRAPS-MIB", "almRingSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almSpanSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwitchToPassthru"),
        ("OPTIX-SONET-TRAPS-MIB", "almPersistentLineSquelching"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackInhibited"),
        ("OPTIX-SONET-TRAPS-MIB", "almLockoutOfTheProtocol"),
        ("OPTIX-SONET-TRAPS-MIB", "almLaserShutDown"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackAllDS1FEAC"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackCrossConnect"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackDS1FEAC"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackDS3FEAC"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackFacilityPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackTerminalPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTestSessionActive"),
        ("OPTIX-SONET-TRAPS-MIB", "almNormalSyncMode"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwitchProtectionToWorkingUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "almSwtichWokingToProtectingUnit"),
        ("OPTIX-SONET-TRAPS-MIB", "almExerciseSwitchSuccess"),
        ("OPTIX-SONET-TRAPS-MIB", "almExerciseSwitchFail"),
        ("OPTIX-SONET-TRAPS-MIB", "almUpgradeInProcess"),
        ("OPTIX-SONET-TRAPS-MIB", "almLCASBandwidthReduced"),
        ("OPTIX-SONET-TRAPS-MIB", "almFanIsOpened"),
        ("OPTIX-SONET-TRAPS-MIB", "almFanIsClosed"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaCVLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaCVCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaCVPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaCVPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaCVSection"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaCVVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaESCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaESLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaESPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaESPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaESSection"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaESVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaPjcsPdet"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaPjcsVdet"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaSESCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaSESLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaSESPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaSESPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaSESSection"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaSESVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaUASCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaUASLine"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaUASPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaUASPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "almTcaUASVT"),
        ("OPTIX-SONET-TRAPS-MIB", "almBlsrSFofRing"),
        ("OPTIX-SONET-TRAPS-MIB", "almBlsrSFofSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almBlsrSDofRing"),
        ("OPTIX-SONET-TRAPS-MIB", "almBlsrSDofSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "almSF"),
        ("OPTIX-SONET-TRAPS-MIB", "almSD"),
        ("OPTIX-SONET-TRAPS-MIB", "almAutoSwitch"),
        ("OPTIX-SONET-TRAPS-MIB", "almLoopbackFAC2NI"),
        ("OPTIX-SONET-TRAPS-MIB", "almMtMode"),
        ("OPTIX-SONET-TRAPS-MIB", "almStateChange"),
        ("OPTIX-SONET-TRAPS-MIB", "envAirCompressorFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envAirConditioningFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envAirDryerFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envBatteryDischarging"),
        ("OPTIX-SONET-TRAPS-MIB", "envBatteryFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envCoolingFacFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envCPMAJOR"),
        ("OPTIX-SONET-TRAPS-MIB", "envCPMINOR"),
        ("OPTIX-SONET-TRAPS-MIB", "envEngineFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envEngineOperating"),
        ("OPTIX-SONET-TRAPS-MIB", "envExplosiveGas"),
        ("OPTIX-SONET-TRAPS-MIB", "envFireDetectorFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envFire"),
        ("OPTIX-SONET-TRAPS-MIB", "envFlood"),
        ("OPTIX-SONET-TRAPS-MIB", "envFuseFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envGeneratorFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envHighAirflow"),
        ("OPTIX-SONET-TRAPS-MIB", "envHighHumidity"),
        ("OPTIX-SONET-TRAPS-MIB", "envHighTemperature"),
        ("OPTIX-SONET-TRAPS-MIB", "envHighWater"),
        ("OPTIX-SONET-TRAPS-MIB", "envIntrusion"),
        ("OPTIX-SONET-TRAPS-MIB", "envLowBatteryVoltage"),
        ("OPTIX-SONET-TRAPS-MIB", "envLowFuel"),
        ("OPTIX-SONET-TRAPS-MIB", "envLowHumidity"),
        ("OPTIX-SONET-TRAPS-MIB", "envLowCablePressure"),
        ("OPTIX-SONET-TRAPS-MIB", "envLowTemperature"),
        ("OPTIX-SONET-TRAPS-MIB", "envLowWater"),
        ("OPTIX-SONET-TRAPS-MIB", "envMiscellaneous"),
        ("OPTIX-SONET-TRAPS-MIB", "envOpenDoor"),
        ("OPTIX-SONET-TRAPS-MIB", "envCommercialPowerFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envPumpFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "env48VoltPowerSupplyFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envRectifierFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "envRectifierHighVoltage"),
        ("OPTIX-SONET-TRAPS-MIB", "envRectiFierLowVoltage"),
        ("OPTIX-SONET-TRAPS-MIB", "envSmoke"),
        ("OPTIX-SONET-TRAPS-MIB", "envToxicGas"),
        ("OPTIX-SONET-TRAPS-MIB", "envVentilationSystemFailure"),
        ("OPTIX-SONET-TRAPS-MIB", "pmSESSection"),
        ("OPTIX-SONET-TRAPS-MIB", "pmCVLine"),
        ("OPTIX-SONET-TRAPS-MIB", "pmESLine"),
        ("OPTIX-SONET-TRAPS-MIB", "pmSESLine"),
        ("OPTIX-SONET-TRAPS-MIB", "pmUASLine"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPSD"),
        ("OPTIX-SONET-TRAPS-MIB", "pmCVPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmESPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPjcsVdet"),
        ("OPTIX-SONET-TRAPS-MIB", "pmBdTempCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmBdTempMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmBdTempMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPmuTempCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPmuTempMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPmuTempMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLbcCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLbcMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLbcMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmOptCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmOptMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmOptMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmOprCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmOprMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmOprMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmCVPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmCVCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmESPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmESCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmSESPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmSESCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmUASPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmUASCPPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPscProtection"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPsdProtection"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPscSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPsdSpan"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPscRing"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPsdRing"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPscWork"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPsdWork"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLCCCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLCCMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLCCMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLTEMPCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLTEMPMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLTEMPMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLAPDBVCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLAPDBVMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmLAPDBVMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPLBCCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPLBCMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPLBCMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPLWCCur"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPLWCMax"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPLWCMin"),
        ("OPTIX-SONET-TRAPS-MIB", "pmCVSection"),
        ("OPTIX-SONET-TRAPS-MIB", "pmESSection"),
        ("OPTIX-SONET-TRAPS-MIB", "pmSESPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmUASPath"),
        ("OPTIX-SONET-TRAPS-MIB", "pmCVVT"),
        ("OPTIX-SONET-TRAPS-MIB", "pmESVT"),
        ("OPTIX-SONET-TRAPS-MIB", "pmSESVT"),
        ("OPTIX-SONET-TRAPS-MIB", "pmUASVT"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPSC"),
        ("OPTIX-SONET-TRAPS-MIB", "pmPjcsPdet"),
        ("OPTIX-SONET-TRAPS-MIB", "almChassisMea"),
        ("OPTIX-SONET-TRAPS-MIB", "evtChassisMea"),
        ("OPTIX-SONET-TRAPS-MIB", "almRmvToMt"),
        ("OPTIX-SONET-TRAPS-MIB", "almRstFromMt"),
        ("OPTIX-SONET-TRAPS-MIB", "almLpbk"),
        ("OPTIX-SONET-TRAPS-MIB", "almRlsLpbk"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRmvToMt"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRstFromMt"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLpbk"),
        ("OPTIX-SONET-TRAPS-MIB", "evtRlsLpbk"),
        ("OPTIX-SONET-TRAPS-MIB", "almPowerExceed"),
        ("OPTIX-SONET-TRAPS-MIB", "almLcasPlct"),
        ("OPTIX-SONET-TRAPS-MIB", "almLcasPlcr"),
        ("OPTIX-SONET-TRAPS-MIB", "almLcasTlct"),
        ("OPTIX-SONET-TRAPS-MIB", "almLcasTlcr"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPowerExceed"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLcasPlct"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLcasPlcr"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLcasTlct"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLcasTlcr"),
        ("OPTIX-SONET-TRAPS-MIB", "almLcasFopt"),
        ("OPTIX-SONET-TRAPS-MIB", "almLcasFopr"),
        ("OPTIX-SONET-TRAPS-MIB", "almGfpCsf"),
        ("OPTIX-SONET-TRAPS-MIB", "almLptRfi"),
        ("OPTIX-SONET-TRAPS-MIB", "almPartialUnprotected"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLcasFopt"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLcasFopr"),
        ("OPTIX-SONET-TRAPS-MIB", "evtGfpCsf"),
        ("OPTIX-SONET-TRAPS-MIB", "evtLptRfi"),
        ("OPTIX-SONET-TRAPS-MIB", "evtPartialUnprotected"),
        ("OPTIX-SONET-TRAPS-MIB", "almFanMea"),
        ("OPTIX-SONET-TRAPS-MIB", "evtFanMea"))
)
if mibBuilder.loadTexts:
    optixSonetTrapsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

optixSonetBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 40, 60, 2, 1)
)
if mibBuilder.loadTexts:
    optixSonetBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-TRAPS-MIB",
    **{"optixSonetTraps": optixSonetTraps,
       "optixTrapsAlarm": optixTrapsAlarm,
       "almLossOfClock": almLossOfClock,
       "almFileLost": almFileLost,
       "almREILine": almREILine,
       "almBiasTemperatureOfPumpHigh": almBiasTemperatureOfPumpHigh,
       "almTimSection": almTimSection,
       "almLossOfAllSynchronousSource": almLossOfAllSynchronousSource,
       "almSynchronousSourceDegrade": almSynchronousSourceDegrade,
       "almSyncLOS": almSyncLOS,
       "almProtectionSwitching": almProtectionSwitching,
       "almDbmsError": almDbmsError,
       "almLossOfMultiplexSignal": almLossOfMultiplexSignal,
       "almLossOfSingleWavelengthSignal": almLossOfSingleWavelengthSignal,
       "almAdditionOfSingleWavelengthSignal": almAdditionOfSingleWavelengthSignal,
       "almLaserDegraded": almLaserDegraded,
       "almPumpDiodeCoolingCurrentHigh": almPumpDiodeCoolingCurrentHigh,
       "almS1ModeSynChange": almS1ModeSynChange,
       "almDbmsIsInProtectMode": almDbmsIsInProtectMode,
       "almSecuAlarm": almSecuAlarm,
       "almForwardErrorCorrectionLossOfFrame": almForwardErrorCorrectionLossOfFrame,
       "almForwardErrorCorrectionOutOfFrame": almForwardErrorCorrectionOutOfFrame,
       "almRateOver": almRateOver,
       "almCardConfigurationFail": almCardConfigurationFail,
       "almLoopback": almLoopback,
       "almCoolingCurrentModeHigh": almCoolingCurrentModeHigh,
       "almOTULossOfFrame": almOTULossOfFrame,
       "almOTUOutOfMultiFrame": almOTUOutOfMultiFrame,
       "almSmTIM": almSmTIM,
       "almPmTIM": almPmTIM,
       "almSmBDI": almSmBDI,
       "almPmBDI": almPmBDI,
       "almSmBEI": almSmBEI,
       "almPmBEI": almPmBEI,
       "almSmIAE": almSmIAE,
       "almSmBipExcessive": almSmBipExcessive,
       "almPmBipExcessive": almPmBipExcessive,
       "almSmBipSignalDefect": almSmBipSignalDefect,
       "almPmBipSignalDefect": almPmBipSignalDefect,
       "almOTUAlarmIndicationSignal": almOTUAlarmIndicationSignal,
       "almODUAlarmIndicationSignal": almODUAlarmIndicationSignal,
       "almODUOpenConnectionIndicationSignal": almODUOpenConnectionIndicationSignal,
       "almODULockedIndicationSignal": almODULockedIndicationSignal,
       "almSumInputOpticalPowerHigh": almSumInputOpticalPowerHigh,
       "almSumInputOpticalPowerLow": almSumInputOpticalPowerLow,
       "almSumOutOpticalPowerHigh": almSumOutOpticalPowerHigh,
       "almOutOpticalPowerLow": almOutOpticalPowerLow,
       "almGainLow": almGainLow,
       "almExcessiveErrorDefectBeforeFEC": almExcessiveErrorDefectBeforeFEC,
       "almDgeAdjustmentFail": almDgeAdjustmentFail,
       "almWavelengthLockFail": almWavelengthLockFail,
       "almHotSwitchControlUnavail": almHotSwitchControlUnavail,
       "almEsconCodeError": almEsconCodeError,
       "almCommitTimeout": almCommitTimeout,
       "almSwdlNePackageCheck": almSwdlNePackageCheck,
       "almSwdlChaGmngmMismatch": almSwdlChaGmngmMismatch,
       "almDBSyncFail": almDBSyncFail,
       "almClientMismatch": almClientMismatch,
       "almLaserModuleMismatch": almLaserModuleMismatch,
       "almDlagProtFail": almDlagProtFail,
       "almOamRemoteLoop": almOamRemoteLoop,
       "almOamRemoteSD": almOamRemoteSD,
       "almOamRemoteSF": almOamRemoteSF,
       "almOamFail": almOamFail,
       "almCcLoss": almCcLoss,
       "almMpConflict": almMpConflict,
       "almLptRfi": almLptRfi,
       "almOamSelfLoop": almOamSelfLoop,
       "almLagPortFail": almLagPortFail,
       "almEthCfmMismerge": almEthCfmMismerge,
       "almEthCfmUnexperi": almEthCfmUnexperi,
       "almEthCfmLoc": almEthCfmLoc,
       "almEthCfmRdi": almEthCfmRdi,
       "almEqptNoServiceAffecting": almEqptNoServiceAffecting,
       "almEqptServiceAffectingFail": almEqptServiceAffectingFail,
       "almApsByteFailure": almApsByteFailure,
       "almFarEndProtectionLineFailure": almFarEndProtectionLineFailure,
       "almApsChannelMismatchFailure": almApsChannelMismatchFailure,
       "almApsModeMismatch": almApsModeMismatch,
       "almApsTypeMismatch": almApsTypeMismatch,
       "almHoldoverSync": almHoldoverSync,
       "almFreeRunSync": almFreeRunSync,
       "almFastStartSync": almFastStartSync,
       "almManualSetSSM": almManualSetSSM,
       "almFanOffline": almFanOffline,
       "almSingleFanFail": almSingleFanFail,
       "almMultiFanFail": almMultiFanFail,
       "almEquipmentTypeMismatch": almEquipmentTypeMismatch,
       "almEquipmentOfflineOrUninstalled": almEquipmentOfflineOrUninstalled,
       "almTransmitterFailure": almTransmitterFailure,
       "almSignalFailureSection": almSignalFailureSection,
       "almInputPowerHigh": almInputPowerHigh,
       "almInputPowerLow": almInputPowerLow,
       "almSignalFailureLine": almSignalFailureLine,
       "almSignalDegradeLine": almSignalDegradeLine,
       "almLaserApprochingEndOfLife": almLaserApprochingEndOfLife,
       "almOutPowerHigh": almOutPowerHigh,
       "almOutPowerLow": almOutPowerLow,
       "almSignalDegradeSection": almSignalDegradeSection,
       "almAlarmIndicationSignalLine": almAlarmIndicationSignalLine,
       "almRemoteFailureIindicationLine": almRemoteFailureIindicationLine,
       "almAlarmIndicationSignalPath": almAlarmIndicationSignalPath,
       "almLossOfPointerPath": almLossOfPointerPath,
       "almTraceIdentifierMismatchPath": almTraceIdentifierMismatchPath,
       "almUnequippedPath": almUnequippedPath,
       "almSignalFailurePath": almSignalFailurePath,
       "almSignalDegradePath": almSignalDegradePath,
       "almRemoteFailureIindicationPath": almRemoteFailureIindicationPath,
       "almALS": almALS,
       "almLoopbackFacility": almLoopbackFacility,
       "almLoopbackTerminal": almLoopbackTerminal,
       "almPayloadLabelMisatch": almPayloadLabelMisatch,
       "almEnhancedRemotePalyloadFailureIndicationPath": almEnhancedRemotePalyloadFailureIndicationPath,
       "almEnhancedRemoteServerFailureIndicationPath": almEnhancedRemoteServerFailureIndicationPath,
       "almEnhancedRemoteConnectivityFailureIndicationPath": almEnhancedRemoteConnectivityFailureIndicationPath,
       "almPDIPath": almPDIPath,
       "almPowerFail": almPowerFail,
       "almLossOfPointerVT": almLossOfPointerVT,
       "almAlarmIndicationSignalVT": almAlarmIndicationSignalVT,
       "almPayloadLabelMismatchVT": almPayloadLabelMismatchVT,
       "almUnequippedVT": almUnequippedVT,
       "almRemoteFailureIndicationVT": almRemoteFailureIndicationVT,
       "almRemoteServerFailureIndicationVT": almRemoteServerFailureIndicationVT,
       "almEnhancedRemoteConnectivityFailureIndicationVT": almEnhancedRemoteConnectivityFailureIndicationVT,
       "almEnhancedRemotePalyloadFailureIndicationVT": almEnhancedRemotePalyloadFailureIndicationVT,
       "almInterFaceCardOffline": almInterFaceCardOffline,
       "almSyncChangeSSM": almSyncChangeSSM,
       "almTimeingModeChange": almTimeingModeChange,
       "almLockoutWorkingUnit": almLockoutWorkingUnit,
       "almLockoutProtectionUnit": almLockoutProtectionUnit,
       "almForcedSwitch": almForcedSwitch,
       "almManualSwitch": almManualSwitch,
       "almExerciseSwitch": almExerciseSwitch,
       "almWaitToRestore": almWaitToRestore,
       "almSwitchToIdle": almSwitchToIdle,
       "almSwitchFail": almSwitchFail,
       "almSyncSwitch": almSyncSwitch,
       "almCommunicationFail": almCommunicationFail,
       "almPowerAFail": almPowerAFail,
       "almPowerBFail": almPowerBFail,
       "almInterfaceLinkMismatch": almInterfaceLinkMismatch,
       "almInterfaceCardFail": almInterfaceCardFail,
       "almAIC": almAIC,
       "almDbmsCfgCorrupted": almDbmsCfgCorrupted,
       "almDefaultKByteDefect": almDefaultKByteDefect,
       "almInconsistentApsCodes": almInconsistentApsCodes,
       "almImproperApsCodes": almImproperApsCodes,
       "almExtraTrafficIsBeingSquelched": almExtraTrafficIsBeingSquelched,
       "almTopologyNeedsUpdatingOrIsInvalid": almTopologyNeedsUpdatingOrIsInvalid,
       "almSquelchTableNeedsUpdatingOrIsInvalid": almSquelchTableNeedsUpdatingOrIsInvalid,
       "almNodeIdDuplicatedOrMismatched": almNodeIdDuplicatedOrMismatched,
       "almXconMismatched": almXconMismatched,
       "almRingModeMisatch": almRingModeMisatch,
       "almSquelchModeMismatch": almSquelchModeMismatch,
       "almLockoutProtectionSpan": almLockoutProtectionSpan,
       "almLockoutWorkingRing": almLockoutWorkingRing,
       "almLockoutWorkingSpan": almLockoutWorkingSpan,
       "almForceSwitchOfRing": almForceSwitchOfRing,
       "almForceSwitchOfSpan": almForceSwitchOfSpan,
       "almManualSwitchOfRing": almManualSwitchOfRing,
       "almManualSwitchOfSpan": almManualSwitchOfSpan,
       "almExerciseSwitchRing": almExerciseSwitchRing,
       "almExerciseSwitchSpan": almExerciseSwitchSpan,
       "almLockoutProtectionForAllSpans": almLockoutProtectionForAllSpans,
       "almRingSwitch": almRingSwitch,
       "almSpanSwitch": almSpanSwitch,
       "almSwitchToPassthru": almSwitchToPassthru,
       "almPersistentLineSquelching": almPersistentLineSquelching,
       "almDbmsCfgBackupFailed": almDbmsCfgBackupFailed,
       "almFanFailures": almFanFailures,
       "almInvalidEQPT": almInvalidEQPT,
       "almLaserApdBiasVoltageHigh": almLaserApdBiasVoltageHigh,
       "almLaserApdBiasVoltageLow": almLaserApdBiasVoltageLow,
       "almLBCHigh": almLBCHigh,
       "almLBCLow": almLBCLow,
       "almLCCHigh": almLCCHigh,
       "almLCCLow": almLCCLow,
       "almLinkError": almLinkError,
       "almLOA": almLOA,
       "almLOF": almLOF,
       "almLOMPath": almLOMPath,
       "almLOS": almLOS,
       "almLaserTemperatureHigh": almLaserTemperatureHigh,
       "almLaserTemperatureLow": almLaserTemperatureLow,
       "almNeBdDataMismatch": almNeBdDataMismatch,
       "almNoLaserParameter": almNoLaserParameter,
       "almSyncReferenceSourceFailure": almSyncReferenceSourceFailure,
       "almSignalDegradeVT": almSignalDegradeVT,
       "almSignalFailureVT": almSignalFailureVT,
       "almSequenceNumberMismatchedVT": almSequenceNumberMismatchedVT,
       "almSoftwareVersionMismatch": almSoftwareVersionMismatch,
       "almTemperatureHigh": almTemperatureHigh,
       "almAIS": almAIS,
       "almLoopbackInhibited": almLoopbackInhibited,
       "almLockoutOfTheProtocol": almLockoutOfTheProtocol,
       "almLaserShutDown": almLaserShutDown,
       "almLoopbackAllDS1FEAC": almLoopbackAllDS1FEAC,
       "almLoopbackCrossConnect": almLoopbackCrossConnect,
       "almLoopbackDS1FEAC": almLoopbackDS1FEAC,
       "almLoopbackDS3FEAC": almLoopbackDS3FEAC,
       "almLoopbackFacilityPath": almLoopbackFacilityPath,
       "almLoopbackTerminalPath": almLoopbackTerminalPath,
       "almPrimaryChannelChange": almPrimaryChannelChange,
       "almRAI": almRAI,
       "almSsmDQL": almSsmDQL,
       "almSsmLOS": almSsmLOS,
       "almTestSessionActive": almTestSessionActive,
       "almNormalSyncMode": almNormalSyncMode,
       "almSwitchProtectionToWorkingUnit": almSwitchProtectionToWorkingUnit,
       "almSwtichWokingToProtectingUnit": almSwtichWokingToProtectingUnit,
       "almATECardOfflineOrUninstalled": almATECardOfflineOrUninstalled,
       "almPIUCardOfflineOrUninstalled": almPIUCardOfflineOrUninstalled,
       "almOOF": almOOF,
       "almExerciseSwitchSuccess": almExerciseSwitchSuccess,
       "almExerciseSwitchFail": almExerciseSwitchFail,
       "almUpgradeInProcess": almUpgradeInProcess,
       "almChassisMea": almChassisMea,
       "almLaserNotExist": almLaserNotExist,
       "almLCASBandwidthReduced": almLCASBandwidthReduced,
       "almGFPLossOfFrame": almGFPLossOfFrame,
       "almFanIsOpened": almFanIsOpened,
       "almFanIsClosed": almFanIsClosed,
       "almPathLevelMismatch": almPathLevelMismatch,
       "almTcaCVLine": almTcaCVLine,
       "almDCCFailureIndication": almDCCFailureIndication,
       "almLanLossOfCarrierSignal": almLanLossOfCarrierSignal,
       "almTcaCVCPPath": almTcaCVCPPath,
       "almTcaCVPath": almTcaCVPath,
       "almTcaCVPPath": almTcaCVPPath,
       "almTcaCVSection": almTcaCVSection,
       "almTcaCVVT": almTcaCVVT,
       "almTcaESCPPath": almTcaESCPPath,
       "almTcaESLine": almTcaESLine,
       "almTcaESPath": almTcaESPath,
       "almTcaESPPath": almTcaESPPath,
       "almTcaESSection": almTcaESSection,
       "almTcaESVT": almTcaESVT,
       "almTcaPjcsPdet": almTcaPjcsPdet,
       "almTcaPjcsVdet": almTcaPjcsVdet,
       "almTcaSESCPPath": almTcaSESCPPath,
       "almTcaSESLine": almTcaSESLine,
       "almTcaSESPath": almTcaSESPath,
       "almTcaSESPPath": almTcaSESPPath,
       "almTcaSESSection": almTcaSESSection,
       "almTcaSESVT": almTcaSESVT,
       "almTcaUASCPPath": almTcaUASCPPath,
       "almTcaUASLine": almTcaUASLine,
       "almTcaUASPath": almTcaUASPath,
       "almTcaUASPPath": almTcaUASPPath,
       "almTcaUASVT": almTcaUASVT,
       "almBitsAIS": almBitsAIS,
       "almBitsLOF": almBitsLOF,
       "almBitsLOS": almBitsLOS,
       "almBitsCodeViolationOver": almBitsCodeViolationOver,
       "almBlsrSFofRing": almBlsrSFofRing,
       "almBlsrSFofSpan": almBlsrSFofSpan,
       "almBlsrSDofRing": almBlsrSDofRing,
       "almBlsrSDofSpan": almBlsrSDofSpan,
       "almBlsrNodeIsolate": almBlsrNodeIsolate,
       "almSF": almSF,
       "almSD": almSD,
       "almAutoSwitch": almAutoSwitch,
       "almLcasPlct": almLcasPlct,
       "almLcasPlcr": almLcasPlcr,
       "almLcasTlct": almLcasTlct,
       "almLcasTlcr": almLcasTlcr,
       "almLcasFopt": almLcasFopt,
       "almLcasFopr": almLcasFopr,
       "almLoopbackFAC2NI": almLoopbackFAC2NI,
       "almGfpCsf": almGfpCsf,
       "almRevertiveModeMismatch": almRevertiveModeMismatch,
       "almRingIDMismatch": almRingIDMismatch,
       "almIncorrectFiberConnection": almIncorrectFiberConnection,
       "almStateChange": almStateChange,
       "almMtMode": almMtMode,
       "almRmvToMt": almRmvToMt,
       "almRstFromMt": almRstFromMt,
       "almLpbk": almLpbk,
       "almRlsLpbk": almRlsLpbk,
       "almSyncNotSyncnronized": almSyncNotSyncnronized,
       "almPowerExceed": almPowerExceed,
       "almPartialUnprotected": almPartialUnprotected,
       "almFanMea": almFanMea,
       "almRemoteClientSF": almRemoteClientSF,
       "almRemoteClientSD": almRemoteClientSD,
       "almPowerSwitch": almPowerSwitch,
       "almPortOffline": almPortOffline,
       "almDataLost": almDataLost,
       "almSqmVT": almSqmVT,
       "almLomVT": almLomVT,
       "almFCSError": almFCSError,
       "optixTrapsEvent": optixTrapsEvent,
       "evtLossOfClock": evtLossOfClock,
       "evtFileLost": evtFileLost,
       "evtREILine": evtREILine,
       "evtBiasTemperatureOfPumpHigh": evtBiasTemperatureOfPumpHigh,
       "evtTimSection": evtTimSection,
       "evtLossOfAllSynchronousSource": evtLossOfAllSynchronousSource,
       "evtSynchronousSourceDegrade": evtSynchronousSourceDegrade,
       "evtSyncLOS": evtSyncLOS,
       "evtProtectionSwitching": evtProtectionSwitching,
       "evtDbmsError": evtDbmsError,
       "evtLossOfMultiplexSignal": evtLossOfMultiplexSignal,
       "evtLossOfSingleWavelengthSignal": evtLossOfSingleWavelengthSignal,
       "evtAdditionOfSingleWavelengthSignal": evtAdditionOfSingleWavelengthSignal,
       "evtLaserDegraded": evtLaserDegraded,
       "evtPumpDiodeCoolingCurrentHigh": evtPumpDiodeCoolingCurrentHigh,
       "evtS1ModeSynChange": evtS1ModeSynChange,
       "evtDbmsIsInProtectMode": evtDbmsIsInProtectMode,
       "evtSecuAlarm": evtSecuAlarm,
       "evtForwardErrorCorrectionLossOfFrame": evtForwardErrorCorrectionLossOfFrame,
       "evtForwardErrorCorrectionOutOfFrame": evtForwardErrorCorrectionOutOfFrame,
       "evtRateOver": evtRateOver,
       "evtCardConfigurationFail": evtCardConfigurationFail,
       "evtLoopback": evtLoopback,
       "evtCoolingCurrentModeHigh": evtCoolingCurrentModeHigh,
       "evtOTULossOfFrame": evtOTULossOfFrame,
       "evtOTUOutOfMultiFrame": evtOTUOutOfMultiFrame,
       "evtSmTIM": evtSmTIM,
       "evtPmTIM": evtPmTIM,
       "evtSmBDI": evtSmBDI,
       "evtPmBDI": evtPmBDI,
       "evtSmBEI": evtSmBEI,
       "evtPmBEI": evtPmBEI,
       "evtSmIAE": evtSmIAE,
       "evtSmBipExcessive": evtSmBipExcessive,
       "evtPmBipExcessive": evtPmBipExcessive,
       "evtSmBipSignalDefect": evtSmBipSignalDefect,
       "evtPmBipSignalDefect": evtPmBipSignalDefect,
       "evtOTUAlarmIndicationSignal": evtOTUAlarmIndicationSignal,
       "evtODUAlarmIndicationSignal": evtODUAlarmIndicationSignal,
       "evtODUOpenConnectionIndicationSignal": evtODUOpenConnectionIndicationSignal,
       "evtODULockedIndicationSignal": evtODULockedIndicationSignal,
       "evtSumInputOpticalPowerHigh": evtSumInputOpticalPowerHigh,
       "evtSumInputOpticalPowerLow": evtSumInputOpticalPowerLow,
       "evtSumOutOpticalPowerHigh": evtSumOutOpticalPowerHigh,
       "evtOutOpticalPowerLow": evtOutOpticalPowerLow,
       "evtGainLow": evtGainLow,
       "evtExcessiveErrorDefectBeforeFEC": evtExcessiveErrorDefectBeforeFEC,
       "evtDgeAdjustmentFail": evtDgeAdjustmentFail,
       "evtWavelengthLockFail": evtWavelengthLockFail,
       "evtHotSwitchControlUnavail": evtHotSwitchControlUnavail,
       "evtEsconCodeError": evtEsconCodeError,
       "evtCommitTimeout": evtCommitTimeout,
       "evtSwdlNePackageCheck": evtSwdlNePackageCheck,
       "evtSwdlChaGmngmMismatch": evtSwdlChaGmngmMismatch,
       "evtDBSyncFail": evtDBSyncFail,
       "evtClientMismatch": evtClientMismatch,
       "evtLaserModuleMismatch": evtLaserModuleMismatch,
       "evtLptRfi": evtLptRfi,
       "evtEqptNoServiceAffecting": evtEqptNoServiceAffecting,
       "evtEqptServiceAffectingFail": evtEqptServiceAffectingFail,
       "evtApsByteFailure": evtApsByteFailure,
       "evtFarEndProtectionLineFailure": evtFarEndProtectionLineFailure,
       "evtApsChannelMismatchFailure": evtApsChannelMismatchFailure,
       "evtApsModeMismatch": evtApsModeMismatch,
       "evtApsTypeMismatch": evtApsTypeMismatch,
       "evtHoldoverSync": evtHoldoverSync,
       "evtFreeRunSync": evtFreeRunSync,
       "evtFastStartSync": evtFastStartSync,
       "evtManualSetSSM": evtManualSetSSM,
       "evtFanOffline": evtFanOffline,
       "evtSingleFanFail": evtSingleFanFail,
       "evtMultiFanFail": evtMultiFanFail,
       "evtEquipmentTypeMismatch": evtEquipmentTypeMismatch,
       "evtEquipmentOfflineOrUninstalled": evtEquipmentOfflineOrUninstalled,
       "evtTransmitterFailure": evtTransmitterFailure,
       "evtSignalFailureSection": evtSignalFailureSection,
       "evtInputPowerHigh": evtInputPowerHigh,
       "evtInputPowerLow": evtInputPowerLow,
       "evtSignalFailureLine": evtSignalFailureLine,
       "evtSignalDegradeLine": evtSignalDegradeLine,
       "evtLaserApprochingEndOfLife": evtLaserApprochingEndOfLife,
       "evtOutPowerHigh": evtOutPowerHigh,
       "evtOutPowerLow": evtOutPowerLow,
       "evtSignalDegradeSection": evtSignalDegradeSection,
       "evtAlarmIndicationSignalLine": evtAlarmIndicationSignalLine,
       "evtRemoteFailureIindicationLine": evtRemoteFailureIindicationLine,
       "evtAlarmIndicationSignalPath": evtAlarmIndicationSignalPath,
       "evtLossOfPointerPath": evtLossOfPointerPath,
       "evtTraceIdentifierMismatchPath": evtTraceIdentifierMismatchPath,
       "evtUnequippedPath": evtUnequippedPath,
       "evtSignalFailurePath": evtSignalFailurePath,
       "evtSignalDegradePath": evtSignalDegradePath,
       "evtRemoteFailureIindicationPath": evtRemoteFailureIindicationPath,
       "evtALS": evtALS,
       "evtLoopbackFacility": evtLoopbackFacility,
       "evtLoopbackTerminal": evtLoopbackTerminal,
       "evtPayloadLabelMisatch": evtPayloadLabelMisatch,
       "evtEnhancedRemotePalyloadFailureIndicationPath": evtEnhancedRemotePalyloadFailureIndicationPath,
       "evtEnhancedRemoteServerFailureIndicationPath": evtEnhancedRemoteServerFailureIndicationPath,
       "evtEnhancedRemoteConnectivityFailureIndicationPath": evtEnhancedRemoteConnectivityFailureIndicationPath,
       "evtPDIPath": evtPDIPath,
       "evtPowerFail": evtPowerFail,
       "evtLossOfPointerVT": evtLossOfPointerVT,
       "evtAlarmIndicationSignalVT": evtAlarmIndicationSignalVT,
       "evtPayloadLabelMismatchVT": evtPayloadLabelMismatchVT,
       "evtUnequippedVT": evtUnequippedVT,
       "evtRemoteFailureIndicationVT": evtRemoteFailureIndicationVT,
       "evtRemoteServerFailureIndicationVT": evtRemoteServerFailureIndicationVT,
       "evtEnhancedRemoteConnectivityFailureIndicationVT": evtEnhancedRemoteConnectivityFailureIndicationVT,
       "evtEnhancedRemotePalyloadFailureIndicationVT": evtEnhancedRemotePalyloadFailureIndicationVT,
       "evtInterFaceCardOffline": evtInterFaceCardOffline,
       "evtSyncChangeSSM": evtSyncChangeSSM,
       "evtTimeingModeChange": evtTimeingModeChange,
       "evtLockoutWorkingUnit": evtLockoutWorkingUnit,
       "evtLockoutProtectionUnit": evtLockoutProtectionUnit,
       "evtForcedSwitch": evtForcedSwitch,
       "evtManualSwitch": evtManualSwitch,
       "evtExerciseSwitch": evtExerciseSwitch,
       "evtWaitToRestore": evtWaitToRestore,
       "evtSwitchToIdle": evtSwitchToIdle,
       "evtSwitchFail": evtSwitchFail,
       "evtSyncSwitch": evtSyncSwitch,
       "evtCommunicationFail": evtCommunicationFail,
       "evtPowerAFail": evtPowerAFail,
       "evtPowerBFail": evtPowerBFail,
       "evtInterfaceLinkMismatch": evtInterfaceLinkMismatch,
       "evtInterfaceCardFail": evtInterfaceCardFail,
       "evtAIC": evtAIC,
       "evtDbmsCfgCorrupted": evtDbmsCfgCorrupted,
       "evtDefaultKByteDefect": evtDefaultKByteDefect,
       "evtInconsistentApsCodes": evtInconsistentApsCodes,
       "evtImproperApsCodes": evtImproperApsCodes,
       "evtExtraTrafficIsBeingSquelched": evtExtraTrafficIsBeingSquelched,
       "evtTopologyNeedsUpdatingOrIsInvalid": evtTopologyNeedsUpdatingOrIsInvalid,
       "evtSquelchTableNeedsUpdatingOrIsInvalid": evtSquelchTableNeedsUpdatingOrIsInvalid,
       "evtNodeIdDuplicatedOrMismatched": evtNodeIdDuplicatedOrMismatched,
       "evtXconMismatched": evtXconMismatched,
       "evtRingModeMisatch": evtRingModeMisatch,
       "evtSquelchModeMismatch": evtSquelchModeMismatch,
       "evtLockoutProtectionSpan": evtLockoutProtectionSpan,
       "evtLockoutWorkingRing": evtLockoutWorkingRing,
       "evtLockoutWorkingSpan": evtLockoutWorkingSpan,
       "evtForceSwitchOfRing": evtForceSwitchOfRing,
       "evtForceSwitchOfSpan": evtForceSwitchOfSpan,
       "evtManualSwitchOfRing": evtManualSwitchOfRing,
       "evtManualSwitchOfSpan": evtManualSwitchOfSpan,
       "evtExerciseSwitchRing": evtExerciseSwitchRing,
       "evtExerciseSwitchSpan": evtExerciseSwitchSpan,
       "evtLockoutProtectionForAllSpans": evtLockoutProtectionForAllSpans,
       "evtRingSwitch": evtRingSwitch,
       "evtSpanSwitch": evtSpanSwitch,
       "evtSwitchToPassthru": evtSwitchToPassthru,
       "evtPersistentLineSquelching": evtPersistentLineSquelching,
       "evtDbmsCfgBackupFailed": evtDbmsCfgBackupFailed,
       "evtFanFailures": evtFanFailures,
       "evtInvalidEQPT": evtInvalidEQPT,
       "evtLaserApdBiasVoltageHigh": evtLaserApdBiasVoltageHigh,
       "evtLaserApdBiasVoltageLow": evtLaserApdBiasVoltageLow,
       "evtLBCHigh": evtLBCHigh,
       "evtLBCLow": evtLBCLow,
       "evtLCCHigh": evtLCCHigh,
       "evtLCCLow": evtLCCLow,
       "evtLinkError": evtLinkError,
       "evtLOA": evtLOA,
       "evtLOF": evtLOF,
       "evtLOMPath": evtLOMPath,
       "evtLOS": evtLOS,
       "evtLaserTemperatureHigh": evtLaserTemperatureHigh,
       "evtLaserTemperatureLow": evtLaserTemperatureLow,
       "evtNeBdDataMismatch": evtNeBdDataMismatch,
       "evtNoLaserParameter": evtNoLaserParameter,
       "evtSyncReferenceSourceFailure": evtSyncReferenceSourceFailure,
       "evtSignalDegradeVT": evtSignalDegradeVT,
       "evtSignalFailureVT": evtSignalFailureVT,
       "evtSequenceNumberMismatchedVT": evtSequenceNumberMismatchedVT,
       "evtSoftwareVersionMismatch": evtSoftwareVersionMismatch,
       "evtTemperatureHigh": evtTemperatureHigh,
       "evtAIS": evtAIS,
       "evtLoopbackInhibited": evtLoopbackInhibited,
       "evtLockoutOfTheProtocol": evtLockoutOfTheProtocol,
       "evtLaserShutDown": evtLaserShutDown,
       "evtLoopbackAllDS1FEAC": evtLoopbackAllDS1FEAC,
       "evtLoopbackCrossConnect": evtLoopbackCrossConnect,
       "evtLoopbackDS1FEAC": evtLoopbackDS1FEAC,
       "evtLoopbackDS3FEAC": evtLoopbackDS3FEAC,
       "evtLoopbackFacilityPath": evtLoopbackFacilityPath,
       "evtLoopbackTerminalPath": evtLoopbackTerminalPath,
       "evtPrimaryChannelChange": evtPrimaryChannelChange,
       "evtRAI": evtRAI,
       "evtSsmDQL": evtSsmDQL,
       "evtSsmLOS": evtSsmLOS,
       "evtTestSessionActive": evtTestSessionActive,
       "evtNormalSyncMode": evtNormalSyncMode,
       "evtSwitchProtectionToWorkingUnit": evtSwitchProtectionToWorkingUnit,
       "evtSwtichWokingToProtectingUnit": evtSwtichWokingToProtectingUnit,
       "evtATECardOfflineOrUninstalled": evtATECardOfflineOrUninstalled,
       "evtPIUCardOfflineOrUninstalled": evtPIUCardOfflineOrUninstalled,
       "evtOOF": evtOOF,
       "evtExerciseSwitchSuccess": evtExerciseSwitchSuccess,
       "evtExerciseSwitchFail": evtExerciseSwitchFail,
       "evtUpgradeInProcess": evtUpgradeInProcess,
       "evtChassisMea": evtChassisMea,
       "evtLaserNotExist": evtLaserNotExist,
       "evtLCASBandwidthReduced": evtLCASBandwidthReduced,
       "evtGFPLossOfFrame": evtGFPLossOfFrame,
       "evtFanIsOpened": evtFanIsOpened,
       "evtFanIsClosed": evtFanIsClosed,
       "evtPathLevelMismatch": evtPathLevelMismatch,
       "evtTcaCVLine": evtTcaCVLine,
       "evtDCCFailureIndication": evtDCCFailureIndication,
       "evtLanLossOfCarrierSignal": evtLanLossOfCarrierSignal,
       "evtTcaCVCPPath": evtTcaCVCPPath,
       "evtTcaCVPath": evtTcaCVPath,
       "evtTcaCVPPath": evtTcaCVPPath,
       "evtTcaCVSection": evtTcaCVSection,
       "evtTcaCVVT": evtTcaCVVT,
       "evtTcaESCPPath": evtTcaESCPPath,
       "evtTcaESLine": evtTcaESLine,
       "evtTcaESPath": evtTcaESPath,
       "evtTcaESPPath": evtTcaESPPath,
       "evtTcaESSection": evtTcaESSection,
       "evtTcaESVT": evtTcaESVT,
       "evtTcaPjcsPdet": evtTcaPjcsPdet,
       "evtTcaPjcsVdet": evtTcaPjcsVdet,
       "evtTcaSESCPPath": evtTcaSESCPPath,
       "evtTcaSESLine": evtTcaSESLine,
       "evtTcaSESPath": evtTcaSESPath,
       "evtTcaSESPPath": evtTcaSESPPath,
       "evtTcaSESSection": evtTcaSESSection,
       "evtTcaSESVT": evtTcaSESVT,
       "evtTcaUASCPPath": evtTcaUASCPPath,
       "evtTcaUASLine": evtTcaUASLine,
       "evtTcaUASPath": evtTcaUASPath,
       "evtTcaUASPPath": evtTcaUASPPath,
       "evtTcaUASVT": evtTcaUASVT,
       "evtBitsAIS": evtBitsAIS,
       "evtBitsLOF": evtBitsLOF,
       "evtBitsLOS": evtBitsLOS,
       "evtBitsCodeViolationOver": evtBitsCodeViolationOver,
       "evtBlsrSFofRing": evtBlsrSFofRing,
       "evtBlsrSFofSpan": evtBlsrSFofSpan,
       "evtBlsrSDofRing": evtBlsrSDofRing,
       "evtBlsrSDofSpan": evtBlsrSDofSpan,
       "evtBlsrNodeIsolate": evtBlsrNodeIsolate,
       "evtSF": evtSF,
       "evtSD": evtSD,
       "evtAutoSwitch": evtAutoSwitch,
       "evtLcasPlct": evtLcasPlct,
       "evtLcasPlcr": evtLcasPlcr,
       "evtLcasTlct": evtLcasTlct,
       "evtLcasTlcr": evtLcasTlcr,
       "evtLcasFopt": evtLcasFopt,
       "evtLcasFopr": evtLcasFopr,
       "evtLoopbackFAC2NI": evtLoopbackFAC2NI,
       "evtGfpCsf": evtGfpCsf,
       "evtRevertiveModeMismatch": evtRevertiveModeMismatch,
       "evtRingIDMismatch": evtRingIDMismatch,
       "evtIncorrectFiberConnection": evtIncorrectFiberConnection,
       "evtStateChange": evtStateChange,
       "evtMtMode": evtMtMode,
       "evtRmvToMt": evtRmvToMt,
       "evtRstFromMt": evtRstFromMt,
       "evtLpbk": evtLpbk,
       "evtRlsLpbk": evtRlsLpbk,
       "evtSyncNotSyncnronized": evtSyncNotSyncnronized,
       "evtPowerExceed": evtPowerExceed,
       "evtPartialUnprotected": evtPartialUnprotected,
       "evtFanMea": evtFanMea,
       "evtRemoteClientSF": evtRemoteClientSF,
       "evtRemoteClientSD": evtRemoteClientSD,
       "evtPowerSwitch": evtPowerSwitch,
       "evtPortOffline": evtPortOffline,
       "evtDataLost": evtDataLost,
       "evtSqmVT": evtSqmVT,
       "evtLomVT": evtLomVT,
       "evtFCSError": evtFCSError,
       "optixTrapsEnvironment": optixTrapsEnvironment,
       "envAirCompressorFailure": envAirCompressorFailure,
       "envAirConditioningFailure": envAirConditioningFailure,
       "envAirDryerFailure": envAirDryerFailure,
       "envBatteryDischarging": envBatteryDischarging,
       "envBatteryFailure": envBatteryFailure,
       "envCoolingFacFailure": envCoolingFacFailure,
       "envCPMAJOR": envCPMAJOR,
       "envCPMINOR": envCPMINOR,
       "envEngineFailure": envEngineFailure,
       "envEngineOperating": envEngineOperating,
       "envExplosiveGas": envExplosiveGas,
       "envFireDetectorFailure": envFireDetectorFailure,
       "envFire": envFire,
       "envFlood": envFlood,
       "envFuseFailure": envFuseFailure,
       "envGeneratorFailure": envGeneratorFailure,
       "envHighAirflow": envHighAirflow,
       "envHighHumidity": envHighHumidity,
       "envHighTemperature": envHighTemperature,
       "envHighWater": envHighWater,
       "envIntrusion": envIntrusion,
       "envLowBatteryVoltage": envLowBatteryVoltage,
       "envLowFuel": envLowFuel,
       "envLowHumidity": envLowHumidity,
       "envLowCablePressure": envLowCablePressure,
       "envLowTemperature": envLowTemperature,
       "envLowWater": envLowWater,
       "envMiscellaneous": envMiscellaneous,
       "envOpenDoor": envOpenDoor,
       "envCommercialPowerFailure": envCommercialPowerFailure,
       "envPumpFailure": envPumpFailure,
       "env48VoltPowerSupplyFailure": env48VoltPowerSupplyFailure,
       "envRectifierFailure": envRectifierFailure,
       "envRectifierHighVoltage": envRectifierHighVoltage,
       "envRectiFierLowVoltage": envRectiFierLowVoltage,
       "envSmoke": envSmoke,
       "envToxicGas": envToxicGas,
       "envVentilationSystemFailure": envVentilationSystemFailure,
       "optixTrapsPerformance": optixTrapsPerformance,
       "pmSESSection": pmSESSection,
       "pmCVLine": pmCVLine,
       "pmESLine": pmESLine,
       "pmSESLine": pmSESLine,
       "pmUASLine": pmUASLine,
       "pmPSD": pmPSD,
       "pmCVPath": pmCVPath,
       "pmESPath": pmESPath,
       "pmPjcsVdet": pmPjcsVdet,
       "pmBdTempCur": pmBdTempCur,
       "pmBdTempMax": pmBdTempMax,
       "pmBdTempMin": pmBdTempMin,
       "pmPmuTempCur": pmPmuTempCur,
       "pmPmuTempMax": pmPmuTempMax,
       "pmPmuTempMin": pmPmuTempMin,
       "pmLbcCur": pmLbcCur,
       "pmLbcMax": pmLbcMax,
       "pmLbcMin": pmLbcMin,
       "pmOptCur": pmOptCur,
       "pmOptMax": pmOptMax,
       "pmOptMin": pmOptMin,
       "pmOprCur": pmOprCur,
       "pmOprMax": pmOprMax,
       "pmOprMin": pmOprMin,
       "pmCVPPath": pmCVPPath,
       "pmCVCPPath": pmCVCPPath,
       "pmESPPath": pmESPPath,
       "pmESCPPath": pmESCPPath,
       "pmSESPPath": pmSESPPath,
       "pmSESCPPath": pmSESCPPath,
       "pmUASPPath": pmUASPPath,
       "pmUASCPPath": pmUASCPPath,
       "pmPscProtection": pmPscProtection,
       "pmPsdProtection": pmPsdProtection,
       "pmPscSpan": pmPscSpan,
       "pmPsdSpan": pmPsdSpan,
       "pmPscRing": pmPscRing,
       "pmPsdRing": pmPsdRing,
       "pmPscWork": pmPscWork,
       "pmPsdWork": pmPsdWork,
       "pmLCCCur": pmLCCCur,
       "pmLCCMax": pmLCCMax,
       "pmLCCMin": pmLCCMin,
       "pmLTEMPCur": pmLTEMPCur,
       "pmLTEMPMax": pmLTEMPMax,
       "pmLTEMPMin": pmLTEMPMin,
       "pmLAPDBVCur": pmLAPDBVCur,
       "pmLAPDBVMax": pmLAPDBVMax,
       "pmLAPDBVMin": pmLAPDBVMin,
       "pmPLBCCur": pmPLBCCur,
       "pmPLBCMax": pmPLBCMax,
       "pmPLBCMin": pmPLBCMin,
       "pmPLWCCur": pmPLWCCur,
       "pmPLWCMax": pmPLWCMax,
       "pmPLWCMin": pmPLWCMin,
       "pmCVSection": pmCVSection,
       "pmESSection": pmESSection,
       "pmSESPath": pmSESPath,
       "pmUASPath": pmUASPath,
       "pmCVVT": pmCVVT,
       "pmESVT": pmESVT,
       "pmSESVT": pmSESVT,
       "pmUASVT": pmUASVT,
       "pmPSC": pmPSC,
       "pmPjcsPdet": pmPjcsPdet,
       "optixTrapsCommon": optixTrapsCommon,
       "rptAlmName": rptAlmName,
       "rptEvtMOD2": rptEvtMOD2,
       "rptEvtSlot": rptEvtSlot,
       "rptEvtPort": rptEvtPort,
       "rptEvtPath": rptEvtPath,
       "rptEvtVT": rptEvtVT,
       "rptEvtDateTime": rptEvtDateTime,
       "rptEvtSrvEff": rptEvtSrvEff,
       "rptEvtNtfcnCde": rptEvtNtfcnCde,
       "rptEvtLocation": rptEvtLocation,
       "rptEvtDirection": rptEvtDirection,
       "rptEvtMonValue": rptEvtMonValue,
       "rptEvtThValue": rptEvtThValue,
       "rptEvtDescription": rptEvtDescription,
       "rptEvtNumber": rptEvtNumber,
       "rptEvtPeriod": rptEvtPeriod,
       "rptEvtVldty": rptEvtVldty,
       "rptEvtEffect": rptEvtEffect,
       "rptEvtState": rptEvtState,
       "rptEvtAiddet": rptEvtAiddet,
       "rptEvtSeqNumber": rptEvtSeqNumber,
       "rptPmName": rptPmName,
       "optixSonetTrapsConformance": optixSonetTrapsConformance,
       "optixSonetTrapsGroups": optixSonetTrapsGroups,
       "optixSonetTrapsObjectGroup": optixSonetTrapsObjectGroup,
       "optixSonetTrapsNotificationGroup": optixSonetTrapsNotificationGroup,
       "optixSonetTrapsCompliances": optixSonetTrapsCompliances,
       "optixSonetBasicCompliance": optixSonetBasicCompliance}
)
