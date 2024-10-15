# SNMP MIB module (ZYXEL-MES2110-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MES2110-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:19 2024
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

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_EsSeries_ObjectIdentity = ObjectIdentity
esSeries = _EsSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8)
)
_Mes2110_MIB_ObjectIdentity = ObjectIdentity
mes2110_MIB = _Mes2110_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110)
)
_Mes2110_SystemInfo_ObjectIdentity = ObjectIdentity
mes2110_SystemInfo = _Mes2110_SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 1)
)


class _Mes2110_SystemContact_Type(DisplayString):
    """Custom type mes2110_SystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Mes2110_SystemContact_Type.__name__ = "DisplayString"
_Mes2110_SystemContact_Object = MibScalar
mes2110_SystemContact = _Mes2110_SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 1, 1),
    _Mes2110_SystemContact_Type()
)
mes2110_SystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mes2110_SystemContact.setStatus("mandatory")


class _Mes2110_SystemName_Type(DisplayString):
    """Custom type mes2110_SystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Mes2110_SystemName_Type.__name__ = "DisplayString"
_Mes2110_SystemName_Object = MibScalar
mes2110_SystemName = _Mes2110_SystemName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 1, 2),
    _Mes2110_SystemName_Type()
)
mes2110_SystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mes2110_SystemName.setStatus("mandatory")


class _Mes2110_SystemLocation_Type(DisplayString):
    """Custom type mes2110_SystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Mes2110_SystemLocation_Type.__name__ = "DisplayString"
_Mes2110_SystemLocation_Object = MibScalar
mes2110_SystemLocation = _Mes2110_SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 1, 3),
    _Mes2110_SystemLocation_Type()
)
mes2110_SystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mes2110_SystemLocation.setStatus("mandatory")
_Mes2110_Mgt_ObjectIdentity = ObjectIdentity
mes2110_Mgt = _Mes2110_Mgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2)
)


class _Mes2110_MgtSnmpVer_Type(Integer32):
    """Custom type mes2110_MgtSnmpVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_Mes2110_MgtSnmpVer_Type.__name__ = "Integer32"
_Mes2110_MgtSnmpVer_Object = MibScalar
mes2110_MgtSnmpVer = _Mes2110_MgtSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 1),
    _Mes2110_MgtSnmpVer_Type()
)
mes2110_MgtSnmpVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mes2110_MgtSnmpVer.setStatus("mandatory")


class _Mes2110_MgtModPN_Type(DisplayString):
    """Custom type mes2110_MgtModPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Mes2110_MgtModPN_Type.__name__ = "DisplayString"
_Mes2110_MgtModPN_Object = MibScalar
mes2110_MgtModPN = _Mes2110_MgtModPN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 2),
    _Mes2110_MgtModPN_Type()
)
mes2110_MgtModPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mes2110_MgtModPN.setStatus("mandatory")


class _Mes2110_MgtModSN_Type(DisplayString):
    """Custom type mes2110_MgtModSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Mes2110_MgtModSN_Type.__name__ = "DisplayString"
_Mes2110_MgtModSN_Object = MibScalar
mes2110_MgtModSN = _Mes2110_MgtModSN_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 3),
    _Mes2110_MgtModSN_Type()
)
mes2110_MgtModSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mes2110_MgtModSN.setStatus("mandatory")


class _Mes2110_MgtModManuDate_Type(DisplayString):
    """Custom type mes2110_MgtModManuDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Mes2110_MgtModManuDate_Type.__name__ = "DisplayString"
_Mes2110_MgtModManuDate_Object = MibScalar
mes2110_MgtModManuDate = _Mes2110_MgtModManuDate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 4),
    _Mes2110_MgtModManuDate_Type()
)
mes2110_MgtModManuDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mes2110_MgtModManuDate.setStatus("mandatory")


class _Mes2110_MgtModRev_Type(DisplayString):
    """Custom type mes2110_MgtModRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Mes2110_MgtModRev_Type.__name__ = "DisplayString"
_Mes2110_MgtModRev_Object = MibScalar
mes2110_MgtModRev = _Mes2110_MgtModRev_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 5),
    _Mes2110_MgtModRev_Type()
)
mes2110_MgtModRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mes2110_MgtModRev.setStatus("mandatory")


