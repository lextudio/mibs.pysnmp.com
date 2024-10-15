# SNMP MIB module (MISSION-CRITICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MISSION-CRITICAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:07 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MissionCritical_ObjectIdentity = ObjectIdentity
missionCritical = _MissionCritical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349)
)
_McsCompanyInfo_ObjectIdentity = ObjectIdentity
mcsCompanyInfo = _McsCompanyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 1)
)


class _OwnershipDetails_Type(DisplayString):
    """Custom type ownershipDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OwnershipDetails_Type.__name__ = "DisplayString"
_OwnershipDetails_Object = MibScalar
ownershipDetails = _OwnershipDetails_Object(
    (1, 3, 6, 1, 4, 1, 2349, 1, 1),
    _OwnershipDetails_Type()
)
ownershipDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ownershipDetails.setStatus("mandatory")


class _ContactDetails_Type(DisplayString):
    """Custom type contactDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ContactDetails_Type.__name__ = "DisplayString"
_ContactDetails_Object = MibScalar
contactDetails = _ContactDetails_Object(
    (1, 3, 6, 1, 4, 1, 2349, 1, 2),
    _ContactDetails_Type()
)
contactDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contactDetails.setStatus("mandatory")
_McsSoftware_ObjectIdentity = ObjectIdentity
mcsSoftware = _McsSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2)
)
_EemProductInfo_ObjectIdentity = ObjectIdentity
eemProductInfo = _EemProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1)
)
_EemService_ObjectIdentity = ObjectIdentity
eemService = _EemService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1)
)


class _Version_Type(DisplayString):
    """Custom type version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Version_Type.__name__ = "DisplayString"
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")


class _PrimaryServer_Type(DisplayString):
    """Custom type primaryServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PrimaryServer_Type.__name__ = "DisplayString"
_PrimaryServer_Object = MibScalar
primaryServer = _PrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 2),
    _PrimaryServer_Type()
)
primaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryServer.setStatus("mandatory")


class _ServiceState_Type(Integer32):
    """Custom type serviceState based on Integer32"""
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


_ServiceState_Type.__name__ = "Integer32"
_ServiceState_Object = MibScalar
serviceState = _ServiceState_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 3),
    _ServiceState_Type()
)
serviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceState.setStatus("mandatory")
_ServiceUpTime_Type = TimeTicks
_ServiceUpTime_Object = MibScalar
serviceUpTime = _ServiceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 4),
    _ServiceUpTime_Type()
)
serviceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceUpTime.setStatus("mandatory")
_RedTrapCount_Type = Counter32
_RedTrapCount_Object = MibScalar
redTrapCount = _RedTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 5),
    _RedTrapCount_Type()
)
redTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTrapCount.setStatus("deprecated")
_OrangeTrapCount_Type = Counter32
_OrangeTrapCount_Object = MibScalar
orangeTrapCount = _OrangeTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 6),
    _OrangeTrapCount_Type()
)
orangeTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    orangeTrapCount.setStatus("deprecated")
_AmberTrapCount_Type = Counter32
_AmberTrapCount_Object = MibScalar
amberTrapCount = _AmberTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 7),
    _AmberTrapCount_Type()
)
amberTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amberTrapCount.setStatus("deprecated")
_BlueTrapCount_Type = Counter32
_BlueTrapCount_Object = MibScalar
blueTrapCount = _BlueTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 8),
    _BlueTrapCount_Type()
)
blueTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blueTrapCount.setStatus("deprecated")
_GreenTrapCount_Type = Counter32
_GreenTrapCount_Object = MibScalar
greenTrapCount = _GreenTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 1, 9),
    _GreenTrapCount_Type()
)
greenTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    greenTrapCount.setStatus("deprecated")
_EemLastTrap_ObjectIdentity = ObjectIdentity
eemLastTrap = _EemLastTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2)
)
_TrapTime_Type = TimeTicks
_TrapTime_Object = MibScalar
trapTime = _TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 1),
    _TrapTime_Type()
)
trapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTime.setStatus("deprecated")


class _AlertLevel_Type(Integer32):
    """Custom type alertLevel based on Integer32"""
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
        *(("blue", 4),
          ("green", 5),
          ("orange", 2),
          ("red", 1),
          ("yellow", 3))
    )


_AlertLevel_Type.__name__ = "Integer32"
_AlertLevel_Object = MibScalar
alertLevel = _AlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 2),
    _AlertLevel_Type()
)
alertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertLevel.setStatus("mandatory")


class _LogType_Type(Integer32):
    """Custom type logType based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("activemonitoring", 5),
          ("application", 2),
          ("eem", 99),
          ("ntevent", 1),
          ("performancemonitoring", 6),
          ("snmp", 3),
          ("timedevent", 7),
          ("wbem", 4))
    )


_LogType_Type.__name__ = "Integer32"
_LogType_Object = MibScalar
logType = _LogType_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 3),
    _LogType_Type()
)
logType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logType.setStatus("mandatory")


class _Server_Type(DisplayString):
    """Custom type server based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Server_Type.__name__ = "DisplayString"
