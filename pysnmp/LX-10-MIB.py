# SNMP MIB module (LX-10-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LX-10-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:36 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TimeAndDate(OctetString):
    """Custom type TimeAndDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Onstream_ObjectIdentity = ObjectIdentity
onstream = _Onstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135)
)
_Lx_10_ObjectIdentity = ObjectIdentity
lx_10 = _Lx_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 1)
)
_SysGenInfo_ObjectIdentity = ObjectIdentity
sysGenInfo = _SysGenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1)
)


class _SysGenInfoShelfName_Type(DisplayString):
    """Custom type sysGenInfoShelfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysGenInfoShelfName_Type.__name__ = "DisplayString"
_SysGenInfoShelfName_Object = MibScalar
sysGenInfoShelfName = _SysGenInfoShelfName_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 1),
    _SysGenInfoShelfName_Type()
)
sysGenInfoShelfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoShelfName.setStatus("mandatory")


class _SysGenInfoCustomerName_Type(DisplayString):
    """Custom type sysGenInfoCustomerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysGenInfoCustomerName_Type.__name__ = "DisplayString"
_SysGenInfoCustomerName_Object = MibScalar
sysGenInfoCustomerName = _SysGenInfoCustomerName_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 2),
    _SysGenInfoCustomerName_Type()
)
sysGenInfoCustomerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoCustomerName.setStatus("mandatory")


class _SysGenInfoPhoneNumber_Type(DisplayString):
    """Custom type sysGenInfoPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysGenInfoPhoneNumber_Type.__name__ = "DisplayString"
_SysGenInfoPhoneNumber_Object = MibScalar
sysGenInfoPhoneNumber = _SysGenInfoPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 3),
    _SysGenInfoPhoneNumber_Type()
)
sysGenInfoPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoPhoneNumber.setStatus("mandatory")


class _SysGenInfoMaintenanceContact_Type(DisplayString):
    """Custom type sysGenInfoMaintenanceContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysGenInfoMaintenanceContact_Type.__name__ = "DisplayString"
_SysGenInfoMaintenanceContact_Object = MibScalar
sysGenInfoMaintenanceContact = _SysGenInfoMaintenanceContact_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 4),
    _SysGenInfoMaintenanceContact_Type()
)
sysGenInfoMaintenanceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoMaintenanceContact.setStatus("mandatory")


class _SysGenInfoLocation_Type(DisplayString):
    """Custom type sysGenInfoLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysGenInfoLocation_Type.__name__ = "DisplayString"
_SysGenInfoLocation_Object = MibScalar
sysGenInfoLocation = _SysGenInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 5),
    _SysGenInfoLocation_Type()
)
sysGenInfoLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoLocation.setStatus("mandatory")


class _SysGenInfoAutoLogoutTime_Type(Integer32):
    """Custom type sysGenInfoAutoLogoutTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_SysGenInfoAutoLogoutTime_Type.__name__ = "Integer32"
_SysGenInfoAutoLogoutTime_Object = MibScalar
sysGenInfoAutoLogoutTime = _SysGenInfoAutoLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 6),
    _SysGenInfoAutoLogoutTime_Type()
)
sysGenInfoAutoLogoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoAutoLogoutTime.setStatus("mandatory")


class _SysGenInfoPassword_Type(OctetString):
    """Custom type sysGenInfoPassword based on OctetString"""
    defaultValue = OctetString("onstream")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysGenInfoPassword_Type.__name__ = "OctetString"
_SysGenInfoPassword_Object = MibScalar
sysGenInfoPassword = _SysGenInfoPassword_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 7),
    _SysGenInfoPassword_Type()
)
sysGenInfoPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoPassword.setStatus("mandatory")


class _SysGenInfoShelfId_Type(Integer32):
    """Custom type sysGenInfoShelfId based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SysGenInfoShelfId_Type.__name__ = "Integer32"
_SysGenInfoShelfId_Object = MibScalar
sysGenInfoShelfId = _SysGenInfoShelfId_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 1, 8),
    _SysGenInfoShelfId_Type()
)
sysGenInfoShelfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysGenInfoShelfId.setStatus("mandatory")
_SysTimeAndDate_Type = TimeAndDate
_SysTimeAndDate_Object = MibScalar
sysTimeAndDate = _SysTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 2),
    _SysTimeAndDate_Type()
)
sysTimeAndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeAndDate.setStatus("mandatory")
_SysIpConfig_ObjectIdentity = ObjectIdentity
sysIpConfig = _SysIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3)
)
_SysIpConfigHostInterfaceTable_Object = MibTable
sysIpConfigHostInterfaceTable = _SysIpConfigHostInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sysIpConfigHostInterfaceTable.setStatus("mandatory")
_SysIpConfigHostInterfaceEntry_Object = MibTableRow
sysIpConfigHostInterfaceEntry = _SysIpConfigHostInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 1, 1)
)
sysIpConfigHostInterfaceEntry.setIndexNames(
    (0, "LX-10-MIB", "sysIpConfigHostInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sysIpConfigHostInterfaceEntry.setStatus("mandatory")


class _SysIpConfigHostInterfaceIndex_Type(Integer32):
    """Custom type sysIpConfigHostInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("nxt1", 3),
          ("slip", 2))
    )


_SysIpConfigHostInterfaceIndex_Type.__name__ = "Integer32"
_SysIpConfigHostInterfaceIndex_Object = MibTableColumn
sysIpConfigHostInterfaceIndex = _SysIpConfigHostInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 1, 1, 1),
    _SysIpConfigHostInterfaceIndex_Type()
)
sysIpConfigHostInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpConfigHostInterfaceIndex.setStatus("mandatory")


class _SysIpConfigHostInterfaceIpAddress_Type(IpAddress):
    """Custom type sysIpConfigHostInterfaceIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SysIpConfigHostInterfaceIpAddress_Object = MibTableColumn
sysIpConfigHostInterfaceIpAddress = _SysIpConfigHostInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 1, 1, 2),
    _SysIpConfigHostInterfaceIpAddress_Type()
)
sysIpConfigHostInterfaceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpConfigHostInterfaceIpAddress.setStatus("mandatory")


class _SysIpConfigHostInterfaceSubnetMask_Type(IpAddress):
    """Custom type sysIpConfigHostInterfaceSubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_SysIpConfigHostInterfaceSubnetMask_Object = MibTableColumn
sysIpConfigHostInterfaceSubnetMask = _SysIpConfigHostInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 1, 1, 3),
    _SysIpConfigHostInterfaceSubnetMask_Type()
)
sysIpConfigHostInterfaceSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpConfigHostInterfaceSubnetMask.setStatus("mandatory")


class _SysIpConfigHostInterfaceXmtRoutingMsg_Type(Integer32):
    """Custom type sysIpConfigHostInterfaceXmtRoutingMsg based on Integer32"""
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


_SysIpConfigHostInterfaceXmtRoutingMsg_Type.__name__ = "Integer32"
_SysIpConfigHostInterfaceXmtRoutingMsg_Object = MibTableColumn
sysIpConfigHostInterfaceXmtRoutingMsg = _SysIpConfigHostInterfaceXmtRoutingMsg_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 1, 1, 4),
    _SysIpConfigHostInterfaceXmtRoutingMsg_Type()
)
sysIpConfigHostInterfaceXmtRoutingMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigHostInterfaceXmtRoutingMsg.setStatus("mandatory")
_SysIpConfigDefaultGateway_ObjectIdentity = ObjectIdentity
sysIpConfigDefaultGateway = _SysIpConfigDefaultGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 2)
)


class _SysIpConfigDefaultGatewayIpAddress_Type(IpAddress):
    """Custom type sysIpConfigDefaultGatewayIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SysIpConfigDefaultGatewayIpAddress_Object = MibScalar
sysIpConfigDefaultGatewayIpAddress = _SysIpConfigDefaultGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 2, 1),
    _SysIpConfigDefaultGatewayIpAddress_Type()
)
sysIpConfigDefaultGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigDefaultGatewayIpAddress.setStatus("mandatory")


