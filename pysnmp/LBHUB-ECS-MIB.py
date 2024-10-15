# SNMP MIB module (LBHUB-ECS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LBHUB-ECS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:25 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 3)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5)
)
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1)
)
_DedicatedBridgeServer_ObjectIdentity = ObjectIdentity
dedicatedBridgeServer = _DedicatedBridgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 2)
)
_DedicatedRouteServer_ObjectIdentity = ObjectIdentity
dedicatedRouteServer = _DedicatedRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 3)
)
_Brouter_ObjectIdentity = ObjectIdentity
brouter = _Brouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4)
)
_GenericMSWorkstation_ObjectIdentity = ObjectIdentity
genericMSWorkstation = _GenericMSWorkstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5)
)
_GenericMSServer_ObjectIdentity = ObjectIdentity
genericMSServer = _GenericMSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 6)
)
_GenericUnixServer_ObjectIdentity = ObjectIdentity
genericUnixServer = _GenericUnixServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 7)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilder3GH_ObjectIdentity = ObjectIdentity
linkBuilder3GH = _LinkBuilder3GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 1)
)
_LinkBuilder10BTi_ObjectIdentity = ObjectIdentity
linkBuilder10BTi = _LinkBuilder10BTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 2)
)
_LinkBuilderECS_ObjectIdentity = ObjectIdentity
linkBuilderECS = _LinkBuilderECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3)
)
_LinkBuilderMSH_ObjectIdentity = ObjectIdentity
linkBuilderMSH = _LinkBuilderMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4)
)
_LinkBuilderFMS_ObjectIdentity = ObjectIdentity
linkBuilderFMS = _LinkBuilderFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 5)
)
_LinkBuilderFMSII_ObjectIdentity = ObjectIdentity
linkBuilderFMSII = _LinkBuilderFMSII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 7)
)
_LinkBuilderFMSLBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMSLBridge = _LinkBuilderFMSLBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 10)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilder3GH_cards_ObjectIdentity = ObjectIdentity
linkBuilder3GH_cards = _LinkBuilder3GH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 1)
)
_LinkBuilder10BTi_cards_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards = _LinkBuilder10BTi_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2)
)
_LinkBuilder10BTi_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards_utp = _LinkBuilder10BTi_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)
)
_LinkBuilder10BT_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BT_cards_utp = _LinkBuilder10BT_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)
)
_LinkBuilderECS_cards_ObjectIdentity = ObjectIdentity
linkBuilderECS_cards = _LinkBuilderECS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 3)
)
_LinkBuilderMSH_cards_ObjectIdentity = ObjectIdentity
linkBuilderMSH_cards = _LinkBuilderMSH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 4)
)
_LinkBuilderFMS_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards = _LinkBuilderFMS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5)
)
_LinkBuilderFMS_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_utp = _LinkBuilderFMS_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)
)
_LinkBuilderFMS_cards_coax_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_coax = _LinkBuilderFMS_cards_coax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)
)
_LinkBuilderFMS_cards_fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_fiber = _LinkBuilderFMS_cards_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)
)
_LinkBuilderFMS_cards_12fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_12fiber = _LinkBuilderFMS_cards_12fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)
)
_LinkBuilderFMS_cards_24utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_24utp = _LinkBuilderFMS_cards_24utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)
)
_LinkBuilderFMSII_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards = _LinkBuilderFMSII_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6)
)
_LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12tp_rj45 = _LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)
)
_LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_10coax_bnc = _LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)
)
_LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_6fiber_st = _LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)
)
_LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12fiber_st = _LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)
)
_LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_rj45 = _LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)
)
_LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_telco = _LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)
)
_Amp_mib_ObjectIdentity = ObjectIdentity
amp_mib = _Amp_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 3)
)
_GenericTrap_ObjectIdentity = ObjectIdentity
genericTrap = _GenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 4)
)
_ViewBuilderApps_ObjectIdentity = ObjectIdentity
viewBuilderApps = _ViewBuilderApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 5)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 6)
)
_LinkBuilder3GH_mib_ObjectIdentity = ObjectIdentity
linkBuilder3GH_mib = _LinkBuilder3GH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_LinkBuilder10BTi_mib_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_mib = _LinkBuilder10BTi_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8)
)
_LinkBuilderECS_mib_ObjectIdentity = ObjectIdentity
linkBuilderECS_mib = _LinkBuilderECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9)
)
_EcsAgent_ObjectIdentity = ObjectIdentity
ecsAgent = _EcsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 1)
)
_EcsAgentSystemIdentifier_ObjectIdentity = ObjectIdentity
ecsAgentSystemIdentifier = _EcsAgentSystemIdentifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 1)
)


class _EcsManufacturerId_Type(DisplayString):
    """Custom type ecsManufacturerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EcsManufacturerId_Type.__name__ = "DisplayString"
_EcsManufacturerId_Object = MibScalar
ecsManufacturerId = _EcsManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 1, 1),
    _EcsManufacturerId_Type()
)
ecsManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsManufacturerId.setStatus("deprecated")


class _EcsManufacturerProductId_Type(DisplayString):
    """Custom type ecsManufacturerProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EcsManufacturerProductId_Type.__name__ = "DisplayString"
_EcsManufacturerProductId_Object = MibScalar
ecsManufacturerProductId = _EcsManufacturerProductId_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 1, 2),
    _EcsManufacturerProductId_Type()
)
ecsManufacturerProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsManufacturerProductId.setStatus("mandatory")


class _EcsSoftwareVersionNumber_Type(DisplayString):
    """Custom type ecsSoftwareVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EcsSoftwareVersionNumber_Type.__name__ = "DisplayString"
_EcsSoftwareVersionNumber_Object = MibScalar
ecsSoftwareVersionNumber = _EcsSoftwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 1, 3),
    _EcsSoftwareVersionNumber_Type()
)
ecsSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSoftwareVersionNumber.setStatus("deprecated")
_EcsHardwareVersionNumber_Type = Integer32
_EcsHardwareVersionNumber_Object = MibScalar
ecsHardwareVersionNumber = _EcsHardwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 1, 4),
    _EcsHardwareVersionNumber_Type()
)
ecsHardwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHardwareVersionNumber.setStatus("deprecated")


class _EcsAgentSystemName_Type(DisplayString):
    """Custom type ecsAgentSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EcsAgentSystemName_Type.__name__ = "DisplayString"
_EcsAgentSystemName_Object = MibScalar
ecsAgentSystemName = _EcsAgentSystemName_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 2),
    _EcsAgentSystemName_Type()
)
ecsAgentSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentSystemName.setStatus("deprecated")


class _EcsAgentSystemLocation_Type(DisplayString):
    """Custom type ecsAgentSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EcsAgentSystemLocation_Type.__name__ = "DisplayString"
_EcsAgentSystemLocation_Object = MibScalar
ecsAgentSystemLocation = _EcsAgentSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 3),
    _EcsAgentSystemLocation_Type()
)
ecsAgentSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentSystemLocation.setStatus("deprecated")
_EcsAgentSystemTime_Type = TimeTicks
_EcsAgentSystemTime_Object = MibScalar
ecsAgentSystemTime = _EcsAgentSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 4),
    _EcsAgentSystemTime_Type()
)
ecsAgentSystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentSystemTime.setStatus("deprecated")


class _EcsAgentStatus_Type(Integer32):
    """Custom type ecsAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_EcsAgentStatus_Type.__name__ = "Integer32"
_EcsAgentStatus_Object = MibScalar
ecsAgentStatus = _EcsAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 5),
    _EcsAgentStatus_Type()
)
ecsAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentStatus.setStatus("mandatory")


class _EcsAgentAuthenticationStatus_Type(Integer32):
    """Custom type ecsAgentAuthenticationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EcsAgentAuthenticationStatus_Type.__name__ = "Integer32"
_EcsAgentAuthenticationStatus_Object = MibScalar
ecsAgentAuthenticationStatus = _EcsAgentAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 6),
    _EcsAgentAuthenticationStatus_Type()
)
ecsAgentAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentAuthenticationStatus.setStatus("mandatory")


class _EcsAgentSecureManagementStatus_Type(Integer32):
    """Custom type ecsAgentSecureManagementStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("secure-config-update", 5),
          ("secure-menu-entered", 3),
          ("secure-password-violation", 4))
    )


_EcsAgentSecureManagementStatus_Type.__name__ = "Integer32"
_EcsAgentSecureManagementStatus_Object = MibScalar
ecsAgentSecureManagementStatus = _EcsAgentSecureManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 7),
    _EcsAgentSecureManagementStatus_Type()
)
ecsAgentSecureManagementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentSecureManagementStatus.setStatus("mandatory")


class _EcsAgentFrontPanelSetupPassword_Type(DisplayString):
    """Custom type ecsAgentFrontPanelSetupPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EcsAgentFrontPanelSetupPassword_Type.__name__ = "DisplayString"
_EcsAgentFrontPanelSetupPassword_Object = MibScalar
ecsAgentFrontPanelSetupPassword = _EcsAgentFrontPanelSetupPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 11),
    _EcsAgentFrontPanelSetupPassword_Type()
)
ecsAgentFrontPanelSetupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentFrontPanelSetupPassword.setStatus("mandatory")


class _EcsAgentFrontPanelDisplay_Type(DisplayString):
    """Custom type ecsAgentFrontPanelDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_EcsAgentFrontPanelDisplay_Type.__name__ = "DisplayString"
_EcsAgentFrontPanelDisplay_Object = MibScalar
ecsAgentFrontPanelDisplay = _EcsAgentFrontPanelDisplay_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 12),
    _EcsAgentFrontPanelDisplay_Type()
)
ecsAgentFrontPanelDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentFrontPanelDisplay.setStatus("mandatory")


class _EcsAgentFrontPanelPassword_Type(DisplayString):
    """Custom type ecsAgentFrontPanelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EcsAgentFrontPanelPassword_Type.__name__ = "DisplayString"
_EcsAgentFrontPanelPassword_Object = MibScalar
ecsAgentFrontPanelPassword = _EcsAgentFrontPanelPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 13),
    _EcsAgentFrontPanelPassword_Type()
)
ecsAgentFrontPanelPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentFrontPanelPassword.setStatus("mandatory")


class _EcsAgentFrontPanelSecurePassword_Type(DisplayString):
    """Custom type ecsAgentFrontPanelSecurePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EcsAgentFrontPanelSecurePassword_Type.__name__ = "DisplayString"
_EcsAgentFrontPanelSecurePassword_Object = MibScalar
ecsAgentFrontPanelSecurePassword = _EcsAgentFrontPanelSecurePassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 14),
    _EcsAgentFrontPanelSecurePassword_Type()
)
ecsAgentFrontPanelSecurePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentFrontPanelSecurePassword.setStatus("mandatory")


class _EcsAgentFrontPanelLock_Type(Integer32):
    """Custom type ecsAgentFrontPanelLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EcsAgentFrontPanelLock_Type.__name__ = "Integer32"
_EcsAgentFrontPanelLock_Object = MibScalar
ecsAgentFrontPanelLock = _EcsAgentFrontPanelLock_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 15),
    _EcsAgentFrontPanelLock_Type()
)
ecsAgentFrontPanelLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentFrontPanelLock.setStatus("mandatory")


class _EcsAgentResetDevice_Type(Integer32):
    """Custom type ecsAgentResetDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 1),
          ("reset", 2))
    )


_EcsAgentResetDevice_Type.__name__ = "Integer32"
_EcsAgentResetDevice_Object = MibScalar
ecsAgentResetDevice = _EcsAgentResetDevice_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 16),
    _EcsAgentResetDevice_Type()
)
ecsAgentResetDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentResetDevice.setStatus("mandatory")


class _EcsAgentRestart_Type(Integer32):
    """Custom type ecsAgentRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notrestart", 1),
          ("restart", 2))
    )


_EcsAgentRestart_Type.__name__ = "Integer32"
_EcsAgentRestart_Object = MibScalar
ecsAgentRestart = _EcsAgentRestart_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 18),
    _EcsAgentRestart_Type()
)
ecsAgentRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentRestart.setStatus("mandatory")


class _EcsAgentDefaultConfig_Type(Integer32):
    """Custom type ecsAgentDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reverting", 2))
    )


_EcsAgentDefaultConfig_Type.__name__ = "Integer32"
_EcsAgentDefaultConfig_Object = MibScalar
ecsAgentDefaultConfig = _EcsAgentDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 19),
    _EcsAgentDefaultConfig_Type()
)
ecsAgentDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentDefaultConfig.setStatus("mandatory")
_EcsAgentManagementTable_Object = MibTable
ecsAgentManagementTable = _EcsAgentManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 20)
)
if mibBuilder.loadTexts:
    ecsAgentManagementTable.setStatus("mandatory")
_EcsAgentManagementEntry_Object = MibTableRow
ecsAgentManagementEntry = _EcsAgentManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 20, 1)
)
ecsAgentManagementEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsAgentManagementAddr"),
)
if mibBuilder.loadTexts:
    ecsAgentManagementEntry.setStatus("mandatory")
_EcsAgentManagementAddr_Type = IpAddress
_EcsAgentManagementAddr_Object = MibTableColumn
ecsAgentManagementAddr = _EcsAgentManagementAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 20, 1, 1),
    _EcsAgentManagementAddr_Type()
)
ecsAgentManagementAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentManagementAddr.setStatus("mandatory")


class _EcsAgentManagementAccess_Type(Integer32):
    """Custom type ecsAgentManagementAccess based on Integer32"""
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
        *(("invalid", 1),
          ("off", 2),
          ("readonly", 5),
          ("readonlysecure", 7),
          ("readwrite", 6),
          ("readwritesecure", 8),
          ("superread", 3),
          ("superreadwrite", 4))
    )