_Server_Object = MibScalar
server = _Server_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 4),
    _Server_Type()
)
server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    server.setStatus("mandatory")


class _Source_Type(DisplayString):
    """Custom type source based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Source_Type.__name__ = "DisplayString"
_Source_Object = MibScalar
source = _Source_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 5),
    _Source_Type()
)
source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    source.setStatus("mandatory")


class _User_Type(DisplayString):
    """Custom type user based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_User_Type.__name__ = "DisplayString"
_User_Object = MibScalar
user = _User_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 6),
    _User_Type()
)
user.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user.setStatus("mandatory")
_EventID_Type = Integer32
_EventID_Object = MibScalar
eventID = _EventID_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 7),
    _EventID_Type()
)
eventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventID.setStatus("mandatory")


class _Description_Type(DisplayString):
    """Custom type description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_Description_Type.__name__ = "DisplayString"
_Description_Object = MibScalar
description = _Description_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 8),
    _Description_Type()
)
description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    description.setStatus("mandatory")
_GenericTrapNumber_Type = Integer32
_GenericTrapNumber_Object = MibScalar
genericTrapNumber = _GenericTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 9),
    _GenericTrapNumber_Type()
)
genericTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTrapNumber.setStatus("mandatory")
_SpecificTrapNumber_Type = Integer32
_SpecificTrapNumber_Object = MibScalar
specificTrapNumber = _SpecificTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 2, 10),
    _SpecificTrapNumber_Type()
)
specificTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificTrapNumber.setStatus("mandatory")
_OmProductInfo_ObjectIdentity = ObjectIdentity
omProductInfo = _OmProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2)
)
_OmService_ObjectIdentity = ObjectIdentity
omService = _OmService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 1)
)
_OmLastTrap_ObjectIdentity = ObjectIdentity
omLastTrap = _OmLastTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2)
)
_OmTrapTime_Type = TimeTicks
_OmTrapTime_Object = MibScalar
omTrapTime = _OmTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 1),
    _OmTrapTime_Type()
)
omTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omTrapTime.setStatus("deprecated")
_OmAlertLevel_Type = Integer32
_OmAlertLevel_Object = MibScalar
omAlertLevel = _OmAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 2),
    _OmAlertLevel_Type()
)
omAlertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omAlertLevel.setStatus("mandatory")


class _OmAlertLevelName_Type(DisplayString):
    """Custom type omAlertLevelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmAlertLevelName_Type.__name__ = "DisplayString"
_OmAlertLevelName_Object = MibScalar
omAlertLevelName = _OmAlertLevelName_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 3),
    _OmAlertLevelName_Type()
)
omAlertLevelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omAlertLevelName.setStatus("mandatory")


class _OmServer_Type(DisplayString):
    """Custom type omServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmServer_Type.__name__ = "DisplayString"
_OmServer_Object = MibScalar
omServer = _OmServer_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 4),
    _OmServer_Type()
)
omServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omServer.setStatus("mandatory")


class _OmSource_Type(DisplayString):
    """Custom type omSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmSource_Type.__name__ = "DisplayString"
_OmSource_Object = MibScalar
omSource = _OmSource_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 5),
    _OmSource_Type()
)
omSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omSource.setStatus("mandatory")


class _OmOwner_Type(DisplayString):
    """Custom type omOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OmOwner_Type.__name__ = "DisplayString"
_OmOwner_Object = MibScalar
omOwner = _OmOwner_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 6),
    _OmOwner_Type()
)
omOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omOwner.setStatus("mandatory")


class _OmDescription_Type(DisplayString):
    """Custom type omDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OmDescription_Type.__name__ = "DisplayString"
_OmDescription_Object = MibScalar
omDescription = _OmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 7),
    _OmDescription_Type()
)
omDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omDescription.setStatus("mandatory")


class _OmCustomField1_Type(DisplayString):
    """Custom type omCustomField1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OmCustomField1_Type.__name__ = "DisplayString"
_OmCustomField1_Object = MibScalar
omCustomField1 = _OmCustomField1_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 8),
    _OmCustomField1_Type()
)
omCustomField1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omCustomField1.setStatus("mandatory")


class _OmCustomField2_Type(DisplayString):
    """Custom type omCustomField2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OmCustomField2_Type.__name__ = "DisplayString"
_OmCustomField2_Object = MibScalar
omCustomField2 = _OmCustomField2_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 9),
    _OmCustomField2_Type()
)
omCustomField2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omCustomField2.setStatus("mandatory")