class _Mes2110_MgtModDesc_Type(DisplayString):
    """Custom type mes2110_MgtModDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Mes2110_MgtModDesc_Type.__name__ = "DisplayString"
_Mes2110_MgtModDesc_Object = MibScalar
mes2110_MgtModDesc = _Mes2110_MgtModDesc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 6),
    _Mes2110_MgtModDesc_Type()
)
mes2110_MgtModDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mes2110_MgtModDesc.setStatus("mandatory")


class _CommunityStringRO_Type(DisplayString):
    """Custom type communityStringRO based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CommunityStringRO_Type.__name__ = "DisplayString"
_CommunityStringRO_Object = MibScalar
communityStringRO = _CommunityStringRO_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 7),
    _CommunityStringRO_Type()
)
communityStringRO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityStringRO.setStatus("mandatory")


class _CommunityStringRW_Type(DisplayString):
    """Custom type communityStringRW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CommunityStringRW_Type.__name__ = "DisplayString"
_CommunityStringRW_Object = MibScalar
communityStringRW = _CommunityStringRW_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 8),
    _CommunityStringRW_Type()
)
communityStringRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityStringRW.setStatus("mandatory")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 9),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("mandatory")
_InterfaceIpAddress_Type = IpAddress
_InterfaceIpAddress_Object = MibScalar
interfaceIpAddress = _InterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 10),
    _InterfaceIpAddress_Type()
)
interfaceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceIpAddress.setStatus("mandatory")
_InterfaceSubnetMask_Type = IpAddress
_InterfaceSubnetMask_Object = MibScalar
interfaceSubnetMask = _InterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 11),
    _InterfaceSubnetMask_Type()
)
interfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceSubnetMask.setStatus("mandatory")


class _MgtStp_Type(Integer32):
    """Custom type mgtStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MgtStp_Type.__name__ = "Integer32"
_MgtStp_Object = MibScalar
mgtStp = _MgtStp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 12),
    _MgtStp_Type()
)
mgtStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgtStp.setStatus("mandatory")
_TrapManagerTable_Object = MibTable
trapManagerTable = _TrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 13)
)
if mibBuilder.loadTexts:
    trapManagerTable.setStatus("mandatory")
_TrapManagerTableEntry_Object = MibTableRow
trapManagerTableEntry = _TrapManagerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 13, 1)
)
trapManagerTableEntry.setIndexNames(
    (0, "ZYXEL-MES2110-MIB", "trapManagerIndex"),
)
if mibBuilder.loadTexts:
    trapManagerTableEntry.setStatus("mandatory")
_TrapManagerIndex_Type = Integer32
_TrapManagerIndex_Object = MibTableColumn
trapManagerIndex = _TrapManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 13, 1, 1),
    _TrapManagerIndex_Type()
)
trapManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapManagerIndex.setStatus("mandatory")
_TrapManagerIpAddress_Type = IpAddress
_TrapManagerIpAddress_Object = MibTableColumn
trapManagerIpAddress = _TrapManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 13, 1, 2),
    _TrapManagerIpAddress_Type()
)
trapManagerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerIpAddress.setStatus("mandatory")


class _TrapManagerName_Type(DisplayString):
    """Custom type trapManagerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrapManagerName_Type.__name__ = "DisplayString"
_TrapManagerName_Object = MibTableColumn
trapManagerName = _TrapManagerName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 13, 1, 3),
    _TrapManagerName_Type()
)
trapManagerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerName.setStatus("mandatory")


class _TrapManagerStatus_Type(Integer32):
    """Custom type trapManagerStatus based on Integer32"""
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


_TrapManagerStatus_Type.__name__ = "Integer32"
_TrapManagerStatus_Object = MibTableColumn
trapManagerStatus = _TrapManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 2, 13, 1, 4),
    _TrapManagerStatus_Type()
)
trapManagerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerStatus.setStatus("mandatory")
_Mes2110_Port_ObjectIdentity = ObjectIdentity
mes2110_Port = _Mes2110_Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3)
)
_Mes2110_PortTable_Object = MibTable
mes2110_PortTable = _Mes2110_PortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1)
)
if mibBuilder.loadTexts:
    mes2110_PortTable.setStatus("mandatory")
_Mes2110_PortEntry_Object = MibTableRow
mes2110_PortEntry = _Mes2110_PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1)
)
mes2110_PortEntry.setIndexNames(
    (0, "ZYXEL-MES2110-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    mes2110_PortEntry.setStatus("mandatory")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("mandatory")


class _PortAdminStatus_Type(Integer32):
    """Custom type portAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 4))
    )


_PortAdminStatus_Type.__name__ = "Integer32"
_PortAdminStatus_Object = MibTableColumn
portAdminStatus = _PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 3),
    _PortAdminStatus_Type()
)
portAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminStatus.setStatus("mandatory")


