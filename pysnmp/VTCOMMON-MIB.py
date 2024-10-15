# SNMP MIB module (VTCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VTCOMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:22 2024
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

_Vocaltec_ObjectIdentity = ObjectIdentity
vocaltec = _Vocaltec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516)
)
_VtCommonMIB_ObjectIdentity = ObjectIdentity
vtCommonMIB = _VtCommonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2516, 1)
)
_ServerOpModeTable_Object = MibTable
serverOpModeTable = _ServerOpModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2516, 1, 1)
)
if mibBuilder.loadTexts:
    serverOpModeTable.setStatus("mandatory")
_OpModeEntry_Object = MibTableRow
opModeEntry = _OpModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2516, 1, 1, 1)
)
opModeEntry.setIndexNames(
    (0, "VTCOMMON-MIB", "serverType"),
    (0, "VTCOMMON-MIB", "serverIPAddress"),
)
if mibBuilder.loadTexts:
    opModeEntry.setStatus("mandatory")


class _VtServerType_Type(Integer32):
    """Custom type vtServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("vgk", 3),
          ("vtgw", 2))
    )


_VtServerType_Type.__name__ = "Integer32"
_VtServerType_Object = MibScalar
vtServerType = _VtServerType_Object(
    (1, 3, 6, 1, 4, 1, 2516, 1, 1, 1, 1),
    _VtServerType_Type()
)
vtServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtServerType.setStatus("mandatory")
_VtServerIPAddress_Type = IpAddress
_VtServerIPAddress_Object = MibScalar
vtServerIPAddress = _VtServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2516, 1, 1, 1, 2),
    _VtServerIPAddress_Type()
)
vtServerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtServerIPAddress.setStatus("mandatory")


class _VtCommand_Type(Integer32):
    """Custom type vtCommand based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("inService", 6),
          ("maintain", 9),
          ("outOfService", 5),
          ("outOfServiceGracefully", 4),
          ("rma-kill", 2),
          ("rma-reboot", 3),
          ("rma-start", 1),
          ("shutdown", 8),
          ("shutdownGracefully", 7))
    )


_VtCommand_Type.__name__ = "Integer32"
_VtCommand_Object = MibScalar
vtCommand = _VtCommand_Object(
    (1, 3, 6, 1, 4, 1, 2516, 1, 1, 1, 3),
    _VtCommand_Type()
)
vtCommand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtCommand.setStatus("mandatory")


class _VtCurrentOpMode_Type(Integer32):
    """Custom type vtCurrentOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
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
        *(("configurationFault", 22),
          ("goingInService", 15),
          ("goingMaintenance", 20),
          ("goingOutOfService", 17),
          ("inService", 16),
          ("loading", 13),
          ("maintenance", 21),
          ("outOfService", 18),
          ("reLoading", 14),
          ("shuttingDown", 19),
          ("unknown", 23))
    )


_VtCurrentOpMode_Type.__name__ = "Integer32"
_VtCurrentOpMode_Object = MibScalar
vtCurrentOpMode = _VtCurrentOpMode_Object(
    (1, 3, 6, 1, 4, 1, 2516, 1, 1, 1, 4),
    _VtCurrentOpMode_Type()
)
vtCurrentOpMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtCurrentOpMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects

serverInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 0, 1)
)
serverInService.setObjects(
    ("VTCOMMON-MIB", "vtServerType")
)
if mibBuilder.loadTexts:
    serverInService.setStatus(
        ""
    )

serverOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 0, 2)
)
serverOutOfService.setObjects(
    ("VTCOMMON-MIB", "vtServerType")
)
if mibBuilder.loadTexts:
    serverOutOfService.setStatus(
        ""
    )

serverShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 0, 3)
)
serverShuttingDown.setObjects(
    ("VTCOMMON-MIB", "vtServerType")
)
if mibBuilder.loadTexts:
    serverShuttingDown.setStatus(
        ""
    )

serverMaintenance = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 0, 4)
)
serverMaintenance.setObjects(
    ("VTCOMMON-MIB", "vtServerType")
)
if mibBuilder.loadTexts:
    serverMaintenance.setStatus(
        ""
    )

serverConfigurationFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 0, 5)
)
serverConfigurationFault.setObjects(
    ("VTCOMMON-MIB", "vtServerType")
)
if mibBuilder.loadTexts:
    serverConfigurationFault.setStatus(
        ""
    )

serverInTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 2516, 0, 6)
)
serverInTransition.setObjects(
      *(("VTCOMMON-MIB", "vtServerType"),
        ("VTCOMMON-MIB", "vtCurrentOpMode"))
)
if mibBuilder.loadTexts:
    serverInTransition.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VTCOMMON-MIB",
    **{"vocaltec": vocaltec,
       "serverInService": serverInService,
       "serverOutOfService": serverOutOfService,
       "serverShuttingDown": serverShuttingDown,
       "serverMaintenance": serverMaintenance,
       "serverConfigurationFault": serverConfigurationFault,
       "serverInTransition": serverInTransition,
       "vtCommonMIB": vtCommonMIB,
       "serverOpModeTable": serverOpModeTable,
       "opModeEntry": opModeEntry,
       "vtServerType": vtServerType,
       "vtServerIPAddress": vtServerIPAddress,
       "vtCommand": vtCommand,
       "vtCurrentOpMode": vtCurrentOpMode}
)