class _SysIpConfigDefaultGatewaySubnetMask_Type(IpAddress):
    """Custom type sysIpConfigDefaultGatewaySubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_SysIpConfigDefaultGatewaySubnetMask_Object = MibScalar
sysIpConfigDefaultGatewaySubnetMask = _SysIpConfigDefaultGatewaySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 2, 2),
    _SysIpConfigDefaultGatewaySubnetMask_Type()
)
sysIpConfigDefaultGatewaySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigDefaultGatewaySubnetMask.setStatus("mandatory")
_SysIpConfigTrapClientTable_Object = MibTable
sysIpConfigTrapClientTable = _SysIpConfigTrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 3)
)
if mibBuilder.loadTexts:
    sysIpConfigTrapClientTable.setStatus("mandatory")
_SysIpConfigTrapClientEntry_Object = MibTableRow
sysIpConfigTrapClientEntry = _SysIpConfigTrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 3, 1)
)
sysIpConfigTrapClientEntry.setIndexNames(
    (0, "LX-10-MIB", "sysIpConfigTrapClientIndex"),
)
if mibBuilder.loadTexts:
    sysIpConfigTrapClientEntry.setStatus("mandatory")


class _SysIpConfigTrapClientIndex_Type(Integer32):
    """Custom type sysIpConfigTrapClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SysIpConfigTrapClientIndex_Type.__name__ = "Integer32"
_SysIpConfigTrapClientIndex_Object = MibTableColumn
sysIpConfigTrapClientIndex = _SysIpConfigTrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 3, 1, 1),
    _SysIpConfigTrapClientIndex_Type()
)
sysIpConfigTrapClientIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigTrapClientIndex.setStatus("mandatory")


class _SysIpConfigTrapClientIpAddress_Type(IpAddress):
    """Custom type sysIpConfigTrapClientIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_SysIpConfigTrapClientIpAddress_Object = MibTableColumn
sysIpConfigTrapClientIpAddress = _SysIpConfigTrapClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 3, 1, 2),
    _SysIpConfigTrapClientIpAddress_Type()
)
sysIpConfigTrapClientIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigTrapClientIpAddress.setStatus("mandatory")


class _SysIpConfigTrapClientSubnetMask_Type(IpAddress):
    """Custom type sysIpConfigTrapClientSubnetMask based on IpAddress"""
    defaultHexValue = "00000000"


_SysIpConfigTrapClientSubnetMask_Object = MibTableColumn
sysIpConfigTrapClientSubnetMask = _SysIpConfigTrapClientSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 3, 1, 3),
    _SysIpConfigTrapClientSubnetMask_Type()
)
sysIpConfigTrapClientSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigTrapClientSubnetMask.setStatus("mandatory")


class _SysIpConfigTrapClientPortNumber_Type(Integer32):
    """Custom type sysIpConfigTrapClientPortNumber based on Integer32"""
    defaultValue = 162


_SysIpConfigTrapClientPortNumber_Object = MibTableColumn
sysIpConfigTrapClientPortNumber = _SysIpConfigTrapClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 3, 1, 4),
    _SysIpConfigTrapClientPortNumber_Type()
)
sysIpConfigTrapClientPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigTrapClientPortNumber.setStatus("mandatory")


class _SysIpConfigCommunityName_Type(DisplayString):
    """Custom type sysIpConfigCommunityName based on DisplayString"""
    defaultValue = OctetString("onstream")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysIpConfigCommunityName_Type.__name__ = "DisplayString"
_SysIpConfigCommunityName_Object = MibScalar
sysIpConfigCommunityName = _SysIpConfigCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 4),
    _SysIpConfigCommunityName_Type()
)
sysIpConfigCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpConfigCommunityName.setStatus("mandatory")
_SysIpConfigMacAddress_Type = PhysAddress
_SysIpConfigMacAddress_Object = MibScalar
sysIpConfigMacAddress = _SysIpConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 3, 5),
    _SysIpConfigMacAddress_Type()
)
sysIpConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIpConfigMacAddress.setStatus("mandatory")
_SysRs232Table_Object = MibTable
sysRs232Table = _SysRs232Table_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4)
)
if mibBuilder.loadTexts:
    sysRs232Table.setStatus("mandatory")
_SysRs232Entry_Object = MibTableRow
sysRs232Entry = _SysRs232Entry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4, 1)
)
sysRs232Entry.setIndexNames(
    (0, "LX-10-MIB", "sysRs232Port"),
)
if mibBuilder.loadTexts:
    sysRs232Entry.setStatus("mandatory")


class _SysRs232Port_Type(Integer32):
    """Custom type sysRs232Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-1", 1),
          ("port-2", 2))
    )


_SysRs232Port_Type.__name__ = "Integer32"
_SysRs232Port_Object = MibTableColumn
sysRs232Port = _SysRs232Port_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4, 1, 1),
    _SysRs232Port_Type()
)
sysRs232Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRs232Port.setStatus("mandatory")


class _SysRs232BaudRate_Type(Integer32):
    """Custom type sysRs232BaudRate based on Integer32"""
    defaultValue = 5

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
        *(("br-1200", 2),
          ("br-19200", 6),
          ("br-2400", 3),
          ("br-300", 1),
          ("br-38400", 7),
          ("br-4800", 4),
          ("br-9600", 5))
    )


_SysRs232BaudRate_Type.__name__ = "Integer32"
_SysRs232BaudRate_Object = MibTableColumn
sysRs232BaudRate = _SysRs232BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4, 1, 2),
    _SysRs232BaudRate_Type()
)
sysRs232BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRs232BaudRate.setStatus("mandatory")


class _SysRs232Parity_Type(Integer32):
    """Custom type sysRs232Parity based on Integer32"""
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
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_SysRs232Parity_Type.__name__ = "Integer32"
_SysRs232Parity_Object = MibTableColumn
sysRs232Parity = _SysRs232Parity_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4, 1, 3),
    _SysRs232Parity_Type()
)
sysRs232Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRs232Parity.setStatus("mandatory")


class _SysRs232DataBits_Type(Integer32):
    """Custom type sysRs232DataBits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("db-7", 1),
          ("db-8", 2))
    )


_SysRs232DataBits_Type.__name__ = "Integer32"
_SysRs232DataBits_Object = MibTableColumn
sysRs232DataBits = _SysRs232DataBits_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4, 1, 4),
    _SysRs232DataBits_Type()
)
sysRs232DataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRs232DataBits.setStatus("mandatory")


class _SysRs232StopBits_Type(Integer32):
    """Custom type sysRs232StopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sb-1", 1),
          ("sb-2", 2))
    )


_SysRs232StopBits_Type.__name__ = "Integer32"
_SysRs232StopBits_Object = MibTableColumn
sysRs232StopBits = _SysRs232StopBits_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 4, 1, 5),
    _SysRs232StopBits_Type()
)
sysRs232StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRs232StopBits.setStatus("mandatory")


class _SysMainProcessorFirmwareRev_Type(DisplayString):
    """Custom type sysMainProcessorFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_SysMainProcessorFirmwareRev_Type.__name__ = "DisplayString"
_SysMainProcessorFirmwareRev_Object = MibScalar
sysMainProcessorFirmwareRev = _SysMainProcessorFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 5),
    _SysMainProcessorFirmwareRev_Type()
)
sysMainProcessorFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMainProcessorFirmwareRev.setStatus("mandatory")


class _SysPortCardFirmwareRev_Type(DisplayString):
    """Custom type sysPortCardFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_SysPortCardFirmwareRev_Type.__name__ = "DisplayString"
_SysPortCardFirmwareRev_Object = MibScalar
sysPortCardFirmwareRev = _SysPortCardFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 1, 6),
    _SysPortCardFirmwareRev_Type()
)
sysPortCardFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPortCardFirmwareRev.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 2)
)
_ConfigDs1Table_Object = MibTable
configDs1Table = _ConfigDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1)
)
if mibBuilder.loadTexts:
    configDs1Table.setStatus("mandatory")
_ConfigDs1Entry_Object = MibTableRow
configDs1Entry = _ConfigDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1)
)
configDs1Entry.setIndexNames(
    (0, "LX-10-MIB", "configDs1Port"),
)
if mibBuilder.loadTexts:
    configDs1Entry.setStatus("mandatory")


class _ConfigDs1Port_Type(Integer32):
    """Custom type configDs1Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ConfigDs1Port_Type.__name__ = "Integer32"
_ConfigDs1Port_Object = MibTableColumn
configDs1Port = _ConfigDs1Port_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 1),
    _ConfigDs1Port_Type()
)
configDs1Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDs1Port.setStatus("mandatory")


class _ConfigDs1AdminStatus_Type(Integer32):
    """Custom type configDs1AdminStatus based on Integer32"""
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


_ConfigDs1AdminStatus_Type.__name__ = "Integer32"
_ConfigDs1AdminStatus_Object = MibTableColumn
configDs1AdminStatus = _ConfigDs1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 2),
    _ConfigDs1AdminStatus_Type()
)
configDs1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDs1AdminStatus.setStatus("mandatory")


class _ConfigDs1OperStatus_Type(Integer32):
    """Custom type configDs1OperStatus based on Integer32"""
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


_ConfigDs1OperStatus_Type.__name__ = "Integer32"
_ConfigDs1OperStatus_Object = MibTableColumn
configDs1OperStatus = _ConfigDs1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 3),
    _ConfigDs1OperStatus_Type()
)
configDs1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDs1OperStatus.setStatus("mandatory")


class _ConfigDs1LBO_Type(Integer32):
    """Custom type configDs1LBO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dB-0", 1),
          ("dB-15", 3),
          ("dB-7-5", 2))
    )