_EcsAgentManagementAccess_Type.__name__ = "Integer32"
_EcsAgentManagementAccess_Object = MibTableColumn
ecsAgentManagementAccess = _EcsAgentManagementAccess_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 20, 1, 2),
    _EcsAgentManagementAccess_Type()
)
ecsAgentManagementAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentManagementAccess.setStatus("mandatory")
_EcsAgentManAccessLevel_Type = Integer32
_EcsAgentManAccessLevel_Object = MibTableColumn
ecsAgentManAccessLevel = _EcsAgentManAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 20, 1, 3),
    _EcsAgentManAccessLevel_Type()
)
ecsAgentManAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentManAccessLevel.setStatus("mandatory")
_EcsAgentTrapReceiverTable_Object = MibTable
ecsAgentTrapReceiverTable = _EcsAgentTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 21)
)
if mibBuilder.loadTexts:
    ecsAgentTrapReceiverTable.setStatus("mandatory")
_EcsAgentTrapReceiverEntry_Object = MibTableRow
ecsAgentTrapReceiverEntry = _EcsAgentTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 21, 1)
)
ecsAgentTrapReceiverEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsAgentTrapReceiverAddr"),
)
if mibBuilder.loadTexts:
    ecsAgentTrapReceiverEntry.setStatus("mandatory")
_EcsAgentTrapReceiverAddr_Type = IpAddress
_EcsAgentTrapReceiverAddr_Object = MibTableColumn
ecsAgentTrapReceiverAddr = _EcsAgentTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 21, 1, 1),
    _EcsAgentTrapReceiverAddr_Type()
)
ecsAgentTrapReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentTrapReceiverAddr.setStatus("mandatory")


class _EcsAgentTrapType_Type(Integer32):
    """Custom type ecsAgentTrapType based on Integer32"""
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
        *(("configuractionchange", 6),
          ("fanfail", 5),
          ("generic", 3),
          ("invalid", 1),
          ("off-on", 2),
          ("port", 7),
          ("psu", 4),
          ("rate", 9),
          ("resilience", 8),
          ("secure", 11),
          ("secureport", 12),
          ("stationlocate", 10))
    )


_EcsAgentTrapType_Type.__name__ = "Integer32"
_EcsAgentTrapType_Object = MibTableColumn
ecsAgentTrapType = _EcsAgentTrapType_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 21, 1, 2),
    _EcsAgentTrapType_Type()
)
ecsAgentTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentTrapType.setStatus("mandatory")


class _EcsAgentTrapReceiverComm_Type(DisplayString):
    """Custom type ecsAgentTrapReceiverComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EcsAgentTrapReceiverComm_Type.__name__ = "DisplayString"
_EcsAgentTrapReceiverComm_Object = MibTableColumn
ecsAgentTrapReceiverComm = _EcsAgentTrapReceiverComm_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 21, 1, 3),
    _EcsAgentTrapReceiverComm_Type()
)
ecsAgentTrapReceiverComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentTrapReceiverComm.setStatus("mandatory")
_EcsAgentTrapLevel_Type = Integer32
_EcsAgentTrapLevel_Object = MibTableColumn
ecsAgentTrapLevel = _EcsAgentTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 21, 1, 4),
    _EcsAgentTrapLevel_Type()
)
ecsAgentTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentTrapLevel.setStatus("mandatory")


class _EcsAgentAuthTrapState_Type(Integer32):
    """Custom type ecsAgentAuthTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_EcsAgentAuthTrapState_Type.__name__ = "Integer32"
_EcsAgentAuthTrapState_Object = MibScalar
ecsAgentAuthTrapState = _EcsAgentAuthTrapState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 22),
    _EcsAgentAuthTrapState_Type()
)
ecsAgentAuthTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentAuthTrapState.setStatus("deprecated")
_EcsAgentIpAddr_Type = IpAddress
_EcsAgentIpAddr_Object = MibScalar
ecsAgentIpAddr = _EcsAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 23),
    _EcsAgentIpAddr_Type()
)
ecsAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentIpAddr.setStatus("mandatory")
_EcsAgentIpNetmask_Type = IpAddress
_EcsAgentIpNetmask_Object = MibScalar
ecsAgentIpNetmask = _EcsAgentIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 24),
    _EcsAgentIpNetmask_Type()
)
ecsAgentIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentIpNetmask.setStatus("mandatory")
_EcsAgentDefaultGateway_Type = IpAddress
_EcsAgentDefaultGateway_Object = MibScalar
ecsAgentDefaultGateway = _EcsAgentDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 25),
    _EcsAgentDefaultGateway_Type()
)
ecsAgentDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentDefaultGateway.setStatus("mandatory")
_EcsAgentIpBroadAddr_Type = IpAddress
_EcsAgentIpBroadAddr_Object = MibScalar
ecsAgentIpBroadAddr = _EcsAgentIpBroadAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 26),
    _EcsAgentIpBroadAddr_Type()
)
ecsAgentIpBroadAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentIpBroadAddr.setStatus("mandatory")
_EcsAgentMACAddress_Type = OctetString
_EcsAgentMACAddress_Object = MibScalar
ecsAgentMACAddress = _EcsAgentMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 27),
    _EcsAgentMACAddress_Type()
)
ecsAgentMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentMACAddress.setStatus("mandatory")


class _EcsAgentSecureTrapState_Type(Integer32):
    """Custom type ecsAgentSecureTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_EcsAgentSecureTrapState_Type.__name__ = "Integer32"
_EcsAgentSecureTrapState_Object = MibScalar
ecsAgentSecureTrapState = _EcsAgentSecureTrapState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 28),
    _EcsAgentSecureTrapState_Type()
)
ecsAgentSecureTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAgentSecureTrapState.setStatus("mandatory")
_EcsAgentLastSystemError_Type = Integer32
_EcsAgentLastSystemError_Object = MibScalar
ecsAgentLastSystemError = _EcsAgentLastSystemError_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 29),
    _EcsAgentLastSystemError_Type()
)
ecsAgentLastSystemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentLastSystemError.setStatus("mandatory")
_EcsAgentLastTrap_Type = TimeTicks
_EcsAgentLastTrap_Object = MibScalar
ecsAgentLastTrap = _EcsAgentLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 1, 30),
    _EcsAgentLastTrap_Type()
)
ecsAgentLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAgentLastTrap.setStatus("mandatory")
_EcsEnvironment_ObjectIdentity = ObjectIdentity
ecsEnvironment = _EcsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 2)
)


class _EcsRackType_Type(Integer32):
    """Custom type ecsRackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ecs10", 3),
          ("ecs4", 2),
          ("unknown", 1))
    )


_EcsRackType_Type.__name__ = "Integer32"
_EcsRackType_Object = MibScalar
ecsRackType = _EcsRackType_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 1),
    _EcsRackType_Type()
)
ecsRackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRackType.setStatus("mandatory")
_EcsRackConfigurationTable_Object = MibTable
ecsRackConfigurationTable = _EcsRackConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2)
)
if mibBuilder.loadTexts:
    ecsRackConfigurationTable.setStatus("mandatory")
_EcsSlotConfigEntry_Object = MibTableRow
ecsSlotConfigEntry = _EcsSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1)
)
ecsSlotConfigEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsSlotConfigIndex"),
)
if mibBuilder.loadTexts:
    ecsSlotConfigEntry.setStatus("mandatory")
_EcsSlotConfigIndex_Type = Integer32
_EcsSlotConfigIndex_Object = MibTableColumn
ecsSlotConfigIndex = _EcsSlotConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 1),
    _EcsSlotConfigIndex_Type()
)
ecsSlotConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSlotConfigIndex.setStatus("mandatory")


class _EcsSlotCardName_Type(DisplayString):
    """Custom type ecsSlotCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EcsSlotCardName_Type.__name__ = "DisplayString"
_EcsSlotCardName_Object = MibTableColumn
ecsSlotCardName = _EcsSlotCardName_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 2),
    _EcsSlotCardName_Type()
)
ecsSlotCardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSlotCardName.setStatus("mandatory")


class _EcsSlotDeviceType_Type(Integer32):
    """Custom type ecsSlotDeviceType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("bridge-Line-Card", 8),
          ("empty", 1),
          ("fanout", 11),
          ("fibre", 7),
          ("managementcard", 3),
          ("monitor", 9),
          ("remotebridge", 18),
          ("secureFanout", 15),
          ("secureFibre", 14),
          ("secureSheildedTP", 13),
          ("secureThinEthernet", 16),
          ("secureUnshieldedTP", 12),
          ("shieldedTwistedPair", 10),
          ("terminalserver", 17),
          ("thinEthernetCard", 4),
          ("thinEthernetCardpAUI", 5),
          ("unknown", 2),
          ("unshieldedTwistedPair", 6),
          ("videoswitch", 19))
    )


_EcsSlotDeviceType_Type.__name__ = "Integer32"
_EcsSlotDeviceType_Object = MibTableColumn
ecsSlotDeviceType = _EcsSlotDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 3),
    _EcsSlotDeviceType_Type()
)
ecsSlotDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSlotDeviceType.setStatus("mandatory")


class _EcsSlotSoftVerNum_Type(DisplayString):
    """Custom type ecsSlotSoftVerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EcsSlotSoftVerNum_Type.__name__ = "DisplayString"
_EcsSlotSoftVerNum_Object = MibTableColumn
ecsSlotSoftVerNum = _EcsSlotSoftVerNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 4),
    _EcsSlotSoftVerNum_Type()
)
ecsSlotSoftVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSlotSoftVerNum.setStatus("mandatory")
_EcsSlotHardVerNum_Type = Integer32
_EcsSlotHardVerNum_Object = MibTableColumn
ecsSlotHardVerNum = _EcsSlotHardVerNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 5),
    _EcsSlotHardVerNum_Type()
)
ecsSlotHardVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSlotHardVerNum.setStatus("mandatory")
_EcsSlotNumOfPorts_Type = Integer32
_EcsSlotNumOfPorts_Object = MibTableColumn
ecsSlotNumOfPorts = _EcsSlotNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 6),
    _EcsSlotNumOfPorts_Type()
)
ecsSlotNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSlotNumOfPorts.setStatus("mandatory")


class _EcsSlotMediaType_Type(DisplayString):
    """Custom type ecsSlotMediaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EcsSlotMediaType_Type.__name__ = "DisplayString"
_EcsSlotMediaType_Object = MibTableColumn
ecsSlotMediaType = _EcsSlotMediaType_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 7),
    _EcsSlotMediaType_Type()
)
ecsSlotMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSlotMediaType.setStatus("mandatory")


class _EcsCardReset_Type(Integer32):
    """Custom type ecsCardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-reset", 1),
          ("reset", 2))
    )


_EcsCardReset_Type.__name__ = "Integer32"
_EcsCardReset_Object = MibTableColumn
ecsCardReset = _EcsCardReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 8),
    _EcsCardReset_Type()
)
ecsCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCardReset.setStatus("mandatory")


class _EcsLampOverRide_Type(Integer32):
    """Custom type ecsLampOverRide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EcsLampOverRide_Type.__name__ = "Integer32"
_EcsLampOverRide_Object = MibTableColumn
ecsLampOverRide = _EcsLampOverRide_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 9),
    _EcsLampOverRide_Type()
)
ecsLampOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsLampOverRide.setStatus("mandatory")


class _EcsCardIsolated_Type(Integer32):
    """Custom type ecsCardIsolated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cant-isolate", 3),
          ("isolated", 2),
          ("not-isolated", 1))
    )


_EcsCardIsolated_Type.__name__ = "Integer32"
_EcsCardIsolated_Object = MibTableColumn
ecsCardIsolated = _EcsCardIsolated_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 10),
    _EcsCardIsolated_Type()
)
ecsCardIsolated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCardIsolated.setStatus("mandatory")
_EcsCardIpAddress_Type = IpAddress
_EcsCardIpAddress_Object = MibTableColumn
ecsCardIpAddress = _EcsCardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 2, 1, 11),
    _EcsCardIpAddress_Type()
)
ecsCardIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCardIpAddress.setStatus("mandatory")


class _EcsPSUStatus_Type(Integer32):
    """Custom type ecsPSUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("psu1failed", 2),
          ("psu2failed", 3))
    )


_EcsPSUStatus_Type.__name__ = "Integer32"
_EcsPSUStatus_Object = MibScalar
ecsPSUStatus = _EcsPSUStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 3),
    _EcsPSUStatus_Type()
)
ecsPSUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsPSUStatus.setStatus("mandatory")