class _OmCustomField3_Type(DisplayString):
    """Custom type omCustomField3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OmCustomField3_Type.__name__ = "DisplayString"
_OmCustomField3_Object = MibScalar
omCustomField3 = _OmCustomField3_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 10),
    _OmCustomField3_Type()
)
omCustomField3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omCustomField3.setStatus("mandatory")


class _OmCustomField4_Type(DisplayString):
    """Custom type omCustomField4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OmCustomField4_Type.__name__ = "DisplayString"
_OmCustomField4_Object = MibScalar
omCustomField4 = _OmCustomField4_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 11),
    _OmCustomField4_Type()
)
omCustomField4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omCustomField4.setStatus("mandatory")


class _OmCustomField5_Type(DisplayString):
    """Custom type omCustomField5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OmCustomField5_Type.__name__ = "DisplayString"
_OmCustomField5_Object = MibScalar
omCustomField5 = _OmCustomField5_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 12),
    _OmCustomField5_Type()
)
omCustomField5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omCustomField5.setStatus("mandatory")


class _OmAlertURL_Type(DisplayString):
    """Custom type omAlertURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_OmAlertURL_Type.__name__ = "DisplayString"
_OmAlertURL_Object = MibScalar
omAlertURL = _OmAlertURL_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 13),
    _OmAlertURL_Type()
)
omAlertURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omAlertURL.setStatus("mandatory")
_OmGenericTrapNumber_Type = Integer32
_OmGenericTrapNumber_Object = MibScalar
omGenericTrapNumber = _OmGenericTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 14),
    _OmGenericTrapNumber_Type()
)
omGenericTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omGenericTrapNumber.setStatus("mandatory")
_OmSpecificTrapNumber_Type = Integer32
_OmSpecificTrapNumber_Object = MibScalar
omSpecificTrapNumber = _OmSpecificTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 2, 15),
    _OmSpecificTrapNumber_Type()
)
omSpecificTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omSpecificTrapNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects

serviceGoingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 2)
)
if mibBuilder.loadTexts:
    serviceGoingDown.setStatus(
        ""
    )

serviceComingUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 3)
)
if mibBuilder.loadTexts:
    serviceComingUp.setStatus(
        ""
    )

gathererServiceGoingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 4)
)
if mibBuilder.loadTexts:
    gathererServiceGoingDown.setStatus(
        ""
    )

gathererServiceComingUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 5)
)
if mibBuilder.loadTexts:
    gathererServiceComingUp.setStatus(
        ""
    )

eemRedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 100)
)
eemRedAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "alertLevel"),
        ("MISSION-CRITICAL-MIB", "logType"),
        ("MISSION-CRITICAL-MIB", "server"),
        ("MISSION-CRITICAL-MIB", "source"),
        ("MISSION-CRITICAL-MIB", "user"),
        ("MISSION-CRITICAL-MIB", "eventID"),
        ("MISSION-CRITICAL-MIB", "description"))
)
if mibBuilder.loadTexts:
    eemRedAlert.setStatus(
        ""
    )

eemOrangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 200)
)
eemOrangeAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "alertLevel"),
        ("MISSION-CRITICAL-MIB", "logType"),
        ("MISSION-CRITICAL-MIB", "server"),
        ("MISSION-CRITICAL-MIB", "source"),
        ("MISSION-CRITICAL-MIB", "user"),
        ("MISSION-CRITICAL-MIB", "eventID"),
        ("MISSION-CRITICAL-MIB", "description"))
)
if mibBuilder.loadTexts:
    eemOrangeAlert.setStatus(
        ""
    )

eemYellowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 300)
)
eemYellowAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "alertLevel"),
        ("MISSION-CRITICAL-MIB", "logType"),
        ("MISSION-CRITICAL-MIB", "server"),
        ("MISSION-CRITICAL-MIB", "source"),
        ("MISSION-CRITICAL-MIB", "user"),
        ("MISSION-CRITICAL-MIB", "eventID"),
        ("MISSION-CRITICAL-MIB", "description"))
)
if mibBuilder.loadTexts:
    eemYellowAlert.setStatus(
        ""
    )

eemBlueAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 400)
)
eemBlueAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "alertLevel"),
        ("MISSION-CRITICAL-MIB", "logType"),
        ("MISSION-CRITICAL-MIB", "server"),
        ("MISSION-CRITICAL-MIB", "source"),
        ("MISSION-CRITICAL-MIB", "user"),
        ("MISSION-CRITICAL-MIB", "eventID"),
        ("MISSION-CRITICAL-MIB", "description"))
)
if mibBuilder.loadTexts:
    eemBlueAlert.setStatus(
        ""
    )

eemGreenAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 1, 0, 500)
)
eemGreenAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "alertLevel"),
        ("MISSION-CRITICAL-MIB", "logType"),
        ("MISSION-CRITICAL-MIB", "server"),
        ("MISSION-CRITICAL-MIB", "source"),
        ("MISSION-CRITICAL-MIB", "user"),
        ("MISSION-CRITICAL-MIB", "eventID"),
        ("MISSION-CRITICAL-MIB", "description"))
)
if mibBuilder.loadTexts:
    eemGreenAlert.setStatus(
        ""
    )

omBlueAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 10)
)
omBlueAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omBlueAlert.setStatus(
        ""
    )

omGreenAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 20)
)
omGreenAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omGreenAlert.setStatus(
        ""
    )

omYellowAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 30)
)
omYellowAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omYellowAlert.setStatus(
        ""
    )

omOrangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 40)
)
omOrangeAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omOrangeAlert.setStatus(
        ""
    )

omRedCriticalErrorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 50)
)
omRedCriticalErrorAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omRedCriticalErrorAlert.setStatus(
        ""
    )

omRedSecurityBreachAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 60)
)
omRedSecurityBreachAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omRedSecurityBreachAlert.setStatus(
        ""
    )

omRedServiceUnavailableAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2349, 2, 2, 0, 70)
)
omRedServiceUnavailableAlert.setObjects(
      *(("MISSION-CRITICAL-MIB", "omAlertLevel"),
        ("MISSION-CRITICAL-MIB", "omAlertLevelName"),
        ("MISSION-CRITICAL-MIB", "omServer"),
        ("MISSION-CRITICAL-MIB", "omSource"),
        ("MISSION-CRITICAL-MIB", "omOwner"),
        ("MISSION-CRITICAL-MIB", "omDescription"),
        ("MISSION-CRITICAL-MIB", "omCustomField1"),
        ("MISSION-CRITICAL-MIB", "omCustomField2"),
        ("MISSION-CRITICAL-MIB", "omCustomField3"),
        ("MISSION-CRITICAL-MIB", "omCustomField4"),
        ("MISSION-CRITICAL-MIB", "omCustomField5"),
        ("MISSION-CRITICAL-MIB", "omAlertURL"))
)
if mibBuilder.loadTexts:
    omRedServiceUnavailableAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MISSION-CRITICAL-MIB",
    **{"missionCritical": missionCritical,
       "mcsCompanyInfo": mcsCompanyInfo,
       "ownershipDetails": ownershipDetails,
       "contactDetails": contactDetails,
       "mcsSoftware": mcsSoftware,
       "eemProductInfo": eemProductInfo,
       "serviceGoingDown": serviceGoingDown,
       "serviceComingUp": serviceComingUp,
       "gathererServiceGoingDown": gathererServiceGoingDown,
       "gathererServiceComingUp": gathererServiceComingUp,
       "eemRedAlert": eemRedAlert,
       "eemOrangeAlert": eemOrangeAlert,
       "eemYellowAlert": eemYellowAlert,
       "eemBlueAlert": eemBlueAlert,
       "eemGreenAlert": eemGreenAlert,
       "eemService": eemService,
       "version": version,
       "primaryServer": primaryServer,
       "serviceState": serviceState,
       "serviceUpTime": serviceUpTime,
       "redTrapCount": redTrapCount,
       "orangeTrapCount": orangeTrapCount,
       "amberTrapCount": amberTrapCount,
       "blueTrapCount": blueTrapCount,
       "greenTrapCount": greenTrapCount,
       "eemLastTrap": eemLastTrap,
       "trapTime": trapTime,
       "alertLevel": alertLevel,
       "logType": logType,
       "server": server,
       "source": source,
       "user": user,
       "eventID": eventID,
       "description": description,
       "genericTrapNumber": genericTrapNumber,
       "specificTrapNumber": specificTrapNumber,
       "omProductInfo": omProductInfo,
       "omBlueAlert": omBlueAlert,
       "omGreenAlert": omGreenAlert,
       "omYellowAlert": omYellowAlert,
       "omOrangeAlert": omOrangeAlert,
       "omRedCriticalErrorAlert": omRedCriticalErrorAlert,
       "omRedSecurityBreachAlert": omRedSecurityBreachAlert,
       "omRedServiceUnavailableAlert": omRedServiceUnavailableAlert,
       "omService": omService,
       "omLastTrap": omLastTrap,
       "omTrapTime": omTrapTime,
       "omAlertLevel": omAlertLevel,
       "omAlertLevelName": omAlertLevelName,
       "omServer": omServer,
       "omSource": omSource,
       "omOwner": omOwner,
       "omDescription": omDescription,
       "omCustomField1": omCustomField1,
       "omCustomField2": omCustomField2,
       "omCustomField3": omCustomField3,
       "omCustomField4": omCustomField4,
       "omCustomField5": omCustomField5,
       "omAlertURL": omAlertURL,
       "omGenericTrapNumber": omGenericTrapNumber,
       "omSpecificTrapNumber": omSpecificTrapNumber}
)