_ConfigDs1LBO_Type.__name__ = "Integer32"
_ConfigDs1LBO_Object = MibTableColumn
configDs1LBO = _ConfigDs1LBO_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 4),
    _ConfigDs1LBO_Type()
)
configDs1LBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDs1LBO.setStatus("mandatory")


class _ConfigDs1Encoding_Type(Integer32):
    """Custom type configDs1Encoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_ConfigDs1Encoding_Type.__name__ = "Integer32"
_ConfigDs1Encoding_Object = MibTableColumn
configDs1Encoding = _ConfigDs1Encoding_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 5),
    _ConfigDs1Encoding_Type()
)
configDs1Encoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDs1Encoding.setStatus("mandatory")


class _ConfigDs1Framing_Type(Integer32):
    """Custom type configDs1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("esf", 1))
    )


_ConfigDs1Framing_Type.__name__ = "Integer32"
_ConfigDs1Framing_Object = MibTableColumn
configDs1Framing = _ConfigDs1Framing_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 6),
    _ConfigDs1Framing_Type()
)
configDs1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDs1Framing.setStatus("mandatory")


class _ConfigDs1XmtAis_Type(Integer32):
    """Custom type configDs1XmtAis based on Integer32"""
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


_ConfigDs1XmtAis_Type.__name__ = "Integer32"
_ConfigDs1XmtAis_Object = MibTableColumn
configDs1XmtAis = _ConfigDs1XmtAis_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 1, 1, 7),
    _ConfigDs1XmtAis_Type()
)
configDs1XmtAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDs1XmtAis.setStatus("mandatory")


class _ConfigDs1Timing_Type(Integer32):
    """Custom type configDs1Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("looped", 1))
    )


_ConfigDs1Timing_Type.__name__ = "Integer32"
_ConfigDs1Timing_Object = MibScalar
configDs1Timing = _ConfigDs1Timing_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 2),
    _ConfigDs1Timing_Type()
)
configDs1Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDs1Timing.setStatus("mandatory")
_ConfigAfa_ObjectIdentity = ObjectIdentity
configAfa = _ConfigAfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3)
)


class _ConfigAfaActivationRate_Type(Integer32):
    """Custom type configAfaActivationRate based on Integer32"""
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
        *(("a-10-4", 1),
          ("a-10-5", 2),
          ("a-10-6", 3),
          ("a-10-7", 4),
          ("a-10-8", 5))
    )


_ConfigAfaActivationRate_Type.__name__ = "Integer32"
_ConfigAfaActivationRate_Object = MibScalar
configAfaActivationRate = _ConfigAfaActivationRate_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3, 1),
    _ConfigAfaActivationRate_Type()
)
configAfaActivationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAfaActivationRate.setStatus("mandatory")


class _ConfigAfaActivationTime_Type(Integer32):
    """Custom type configAfaActivationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_ConfigAfaActivationTime_Type.__name__ = "Integer32"
_ConfigAfaActivationTime_Object = MibScalar
configAfaActivationTime = _ConfigAfaActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3, 2),
    _ConfigAfaActivationTime_Type()
)
configAfaActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAfaActivationTime.setStatus("mandatory")


class _ConfigAfaDeactivationRate_Type(Integer32):
    """Custom type configAfaDeactivationRate based on Integer32"""
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
        *(("d-10-6", 1),
          ("d-10-7", 2),
          ("d-10-8", 3),
          ("d-10-9", 4))
    )


_ConfigAfaDeactivationRate_Type.__name__ = "Integer32"
_ConfigAfaDeactivationRate_Object = MibScalar
configAfaDeactivationRate = _ConfigAfaDeactivationRate_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3, 3),
    _ConfigAfaDeactivationRate_Type()
)
configAfaDeactivationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAfaDeactivationRate.setStatus("mandatory")


class _ConfigAfaDeactivationTime_Type(Integer32):
    """Custom type configAfaDeactivationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 30),
    )


_ConfigAfaDeactivationTime_Type.__name__ = "Integer32"
_ConfigAfaDeactivationTime_Object = MibScalar
configAfaDeactivationTime = _ConfigAfaDeactivationTime_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3, 4),
    _ConfigAfaDeactivationTime_Type()
)
configAfaDeactivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAfaDeactivationTime.setStatus("mandatory")


class _ConfigAfaStatus_Type(Integer32):
    """Custom type configAfaStatus based on Integer32"""
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


_ConfigAfaStatus_Type.__name__ = "Integer32"
_ConfigAfaStatus_Object = MibScalar
configAfaStatus = _ConfigAfaStatus_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3, 5),
    _ConfigAfaStatus_Type()
)
configAfaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAfaStatus.setStatus("mandatory")


class _ConfigAfaFarEndLpbkDetect_Type(Integer32):
    """Custom type configAfaFarEndLpbkDetect based on Integer32"""
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


_ConfigAfaFarEndLpbkDetect_Type.__name__ = "Integer32"
_ConfigAfaFarEndLpbkDetect_Object = MibScalar
configAfaFarEndLpbkDetect = _ConfigAfaFarEndLpbkDetect_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 3, 6),
    _ConfigAfaFarEndLpbkDetect_Type()
)
configAfaFarEndLpbkDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configAfaFarEndLpbkDetect.setStatus("mandatory")


class _ConfigPortCardType_Type(Integer32):
    """Custom type configPortCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("hsdp", 1),
          ("token-ring", 3))
    )


_ConfigPortCardType_Type.__name__ = "Integer32"
_ConfigPortCardType_Object = MibScalar
configPortCardType = _ConfigPortCardType_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 4),
    _ConfigPortCardType_Type()
)
configPortCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortCardType.setStatus("mandatory")
_ConfigHsdp_ObjectIdentity = ObjectIdentity
configHsdp = _ConfigHsdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5)
)


class _ConfigHsdpMode_Type(Integer32):
    """Custom type configHsdpMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hssi", 3),
          ("rs-422", 2),
          ("v-35", 1))
    )


_ConfigHsdpMode_Type.__name__ = "Integer32"
_ConfigHsdpMode_Object = MibScalar
configHsdpMode = _ConfigHsdpMode_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 1),
    _ConfigHsdpMode_Type()
)
configHsdpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHsdpMode.setStatus("mandatory")


class _ConfigHsdpCtsControl_Type(Integer32):
    """Custom type configHsdpCtsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frequency-change", 3),
          ("no-bandwidth", 2),
          ("set", 1))
    )


_ConfigHsdpCtsControl_Type.__name__ = "Integer32"
_ConfigHsdpCtsControl_Object = MibScalar
configHsdpCtsControl = _ConfigHsdpCtsControl_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 2),
    _ConfigHsdpCtsControl_Type()
)
configHsdpCtsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHsdpCtsControl.setStatus("mandatory")


class _ConfigHsdpCtsStatus_Type(Integer32):
    """Custom type configHsdpCtsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_ConfigHsdpCtsStatus_Type.__name__ = "Integer32"
_ConfigHsdpCtsStatus_Object = MibScalar
configHsdpCtsStatus = _ConfigHsdpCtsStatus_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 3),
    _ConfigHsdpCtsStatus_Type()
)
configHsdpCtsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configHsdpCtsStatus.setStatus("mandatory")


class _ConfigHsdpTermTimingSource_Type(Integer32):
    """Custom type configHsdpTermTimingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_ConfigHsdpTermTimingSource_Type.__name__ = "Integer32"
_ConfigHsdpTermTimingSource_Object = MibScalar
configHsdpTermTimingSource = _ConfigHsdpTermTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 4),
    _ConfigHsdpTermTimingSource_Type()
)
configHsdpTermTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHsdpTermTimingSource.setStatus("mandatory")


class _ConfigHsdpTermTiming_Type(Integer32):
    """Custom type configHsdpTermTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_ConfigHsdpTermTiming_Type.__name__ = "Integer32"
_ConfigHsdpTermTiming_Object = MibScalar
configHsdpTermTiming = _ConfigHsdpTermTiming_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 5),
    _ConfigHsdpTermTiming_Type()
)
configHsdpTermTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHsdpTermTiming.setStatus("mandatory")


class _ConfigHsdpRecvTiming_Type(Integer32):
    """Custom type configHsdpRecvTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_ConfigHsdpRecvTiming_Type.__name__ = "Integer32"