class _EcsFanStatus_Type(Integer32):
    """Custom type ecsFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_EcsFanStatus_Type.__name__ = "Integer32"
_EcsFanStatus_Object = MibScalar
ecsFanStatus = _EcsFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 2, 4),
    _EcsFanStatus_Type()
)
ecsFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsFanStatus.setStatus("mandatory")
_EcsRLCResilientLinks_ObjectIdentity = ObjectIdentity
ecsRLCResilientLinks = _EcsRLCResilientLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 3)
)
_EcsRLCNumberOfResilientLinks_Type = Integer32
_EcsRLCNumberOfResilientLinks_Object = MibScalar
ecsRLCNumberOfResilientLinks = _EcsRLCNumberOfResilientLinks_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 1),
    _EcsRLCNumberOfResilientLinks_Type()
)
ecsRLCNumberOfResilientLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCNumberOfResilientLinks.setStatus("mandatory")
_EcsRLCNumberOfDOBPorts_Type = Integer32
_EcsRLCNumberOfDOBPorts_Object = MibScalar
ecsRLCNumberOfDOBPorts = _EcsRLCNumberOfDOBPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 2),
    _EcsRLCNumberOfDOBPorts_Type()
)
ecsRLCNumberOfDOBPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCNumberOfDOBPorts.setStatus("mandatory")
_EcsRLCResilientLinkTable_Object = MibTable
ecsRLCResilientLinkTable = _EcsRLCResilientLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3)
)
if mibBuilder.loadTexts:
    ecsRLCResilientLinkTable.setStatus("mandatory")
_EcsRLCResilientLinkEntry_Object = MibTableRow
ecsRLCResilientLinkEntry = _EcsRLCResilientLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1)
)
ecsRLCResilientLinkEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsRLMainLinkSlot"),
    (0, "LBHUB-ECS-MIB", "ecsRLMainLinkPort"),
)
if mibBuilder.loadTexts:
    ecsRLCResilientLinkEntry.setStatus("mandatory")
_EcsRLMainLinkSlot_Type = Integer32
_EcsRLMainLinkSlot_Object = MibTableColumn
ecsRLMainLinkSlot = _EcsRLMainLinkSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1, 1),
    _EcsRLMainLinkSlot_Type()
)
ecsRLMainLinkSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLMainLinkSlot.setStatus("mandatory")
_EcsRLMainLinkPort_Type = Integer32
_EcsRLMainLinkPort_Object = MibTableColumn
ecsRLMainLinkPort = _EcsRLMainLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1, 2),
    _EcsRLMainLinkPort_Type()
)
ecsRLMainLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLMainLinkPort.setStatus("mandatory")
_EcsRLStandbySlot_Type = Integer32
_EcsRLStandbySlot_Object = MibTableColumn
ecsRLStandbySlot = _EcsRLStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1, 3),
    _EcsRLStandbySlot_Type()
)
ecsRLStandbySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLStandbySlot.setStatus("mandatory")
_EcsRLStandbyPort_Type = Integer32
_EcsRLStandbyPort_Object = MibTableColumn
ecsRLStandbyPort = _EcsRLStandbyPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1, 4),
    _EcsRLStandbyPort_Type()
)
ecsRLStandbyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLStandbyPort.setStatus("mandatory")


class _EcsRLActiveLink_Type(Integer32):
    """Custom type ecsRLActiveLink based on Integer32"""
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
        *(("both", 5),
          ("main", 3),
          ("none", 2),
          ("standby", 4),
          ("unknown", 1))
    )


_EcsRLActiveLink_Type.__name__ = "Integer32"
_EcsRLActiveLink_Object = MibTableColumn
ecsRLActiveLink = _EcsRLActiveLink_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1, 5),
    _EcsRLActiveLink_Type()
)
ecsRLActiveLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLActiveLink.setStatus("mandatory")


class _EcsResLinkState_Type(Integer32):
    """Custom type ecsResLinkState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("both-failed", 10),
          ("invalid", 1),
          ("main-absent", 6),
          ("main-failed", 8),
          ("non-operational", 3),
          ("operational", 2),
          ("standby-absent", 7),
          ("standby-failed", 9),
          ("standby-jumperfault", 5),
          ("switchlink", 4))
    )


_EcsResLinkState_Type.__name__ = "Integer32"
_EcsResLinkState_Object = MibTableColumn
ecsResLinkState = _EcsResLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 3, 3, 1, 6),
    _EcsResLinkState_Type()
)
ecsResLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsResLinkState.setStatus("mandatory")
_EcsSecureRepeaterLineCards_ObjectIdentity = ObjectIdentity
ecsSecureRepeaterLineCards = _EcsSecureRepeaterLineCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 4)
)


class _EcsSecureRLCMode_Type(Integer32):
    """Custom type ecsSecureRLCMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EcsSecureRLCMode_Type.__name__ = "Integer32"
_EcsSecureRLCMode_Object = MibScalar
ecsSecureRLCMode = _EcsSecureRLCMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 1),
    _EcsSecureRLCMode_Type()
)
ecsSecureRLCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSecureRLCMode.setStatus("mandatory")


class _EcsSecureTrapRepRate_Type(Integer32):
    """Custom type ecsSecureTrapRepRate based on Integer32"""
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
        *(("continuous", 1),
          ("fifteen-mins", 3),
          ("one-minute", 2),
          ("sixty-minutes", 4))
    )


_EcsSecureTrapRepRate_Type.__name__ = "Integer32"
_EcsSecureTrapRepRate_Object = MibScalar
ecsSecureTrapRepRate = _EcsSecureTrapRepRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 2),
    _EcsSecureTrapRepRate_Type()
)
ecsSecureTrapRepRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecureTrapRepRate.setStatus("mandatory")
_EcsSecureRLCTable_Object = MibTable
ecsSecureRLCTable = _EcsSecureRLCTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3)
)
if mibBuilder.loadTexts:
    ecsSecureRLCTable.setStatus("mandatory")
_EcsSecureRLCEntry_Object = MibTableRow
ecsSecureRLCEntry = _EcsSecureRLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1)
)
ecsSecureRLCEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsSecRLCSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsSecRLCPortIndex"),
)
if mibBuilder.loadTexts:
    ecsSecureRLCEntry.setStatus("mandatory")
_EcsSecRLCSlotIndex_Type = Integer32
_EcsSecRLCSlotIndex_Object = MibTableColumn
ecsSecRLCSlotIndex = _EcsSecRLCSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 1),
    _EcsSecRLCSlotIndex_Type()
)
ecsSecRLCSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSecRLCSlotIndex.setStatus("mandatory")
_EcsSecRLCPortIndex_Type = Integer32
_EcsSecRLCPortIndex_Object = MibTableColumn
ecsSecRLCPortIndex = _EcsSecRLCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 2),
    _EcsSecRLCPortIndex_Type()
)
ecsSecRLCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSecRLCPortIndex.setStatus("mandatory")


class _EcsSecRLCLinkState_Type(Integer32):
    """Custom type ecsSecRLCLinkState based on Integer32"""
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
          ("repeater", 3),
          ("secure", 2))
    )


_EcsSecRLCLinkState_Type.__name__ = "Integer32"
_EcsSecRLCLinkState_Object = MibTableColumn
ecsSecRLCLinkState = _EcsSecRLCLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 3),
    _EcsSecRLCLinkState_Type()
)
ecsSecRLCLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsSecRLCLinkState.setStatus("mandatory")


class _EcsSecRLCPortState_Type(Integer32):
    """Custom type ecsSecRLCPortState based on Integer32"""
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
        *(("authorised-station-learnt", 6),
          ("disabled", 2),
          ("enabled", 3),
          ("other", 1),
          ("unauthorised-station-port-disabled", 5),
          ("unauthorised-station-seen", 4))
    )


_EcsSecRLCPortState_Type.__name__ = "Integer32"
_EcsSecRLCPortState_Object = MibTableColumn
ecsSecRLCPortState = _EcsSecRLCPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 4),
    _EcsSecRLCPortState_Type()
)
ecsSecRLCPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCPortState.setStatus("mandatory")


class _EcsSecRLCNTKState_Type(Integer32):
    """Custom type ecsSecRLCNTKState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_EcsSecRLCNTKState_Type.__name__ = "Integer32"
_EcsSecRLCNTKState_Object = MibTableColumn
ecsSecRLCNTKState = _EcsSecRLCNTKState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 5),
    _EcsSecRLCNTKState_Type()
)
ecsSecRLCNTKState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCNTKState.setStatus("mandatory")


class _EcsSecRLCBroadState_Type(Integer32):
    """Custom type ecsSecRLCBroadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_EcsSecRLCBroadState_Type.__name__ = "Integer32"
_EcsSecRLCBroadState_Object = MibTableColumn
ecsSecRLCBroadState = _EcsSecRLCBroadState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 6),
    _EcsSecRLCBroadState_Type()
)
ecsSecRLCBroadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCBroadState.setStatus("mandatory")


class _EcsSecRLCMultiState_Type(Integer32):
    """Custom type ecsSecRLCMultiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_EcsSecRLCMultiState_Type.__name__ = "Integer32"
_EcsSecRLCMultiState_Object = MibTableColumn
ecsSecRLCMultiState = _EcsSecRLCMultiState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 7),
    _EcsSecRLCMultiState_Type()
)
ecsSecRLCMultiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCMultiState.setStatus("mandatory")


class _EcsSecRLCLearnMode_Type(Integer32):
    """Custom type ecsSecRLCLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("continual", 3),
          ("off", 1),
          ("single", 2))
    )


_EcsSecRLCLearnMode_Type.__name__ = "Integer32"
_EcsSecRLCLearnMode_Object = MibTableColumn
ecsSecRLCLearnMode = _EcsSecRLCLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 8),
    _EcsSecRLCLearnMode_Type()
)
ecsSecRLCLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCLearnMode.setStatus("mandatory")


class _EcsSecRLCReportMode_Type(Integer32):
    """Custom type ecsSecRLCReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnectandreport", 3),
          ("off", 1),
          ("reportonly", 2))
    )


_EcsSecRLCReportMode_Type.__name__ = "Integer32"
_EcsSecRLCReportMode_Object = MibTableColumn
ecsSecRLCReportMode = _EcsSecRLCReportMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 9),
    _EcsSecRLCReportMode_Type()
)
ecsSecRLCReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCReportMode.setStatus("mandatory")
_EcsSecRLCMACAddress_Type = OctetString
_EcsSecRLCMACAddress_Object = MibTableColumn
ecsSecRLCMACAddress = _EcsSecRLCMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 4, 3, 1, 10),
    _EcsSecRLCMACAddress_Type()
)
ecsSecRLCMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsSecRLCMACAddress.setStatus("mandatory")
_EcsRepeaterLineCard_ObjectIdentity = ObjectIdentity
ecsRepeaterLineCard = _EcsRepeaterLineCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 5)
)
_EcsRLCPortStatisticsTable_Object = MibTable
ecsRLCPortStatisticsTable = _EcsRLCPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1)
)
if mibBuilder.loadTexts:
    ecsRLCPortStatisticsTable.setStatus("mandatory")
_EcsRLCPortStatisticsEntry_Object = MibTableRow
ecsRLCPortStatisticsEntry = _EcsRLCPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1)
)
ecsRLCPortStatisticsEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsRepeaterSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsRepeaterPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCPortStatisticsEntry.setStatus("mandatory")
_EcsRepeaterSlotIndex_Type = Integer32
_EcsRepeaterSlotIndex_Object = MibTableColumn
ecsRepeaterSlotIndex = _EcsRepeaterSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 1),
    _EcsRepeaterSlotIndex_Type()
)
ecsRepeaterSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRepeaterSlotIndex.setStatus("mandatory")
_EcsRepeaterPortIndex_Type = Integer32
_EcsRepeaterPortIndex_Object = MibTableColumn
ecsRepeaterPortIndex = _EcsRepeaterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 2),
    _EcsRepeaterPortIndex_Type()
)
ecsRepeaterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRepeaterPortIndex.setStatus("mandatory")


class _EcsRepeaterPortState_Type(Integer32):
    """Custom type ecsRepeaterPortState based on Integer32"""
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
        *(("disabled", 1),
          ("disabled-linkdown", 3),
          ("disabled-linkup", 5),
          ("enabled", 2),
          ("enabled-linkdown", 4),
          ("enabled-linkup", 6))
    )


_EcsRepeaterPortState_Type.__name__ = "Integer32"
_EcsRepeaterPortState_Object = MibTableColumn
ecsRepeaterPortState = _EcsRepeaterPortState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 3),
    _EcsRepeaterPortState_Type()
)
ecsRepeaterPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRepeaterPortState.setStatus("mandatory")