class _PortLinkStatus_Type(Integer32):
    """Custom type portLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PortLinkStatus_Type.__name__ = "Integer32"
_PortLinkStatus_Object = MibTableColumn
portLinkStatus = _PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 4),
    _PortLinkStatus_Type()
)
portLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkStatus.setStatus("mandatory")


class _PortSpeedMode_Type(Integer32):
    """Custom type portSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-1000M", 3),
          ("speed-100M", 2),
          ("speed-10M", 1))
    )


_PortSpeedMode_Type.__name__ = "Integer32"
_PortSpeedMode_Object = MibTableColumn
portSpeedMode = _PortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 5),
    _PortSpeedMode_Type()
)
portSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedMode.setStatus("mandatory")


class _PortDuplexMode_Type(Integer32):
    """Custom type portDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_PortDuplexMode_Type.__name__ = "Integer32"
_PortDuplexMode_Object = MibTableColumn
portDuplexMode = _PortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 6),
    _PortDuplexMode_Type()
)
portDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDuplexMode.setStatus("mandatory")


class _PortAuto_Type(Integer32):
    """Custom type portAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortAuto_Type.__name__ = "Integer32"
_PortAuto_Object = MibTableColumn
portAuto = _PortAuto_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 7),
    _PortAuto_Type()
)
portAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuto.setStatus("mandatory")


class _PortFfc_Type(Integer32):
    """Custom type portFfc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortFfc_Type.__name__ = "Integer32"
_PortFfc_Object = MibTableColumn
portFfc = _PortFfc_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 3, 1, 1, 8),
    _PortFfc_Type()
)
portFfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFfc.setStatus("mandatory")
_Mes2110_Traps_ObjectIdentity = ObjectIdentity
mes2110_Traps = _Mes2110_Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 4)
)

# Managed Objects groups


# Notification objects

almColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 4, 0, 1)
)
if mibBuilder.loadTexts:
    almColdStart.setStatus(
        ""
    )

almWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 4, 0, 2)
)
if mibBuilder.loadTexts:
    almWarmStart.setStatus(
        ""
    )

almLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 4, 0, 3)
)
if mibBuilder.loadTexts:
    almLinkUp.setStatus(
        ""
    )

almLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 4, 0, 4)
)
if mibBuilder.loadTexts:
    almLinkDown.setStatus(
        ""
    )

almConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 2110, 4, 0, 5)
)
if mibBuilder.loadTexts:
    almConfChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MES2110-MIB",
    **{"zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "esSeries": esSeries,
       "mes2110_MIB": mes2110_MIB,
       "mes2110_SystemInfo": mes2110_SystemInfo,
       "mes2110_SystemContact": mes2110_SystemContact,
       "mes2110_SystemName": mes2110_SystemName,
       "mes2110_SystemLocation": mes2110_SystemLocation,
       "mes2110_Mgt": mes2110_Mgt,
       "mes2110_MgtSnmpVer": mes2110_MgtSnmpVer,
       "mes2110_MgtModPN": mes2110_MgtModPN,
       "mes2110_MgtModSN": mes2110_MgtModSN,
       "mes2110_MgtModManuDate": mes2110_MgtModManuDate,
       "mes2110_MgtModRev": mes2110_MgtModRev,
       "mes2110_MgtModDesc": mes2110_MgtModDesc,
       "communityStringRO": communityStringRO,
       "communityStringRW": communityStringRW,
       "defaultGateway": defaultGateway,
       "interfaceIpAddress": interfaceIpAddress,
       "interfaceSubnetMask": interfaceSubnetMask,
       "mgtStp": mgtStp,
       "trapManagerTable": trapManagerTable,
       "trapManagerTableEntry": trapManagerTableEntry,
       "trapManagerIndex": trapManagerIndex,
       "trapManagerIpAddress": trapManagerIpAddress,
       "trapManagerName": trapManagerName,
       "trapManagerStatus": trapManagerStatus,
       "mes2110_Port": mes2110_Port,
       "mes2110_PortTable": mes2110_PortTable,
       "mes2110_PortEntry": mes2110_PortEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portAdminStatus": portAdminStatus,
       "portLinkStatus": portLinkStatus,
       "portSpeedMode": portSpeedMode,
       "portDuplexMode": portDuplexMode,
       "portAuto": portAuto,
       "portFfc": portFfc,
       "mes2110_Traps": mes2110_Traps,
       "almColdStart": almColdStart,
       "almWarmStart": almWarmStart,
       "almLinkUp": almLinkUp,
       "almLinkDown": almLinkDown,
       "almConfChange": almConfChange}
)