_ConfigHsdpRecvTiming_Object = MibScalar
configHsdpRecvTiming = _ConfigHsdpRecvTiming_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 6),
    _ConfigHsdpRecvTiming_Type()
)
configHsdpRecvTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHsdpRecvTiming.setStatus("mandatory")


class _ConfigHsdpHoldoffSeconds_Type(Integer32):
    """Custom type configHsdpHoldoffSeconds based on Integer32"""
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
        *(("sec1", 1),
          ("sec2", 2),
          ("sec3", 3),
          ("sec4", 4),
          ("sec5", 5))
    )


_ConfigHsdpHoldoffSeconds_Type.__name__ = "Integer32"
_ConfigHsdpHoldoffSeconds_Object = MibScalar
configHsdpHoldoffSeconds = _ConfigHsdpHoldoffSeconds_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 5, 7),
    _ConfigHsdpHoldoffSeconds_Type()
)
configHsdpHoldoffSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHsdpHoldoffSeconds.setStatus("mandatory")
_ConfigHdlc_ObjectIdentity = ObjectIdentity
configHdlc = _ConfigHdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 6)
)


class _ConfigHdlcMode_Type(Integer32):
    """Custom type configHdlcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_ConfigHdlcMode_Type.__name__ = "Integer32"
_ConfigHdlcMode_Object = MibScalar
configHdlcMode = _ConfigHdlcMode_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 6, 1),
    _ConfigHdlcMode_Type()
)
configHdlcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHdlcMode.setStatus("mandatory")


class _ConfigHdlcLocalPort_Type(Integer32):
    """Custom type configHdlcLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ConfigHdlcLocalPort_Type.__name__ = "Integer32"
_ConfigHdlcLocalPort_Object = MibScalar
configHdlcLocalPort = _ConfigHdlcLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 6, 2),
    _ConfigHdlcLocalPort_Type()
)
configHdlcLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configHdlcLocalPort.setStatus("mandatory")


class _ConfigHdlcFarEndPort_Type(Integer32):
    """Custom type configHdlcFarEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ConfigHdlcFarEndPort_Type.__name__ = "Integer32"
_ConfigHdlcFarEndPort_Object = MibScalar
configHdlcFarEndPort = _ConfigHdlcFarEndPort_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 6, 3),
    _ConfigHdlcFarEndPort_Type()
)
configHdlcFarEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configHdlcFarEndPort.setStatus("mandatory")


class _ConfigInverseMux_Type(Integer32):
    """Custom type configInverseMux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 1))
    )


_ConfigInverseMux_Type.__name__ = "Integer32"
_ConfigInverseMux_Object = MibScalar
configInverseMux = _ConfigInverseMux_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 2, 7),
    _ConfigInverseMux_Type()
)
configInverseMux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configInverseMux.setStatus("mandatory")
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 3)
)
_FaultDs1_ObjectIdentity = ObjectIdentity
faultDs1 = _FaultDs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 1)
)
_FaultDs1LoopbackTable_Object = MibTable
faultDs1LoopbackTable = _FaultDs1LoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 1, 1)
)
if mibBuilder.loadTexts:
    faultDs1LoopbackTable.setStatus("mandatory")
_FaultDs1LoopbackEntry_Object = MibTableRow
faultDs1LoopbackEntry = _FaultDs1LoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 1, 1, 1)
)
faultDs1LoopbackEntry.setIndexNames(
    (0, "LX-10-MIB", "faultDs1LoopbackPort"),
)
if mibBuilder.loadTexts:
    faultDs1LoopbackEntry.setStatus("mandatory")


class _FaultDs1LoopbackPort_Type(Integer32):
    """Custom type faultDs1LoopbackPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FaultDs1LoopbackPort_Type.__name__ = "Integer32"
_FaultDs1LoopbackPort_Object = MibTableColumn
faultDs1LoopbackPort = _FaultDs1LoopbackPort_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 1, 1, 1, 1),
    _FaultDs1LoopbackPort_Type()
)
faultDs1LoopbackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDs1LoopbackPort.setStatus("mandatory")


class _FaultDs1LoopbackNetworkLoopback_Type(Integer32):
    """Custom type faultDs1LoopbackNetworkLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("card", 2),
          ("line", 3),
          ("none", 1))
    )


_FaultDs1LoopbackNetworkLoopback_Type.__name__ = "Integer32"
_FaultDs1LoopbackNetworkLoopback_Object = MibTableColumn
faultDs1LoopbackNetworkLoopback = _FaultDs1LoopbackNetworkLoopback_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 1, 1, 1, 2),
    _FaultDs1LoopbackNetworkLoopback_Type()
)
faultDs1LoopbackNetworkLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultDs1LoopbackNetworkLoopback.setStatus("mandatory")


class _FaultDs1RemoteLineLoopback_Type(Integer32):
    """Custom type faultDs1RemoteLineLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_FaultDs1RemoteLineLoopback_Type.__name__ = "Integer32"
_FaultDs1RemoteLineLoopback_Object = MibScalar
faultDs1RemoteLineLoopback = _FaultDs1RemoteLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 1, 2),
    _FaultDs1RemoteLineLoopback_Type()
)
faultDs1RemoteLineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDs1RemoteLineLoopback.setStatus("mandatory")
_FaultDte_ObjectIdentity = ObjectIdentity
faultDte = _FaultDte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2)
)


class _FaultDteLaLead_Type(Integer32):
    """Custom type faultDteLaLead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_FaultDteLaLead_Type.__name__ = "Integer32"
_FaultDteLaLead_Object = MibScalar
faultDteLaLead = _FaultDteLaLead_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2, 1),
    _FaultDteLaLead_Type()
)
faultDteLaLead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDteLaLead.setStatus("mandatory")


class _FaultDteLbLead_Type(Integer32):
    """Custom type faultDteLbLead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_FaultDteLbLead_Type.__name__ = "Integer32"
_FaultDteLbLead_Object = MibScalar
faultDteLbLead = _FaultDteLbLead_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2, 2),
    _FaultDteLbLead_Type()
)
faultDteLbLead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDteLbLead.setStatus("mandatory")


class _FaultDteLaLbTranslation_Type(Integer32):
    """Custom type faultDteLaLbTranslation based on Integer32"""
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
        *(("dte", 4),
          ("local-line", 2),
          ("none", 1),
          ("remote-line", 3))
    )


_FaultDteLaLbTranslation_Type.__name__ = "Integer32"
_FaultDteLaLbTranslation_Object = MibScalar
faultDteLaLbTranslation = _FaultDteLaLbTranslation_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2, 3),
    _FaultDteLaLbTranslation_Type()
)
faultDteLaLbTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultDteLaLbTranslation.setStatus("mandatory")


class _FaultDteLaLbLoopbackEnable_Type(Integer32):
    """Custom type faultDteLaLbLoopbackEnable based on Integer32"""
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


_FaultDteLaLbLoopbackEnable_Type.__name__ = "Integer32"
_FaultDteLaLbLoopbackEnable_Object = MibScalar
faultDteLaLbLoopbackEnable = _FaultDteLaLbLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2, 4),
    _FaultDteLaLbLoopbackEnable_Type()
)
faultDteLaLbLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultDteLaLbLoopbackEnable.setStatus("mandatory")


class _FaultDteCustomerLoopback_Type(Integer32):
    """Custom type faultDteCustomerLoopback based on Integer32"""
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


_FaultDteCustomerLoopback_Type.__name__ = "Integer32"
_FaultDteCustomerLoopback_Object = MibScalar
faultDteCustomerLoopback = _FaultDteCustomerLoopback_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2, 5),
    _FaultDteCustomerLoopback_Type()
)
faultDteCustomerLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultDteCustomerLoopback.setStatus("mandatory")


class _FaultDteDteLoopback_Type(Integer32):
    """Custom type faultDteDteLoopback based on Integer32"""
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


_FaultDteDteLoopback_Type.__name__ = "Integer32"
_FaultDteDteLoopback_Object = MibScalar
faultDteDteLoopback = _FaultDteDteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 2, 6),
    _FaultDteDteLoopback_Type()
)
faultDteDteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultDteDteLoopback.setStatus("mandatory")
_FaultClearCurrentAlarms_Type = Integer32
_FaultClearCurrentAlarms_Object = MibScalar
faultClearCurrentAlarms = _FaultClearCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 3),
    _FaultClearCurrentAlarms_Type()
)
faultClearCurrentAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultClearCurrentAlarms.setStatus("mandatory")
_FaultClearHistoryAlarms_Type = Integer32
_FaultClearHistoryAlarms_Object = MibScalar
faultClearHistoryAlarms = _FaultClearHistoryAlarms_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 4),
    _FaultClearHistoryAlarms_Type()
)
faultClearHistoryAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultClearHistoryAlarms.setStatus("mandatory")
_FaultCurrentAlarmTable_Object = MibTable
faultCurrentAlarmTable = _FaultCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5)
)
if mibBuilder.loadTexts:
    faultCurrentAlarmTable.setStatus("mandatory")
_FaultCurrentAlarmEntry_Object = MibTableRow
faultCurrentAlarmEntry = _FaultCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1)
)
faultCurrentAlarmEntry.setIndexNames(
    (0, "LX-10-MIB", "faultCurrentAlarmTag"),
)
if mibBuilder.loadTexts:
    faultCurrentAlarmEntry.setStatus("mandatory")


class _FaultCurrentAlarmTag_Type(Integer32):
    """Custom type faultCurrentAlarmTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_FaultCurrentAlarmTag_Type.__name__ = "Integer32"