class _EcsRepeaterPartitionState_Type(Integer32):
    """Custom type ecsRepeaterPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("partitioned", 2))
    )


_EcsRepeaterPartitionState_Type.__name__ = "Integer32"
_EcsRepeaterPartitionState_Object = MibTableColumn
ecsRepeaterPartitionState = _EcsRepeaterPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 4),
    _EcsRepeaterPartitionState_Type()
)
ecsRepeaterPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRepeaterPartitionState.setStatus("mandatory")
_EcsGoodRcvdFrames_Type = Counter32
_EcsGoodRcvdFrames_Object = MibTableColumn
ecsGoodRcvdFrames = _EcsGoodRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 5),
    _EcsGoodRcvdFrames_Type()
)
ecsGoodRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsGoodRcvdFrames.setStatus("mandatory")
_EcsTotalByteCount_Type = Counter32
_EcsTotalByteCount_Object = MibTableColumn
ecsTotalByteCount = _EcsTotalByteCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 6),
    _EcsTotalByteCount_Type()
)
ecsTotalByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsTotalByteCount.setStatus("mandatory")
_EcsTotalErrorCount_Type = Counter32
_EcsTotalErrorCount_Object = MibTableColumn
ecsTotalErrorCount = _EcsTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 7),
    _EcsTotalErrorCount_Type()
)
ecsTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsTotalErrorCount.setStatus("mandatory")
_EcsRxBroadcastFrames_Type = Counter32
_EcsRxBroadcastFrames_Object = MibTableColumn
ecsRxBroadcastFrames = _EcsRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 8),
    _EcsRxBroadcastFrames_Type()
)
ecsRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRxBroadcastFrames.setStatus("mandatory")
_EcsRxMulticastFrames_Type = Counter32
_EcsRxMulticastFrames_Object = MibTableColumn
ecsRxMulticastFrames = _EcsRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 1, 1, 9),
    _EcsRxMulticastFrames_Type()
)
ecsRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRxMulticastFrames.setStatus("mandatory")
_EcsRLCPortErrorTable_Object = MibTable
ecsRLCPortErrorTable = _EcsRLCPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2)
)
if mibBuilder.loadTexts:
    ecsRLCPortErrorTable.setStatus("mandatory")
_EcsRLCPortErrorEntry_Object = MibTableRow
ecsRLCPortErrorEntry = _EcsRLCPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1)
)
ecsRLCPortErrorEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsErrorSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsErrorPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCPortErrorEntry.setStatus("mandatory")
_EcsErrorSlotIndex_Type = Integer32
_EcsErrorSlotIndex_Object = MibTableColumn
ecsErrorSlotIndex = _EcsErrorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 1),
    _EcsErrorSlotIndex_Type()
)
ecsErrorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsErrorSlotIndex.setStatus("mandatory")
_EcsErrorPortIndex_Type = Integer32
_EcsErrorPortIndex_Object = MibTableColumn
ecsErrorPortIndex = _EcsErrorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 2),
    _EcsErrorPortIndex_Type()
)
ecsErrorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsErrorPortIndex.setStatus("mandatory")
_EcsCollisionsCount_Type = Counter32
_EcsCollisionsCount_Object = MibTableColumn
ecsCollisionsCount = _EcsCollisionsCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 3),
    _EcsCollisionsCount_Type()
)
ecsCollisionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCollisionsCount.setStatus("mandatory")
_EcsPartitions_Type = Counter32
_EcsPartitions_Object = MibTableColumn
ecsPartitions = _EcsPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 4),
    _EcsPartitions_Type()
)
ecsPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsPartitions.setStatus("mandatory")
_EcsCarrierSenseErrors_Type = Counter32
_EcsCarrierSenseErrors_Object = MibTableColumn
ecsCarrierSenseErrors = _EcsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 5),
    _EcsCarrierSenseErrors_Type()
)
ecsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCarrierSenseErrors.setStatus("mandatory")
_EcsAlignErrors_Type = Counter32
_EcsAlignErrors_Object = MibTableColumn
ecsAlignErrors = _EcsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 6),
    _EcsAlignErrors_Type()
)
ecsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAlignErrors.setStatus("mandatory")
_EcsCRCErrors_Type = Counter32
_EcsCRCErrors_Object = MibTableColumn
ecsCRCErrors = _EcsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 7),
    _EcsCRCErrors_Type()
)
ecsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCRCErrors.setStatus("mandatory")
_EcsJabberErrors_Type = Counter32
_EcsJabberErrors_Object = MibTableColumn
ecsJabberErrors = _EcsJabberErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 2, 1, 8),
    _EcsJabberErrors_Type()
)
ecsJabberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsJabberErrors.setStatus("mandatory")
_EcsRLCPortInfoTable_Object = MibTable
ecsRLCPortInfoTable = _EcsRLCPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3)
)
if mibBuilder.loadTexts:
    ecsRLCPortInfoTable.setStatus("mandatory")
_EcsRLCPortInfoEntry_Object = MibTableRow
ecsRLCPortInfoEntry = _EcsRLCPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1)
)
ecsRLCPortInfoEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsInfoSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsInfoPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCPortInfoEntry.setStatus("mandatory")
_EcsInfoSlotIndex_Type = Integer32
_EcsInfoSlotIndex_Object = MibTableColumn
ecsInfoSlotIndex = _EcsInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 1),
    _EcsInfoSlotIndex_Type()
)
ecsInfoSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsInfoSlotIndex.setStatus("mandatory")
_EcsInfoPortIndex_Type = Integer32
_EcsInfoPortIndex_Object = MibTableColumn
ecsInfoPortIndex = _EcsInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 2),
    _EcsInfoPortIndex_Type()
)
ecsInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsInfoPortIndex.setStatus("mandatory")


class _EcsInfoPortName_Type(DisplayString):
    """Custom type ecsInfoPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EcsInfoPortName_Type.__name__ = "DisplayString"
_EcsInfoPortName_Object = MibTableColumn
ecsInfoPortName = _EcsInfoPortName_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 3),
    _EcsInfoPortName_Type()
)
ecsInfoPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsInfoPortName.setStatus("mandatory")


class _EcsRepeaterPartitionAlgor_Type(Integer32):
    """Custom type ecsRepeaterPartitionAlgor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EcsRepeaterPartitionAlgor_Type.__name__ = "Integer32"
_EcsRepeaterPartitionAlgor_Object = MibTableColumn
ecsRepeaterPartitionAlgor = _EcsRepeaterPartitionAlgor_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 4),
    _EcsRepeaterPartitionAlgor_Type()
)
ecsRepeaterPartitionAlgor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRepeaterPartitionAlgor.setStatus("mandatory")


class _EcsJabberLockProtect_Type(Integer32):
    """Custom type ecsJabberLockProtect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EcsJabberLockProtect_Type.__name__ = "Integer32"
_EcsJabberLockProtect_Object = MibTableColumn
ecsJabberLockProtect = _EcsJabberLockProtect_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 5),
    _EcsJabberLockProtect_Type()
)
ecsJabberLockProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsJabberLockProtect.setStatus("mandatory")


class _EcsPortTest_Type(Integer32):
    """Custom type ecsPortTest based on Integer32"""
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
        *(("failed", 4),
          ("not-in-test", 1),
          ("passed", 3),
          ("test", 2))
    )


_EcsPortTest_Type.__name__ = "Integer32"
_EcsPortTest_Object = MibTableColumn
ecsPortTest = _EcsPortTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 6),
    _EcsPortTest_Type()
)
ecsPortTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsPortTest.setStatus("mandatory")


class _EcsPortErrorState_Type(Integer32):
    """Custom type ecsPortErrorState based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 255),
          ("hi-collision", 3),
          ("high-alignment-errorrate", 6),
          ("high-carriersense-errorrate", 9),
          ("high-crc-errorrate", 5),
          ("high-jabber-errorrate", 8),
          ("high-traffic-rate", 7),
          ("linkstatechange-down", 12),
          ("linkstatechange-up", 11),
          ("none", 1),
          ("normal", 2),
          ("partition", 4),
          ("unpartitioned", 10))
    )


_EcsPortErrorState_Type.__name__ = "Integer32"
_EcsPortErrorState_Object = MibTableColumn
ecsPortErrorState = _EcsPortErrorState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 7),
    _EcsPortErrorState_Type()
)
ecsPortErrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsPortErrorState.setStatus("mandatory")


class _EcsPortReset_Type(Integer32):
    """Custom type ecsPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-reset", 1),
          ("reset", 2))
    )


_EcsPortReset_Type.__name__ = "Integer32"
_EcsPortReset_Object = MibTableColumn
ecsPortReset = _EcsPortReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 8),
    _EcsPortReset_Type()
)
ecsPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsPortReset.setStatus("mandatory")


class _EcsPortPartitionTraps_Type(Integer32):
    """Custom type ecsPortPartitionTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_EcsPortPartitionTraps_Type.__name__ = "Integer32"
_EcsPortPartitionTraps_Object = MibTableColumn
ecsPortPartitionTraps = _EcsPortPartitionTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 9),
    _EcsPortPartitionTraps_Type()
)
ecsPortPartitionTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsPortPartitionTraps.setStatus("mandatory")


class _EcsPortLinkTraps_Type(Integer32):
    """Custom type ecsPortLinkTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("not-applicable", 3),
          ("yes", 1))
    )


_EcsPortLinkTraps_Type.__name__ = "Integer32"
_EcsPortLinkTraps_Object = MibTableColumn
ecsPortLinkTraps = _EcsPortLinkTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 10),
    _EcsPortLinkTraps_Type()
)
ecsPortLinkTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsPortLinkTraps.setStatus("mandatory")


class _EcsPortBootState_Type(Integer32):
    """Custom type ecsPortBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_EcsPortBootState_Type.__name__ = "Integer32"
_EcsPortBootState_Object = MibTableColumn
ecsPortBootState = _EcsPortBootState_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 11),
    _EcsPortBootState_Type()
)
ecsPortBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsPortBootState.setStatus("mandatory")


class _EcsPortSLMode_Type(Integer32):
    """Custom type ecsPortSLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_EcsPortSLMode_Type.__name__ = "Integer32"
_EcsPortSLMode_Object = MibTableColumn
ecsPortSLMode = _EcsPortSLMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 3, 1, 12),
    _EcsPortSLMode_Type()
)
ecsPortSLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsPortSLMode.setStatus("mandatory")
_EcsRLCcrcTable_Object = MibTable
ecsRLCcrcTable = _EcsRLCcrcTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4)
)
if mibBuilder.loadTexts:
    ecsRLCcrcTable.setStatus("mandatory")
_EcsRLCcrcEntry_Object = MibTableRow
ecsRLCcrcEntry = _EcsRLCcrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1)
)
ecsRLCcrcEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsCRCSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsCRCPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCcrcEntry.setStatus("mandatory")
_EcsCRCSlotIndex_Type = Integer32
_EcsCRCSlotIndex_Object = MibTableColumn
ecsCRCSlotIndex = _EcsCRCSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 1),
    _EcsCRCSlotIndex_Type()
)
ecsCRCSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCRCSlotIndex.setStatus("mandatory")
_EcsCRCPortIndex_Type = Integer32
_EcsCRCPortIndex_Object = MibTableColumn
ecsCRCPortIndex = _EcsCRCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 2),
    _EcsCRCPortIndex_Type()
)
ecsCRCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCRCPortIndex.setStatus("mandatory")
_EcsCRCErrorRate_Type = Gauge32
_EcsCRCErrorRate_Object = MibTableColumn
ecsCRCErrorRate = _EcsCRCErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 3),
    _EcsCRCErrorRate_Type()
)
ecsCRCErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCRCErrorRate.setStatus("mandatory")
_EcsCRCThreshold_Type = Integer32
_EcsCRCThreshold_Object = MibTableColumn
ecsCRCThreshold = _EcsCRCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 4),
    _EcsCRCThreshold_Type()
)
ecsCRCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCRCThreshold.setStatus("mandatory")
_EcsCRCDecRateValue_Type = Integer32
_EcsCRCDecRateValue_Object = MibTableColumn
ecsCRCDecRateValue = _EcsCRCDecRateValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 5),
    _EcsCRCDecRateValue_Type()
)
ecsCRCDecRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCRCDecRateValue.setStatus("mandatory")


class _EcsCRCDecRateUnits_Type(Integer32):
    """Custom type ecsCRCDecRateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("days", 7),
          ("hours", 6),
          ("microseconds", 2),
          ("milliseconds", 3),
          ("minutes", 5),
          ("other", 1),
          ("seconds", 4))
    )


_EcsCRCDecRateUnits_Type.__name__ = "Integer32"
_EcsCRCDecRateUnits_Object = MibTableColumn
ecsCRCDecRateUnits = _EcsCRCDecRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 6),
    _EcsCRCDecRateUnits_Type()
)
ecsCRCDecRateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCRCDecRateUnits.setStatus("mandatory")
_EcsCRCHysteresisValue_Type = Integer32
_EcsCRCHysteresisValue_Object = MibTableColumn
ecsCRCHysteresisValue = _EcsCRCHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 4, 1, 7),
    _EcsCRCHysteresisValue_Type()
)
ecsCRCHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCRCHysteresisValue.setStatus("mandatory")
_EcsRLCtrafficTable_Object = MibTable
ecsRLCtrafficTable = _EcsRLCtrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5)
)
if mibBuilder.loadTexts:
    ecsRLCtrafficTable.setStatus("mandatory")
_EcsRLCtrafficEntry_Object = MibTableRow
ecsRLCtrafficEntry = _EcsRLCtrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1)
)
ecsRLCtrafficEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsTrafficSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsTrafficPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCtrafficEntry.setStatus("mandatory")
_EcsTrafficSlotIndex_Type = Integer32
_EcsTrafficSlotIndex_Object = MibTableColumn
ecsTrafficSlotIndex = _EcsTrafficSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 1),
    _EcsTrafficSlotIndex_Type()
)
ecsTrafficSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsTrafficSlotIndex.setStatus("mandatory")
_EcsTrafficPortIndex_Type = Integer32
_EcsTrafficPortIndex_Object = MibTableColumn
ecsTrafficPortIndex = _EcsTrafficPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 2),
    _EcsTrafficPortIndex_Type()
)
ecsTrafficPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsTrafficPortIndex.setStatus("mandatory")
_EcsTrafficRate_Type = Gauge32
_EcsTrafficRate_Object = MibTableColumn
ecsTrafficRate = _EcsTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 3),
    _EcsTrafficRate_Type()
)
ecsTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsTrafficRate.setStatus("mandatory")
_EcsTrafficThreshold_Type = Integer32
_EcsTrafficThreshold_Object = MibTableColumn
ecsTrafficThreshold = _EcsTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 4),
    _EcsTrafficThreshold_Type()
)
ecsTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsTrafficThreshold.setStatus("mandatory")
_EcsTrafficDecRateValue_Type = Integer32
_EcsTrafficDecRateValue_Object = MibTableColumn
ecsTrafficDecRateValue = _EcsTrafficDecRateValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 5),
    _EcsTrafficDecRateValue_Type()
)
ecsTrafficDecRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsTrafficDecRateValue.setStatus("mandatory")


class _EcsTrafficDecRateUnits_Type(Integer32):
    """Custom type ecsTrafficDecRateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("days", 7),
          ("hours", 6),
          ("microseconds", 2),
          ("milliseconds", 3),
          ("minutes", 5),
          ("other", 1),
          ("seconds", 4))
    )