_FaultCurrentAlarmTag_Object = MibTableColumn
faultCurrentAlarmTag = _FaultCurrentAlarmTag_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 1),
    _FaultCurrentAlarmTag_Type()
)
faultCurrentAlarmTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmTag.setStatus("mandatory")


class _FaultCurrentAlarmAlarmType_Type(Integer32):
    """Custom type faultCurrentAlarmAlarmType based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("alarm-history-cleared", 25),
          ("alarm1-in", 68),
          ("alarm2-in", 69),
          ("alarm3-in", 70),
          ("all-alarms-cleared", 23),
          ("att-fdl-loopback", 74),
          ("card-fail", 12),
          ("cim-card-config-mismatch", 20),
          ("cpu-restarted", 21),
          ("customer-lpbk", 8),
          ("ds1-afa-alarm", 24),
          ("ds1-ais", 15),
          ("ds1-los", 13),
          ("ds1-net-card-lpbk", 1),
          ("ds1-net-line-lpbk", 2),
          ("ds1-oof", 14),
          ("ds1-yel", 16),
          ("dte-clk-loss", 9),
          ("dte-lpbk", 7),
          ("fan1-failed", 17),
          ("fan2-failed", 18),
          ("far-end-loopback", 72),
          ("hdlc-unlocked", 71),
          ("hsdc-ga-oof", 10),
          ("inband-loopback", 75),
          ("la-lb-dte-lpbk", 3),
          ("la-lb-local-lpbk", 4),
          ("la-lb-remote-lpbk", 5),
          ("p1-connected-to-p2", 26),
          ("p1-connected-to-p3", 27),
          ("p1-connected-to-p4", 28),
          ("p1-connected-to-p5", 29),
          ("p1-connected-to-p6", 30),
          ("p1-connected-to-p7", 31),
          ("p2-connected-to-p1", 32),
          ("p2-connected-to-p3", 33),
          ("p2-connected-to-p4", 34),
          ("p2-connected-to-p5", 35),
          ("p2-connected-to-p6", 36),
          ("p2-connected-to-p7", 37),
          ("p3-connected-to-p1", 38),
          ("p3-connected-to-p2", 39),
          ("p3-connected-to-p4", 40),
          ("p3-connected-to-p5", 41),
          ("p3-connected-to-p6", 42),
          ("p3-connected-to-p7", 43),
          ("p4-connected-to-p1", 44),
          ("p4-connected-to-p2", 45),
          ("p4-connected-to-p3", 46),
          ("p4-connected-to-p5", 47),
          ("p4-connected-to-p6", 48),
          ("p4-connected-to-p7", 49),
          ("p5-connected-to-p1", 50),
          ("p5-connected-to-p2", 51),
          ("p5-connected-to-p3", 52),
          ("p5-connected-to-p4", 53),
          ("p5-connected-to-p6", 54),
          ("p5-connected-to-p7", 55),
          ("p6-connected-to-p1", 56),
          ("p6-connected-to-p2", 57),
          ("p6-connected-to-p3", 58),
          ("p6-connected-to-p4", 59),
          ("p6-connected-to-p5", 60),
          ("p6-connected-to-p7", 61),
          ("p7-connected-to-p1", 62),
          ("p7-connected-to-p2", 63),
          ("p7-connected-to-p3", 64),
          ("p7-connected-to-p4", 65),
          ("p7-connected-to-p5", 66),
          ("p7-connected-to-p6", 67),
          ("pll-fail", 11),
          ("port-alarms-cleared", 22),
          ("ports-out-of-sequence", 77),
          ("remote-afa", 73),
          ("remote-line-lpbk", 6),
          ("t1-link-down", 76),
          ("trunk-card-config-mismatch", 19))
    )


_FaultCurrentAlarmAlarmType_Type.__name__ = "Integer32"
_FaultCurrentAlarmAlarmType_Object = MibTableColumn
faultCurrentAlarmAlarmType = _FaultCurrentAlarmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 2),
    _FaultCurrentAlarmAlarmType_Type()
)
faultCurrentAlarmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmAlarmType.setStatus("mandatory")


class _FaultCurrentAlarmSeverity_Type(Integer32):
    """Custom type faultCurrentAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 3),
          ("minor", 2))
    )


_FaultCurrentAlarmSeverity_Type.__name__ = "Integer32"
_FaultCurrentAlarmSeverity_Object = MibTableColumn
faultCurrentAlarmSeverity = _FaultCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 3),
    _FaultCurrentAlarmSeverity_Type()
)
faultCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmSeverity.setStatus("mandatory")


class _FaultCurrentAlarmCardType_Type(Integer32):
    """Custom type faultCurrentAlarmCardType based on Integer32"""
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
        *(("ds1", 4),
          ("ethernet", 2),
          ("hsdp", 1),
          ("token-ring", 3))
    )


_FaultCurrentAlarmCardType_Type.__name__ = "Integer32"
_FaultCurrentAlarmCardType_Object = MibTableColumn
faultCurrentAlarmCardType = _FaultCurrentAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 4),
    _FaultCurrentAlarmCardType_Type()
)
faultCurrentAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmCardType.setStatus("mandatory")


class _FaultCurrentAlarmPortNumber_Type(Integer32):
    """Custom type faultCurrentAlarmPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FaultCurrentAlarmPortNumber_Type.__name__ = "Integer32"
_FaultCurrentAlarmPortNumber_Object = MibTableColumn
faultCurrentAlarmPortNumber = _FaultCurrentAlarmPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 5),
    _FaultCurrentAlarmPortNumber_Type()
)
faultCurrentAlarmPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmPortNumber.setStatus("mandatory")
_FaultCurrentAlarmSetTime_Type = TimeAndDate
_FaultCurrentAlarmSetTime_Object = MibTableColumn
faultCurrentAlarmSetTime = _FaultCurrentAlarmSetTime_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 6),
    _FaultCurrentAlarmSetTime_Type()
)
faultCurrentAlarmSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmSetTime.setStatus("mandatory")
_FaultCurrentAlarmDescription_Type = DisplayString
_FaultCurrentAlarmDescription_Object = MibTableColumn
faultCurrentAlarmDescription = _FaultCurrentAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 5, 1, 8),
    _FaultCurrentAlarmDescription_Type()
)
faultCurrentAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultCurrentAlarmDescription.setStatus("mandatory")
_FaultHistoryAlarmTable_Object = MibTable
faultHistoryAlarmTable = _FaultHistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6)
)
if mibBuilder.loadTexts:
    faultHistoryAlarmTable.setStatus("mandatory")
_FaultHistoryAlarmEntry_Object = MibTableRow
faultHistoryAlarmEntry = _FaultHistoryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1)
)
faultHistoryAlarmEntry.setIndexNames(
    (0, "LX-10-MIB", "faultHistoryAlarmTag"),
)
if mibBuilder.loadTexts:
    faultHistoryAlarmEntry.setStatus("mandatory")


class _FaultHistoryAlarmTag_Type(Integer32):
    """Custom type faultHistoryAlarmTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_FaultHistoryAlarmTag_Type.__name__ = "Integer32"
_FaultHistoryAlarmTag_Object = MibTableColumn
faultHistoryAlarmTag = _FaultHistoryAlarmTag_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 1),
    _FaultHistoryAlarmTag_Type()
)
faultHistoryAlarmTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmTag.setStatus("mandatory")


class _FaultHistoryAlarmAlarmType_Type(Integer32):
    """Custom type faultHistoryAlarmAlarmType based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77)
        )
    )
    namedValues = NamedValues(
        *(("alarm-history-cleared", 25),
          ("alarm1-in", 68),
          ("alarm2-in", 69),
          ("alarm3-in", 70),
          ("all-alarms-cleared", 23),
          ("att-fdl-loopback", 74),
          ("card-fail", 12),
          ("cim-card-config-mismatch", 20),
          ("cpu-restarted", 21),
          ("customer-lpbk", 8),
          ("ds1-afa-alarm", 24),
          ("ds1-ais", 15),
          ("ds1-los", 13),
          ("ds1-net-card-lpbk", 1),
          ("ds1-net-line-lpbk", 2),
          ("ds1-oof", 14),
          ("ds1-yel", 16),
          ("dte-clk-loss", 9),
          ("dte-lpbk", 7),
          ("fan1-failed", 17),
          ("fan2-failed", 18),
          ("far-end-loopback", 72),
          ("hdlc-unlocked", 71),
          ("hsdc-ga-oof", 10),
          ("inband-loopback", 75),
          ("la-lb-dte-lpbk", 3),
          ("la-lb-local-lpbk", 4),
          ("la-lb-remote-lpbk", 5),
          ("p1-connected-to-p2", 26),
          ("p1-connected-to-p3", 27),
          ("p1-connected-to-p4", 28),
          ("p1-connected-to-p5", 29),
          ("p1-connected-to-p6", 30),
          ("p1-connected-to-p7", 31),
          ("p2-connected-to-p1", 32),
          ("p2-connected-to-p3", 33),
          ("p2-connected-to-p4", 34),
          ("p2-connected-to-p5", 35),
          ("p2-connected-to-p6", 36),
          ("p2-connected-to-p7", 37),
          ("p3-connected-to-p1", 38),
          ("p3-connected-to-p2", 39),
          ("p3-connected-to-p4", 40),
          ("p3-connected-to-p5", 41),
          ("p3-connected-to-p6", 42),
          ("p3-connected-to-p7", 43),
          ("p4-connected-to-p1", 44),
          ("p4-connected-to-p2", 45),
          ("p4-connected-to-p3", 46),
          ("p4-connected-to-p5", 47),
          ("p4-connected-to-p6", 48),
          ("p4-connected-to-p7", 49),
          ("p5-connected-to-p1", 50),
          ("p5-connected-to-p2", 51),
          ("p5-connected-to-p3", 52),
          ("p5-connected-to-p4", 53),
          ("p5-connected-to-p6", 54),
          ("p5-connected-to-p7", 55),
          ("p6-connected-to-p1", 56),
          ("p6-connected-to-p2", 57),
          ("p6-connected-to-p3", 58),
          ("p6-connected-to-p4", 59),
          ("p6-connected-to-p5", 60),
          ("p6-connected-to-p7", 61),
          ("p7-connected-to-p1", 62),
          ("p7-connected-to-p2", 63),
          ("p7-connected-to-p3", 64),
          ("p7-connected-to-p4", 65),
          ("p7-connected-to-p5", 66),
          ("p7-connected-to-p6", 67),
          ("pll-fail", 11),
          ("port-alarms-cleared", 22),
          ("ports-out-of-sequence", 77),
          ("remote-afa", 73),
          ("remote-line-lpbk", 6),
          ("t1-link-down", 76),
          ("trunk-card-config-mismatch", 19))
    )


_FaultHistoryAlarmAlarmType_Type.__name__ = "Integer32"
_FaultHistoryAlarmAlarmType_Object = MibTableColumn
faultHistoryAlarmAlarmType = _FaultHistoryAlarmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 2),
    _FaultHistoryAlarmAlarmType_Type()
)
faultHistoryAlarmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmAlarmType.setStatus("mandatory")


class _FaultHistoryAlarmSeverity_Type(Integer32):
    """Custom type faultHistoryAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("info", 1),
          ("major", 3),
          ("minor", 2))
    )


_FaultHistoryAlarmSeverity_Type.__name__ = "Integer32"
_FaultHistoryAlarmSeverity_Object = MibTableColumn
faultHistoryAlarmSeverity = _FaultHistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 3),
    _FaultHistoryAlarmSeverity_Type()
)
faultHistoryAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmSeverity.setStatus("mandatory")


class _FaultHistoryAlarmCardType_Type(Integer32):
    """Custom type faultHistoryAlarmCardType based on Integer32"""
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
        *(("ds1", 4),
          ("ethernet", 2),
          ("hsdp", 1),
          ("token-ring", 3))
    )


_FaultHistoryAlarmCardType_Type.__name__ = "Integer32"
_FaultHistoryAlarmCardType_Object = MibTableColumn
faultHistoryAlarmCardType = _FaultHistoryAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 4),
    _FaultHistoryAlarmCardType_Type()
)
faultHistoryAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmCardType.setStatus("mandatory")