_EcsTrafficDecRateUnits_Type.__name__ = "Integer32"
_EcsTrafficDecRateUnits_Object = MibTableColumn
ecsTrafficDecRateUnits = _EcsTrafficDecRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 6),
    _EcsTrafficDecRateUnits_Type()
)
ecsTrafficDecRateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsTrafficDecRateUnits.setStatus("mandatory")
_EcsTrafficHysteresisValue_Type = Integer32
_EcsTrafficHysteresisValue_Object = MibTableColumn
ecsTrafficHysteresisValue = _EcsTrafficHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 5, 1, 7),
    _EcsTrafficHysteresisValue_Type()
)
ecsTrafficHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsTrafficHysteresisValue.setStatus("mandatory")
_EcsRLCcollisionTable_Object = MibTable
ecsRLCcollisionTable = _EcsRLCcollisionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6)
)
if mibBuilder.loadTexts:
    ecsRLCcollisionTable.setStatus("mandatory")
_EcsRLCcollisionEntry_Object = MibTableRow
ecsRLCcollisionEntry = _EcsRLCcollisionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1)
)
ecsRLCcollisionEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsCollisionSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsCollisionPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCcollisionEntry.setStatus("mandatory")
_EcsCollisionSlotIndex_Type = Integer32
_EcsCollisionSlotIndex_Object = MibTableColumn
ecsCollisionSlotIndex = _EcsCollisionSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 1),
    _EcsCollisionSlotIndex_Type()
)
ecsCollisionSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCollisionSlotIndex.setStatus("mandatory")
_EcsCollisionPortIndex_Type = Integer32
_EcsCollisionPortIndex_Object = MibTableColumn
ecsCollisionPortIndex = _EcsCollisionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 2),
    _EcsCollisionPortIndex_Type()
)
ecsCollisionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCollisionPortIndex.setStatus("mandatory")
_EcsCollisionRate_Type = Gauge32
_EcsCollisionRate_Object = MibTableColumn
ecsCollisionRate = _EcsCollisionRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 3),
    _EcsCollisionRate_Type()
)
ecsCollisionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCollisionRate.setStatus("mandatory")
_EcsCollisionThreshold_Type = Integer32
_EcsCollisionThreshold_Object = MibTableColumn
ecsCollisionThreshold = _EcsCollisionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 4),
    _EcsCollisionThreshold_Type()
)
ecsCollisionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCollisionThreshold.setStatus("mandatory")
_EcsCollisionDecRateValue_Type = Integer32
_EcsCollisionDecRateValue_Object = MibTableColumn
ecsCollisionDecRateValue = _EcsCollisionDecRateValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 5),
    _EcsCollisionDecRateValue_Type()
)
ecsCollisionDecRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCollisionDecRateValue.setStatus("mandatory")


class _EcsCollisionDecRateUnits_Type(Integer32):
    """Custom type ecsCollisionDecRateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("days", 7),
          ("hours", 6),
          ("microseconds", 2),
          ("milliseconds", 3),
          ("minutes", 5),
          ("other", 1),
          ("seconds", 4))
    )


_EcsCollisionDecRateUnits_Type.__name__ = "Integer32"
_EcsCollisionDecRateUnits_Object = MibTableColumn
ecsCollisionDecRateUnits = _EcsCollisionDecRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 6),
    _EcsCollisionDecRateUnits_Type()
)
ecsCollisionDecRateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCollisionDecRateUnits.setStatus("mandatory")
_EcsCollisionHysteresisValue_Type = Integer32
_EcsCollisionHysteresisValue_Object = MibTableColumn
ecsCollisionHysteresisValue = _EcsCollisionHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 6, 1, 7),
    _EcsCollisionHysteresisValue_Type()
)
ecsCollisionHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCollisionHysteresisValue.setStatus("mandatory")
_EcsRLCjabberTable_Object = MibTable
ecsRLCjabberTable = _EcsRLCjabberTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7)
)
if mibBuilder.loadTexts:
    ecsRLCjabberTable.setStatus("mandatory")
_EcsRLCjabberEntry_Object = MibTableRow
ecsRLCjabberEntry = _EcsRLCjabberEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1)
)
ecsRLCjabberEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsJabberSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsJabberPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCjabberEntry.setStatus("mandatory")
_EcsJabberSlotIndex_Type = Integer32
_EcsJabberSlotIndex_Object = MibTableColumn
ecsJabberSlotIndex = _EcsJabberSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 1),
    _EcsJabberSlotIndex_Type()
)
ecsJabberSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsJabberSlotIndex.setStatus("mandatory")
_EcsJabberPortIndex_Type = Integer32
_EcsJabberPortIndex_Object = MibTableColumn
ecsJabberPortIndex = _EcsJabberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 2),
    _EcsJabberPortIndex_Type()
)
ecsJabberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsJabberPortIndex.setStatus("mandatory")
_EcsJabberErrorRate_Type = Gauge32
_EcsJabberErrorRate_Object = MibTableColumn
ecsJabberErrorRate = _EcsJabberErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 3),
    _EcsJabberErrorRate_Type()
)
ecsJabberErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsJabberErrorRate.setStatus("mandatory")
_EcsJabberThreshold_Type = Integer32
_EcsJabberThreshold_Object = MibTableColumn
ecsJabberThreshold = _EcsJabberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 4),
    _EcsJabberThreshold_Type()
)
ecsJabberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsJabberThreshold.setStatus("mandatory")
_EcsJabberDecRateValue_Type = Integer32
_EcsJabberDecRateValue_Object = MibTableColumn
ecsJabberDecRateValue = _EcsJabberDecRateValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 5),
    _EcsJabberDecRateValue_Type()
)
ecsJabberDecRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsJabberDecRateValue.setStatus("mandatory")


class _EcsJabberDecRateUnits_Type(Integer32):
    """Custom type ecsJabberDecRateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("days", 7),
          ("hours", 6),
          ("microseconds", 2),
          ("milliseconds", 3),
          ("minutes", 5),
          ("other", 1),
          ("seconds", 4))
    )


_EcsJabberDecRateUnits_Type.__name__ = "Integer32"
_EcsJabberDecRateUnits_Object = MibTableColumn
ecsJabberDecRateUnits = _EcsJabberDecRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 6),
    _EcsJabberDecRateUnits_Type()
)
ecsJabberDecRateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsJabberDecRateUnits.setStatus("mandatory")
_EcsJabberHysteresisValue_Type = Integer32
_EcsJabberHysteresisValue_Object = MibTableColumn
ecsJabberHysteresisValue = _EcsJabberHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 7, 1, 7),
    _EcsJabberHysteresisValue_Type()
)
ecsJabberHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsJabberHysteresisValue.setStatus("mandatory")
_EcsRLCalignTable_Object = MibTable
ecsRLCalignTable = _EcsRLCalignTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8)
)
if mibBuilder.loadTexts:
    ecsRLCalignTable.setStatus("mandatory")
_EcsRLCalignEntry_Object = MibTableRow
ecsRLCalignEntry = _EcsRLCalignEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1)
)
ecsRLCalignEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsAlignSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsAlignPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCalignEntry.setStatus("mandatory")
_EcsAlignSlotIndex_Type = Integer32
_EcsAlignSlotIndex_Object = MibTableColumn
ecsAlignSlotIndex = _EcsAlignSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 1),
    _EcsAlignSlotIndex_Type()
)
ecsAlignSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAlignSlotIndex.setStatus("mandatory")
_EcsAlignPortIndex_Type = Integer32
_EcsAlignPortIndex_Object = MibTableColumn
ecsAlignPortIndex = _EcsAlignPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 2),
    _EcsAlignPortIndex_Type()
)
ecsAlignPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAlignPortIndex.setStatus("mandatory")
_EcsAlignErrorRate_Type = Gauge32
_EcsAlignErrorRate_Object = MibTableColumn
ecsAlignErrorRate = _EcsAlignErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 3),
    _EcsAlignErrorRate_Type()
)
ecsAlignErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsAlignErrorRate.setStatus("mandatory")
_EcsAlignThreshold_Type = Integer32
_EcsAlignThreshold_Object = MibTableColumn
ecsAlignThreshold = _EcsAlignThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 4),
    _EcsAlignThreshold_Type()
)
ecsAlignThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAlignThreshold.setStatus("mandatory")
_EcsAlignDecRateValue_Type = Integer32
_EcsAlignDecRateValue_Object = MibTableColumn
ecsAlignDecRateValue = _EcsAlignDecRateValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 5),
    _EcsAlignDecRateValue_Type()
)
ecsAlignDecRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAlignDecRateValue.setStatus("mandatory")


class _EcsAlignDecRateUnits_Type(Integer32):
    """Custom type ecsAlignDecRateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("days", 7),
          ("hours", 6),
          ("microseconds", 2),
          ("milliseconds", 3),
          ("minutes", 5),
          ("other", 1),
          ("seconds", 4))
    )


_EcsAlignDecRateUnits_Type.__name__ = "Integer32"
_EcsAlignDecRateUnits_Object = MibTableColumn
ecsAlignDecRateUnits = _EcsAlignDecRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 6),
    _EcsAlignDecRateUnits_Type()
)
ecsAlignDecRateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAlignDecRateUnits.setStatus("mandatory")
_EcsAlignHysteresisValue_Type = Integer32
_EcsAlignHysteresisValue_Object = MibTableColumn
ecsAlignHysteresisValue = _EcsAlignHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 8, 1, 7),
    _EcsAlignHysteresisValue_Type()
)
ecsAlignHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsAlignHysteresisValue.setStatus("mandatory")
_EcsRLCcarrierTable_Object = MibTable
ecsRLCcarrierTable = _EcsRLCcarrierTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9)
)
if mibBuilder.loadTexts:
    ecsRLCcarrierTable.setStatus("mandatory")
_EcsRLCcarrierEntry_Object = MibTableRow
ecsRLCcarrierEntry = _EcsRLCcarrierEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1)
)
ecsRLCcarrierEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsCarrierSlotIndex"),
    (0, "LBHUB-ECS-MIB", "ecsCarrierPortIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCcarrierEntry.setStatus("mandatory")
_EcsCarrierSlotIndex_Type = Integer32
_EcsCarrierSlotIndex_Object = MibTableColumn
ecsCarrierSlotIndex = _EcsCarrierSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 1),
    _EcsCarrierSlotIndex_Type()
)
ecsCarrierSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCarrierSlotIndex.setStatus("mandatory")
_EcsCarrierPortIndex_Type = Integer32
_EcsCarrierPortIndex_Object = MibTableColumn
ecsCarrierPortIndex = _EcsCarrierPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 2),
    _EcsCarrierPortIndex_Type()
)
ecsCarrierPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCarrierPortIndex.setStatus("mandatory")
_EcsCarrierSenseErrorRate_Type = Gauge32
_EcsCarrierSenseErrorRate_Object = MibTableColumn
ecsCarrierSenseErrorRate = _EcsCarrierSenseErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 3),
    _EcsCarrierSenseErrorRate_Type()
)
ecsCarrierSenseErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsCarrierSenseErrorRate.setStatus("mandatory")
_EcsCarrierSenseThreshold_Type = Integer32
_EcsCarrierSenseThreshold_Object = MibTableColumn
ecsCarrierSenseThreshold = _EcsCarrierSenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 4),
    _EcsCarrierSenseThreshold_Type()
)
ecsCarrierSenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCarrierSenseThreshold.setStatus("mandatory")
_EcsCarrierSenseRateValue_Type = Integer32
_EcsCarrierSenseRateValue_Object = MibTableColumn
ecsCarrierSenseRateValue = _EcsCarrierSenseRateValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 5),
    _EcsCarrierSenseRateValue_Type()
)
ecsCarrierSenseRateValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCarrierSenseRateValue.setStatus("mandatory")


class _EcsCarrierSenseRateUnits_Type(Integer32):
    """Custom type ecsCarrierSenseRateUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("days", 7),
          ("hours", 6),
          ("microseconds", 2),
          ("milliseconds", 3),
          ("minutes", 5),
          ("other", 1),
          ("seconds", 4))
    )


_EcsCarrierSenseRateUnits_Type.__name__ = "Integer32"
_EcsCarrierSenseRateUnits_Object = MibTableColumn
ecsCarrierSenseRateUnits = _EcsCarrierSenseRateUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 6),
    _EcsCarrierSenseRateUnits_Type()
)
ecsCarrierSenseRateUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCarrierSenseRateUnits.setStatus("mandatory")
_EcsCarrierSenseHysteresisValue_Type = Integer32
_EcsCarrierSenseHysteresisValue_Object = MibTableColumn
ecsCarrierSenseHysteresisValue = _EcsCarrierSenseHysteresisValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 9, 1, 7),
    _EcsCarrierSenseHysteresisValue_Type()
)
ecsCarrierSenseHysteresisValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsCarrierSenseHysteresisValue.setStatus("mandatory")
_EcsRLCSlotStatisticsTable_Object = MibTable
ecsRLCSlotStatisticsTable = _EcsRLCSlotStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10)
)
if mibBuilder.loadTexts:
    ecsRLCSlotStatisticsTable.setStatus("mandatory")