class _FaultHistoryAlarmPortNumber_Type(Integer32):
    """Custom type faultHistoryAlarmPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FaultHistoryAlarmPortNumber_Type.__name__ = "Integer32"
_FaultHistoryAlarmPortNumber_Object = MibTableColumn
faultHistoryAlarmPortNumber = _FaultHistoryAlarmPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 5),
    _FaultHistoryAlarmPortNumber_Type()
)
faultHistoryAlarmPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmPortNumber.setStatus("mandatory")
_FaultHistoryAlarmSetTime_Type = TimeAndDate
_FaultHistoryAlarmSetTime_Object = MibTableColumn
faultHistoryAlarmSetTime = _FaultHistoryAlarmSetTime_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 6),
    _FaultHistoryAlarmSetTime_Type()
)
faultHistoryAlarmSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmSetTime.setStatus("mandatory")
_FaultHistoryAlarmClearTime_Type = TimeAndDate
_FaultHistoryAlarmClearTime_Object = MibTableColumn
faultHistoryAlarmClearTime = _FaultHistoryAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 7),
    _FaultHistoryAlarmClearTime_Type()
)
faultHistoryAlarmClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmClearTime.setStatus("mandatory")
_FaultHistoryAlarmDescription_Type = DisplayString
_FaultHistoryAlarmDescription_Object = MibTableColumn
faultHistoryAlarmDescription = _FaultHistoryAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 3, 6, 1, 8),
    _FaultHistoryAlarmDescription_Type()
)
faultHistoryAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultHistoryAlarmDescription.setStatus("mandatory")
_Perf_ObjectIdentity = ObjectIdentity
perf = _Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 4)
)
_PerfClearDs1Performance_Type = Integer32
_PerfClearDs1Performance_Object = MibScalar
perfClearDs1Performance = _PerfClearDs1Performance_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 1),
    _PerfClearDs1Performance_Type()
)
perfClearDs1Performance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfClearDs1Performance.setStatus("mandatory")
_PerfClearEnetPortCardStats_Type = Integer32
_PerfClearEnetPortCardStats_Object = MibScalar
perfClearEnetPortCardStats = _PerfClearEnetPortCardStats_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 2),
    _PerfClearEnetPortCardStats_Type()
)
perfClearEnetPortCardStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfClearEnetPortCardStats.setStatus("mandatory")
_EnetPortCardStats_ObjectIdentity = ObjectIdentity
enetPortCardStats = _EnetPortCardStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3)
)
_EnetPortCardStatsFramesReceived_Type = Counter32
_EnetPortCardStatsFramesReceived_Object = MibScalar
enetPortCardStatsFramesReceived = _EnetPortCardStatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 1),
    _EnetPortCardStatsFramesReceived_Type()
)
enetPortCardStatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsFramesReceived.setStatus("mandatory")
_EnetPortCardStatsBytesReceived_Type = Counter32
_EnetPortCardStatsBytesReceived_Object = MibScalar
enetPortCardStatsBytesReceived = _EnetPortCardStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 2),
    _EnetPortCardStatsBytesReceived_Type()
)
enetPortCardStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsBytesReceived.setStatus("mandatory")
_EnetPortCardStatsFramesTransmitted_Type = Counter32
_EnetPortCardStatsFramesTransmitted_Object = MibScalar
enetPortCardStatsFramesTransmitted = _EnetPortCardStatsFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 3),
    _EnetPortCardStatsFramesTransmitted_Type()
)
enetPortCardStatsFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsFramesTransmitted.setStatus("mandatory")
_EnetPortCardStatsBytesTransmitted_Type = Counter32
_EnetPortCardStatsBytesTransmitted_Object = MibScalar
enetPortCardStatsBytesTransmitted = _EnetPortCardStatsBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 4),
    _EnetPortCardStatsBytesTransmitted_Type()
)
enetPortCardStatsBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsBytesTransmitted.setStatus("mandatory")
_EnetPortCardStatsAlignmentErrors_Type = Counter32
_EnetPortCardStatsAlignmentErrors_Object = MibScalar
enetPortCardStatsAlignmentErrors = _EnetPortCardStatsAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 5),
    _EnetPortCardStatsAlignmentErrors_Type()
)
enetPortCardStatsAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsAlignmentErrors.setStatus("mandatory")
_EnetPortCardStatsFCSErrors_Type = Counter32
_EnetPortCardStatsFCSErrors_Object = MibScalar
enetPortCardStatsFCSErrors = _EnetPortCardStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 6),
    _EnetPortCardStatsFCSErrors_Type()
)
enetPortCardStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsFCSErrors.setStatus("mandatory")
_EnetPortCardStatsSingleCollisionFrames_Type = Counter32
_EnetPortCardStatsSingleCollisionFrames_Object = MibScalar
enetPortCardStatsSingleCollisionFrames = _EnetPortCardStatsSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 7),
    _EnetPortCardStatsSingleCollisionFrames_Type()
)
enetPortCardStatsSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsSingleCollisionFrames.setStatus("mandatory")
_EnetPortCardStatsMultipleCollisionFrames_Type = Counter32
_EnetPortCardStatsMultipleCollisionFrames_Object = MibScalar
enetPortCardStatsMultipleCollisionFrames = _EnetPortCardStatsMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 8),
    _EnetPortCardStatsMultipleCollisionFrames_Type()
)
enetPortCardStatsMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsMultipleCollisionFrames.setStatus("mandatory")
_EnetPortCardStatsDeferredTransmissions_Type = Counter32
_EnetPortCardStatsDeferredTransmissions_Object = MibScalar
enetPortCardStatsDeferredTransmissions = _EnetPortCardStatsDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 9),
    _EnetPortCardStatsDeferredTransmissions_Type()
)
enetPortCardStatsDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsDeferredTransmissions.setStatus("mandatory")
_EnetPortCardStatsLateCollisions_Type = Counter32
_EnetPortCardStatsLateCollisions_Object = MibScalar
enetPortCardStatsLateCollisions = _EnetPortCardStatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 10),
    _EnetPortCardStatsLateCollisions_Type()
)
enetPortCardStatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsLateCollisions.setStatus("mandatory")
_EnetPortCardStatsExcessiveCollisions_Type = Counter32
_EnetPortCardStatsExcessiveCollisions_Object = MibScalar
enetPortCardStatsExcessiveCollisions = _EnetPortCardStatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 11),
    _EnetPortCardStatsExcessiveCollisions_Type()
)
enetPortCardStatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsExcessiveCollisions.setStatus("mandatory")
_EnetPortCardStatsInternalMacTransmitErrors_Type = Counter32
_EnetPortCardStatsInternalMacTransmitErrors_Object = MibScalar
enetPortCardStatsInternalMacTransmitErrors = _EnetPortCardStatsInternalMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 12),
    _EnetPortCardStatsInternalMacTransmitErrors_Type()
)
enetPortCardStatsInternalMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsInternalMacTransmitErrors.setStatus("mandatory")
_EnetPortCardStatsCarrierSenseErrors_Type = Counter32
_EnetPortCardStatsCarrierSenseErrors_Object = MibScalar
enetPortCardStatsCarrierSenseErrors = _EnetPortCardStatsCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 13),
    _EnetPortCardStatsCarrierSenseErrors_Type()
)
enetPortCardStatsCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsCarrierSenseErrors.setStatus("mandatory")
_EnetPortCardStatsFrameTooLongs_Type = Counter32
_EnetPortCardStatsFrameTooLongs_Object = MibScalar
enetPortCardStatsFrameTooLongs = _EnetPortCardStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 3, 14),
    _EnetPortCardStatsFrameTooLongs_Type()
)
enetPortCardStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetPortCardStatsFrameTooLongs.setStatus("mandatory")
_PerfClearNxT1PortStats_Type = Integer32
_PerfClearNxT1PortStats_Object = MibScalar
perfClearNxT1PortStats = _PerfClearNxT1PortStats_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 4),
    _PerfClearNxT1PortStats_Type()
)
perfClearNxT1PortStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfClearNxT1PortStats.setStatus("mandatory")
_Nxt1PortStats_ObjectIdentity = ObjectIdentity
nxt1PortStats = _Nxt1PortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 5)
)
_Nxt1PortStatsFramesReceived_Type = Counter32
_Nxt1PortStatsFramesReceived_Object = MibScalar
nxt1PortStatsFramesReceived = _Nxt1PortStatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 5, 1),
    _Nxt1PortStatsFramesReceived_Type()
)
nxt1PortStatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nxt1PortStatsFramesReceived.setStatus("mandatory")
_Nxt1PortStatsBytesReceived_Type = Counter32
_Nxt1PortStatsBytesReceived_Object = MibScalar
nxt1PortStatsBytesReceived = _Nxt1PortStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 5, 2),
    _Nxt1PortStatsBytesReceived_Type()
)
nxt1PortStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nxt1PortStatsBytesReceived.setStatus("mandatory")
_Nxt1PortStatsFramesTransmitted_Type = Counter32
_Nxt1PortStatsFramesTransmitted_Object = MibScalar
nxt1PortStatsFramesTransmitted = _Nxt1PortStatsFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 5, 3),
    _Nxt1PortStatsFramesTransmitted_Type()
)
nxt1PortStatsFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nxt1PortStatsFramesTransmitted.setStatus("mandatory")
_Nxt1PortStatsBytesTransmitted_Type = Counter32
_Nxt1PortStatsBytesTransmitted_Object = MibScalar
nxt1PortStatsBytesTransmitted = _Nxt1PortStatsBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 5, 4),
    _Nxt1PortStatsBytesTransmitted_Type()
)
nxt1PortStatsBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nxt1PortStatsBytesTransmitted.setStatus("mandatory")
_Nxt1PortStatsCrcErrors_Type = Counter32
_Nxt1PortStatsCrcErrors_Object = MibScalar
nxt1PortStatsCrcErrors = _Nxt1PortStatsCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 135, 22, 4, 5, 5),
    _Nxt1PortStatsCrcErrors_Type()
)
nxt1PortStatsCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nxt1PortStatsCrcErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmOnReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 135, 22, 0, 1)
)
alarmOnReport.setObjects(
      *(("LX-10-MIB", "faultCurrentAlarmAlarmType"),
        ("LX-10-MIB", "faultCurrentAlarmSeverity"),
        ("LX-10-MIB", "faultCurrentAlarmCardType"),
        ("LX-10-MIB", "faultCurrentAlarmPortNumber"),
        ("LX-10-MIB", "faultCurrentAlarmSetTime"),
        ("LX-10-MIB", "faultCurrentAlarmDescription"))
)
if mibBuilder.loadTexts:
    alarmOnReport.setStatus(
        ""
    )

alarmOffReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 135, 22, 0, 2)
)
alarmOffReport.setObjects(
      *(("LX-10-MIB", "faultHistoryAlarmAlarmType"),
        ("LX-10-MIB", "faultHistoryAlarmSeverity"),
        ("LX-10-MIB", "faultHistoryAlarmCardType"),
        ("LX-10-MIB", "faultHistoryAlarmPortNumber"),
        ("LX-10-MIB", "faultHistoryAlarmSetTime"),
        ("LX-10-MIB", "faultHistoryAlarmClearTime"),
        ("LX-10-MIB", "faultHistoryAlarmDescription"))
)
if mibBuilder.loadTexts:
    alarmOffReport.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LX-10-MIB",
    **{"TimeAndDate": TimeAndDate,
       "onstream": onstream,
       "lx-10": lx_10,
       "alarmOnReport": alarmOnReport,
       "alarmOffReport": alarmOffReport,
       "sys": sys,
       "sysGenInfo": sysGenInfo,
       "sysGenInfoShelfName": sysGenInfoShelfName,
       "sysGenInfoCustomerName": sysGenInfoCustomerName,
       "sysGenInfoPhoneNumber": sysGenInfoPhoneNumber,
       "sysGenInfoMaintenanceContact": sysGenInfoMaintenanceContact,
       "sysGenInfoLocation": sysGenInfoLocation,
       "sysGenInfoAutoLogoutTime": sysGenInfoAutoLogoutTime,
       "sysGenInfoPassword": sysGenInfoPassword,
       "sysGenInfoShelfId": sysGenInfoShelfId,
       "sysTimeAndDate": sysTimeAndDate,
       "sysIpConfig": sysIpConfig,
       "sysIpConfigHostInterfaceTable": sysIpConfigHostInterfaceTable,
       "sysIpConfigHostInterfaceEntry": sysIpConfigHostInterfaceEntry,
       "sysIpConfigHostInterfaceIndex": sysIpConfigHostInterfaceIndex,
       "sysIpConfigHostInterfaceIpAddress": sysIpConfigHostInterfaceIpAddress,
       "sysIpConfigHostInterfaceSubnetMask": sysIpConfigHostInterfaceSubnetMask,
       "sysIpConfigHostInterfaceXmtRoutingMsg": sysIpConfigHostInterfaceXmtRoutingMsg,
       "sysIpConfigDefaultGateway": sysIpConfigDefaultGateway,
       "sysIpConfigDefaultGatewayIpAddress": sysIpConfigDefaultGatewayIpAddress,
       "sysIpConfigDefaultGatewaySubnetMask": sysIpConfigDefaultGatewaySubnetMask,
       "sysIpConfigTrapClientTable": sysIpConfigTrapClientTable,
       "sysIpConfigTrapClientEntry": sysIpConfigTrapClientEntry,
       "sysIpConfigTrapClientIndex": sysIpConfigTrapClientIndex,
       "sysIpConfigTrapClientIpAddress": sysIpConfigTrapClientIpAddress,
       "sysIpConfigTrapClientSubnetMask": sysIpConfigTrapClientSubnetMask,
       "sysIpConfigTrapClientPortNumber": sysIpConfigTrapClientPortNumber,
       "sysIpConfigCommunityName": sysIpConfigCommunityName,
       "sysIpConfigMacAddress": sysIpConfigMacAddress,
       "sysRs232Table": sysRs232Table,
       "sysRs232Entry": sysRs232Entry,
       "sysRs232Port": sysRs232Port,
       "sysRs232BaudRate": sysRs232BaudRate,
       "sysRs232Parity": sysRs232Parity,
       "sysRs232DataBits": sysRs232DataBits,
       "sysRs232StopBits": sysRs232StopBits,
       "sysMainProcessorFirmwareRev": sysMainProcessorFirmwareRev,
       "sysPortCardFirmwareRev": sysPortCardFirmwareRev,
       "config": config,
       "configDs1Table": configDs1Table,
       "configDs1Entry": configDs1Entry,
       "configDs1Port": configDs1Port,
       "configDs1AdminStatus": configDs1AdminStatus,
       "configDs1OperStatus": configDs1OperStatus,
       "configDs1LBO": configDs1LBO,
       "configDs1Encoding": configDs1Encoding,
       "configDs1Framing": configDs1Framing,
       "configDs1XmtAis": configDs1XmtAis,
       "configDs1Timing": configDs1Timing,
       "configAfa": configAfa,
       "configAfaActivationRate": configAfaActivationRate,
       "configAfaActivationTime": configAfaActivationTime,
       "configAfaDeactivationRate": configAfaDeactivationRate,
       "configAfaDeactivationTime": configAfaDeactivationTime,
       "configAfaStatus": configAfaStatus,
       "configAfaFarEndLpbkDetect": configAfaFarEndLpbkDetect,
       "configPortCardType": configPortCardType,
       "configHsdp": configHsdp,
       "configHsdpMode": configHsdpMode,
       "configHsdpCtsControl": configHsdpCtsControl,
       "configHsdpCtsStatus": configHsdpCtsStatus,
       "configHsdpTermTimingSource": configHsdpTermTimingSource,
       "configHsdpTermTiming": configHsdpTermTiming,
       "configHsdpRecvTiming": configHsdpRecvTiming,
       "configHsdpHoldoffSeconds": configHsdpHoldoffSeconds,
       "configHdlc": configHdlc,
       "configHdlcMode": configHdlcMode,
       "configHdlcLocalPort": configHdlcLocalPort,
       "configHdlcFarEndPort": configHdlcFarEndPort,
       "configInverseMux": configInverseMux,
       "fault": fault,
       "faultDs1": faultDs1,
       "faultDs1LoopbackTable": faultDs1LoopbackTable,
       "faultDs1LoopbackEntry": faultDs1LoopbackEntry,
       "faultDs1LoopbackPort": faultDs1LoopbackPort,
       "faultDs1LoopbackNetworkLoopback": faultDs1LoopbackNetworkLoopback,
       "faultDs1RemoteLineLoopback": faultDs1RemoteLineLoopback,
       "faultDte": faultDte,
       "faultDteLaLead": faultDteLaLead,
       "faultDteLbLead": faultDteLbLead,
       "faultDteLaLbTranslation": faultDteLaLbTranslation,
       "faultDteLaLbLoopbackEnable": faultDteLaLbLoopbackEnable,
       "faultDteCustomerLoopback": faultDteCustomerLoopback,
       "faultDteDteLoopback": faultDteDteLoopback,
       "faultClearCurrentAlarms": faultClearCurrentAlarms,
       "faultClearHistoryAlarms": faultClearHistoryAlarms,
       "faultCurrentAlarmTable": faultCurrentAlarmTable,
       "faultCurrentAlarmEntry": faultCurrentAlarmEntry,
       "faultCurrentAlarmTag": faultCurrentAlarmTag,
       "faultCurrentAlarmAlarmType": faultCurrentAlarmAlarmType,
       "faultCurrentAlarmSeverity": faultCurrentAlarmSeverity,
       "faultCurrentAlarmCardType": faultCurrentAlarmCardType,
       "faultCurrentAlarmPortNumber": faultCurrentAlarmPortNumber,
       "faultCurrentAlarmSetTime": faultCurrentAlarmSetTime,
       "faultCurrentAlarmDescription": faultCurrentAlarmDescription,
       "faultHistoryAlarmTable": faultHistoryAlarmTable,
       "faultHistoryAlarmEntry": faultHistoryAlarmEntry,
       "faultHistoryAlarmTag": faultHistoryAlarmTag,
       "faultHistoryAlarmAlarmType": faultHistoryAlarmAlarmType,
       "faultHistoryAlarmSeverity": faultHistoryAlarmSeverity,
       "faultHistoryAlarmCardType": faultHistoryAlarmCardType,
       "faultHistoryAlarmPortNumber": faultHistoryAlarmPortNumber,
       "faultHistoryAlarmSetTime": faultHistoryAlarmSetTime,
       "faultHistoryAlarmClearTime": faultHistoryAlarmClearTime,
       "faultHistoryAlarmDescription": faultHistoryAlarmDescription,
       "perf": perf,
       "perfClearDs1Performance": perfClearDs1Performance,
       "perfClearEnetPortCardStats": perfClearEnetPortCardStats,
       "enetPortCardStats": enetPortCardStats,
       "enetPortCardStatsFramesReceived": enetPortCardStatsFramesReceived,
       "enetPortCardStatsBytesReceived": enetPortCardStatsBytesReceived,
       "enetPortCardStatsFramesTransmitted": enetPortCardStatsFramesTransmitted,
       "enetPortCardStatsBytesTransmitted": enetPortCardStatsBytesTransmitted,
       "enetPortCardStatsAlignmentErrors": enetPortCardStatsAlignmentErrors,
       "enetPortCardStatsFCSErrors": enetPortCardStatsFCSErrors,
       "enetPortCardStatsSingleCollisionFrames": enetPortCardStatsSingleCollisionFrames,
       "enetPortCardStatsMultipleCollisionFrames": enetPortCardStatsMultipleCollisionFrames,
       "enetPortCardStatsDeferredTransmissions": enetPortCardStatsDeferredTransmissions,
       "enetPortCardStatsLateCollisions": enetPortCardStatsLateCollisions,
       "enetPortCardStatsExcessiveCollisions": enetPortCardStatsExcessiveCollisions,
       "enetPortCardStatsInternalMacTransmitErrors": enetPortCardStatsInternalMacTransmitErrors,
       "enetPortCardStatsCarrierSenseErrors": enetPortCardStatsCarrierSenseErrors,
       "enetPortCardStatsFrameTooLongs": enetPortCardStatsFrameTooLongs,
       "perfClearNxT1PortStats": perfClearNxT1PortStats,
       "nxt1PortStats": nxt1PortStats,
       "nxt1PortStatsFramesReceived": nxt1PortStatsFramesReceived,
       "nxt1PortStatsBytesReceived": nxt1PortStatsBytesReceived,
       "nxt1PortStatsFramesTransmitted": nxt1PortStatsFramesTransmitted,
       "nxt1PortStatsBytesTransmitted": nxt1PortStatsBytesTransmitted,
       "nxt1PortStatsCrcErrors": nxt1PortStatsCrcErrors}
)