_EcsRLCSlotStatisticsEntry_Object = MibTableRow
ecsRLCSlotStatisticsEntry = _EcsRLCSlotStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1)
)
ecsRLCSlotStatisticsEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsRLCSlotIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCSlotStatisticsEntry.setStatus("mandatory")
_EcsRLCSlotIndex_Type = Integer32
_EcsRLCSlotIndex_Object = MibTableColumn
ecsRLCSlotIndex = _EcsRLCSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1, 1),
    _EcsRLCSlotIndex_Type()
)
ecsRLCSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCSlotIndex.setStatus("mandatory")
_EcsRLCGoodRcvdFrames_Type = Counter32
_EcsRLCGoodRcvdFrames_Object = MibTableColumn
ecsRLCGoodRcvdFrames = _EcsRLCGoodRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1, 2),
    _EcsRLCGoodRcvdFrames_Type()
)
ecsRLCGoodRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCGoodRcvdFrames.setStatus("mandatory")
_EcsRLCTotalByteCount_Type = Counter32
_EcsRLCTotalByteCount_Object = MibTableColumn
ecsRLCTotalByteCount = _EcsRLCTotalByteCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1, 3),
    _EcsRLCTotalByteCount_Type()
)
ecsRLCTotalByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCTotalByteCount.setStatus("mandatory")
_EcsRLCTotalErrorCount_Type = Counter32
_EcsRLCTotalErrorCount_Object = MibTableColumn
ecsRLCTotalErrorCount = _EcsRLCTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1, 4),
    _EcsRLCTotalErrorCount_Type()
)
ecsRLCTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCTotalErrorCount.setStatus("mandatory")
_EcsRLCTotalBroadcasts_Type = Counter32
_EcsRLCTotalBroadcasts_Object = MibTableColumn
ecsRLCTotalBroadcasts = _EcsRLCTotalBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1, 5),
    _EcsRLCTotalBroadcasts_Type()
)
ecsRLCTotalBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCTotalBroadcasts.setStatus("mandatory")
_EcsRLCTotalMulticasts_Type = Counter32
_EcsRLCTotalMulticasts_Object = MibTableColumn
ecsRLCTotalMulticasts = _EcsRLCTotalMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 10, 1, 6),
    _EcsRLCTotalMulticasts_Type()
)
ecsRLCTotalMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCTotalMulticasts.setStatus("mandatory")
_EcsRLCSlotErrorTable_Object = MibTable
ecsRLCSlotErrorTable = _EcsRLCSlotErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11)
)
if mibBuilder.loadTexts:
    ecsRLCSlotErrorTable.setStatus("mandatory")
_EcsRLCSlotErrorEntry_Object = MibTableRow
ecsRLCSlotErrorEntry = _EcsRLCSlotErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1)
)
ecsRLCSlotErrorEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsRLCErrorSlotIndex"),
)
if mibBuilder.loadTexts:
    ecsRLCSlotErrorEntry.setStatus("mandatory")
_EcsRLCErrorSlotIndex_Type = Integer32
_EcsRLCErrorSlotIndex_Object = MibTableColumn
ecsRLCErrorSlotIndex = _EcsRLCErrorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 1),
    _EcsRLCErrorSlotIndex_Type()
)
ecsRLCErrorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCErrorSlotIndex.setStatus("mandatory")
_EcsRLCCollisionsCount_Type = Counter32
_EcsRLCCollisionsCount_Object = MibTableColumn
ecsRLCCollisionsCount = _EcsRLCCollisionsCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 2),
    _EcsRLCCollisionsCount_Type()
)
ecsRLCCollisionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCCollisionsCount.setStatus("mandatory")
_EcsRLCPartitions_Type = Counter32
_EcsRLCPartitions_Object = MibTableColumn
ecsRLCPartitions = _EcsRLCPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 3),
    _EcsRLCPartitions_Type()
)
ecsRLCPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCPartitions.setStatus("mandatory")
_EcsRLCCarrierSenseErrors_Type = Counter32
_EcsRLCCarrierSenseErrors_Object = MibTableColumn
ecsRLCCarrierSenseErrors = _EcsRLCCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 4),
    _EcsRLCCarrierSenseErrors_Type()
)
ecsRLCCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCCarrierSenseErrors.setStatus("mandatory")
_EcsRLCAlignErrors_Type = Counter32
_EcsRLCAlignErrors_Object = MibTableColumn
ecsRLCAlignErrors = _EcsRLCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 5),
    _EcsRLCAlignErrors_Type()
)
ecsRLCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCAlignErrors.setStatus("mandatory")
_EcsRLCCRCErrors_Type = Counter32
_EcsRLCCRCErrors_Object = MibTableColumn
ecsRLCCRCErrors = _EcsRLCCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 6),
    _EcsRLCCRCErrors_Type()
)
ecsRLCCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCCRCErrors.setStatus("mandatory")
_EcsRLCJabberErrors_Type = Counter32
_EcsRLCJabberErrors_Object = MibTableColumn
ecsRLCJabberErrors = _EcsRLCJabberErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 5, 11, 1, 7),
    _EcsRLCJabberErrors_Type()
)
ecsRLCJabberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCJabberErrors.setStatus("mandatory")
_EcsRLCStationLocate_ObjectIdentity = ObjectIdentity
ecsRLCStationLocate = _EcsRLCStationLocate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 6)
)
_EcsRLCSizeOfStationLocateDB_Type = Integer32
_EcsRLCSizeOfStationLocateDB_Object = MibScalar
ecsRLCSizeOfStationLocateDB = _EcsRLCSizeOfStationLocateDB_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 1),
    _EcsRLCSizeOfStationLocateDB_Type()
)
ecsRLCSizeOfStationLocateDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCSizeOfStationLocateDB.setStatus("mandatory")
_EcsRLCNumbOfSLEntries_Type = Integer32
_EcsRLCNumbOfSLEntries_Object = MibScalar
ecsRLCNumbOfSLEntries = _EcsRLCNumbOfSLEntries_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 2),
    _EcsRLCNumbOfSLEntries_Type()
)
ecsRLCNumbOfSLEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCNumbOfSLEntries.setStatus("mandatory")


class _EcsRLCSLDataBaseStatus_Type(Integer32):
    """Custom type ecsRLCSLDataBaseStatus based on Integer32"""
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
        *(("changed", 1),
          ("clear", 3),
          ("full", 4),
          ("unchanged", 2))
    )


_EcsRLCSLDataBaseStatus_Type.__name__ = "Integer32"
_EcsRLCSLDataBaseStatus_Object = MibScalar
ecsRLCSLDataBaseStatus = _EcsRLCSLDataBaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 3),
    _EcsRLCSLDataBaseStatus_Type()
)
ecsRLCSLDataBaseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLCSLDataBaseStatus.setStatus("mandatory")
_EcsRLCSLowFilterAddress_Type = OctetString
_EcsRLCSLowFilterAddress_Object = MibScalar
ecsRLCSLowFilterAddress = _EcsRLCSLowFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 4),
    _EcsRLCSLowFilterAddress_Type()
)
ecsRLCSLowFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLCSLowFilterAddress.setStatus("mandatory")
_EcsRLCSLhighFilterAddress_Type = OctetString
_EcsRLCSLhighFilterAddress_Object = MibScalar
ecsRLCSLhighFilterAddress = _EcsRLCSLhighFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 5),
    _EcsRLCSLhighFilterAddress_Type()
)
ecsRLCSLhighFilterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLCSLhighFilterAddress.setStatus("mandatory")
_EcsRLCStationLocateTable_Object = MibTable
ecsRLCStationLocateTable = _EcsRLCStationLocateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 6)
)
if mibBuilder.loadTexts:
    ecsRLCStationLocateTable.setStatus("mandatory")
_EcsRLCStationLocateEntry_Object = MibTableRow
ecsRLCStationLocateEntry = _EcsRLCStationLocateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 6, 1)
)
ecsRLCStationLocateEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsRLCSLAddress"),
)
if mibBuilder.loadTexts:
    ecsRLCStationLocateEntry.setStatus("mandatory")
_EcsRLCSLAddress_Type = OctetString
_EcsRLCSLAddress_Object = MibTableColumn
ecsRLCSLAddress = _EcsRLCSLAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 6, 1, 1),
    _EcsRLCSLAddress_Type()
)
ecsRLCSLAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCSLAddress.setStatus("mandatory")
_EcsRLCSLSlotIndex_Type = Integer32
_EcsRLCSLSlotIndex_Object = MibTableColumn
ecsRLCSLSlotIndex = _EcsRLCSLSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 6, 1, 2),
    _EcsRLCSLSlotIndex_Type()
)
ecsRLCSLSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCSLSlotIndex.setStatus("mandatory")
_EcsRLCSLPortIndex_Type = Integer32
_EcsRLCSLPortIndex_Object = MibTableColumn
ecsRLCSLPortIndex = _EcsRLCSLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 6, 1, 3),
    _EcsRLCSLPortIndex_Type()
)
ecsRLCSLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCSLPortIndex.setStatus("mandatory")


class _EcsRLCSLStatus_Type(Integer32):
    """Custom type ecsRLCSLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_EcsRLCSLStatus_Type.__name__ = "Integer32"
_EcsRLCSLStatus_Object = MibTableColumn
ecsRLCSLStatus = _EcsRLCSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 6, 1, 4),
    _EcsRLCSLStatus_Type()
)
ecsRLCSLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsRLCSLStatus.setStatus("mandatory")
_EcsRLCNewStationLocateTable_Object = MibTable
ecsRLCNewStationLocateTable = _EcsRLCNewStationLocateTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 7)
)
if mibBuilder.loadTexts:
    ecsRLCNewStationLocateTable.setStatus("mandatory")
_EcsRLCNewStationLocateEntry_Object = MibTableRow
ecsRLCNewStationLocateEntry = _EcsRLCNewStationLocateEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 7, 1)
)
ecsRLCNewStationLocateEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsRLCNewSLAddress"),
)
if mibBuilder.loadTexts:
    ecsRLCNewStationLocateEntry.setStatus("mandatory")
_EcsRLCNewSLAddress_Type = OctetString
_EcsRLCNewSLAddress_Object = MibTableColumn
ecsRLCNewSLAddress = _EcsRLCNewSLAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 7, 1, 1),
    _EcsRLCNewSLAddress_Type()
)
ecsRLCNewSLAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCNewSLAddress.setStatus("mandatory")
_EcsRLCNewSLSlotIndex_Type = Integer32
_EcsRLCNewSLSlotIndex_Object = MibTableColumn
ecsRLCNewSLSlotIndex = _EcsRLCNewSLSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 7, 1, 2),
    _EcsRLCNewSLSlotIndex_Type()
)
ecsRLCNewSLSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCNewSLSlotIndex.setStatus("mandatory")
_EcsRLCNewSLPortIndex_Type = Integer32
_EcsRLCNewSLPortIndex_Object = MibTableColumn
ecsRLCNewSLPortIndex = _EcsRLCNewSLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 6, 7, 1, 3),
    _EcsRLCNewSLPortIndex_Type()
)
ecsRLCNewSLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsRLCNewSLPortIndex.setStatus("mandatory")
_EcsHubStatistics_ObjectIdentity = ObjectIdentity
ecsHubStatistics = _EcsHubStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 8)
)
_EcsHubTotalGoodRcvdFrames_Type = Counter32
_EcsHubTotalGoodRcvdFrames_Object = MibScalar
ecsHubTotalGoodRcvdFrames = _EcsHubTotalGoodRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 1),
    _EcsHubTotalGoodRcvdFrames_Type()
)
ecsHubTotalGoodRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalGoodRcvdFrames.setStatus("mandatory")
_EcsHubTotalByteCount_Type = Counter32
_EcsHubTotalByteCount_Object = MibScalar
ecsHubTotalByteCount = _EcsHubTotalByteCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 2),
    _EcsHubTotalByteCount_Type()
)
ecsHubTotalByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalByteCount.setStatus("mandatory")
_EcsHubTotalErrorCount_Type = Counter32
_EcsHubTotalErrorCount_Object = MibScalar
ecsHubTotalErrorCount = _EcsHubTotalErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 3),
    _EcsHubTotalErrorCount_Type()
)
ecsHubTotalErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalErrorCount.setStatus("mandatory")
_EcsHubTotalBroadcasts_Type = Counter32
_EcsHubTotalBroadcasts_Object = MibScalar
ecsHubTotalBroadcasts = _EcsHubTotalBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 4),
    _EcsHubTotalBroadcasts_Type()
)
ecsHubTotalBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalBroadcasts.setStatus("mandatory")
_EcsHubTotalMultiFrames_Type = Counter32
_EcsHubTotalMultiFrames_Object = MibScalar
ecsHubTotalMultiFrames = _EcsHubTotalMultiFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 5),
    _EcsHubTotalMultiFrames_Type()
)
ecsHubTotalMultiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalMultiFrames.setStatus("mandatory")
_EcsHubTotalCollisionsCount_Type = Counter32
_EcsHubTotalCollisionsCount_Object = MibScalar
ecsHubTotalCollisionsCount = _EcsHubTotalCollisionsCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 6),
    _EcsHubTotalCollisionsCount_Type()
)
ecsHubTotalCollisionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalCollisionsCount.setStatus("mandatory")
_EcsHubTotalPartitions_Type = Counter32
_EcsHubTotalPartitions_Object = MibScalar
ecsHubTotalPartitions = _EcsHubTotalPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 7),
    _EcsHubTotalPartitions_Type()
)
ecsHubTotalPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalPartitions.setStatus("mandatory")
_EcsHubTotalCarrierSenseErrors_Type = Counter32
_EcsHubTotalCarrierSenseErrors_Object = MibScalar
ecsHubTotalCarrierSenseErrors = _EcsHubTotalCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 8),
    _EcsHubTotalCarrierSenseErrors_Type()
)
ecsHubTotalCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalCarrierSenseErrors.setStatus("mandatory")
_EcsHubTotalAlignErrors_Type = Counter32
_EcsHubTotalAlignErrors_Object = MibScalar
ecsHubTotalAlignErrors = _EcsHubTotalAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 9),
    _EcsHubTotalAlignErrors_Type()
)
ecsHubTotalAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalAlignErrors.setStatus("mandatory")
_EcsHubTotalCRCErrors_Type = Counter32
_EcsHubTotalCRCErrors_Object = MibScalar
ecsHubTotalCRCErrors = _EcsHubTotalCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 10),
    _EcsHubTotalCRCErrors_Type()
)
ecsHubTotalCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalCRCErrors.setStatus("mandatory")
_EcsHubTotalJabberErrors_Type = Counter32
_EcsHubTotalJabberErrors_Object = MibScalar
ecsHubTotalJabberErrors = _EcsHubTotalJabberErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 8, 11),
    _EcsHubTotalJabberErrors_Type()
)
ecsHubTotalJabberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsHubTotalJabberErrors.setStatus("mandatory")
_EcsVideo_ObjectIdentity = ObjectIdentity
ecsVideo = _EcsVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 9)
)
_LbecsXENDOFMIB_ObjectIdentity = ObjectIdentity
lbecsXENDOFMIB = _LbecsXENDOFMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9, 255)
)
_XecsDummyTable_Object = MibTable
xecsDummyTable = _XecsDummyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 255, 1)
)
if mibBuilder.loadTexts:
    xecsDummyTable.setStatus("mandatory")
_EcsDummyEntry_Object = MibTableRow
ecsDummyEntry = _EcsDummyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 255, 1, 1)
)
ecsDummyEntry.setIndexNames(
    (0, "LBHUB-ECS-MIB", "ecsDummyIndex"),
)
if mibBuilder.loadTexts:
    ecsDummyEntry.setStatus("mandatory")
_EcsDummyIndex_Type = Integer32
_EcsDummyIndex_Object = MibTableColumn
ecsDummyIndex = _EcsDummyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 255, 1, 1, 1),
    _EcsDummyIndex_Type()
)
ecsDummyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecsDummyIndex.setStatus("mandatory")
_EcsDummyValue_Type = Integer32
_EcsDummyValue_Object = MibTableColumn
ecsDummyValue = _EcsDummyValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 9, 255, 1, 1, 2),
    _EcsDummyValue_Type()
)
ecsDummyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ecsDummyValue.setStatus("mandatory")
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_TestData_ObjectIdentity = ObjectIdentity
testData = _TestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 1)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 2)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2)
)
_SysLoader_ObjectIdentity = ObjectIdentity
sysLoader = _SysLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 3)
)
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 4)
)
_Gauges_ObjectIdentity = ObjectIdentity
gauges = _Gauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 5)
)
_AsciiAgent_ObjectIdentity = ObjectIdentity
asciiAgent = _AsciiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 6)
)
_SerialIf_ObjectIdentity = ObjectIdentity
serialIf = _SerialIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 7)
)
_RepeaterMgmt_ObjectIdentity = ObjectIdentity
repeaterMgmt = _RepeaterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8)
)
_EndStation_ObjectIdentity = ObjectIdentity
endStation = _EndStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 9)
)
_LocalSnmp_ObjectIdentity = ObjectIdentity
localSnmp = _LocalSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 10)
)
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 11)
)
_UnusedGeneric12_ObjectIdentity = ObjectIdentity
unusedGeneric12 = _UnusedGeneric12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14)
)
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16)
)
_MultiRepeater_ObjectIdentity = ObjectIdentity
multiRepeater = _MultiRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17)
)
_BridgeMgmt_ObjectIdentity = ObjectIdentity
bridgeMgmt = _BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 19)
)
_Poll_ObjectIdentity = ObjectIdentity
poll = _Poll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 20)
)
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21)
)
_NetBuilder_mib_ObjectIdentity = ObjectIdentity
netBuilder_mib = _NetBuilder_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 11)
)
_LBridgeECS_mib_ObjectIdentity = ObjectIdentity
lBridgeECS_mib = _LBridgeECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 12)
)
_DeskMan_mib_ObjectIdentity = ObjectIdentity
deskMan_mib = _DeskMan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 13)
)
_LinkBuilderMSH_mib_ObjectIdentity = ObjectIdentity
linkBuilderMSH_mib = _LinkBuilderMSH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14)
)

# Managed Objects groups


# Notification objects

powerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 0)
)
powerSupplyFailure.setObjects(
    ("LBHUB-ECS-MIB", "ecsPSUStatus")
)
if mibBuilder.loadTexts:
    powerSupplyFailure.setStatus(
        ""
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 1)
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        ""
    )

configurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 2)
)
if mibBuilder.loadTexts:
    configurationChanged.setStatus(
        ""
    )

portTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 3)
)
portTrap.setObjects(
      *(("LBHUB-ECS-MIB", "ecsInfoSlotIndex"),
        ("LBHUB-ECS-MIB", "ecsInfoPortIndex"),
        ("LBHUB-ECS-MIB", "ecsPortErrorState"))
)
if mibBuilder.loadTexts:
    portTrap.setStatus(
        ""
    )

resilientLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 4)
)
resilientLinkTrap.setObjects(
      *(("LBHUB-ECS-MIB", "ecsRLMainLinkSlot"),
        ("LBHUB-ECS-MIB", "ecsRLMainLinkPort"),
        ("LBHUB-ECS-MIB", "ecsRLStandbySlot"),
        ("LBHUB-ECS-MIB", "ecsRLStandbyPort"),
        ("LBHUB-ECS-MIB", "ecsRLActiveLink"),
        ("LBHUB-ECS-MIB", "ecsResLinkState"))
)
if mibBuilder.loadTexts:
    resilientLinkTrap.setStatus(
        ""
    )

rateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 5)
)
rateTrap.setObjects(
      *(("LBHUB-ECS-MIB", "ecsInfoSlotIndex"),
        ("LBHUB-ECS-MIB", "ecsInfoPortIndex"),
        ("LBHUB-ECS-MIB", "ecsPortErrorState"))
)
if mibBuilder.loadTexts:
    rateTrap.setStatus(
        ""
    )

stationlocateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 6)
)
stationlocateTrap.setObjects(
    ("LBHUB-ECS-MIB", "ecsRLCSLDataBaseStatus")
)
if mibBuilder.loadTexts:
    stationlocateTrap.setStatus(
        ""
    )

secureRLCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 7)
)
secureRLCTrap.setObjects(
    ("LBHUB-ECS-MIB", "ecsAgentSecureManagementStatus")
)
if mibBuilder.loadTexts:
    secureRLCTrap.setStatus(
        ""
    )

secureRLCportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3, 0, 8)
)
secureRLCportTrap.setObjects(
      *(("LBHUB-ECS-MIB", "ecsSecRLCSlotIndex"),
        ("LBHUB-ECS-MIB", "ecsSecRLCPortIndex"),
        ("LBHUB-ECS-MIB", "ecsSecRLCPortState"),
        ("LBHUB-ECS-MIB", "ecsSecRLCMACAddress"))
)
if mibBuilder.loadTexts:
    secureRLCportTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LBHUB-ECS-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "mib-2": mib_2,
       "system": system,
       "interfaces": interfaces,
       "at": at,
       "ip": ip,
       "icmp": icmp,
       "tcp": tcp,
       "udp": udp,
       "egp": egp,
       "transmission": transmission,
       "snmp": snmp,
       "a3Com": a3Com,
       "products": products,
       "terminalServer": terminalServer,
       "dedicatedBridgeServer": dedicatedBridgeServer,
       "dedicatedRouteServer": dedicatedRouteServer,
       "brouter": brouter,
       "genericMSWorkstation": genericMSWorkstation,
       "genericMSServer": genericMSServer,
       "genericUnixServer": genericUnixServer,
       "hub": hub,
       "linkBuilder3GH": linkBuilder3GH,
       "linkBuilder10BTi": linkBuilder10BTi,
       "linkBuilderECS": linkBuilderECS,
       "powerSupplyFailure": powerSupplyFailure,
       "fanFailure": fanFailure,
       "configurationChanged": configurationChanged,
       "portTrap": portTrap,
       "resilientLinkTrap": resilientLinkTrap,
       "rateTrap": rateTrap,
       "stationlocateTrap": stationlocateTrap,
       "secureRLCTrap": secureRLCTrap,
       "secureRLCportTrap": secureRLCportTrap,
       "linkBuilderMSH": linkBuilderMSH,
       "linkBuilderFMS": linkBuilderFMS,
       "linkBuilderFMSII": linkBuilderFMSII,
       "linkBuilderFMSLBridge": linkBuilderFMSLBridge,
       "cards": cards,
       "linkBuilder3GH-cards": linkBuilder3GH_cards,
       "linkBuilder10BTi-cards": linkBuilder10BTi_cards,
       "linkBuilder10BTi-cards-utp": linkBuilder10BTi_cards_utp,
       "linkBuilder10BT-cards-utp": linkBuilder10BT_cards_utp,
       "linkBuilderECS-cards": linkBuilderECS_cards,
       "linkBuilderMSH-cards": linkBuilderMSH_cards,
       "linkBuilderFMS-cards": linkBuilderFMS_cards,
       "linkBuilderFMS-cards-utp": linkBuilderFMS_cards_utp,
       "linkBuilderFMS-cards-coax": linkBuilderFMS_cards_coax,
       "linkBuilderFMS-cards-fiber": linkBuilderFMS_cards_fiber,
       "linkBuilderFMS-cards-12fiber": linkBuilderFMS_cards_12fiber,
       "linkBuilderFMS-cards-24utp": linkBuilderFMS_cards_24utp,
       "linkBuilderFMSII-cards": linkBuilderFMSII_cards,
       "linkBuilderFMSII-cards-12tp-rj45": linkBuilderFMSII_cards_12tp_rj45,
       "linkBuilderFMSII-cards-10coax-bnc": linkBuilderFMSII_cards_10coax_bnc,
       "linkBuilderFMSII-cards-6fiber-st": linkBuilderFMSII_cards_6fiber_st,
       "linkBuilderFMSII-cards-12fiber-st": linkBuilderFMSII_cards_12fiber_st,
       "linkBuilderFMSII-cards-24tp-rj45": linkBuilderFMSII_cards_24tp_rj45,
       "linkBuilderFMSII-cards-24tp-telco": linkBuilderFMSII_cards_24tp_telco,
       "amp-mib": amp_mib,
       "genericTrap": genericTrap,
       "viewBuilderApps": viewBuilderApps,
       "specificTrap": specificTrap,
       "linkBuilder3GH-mib": linkBuilder3GH_mib,
       "linkBuilder10BTi-mib": linkBuilder10BTi_mib,
       "linkBuilderECS-mib": linkBuilderECS_mib,
       "ecsAgent": ecsAgent,
       "ecsAgentSystemIdentifier": ecsAgentSystemIdentifier,
       "ecsManufacturerId": ecsManufacturerId,
       "ecsManufacturerProductId": ecsManufacturerProductId,
       "ecsSoftwareVersionNumber": ecsSoftwareVersionNumber,
       "ecsHardwareVersionNumber": ecsHardwareVersionNumber,
       "ecsAgentSystemName": ecsAgentSystemName,
       "ecsAgentSystemLocation": ecsAgentSystemLocation,
       "ecsAgentSystemTime": ecsAgentSystemTime,
       "ecsAgentStatus": ecsAgentStatus,
       "ecsAgentAuthenticationStatus": ecsAgentAuthenticationStatus,
       "ecsAgentSecureManagementStatus": ecsAgentSecureManagementStatus,
       "ecsAgentFrontPanelSetupPassword": ecsAgentFrontPanelSetupPassword,
       "ecsAgentFrontPanelDisplay": ecsAgentFrontPanelDisplay,
       "ecsAgentFrontPanelPassword": ecsAgentFrontPanelPassword,
       "ecsAgentFrontPanelSecurePassword": ecsAgentFrontPanelSecurePassword,
       "ecsAgentFrontPanelLock": ecsAgentFrontPanelLock,
       "ecsAgentResetDevice": ecsAgentResetDevice,
       "ecsAgentRestart": ecsAgentRestart,
       "ecsAgentDefaultConfig": ecsAgentDefaultConfig,
       "ecsAgentManagementTable": ecsAgentManagementTable,
       "ecsAgentManagementEntry": ecsAgentManagementEntry,
       "ecsAgentManagementAddr": ecsAgentManagementAddr,
       "ecsAgentManagementAccess": ecsAgentManagementAccess,
       "ecsAgentManAccessLevel": ecsAgentManAccessLevel,
       "ecsAgentTrapReceiverTable": ecsAgentTrapReceiverTable,
       "ecsAgentTrapReceiverEntry": ecsAgentTrapReceiverEntry,
       "ecsAgentTrapReceiverAddr": ecsAgentTrapReceiverAddr,
       "ecsAgentTrapType": ecsAgentTrapType,
       "ecsAgentTrapReceiverComm": ecsAgentTrapReceiverComm,
       "ecsAgentTrapLevel": ecsAgentTrapLevel,
       "ecsAgentAuthTrapState": ecsAgentAuthTrapState,
       "ecsAgentIpAddr": ecsAgentIpAddr,
       "ecsAgentIpNetmask": ecsAgentIpNetmask,
       "ecsAgentDefaultGateway": ecsAgentDefaultGateway,
       "ecsAgentIpBroadAddr": ecsAgentIpBroadAddr,
       "ecsAgentMACAddress": ecsAgentMACAddress,
       "ecsAgentSecureTrapState": ecsAgentSecureTrapState,
       "ecsAgentLastSystemError": ecsAgentLastSystemError,
       "ecsAgentLastTrap": ecsAgentLastTrap,
       "ecsEnvironment": ecsEnvironment,
       "ecsRackType": ecsRackType,
       "ecsRackConfigurationTable": ecsRackConfigurationTable,
       "ecsSlotConfigEntry": ecsSlotConfigEntry,
       "ecsSlotConfigIndex": ecsSlotConfigIndex,
       "ecsSlotCardName": ecsSlotCardName,
       "ecsSlotDeviceType": ecsSlotDeviceType,
       "ecsSlotSoftVerNum": ecsSlotSoftVerNum,
       "ecsSlotHardVerNum": ecsSlotHardVerNum,
       "ecsSlotNumOfPorts": ecsSlotNumOfPorts,
       "ecsSlotMediaType": ecsSlotMediaType,
       "ecsCardReset": ecsCardReset,
       "ecsLampOverRide": ecsLampOverRide,
       "ecsCardIsolated": ecsCardIsolated,
       "ecsCardIpAddress": ecsCardIpAddress,
       "ecsPSUStatus": ecsPSUStatus,
       "ecsFanStatus": ecsFanStatus,
       "ecsRLCResilientLinks": ecsRLCResilientLinks,
       "ecsRLCNumberOfResilientLinks": ecsRLCNumberOfResilientLinks,
       "ecsRLCNumberOfDOBPorts": ecsRLCNumberOfDOBPorts,
       "ecsRLCResilientLinkTable": ecsRLCResilientLinkTable,
       "ecsRLCResilientLinkEntry": ecsRLCResilientLinkEntry,
       "ecsRLMainLinkSlot": ecsRLMainLinkSlot,
       "ecsRLMainLinkPort": ecsRLMainLinkPort,
       "ecsRLStandbySlot": ecsRLStandbySlot,
       "ecsRLStandbyPort": ecsRLStandbyPort,
       "ecsRLActiveLink": ecsRLActiveLink,
       "ecsResLinkState": ecsResLinkState,
       "ecsSecureRepeaterLineCards": ecsSecureRepeaterLineCards,
       "ecsSecureRLCMode": ecsSecureRLCMode,
       "ecsSecureTrapRepRate": ecsSecureTrapRepRate,
       "ecsSecureRLCTable": ecsSecureRLCTable,
       "ecsSecureRLCEntry": ecsSecureRLCEntry,
       "ecsSecRLCSlotIndex": ecsSecRLCSlotIndex,
       "ecsSecRLCPortIndex": ecsSecRLCPortIndex,
       "ecsSecRLCLinkState": ecsSecRLCLinkState,
       "ecsSecRLCPortState": ecsSecRLCPortState,
       "ecsSecRLCNTKState": ecsSecRLCNTKState,
       "ecsSecRLCBroadState": ecsSecRLCBroadState,
       "ecsSecRLCMultiState": ecsSecRLCMultiState,
       "ecsSecRLCLearnMode": ecsSecRLCLearnMode,
       "ecsSecRLCReportMode": ecsSecRLCReportMode,
       "ecsSecRLCMACAddress": ecsSecRLCMACAddress,
       "ecsRepeaterLineCard": ecsRepeaterLineCard,
       "ecsRLCPortStatisticsTable": ecsRLCPortStatisticsTable,
       "ecsRLCPortStatisticsEntry": ecsRLCPortStatisticsEntry,
       "ecsRepeaterSlotIndex": ecsRepeaterSlotIndex,
       "ecsRepeaterPortIndex": ecsRepeaterPortIndex,
       "ecsRepeaterPortState": ecsRepeaterPortState,
       "ecsRepeaterPartitionState": ecsRepeaterPartitionState,
       "ecsGoodRcvdFrames": ecsGoodRcvdFrames,
       "ecsTotalByteCount": ecsTotalByteCount,
       "ecsTotalErrorCount": ecsTotalErrorCount,
       "ecsRxBroadcastFrames": ecsRxBroadcastFrames,
       "ecsRxMulticastFrames": ecsRxMulticastFrames,
       "ecsRLCPortErrorTable": ecsRLCPortErrorTable,
       "ecsRLCPortErrorEntry": ecsRLCPortErrorEntry,
       "ecsErrorSlotIndex": ecsErrorSlotIndex,
       "ecsErrorPortIndex": ecsErrorPortIndex,
       "ecsCollisionsCount": ecsCollisionsCount,
       "ecsPartitions": ecsPartitions,
       "ecsCarrierSenseErrors": ecsCarrierSenseErrors,
       "ecsAlignErrors": ecsAlignErrors,
       "ecsCRCErrors": ecsCRCErrors,
       "ecsJabberErrors": ecsJabberErrors,
       "ecsRLCPortInfoTable": ecsRLCPortInfoTable,
       "ecsRLCPortInfoEntry": ecsRLCPortInfoEntry,
       "ecsInfoSlotIndex": ecsInfoSlotIndex,
       "ecsInfoPortIndex": ecsInfoPortIndex,
       "ecsInfoPortName": ecsInfoPortName,
       "ecsRepeaterPartitionAlgor": ecsRepeaterPartitionAlgor,
       "ecsJabberLockProtect": ecsJabberLockProtect,
       "ecsPortTest": ecsPortTest,
       "ecsPortErrorState": ecsPortErrorState,
       "ecsPortReset": ecsPortReset,
       "ecsPortPartitionTraps": ecsPortPartitionTraps,
       "ecsPortLinkTraps": ecsPortLinkTraps,
       "ecsPortBootState": ecsPortBootState,
       "ecsPortSLMode": ecsPortSLMode,
       "ecsRLCcrcTable": ecsRLCcrcTable,
       "ecsRLCcrcEntry": ecsRLCcrcEntry,
       "ecsCRCSlotIndex": ecsCRCSlotIndex,
       "ecsCRCPortIndex": ecsCRCPortIndex,
       "ecsCRCErrorRate": ecsCRCErrorRate,
       "ecsCRCThreshold": ecsCRCThreshold,
       "ecsCRCDecRateValue": ecsCRCDecRateValue,
       "ecsCRCDecRateUnits": ecsCRCDecRateUnits,
       "ecsCRCHysteresisValue": ecsCRCHysteresisValue,
       "ecsRLCtrafficTable": ecsRLCtrafficTable,
       "ecsRLCtrafficEntry": ecsRLCtrafficEntry,
       "ecsTrafficSlotIndex": ecsTrafficSlotIndex,
       "ecsTrafficPortIndex": ecsTrafficPortIndex,
       "ecsTrafficRate": ecsTrafficRate,
       "ecsTrafficThreshold": ecsTrafficThreshold,
       "ecsTrafficDecRateValue": ecsTrafficDecRateValue,
       "ecsTrafficDecRateUnits": ecsTrafficDecRateUnits,
       "ecsTrafficHysteresisValue": ecsTrafficHysteresisValue,
       "ecsRLCcollisionTable": ecsRLCcollisionTable,
       "ecsRLCcollisionEntry": ecsRLCcollisionEntry,
       "ecsCollisionSlotIndex": ecsCollisionSlotIndex,
       "ecsCollisionPortIndex": ecsCollisionPortIndex,
       "ecsCollisionRate": ecsCollisionRate,
       "ecsCollisionThreshold": ecsCollisionThreshold,
       "ecsCollisionDecRateValue": ecsCollisionDecRateValue,
       "ecsCollisionDecRateUnits": ecsCollisionDecRateUnits,
       "ecsCollisionHysteresisValue": ecsCollisionHysteresisValue,
       "ecsRLCjabberTable": ecsRLCjabberTable,
       "ecsRLCjabberEntry": ecsRLCjabberEntry,
       "ecsJabberSlotIndex": ecsJabberSlotIndex,
       "ecsJabberPortIndex": ecsJabberPortIndex,
       "ecsJabberErrorRate": ecsJabberErrorRate,
       "ecsJabberThreshold": ecsJabberThreshold,
       "ecsJabberDecRateValue": ecsJabberDecRateValue,
       "ecsJabberDecRateUnits": ecsJabberDecRateUnits,
       "ecsJabberHysteresisValue": ecsJabberHysteresisValue,
       "ecsRLCalignTable": ecsRLCalignTable,
       "ecsRLCalignEntry": ecsRLCalignEntry,
       "ecsAlignSlotIndex": ecsAlignSlotIndex,
       "ecsAlignPortIndex": ecsAlignPortIndex,
       "ecsAlignErrorRate": ecsAlignErrorRate,
       "ecsAlignThreshold": ecsAlignThreshold,
       "ecsAlignDecRateValue": ecsAlignDecRateValue,
       "ecsAlignDecRateUnits": ecsAlignDecRateUnits,
       "ecsAlignHysteresisValue": ecsAlignHysteresisValue,
       "ecsRLCcarrierTable": ecsRLCcarrierTable,
       "ecsRLCcarrierEntry": ecsRLCcarrierEntry,
       "ecsCarrierSlotIndex": ecsCarrierSlotIndex,
       "ecsCarrierPortIndex": ecsCarrierPortIndex,
       "ecsCarrierSenseErrorRate": ecsCarrierSenseErrorRate,
       "ecsCarrierSenseThreshold": ecsCarrierSenseThreshold,
       "ecsCarrierSenseRateValue": ecsCarrierSenseRateValue,
       "ecsCarrierSenseRateUnits": ecsCarrierSenseRateUnits,
       "ecsCarrierSenseHysteresisValue": ecsCarrierSenseHysteresisValue,
       "ecsRLCSlotStatisticsTable": ecsRLCSlotStatisticsTable,
       "ecsRLCSlotStatisticsEntry": ecsRLCSlotStatisticsEntry,
       "ecsRLCSlotIndex": ecsRLCSlotIndex,
       "ecsRLCGoodRcvdFrames": ecsRLCGoodRcvdFrames,
       "ecsRLCTotalByteCount": ecsRLCTotalByteCount,
       "ecsRLCTotalErrorCount": ecsRLCTotalErrorCount,
       "ecsRLCTotalBroadcasts": ecsRLCTotalBroadcasts,
       "ecsRLCTotalMulticasts": ecsRLCTotalMulticasts,
       "ecsRLCSlotErrorTable": ecsRLCSlotErrorTable,
       "ecsRLCSlotErrorEntry": ecsRLCSlotErrorEntry,
       "ecsRLCErrorSlotIndex": ecsRLCErrorSlotIndex,
       "ecsRLCCollisionsCount": ecsRLCCollisionsCount,
       "ecsRLCPartitions": ecsRLCPartitions,
       "ecsRLCCarrierSenseErrors": ecsRLCCarrierSenseErrors,
       "ecsRLCAlignErrors": ecsRLCAlignErrors,
       "ecsRLCCRCErrors": ecsRLCCRCErrors,
       "ecsRLCJabberErrors": ecsRLCJabberErrors,
       "ecsRLCStationLocate": ecsRLCStationLocate,
       "ecsRLCSizeOfStationLocateDB": ecsRLCSizeOfStationLocateDB,
       "ecsRLCNumbOfSLEntries": ecsRLCNumbOfSLEntries,
       "ecsRLCSLDataBaseStatus": ecsRLCSLDataBaseStatus,
       "ecsRLCSLowFilterAddress": ecsRLCSLowFilterAddress,
       "ecsRLCSLhighFilterAddress": ecsRLCSLhighFilterAddress,
       "ecsRLCStationLocateTable": ecsRLCStationLocateTable,
       "ecsRLCStationLocateEntry": ecsRLCStationLocateEntry,
       "ecsRLCSLAddress": ecsRLCSLAddress,
       "ecsRLCSLSlotIndex": ecsRLCSLSlotIndex,
       "ecsRLCSLPortIndex": ecsRLCSLPortIndex,
       "ecsRLCSLStatus": ecsRLCSLStatus,
       "ecsRLCNewStationLocateTable": ecsRLCNewStationLocateTable,
       "ecsRLCNewStationLocateEntry": ecsRLCNewStationLocateEntry,
       "ecsRLCNewSLAddress": ecsRLCNewSLAddress,
       "ecsRLCNewSLSlotIndex": ecsRLCNewSLSlotIndex,
       "ecsRLCNewSLPortIndex": ecsRLCNewSLPortIndex,
       "ecsHubStatistics": ecsHubStatistics,
       "ecsHubTotalGoodRcvdFrames": ecsHubTotalGoodRcvdFrames,
       "ecsHubTotalByteCount": ecsHubTotalByteCount,
       "ecsHubTotalErrorCount": ecsHubTotalErrorCount,
       "ecsHubTotalBroadcasts": ecsHubTotalBroadcasts,
       "ecsHubTotalMultiFrames": ecsHubTotalMultiFrames,
       "ecsHubTotalCollisionsCount": ecsHubTotalCollisionsCount,
       "ecsHubTotalPartitions": ecsHubTotalPartitions,
       "ecsHubTotalCarrierSenseErrors": ecsHubTotalCarrierSenseErrors,
       "ecsHubTotalAlignErrors": ecsHubTotalAlignErrors,
       "ecsHubTotalCRCErrors": ecsHubTotalCRCErrors,
       "ecsHubTotalJabberErrors": ecsHubTotalJabberErrors,
       "ecsVideo": ecsVideo,
       "lbecsXENDOFMIB": lbecsXENDOFMIB,
       "xecsDummyTable": xecsDummyTable,
       "ecsDummyEntry": ecsDummyEntry,
       "ecsDummyIndex": ecsDummyIndex,
       "ecsDummyValue": ecsDummyValue,
       "generic": generic,
       "genExperimental": genExperimental,
       "testData": testData,
       "ifExtensions": ifExtensions,
       "setup": setup,
       "sysLoader": sysLoader,
       "security": security,
       "gauges": gauges,
       "asciiAgent": asciiAgent,
       "serialIf": serialIf,
       "repeaterMgmt": repeaterMgmt,
       "endStation": endStation,
       "localSnmp": localSnmp,
       "manager": manager,
       "unusedGeneric12": unusedGeneric12,
       "chassis": chassis,
       "mrmResilience": mrmResilience,
       "tokenRing": tokenRing,
       "multiRepeater": multiRepeater,
       "bridgeMgmt": bridgeMgmt,
       "fault": fault,
       "poll": poll,
       "powerSupply": powerSupply,
       "netBuilder-mib": netBuilder_mib,
       "lBridgeECS-mib": lBridgeECS_mib,
       "deskMan-mib": deskMan_mib,
       "linkBuilderMSH-mib": linkBuilderMSH_mib}
)
