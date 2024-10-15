# SNMP MIB module (HM2-PLATFORM-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:22 2024
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

(HmEnabledStatus,
 hm2PlatformMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2PlatformMibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2PlatformRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 8)
)
hm2PlatformRadius.setRevisions(
        ("2013-06-05 00:00",
         "2013-03-01 00:00",
         "2011-06-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentRadiusConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentRadiusConfigGroup = _Hm2AgentRadiusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1)
)


class _Hm2AgentRadiusMaxTransmit_Type(Unsigned32):
    """Custom type hm2AgentRadiusMaxTransmit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2AgentRadiusMaxTransmit_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusMaxTransmit_Object = MibScalar
hm2AgentRadiusMaxTransmit = _Hm2AgentRadiusMaxTransmit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 1),
    _Hm2AgentRadiusMaxTransmit_Type()
)
hm2AgentRadiusMaxTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusMaxTransmit.setStatus("current")


class _Hm2AgentRadiusTimeout_Type(Unsigned32):
    """Custom type hm2AgentRadiusTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Hm2AgentRadiusTimeout_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusTimeout_Object = MibScalar
hm2AgentRadiusTimeout = _Hm2AgentRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 2),
    _Hm2AgentRadiusTimeout_Type()
)
hm2AgentRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusTimeout.setStatus("current")


class _Hm2AgentRadiusAccountingMode_Type(HmEnabledStatus):
    """Custom type hm2AgentRadiusAccountingMode based on HmEnabledStatus"""


_Hm2AgentRadiusAccountingMode_Object = MibScalar
hm2AgentRadiusAccountingMode = _Hm2AgentRadiusAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 3),
    _Hm2AgentRadiusAccountingMode_Type()
)
hm2AgentRadiusAccountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingMode.setStatus("current")


class _Hm2AgentRadiusStatsClear_Type(HmEnabledStatus):
    """Custom type hm2AgentRadiusStatsClear based on HmEnabledStatus"""


_Hm2AgentRadiusStatsClear_Object = MibScalar
hm2AgentRadiusStatsClear = _Hm2AgentRadiusStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 4),
    _Hm2AgentRadiusStatsClear_Type()
)
hm2AgentRadiusStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusStatsClear.setStatus("current")


class _Hm2AgentRadiusAccountingIndexNextValid_Type(Integer32):
    """Custom type hm2AgentRadiusAccountingIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_Hm2AgentRadiusAccountingIndexNextValid_Type.__name__ = "Integer32"
_Hm2AgentRadiusAccountingIndexNextValid_Object = MibScalar
hm2AgentRadiusAccountingIndexNextValid = _Hm2AgentRadiusAccountingIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 5),
    _Hm2AgentRadiusAccountingIndexNextValid_Type()
)
hm2AgentRadiusAccountingIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingIndexNextValid.setStatus("current")
_Hm2AgentRadiusAccountingConfigTable_Object = MibTable
hm2AgentRadiusAccountingConfigTable = _Hm2AgentRadiusAccountingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingConfigTable.setStatus("current")
_Hm2AgentRadiusAccountingConfigEntry_Object = MibTableRow
hm2AgentRadiusAccountingConfigEntry = _Hm2AgentRadiusAccountingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1)
)
hm2AgentRadiusAccountingConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-RADIUS-MIB", "hm2AgentRadiusAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingConfigEntry.setStatus("current")


class _Hm2AgentRadiusAccountingServerIndex_Type(Integer32):
    """Custom type hm2AgentRadiusAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hm2AgentRadiusAccountingServerIndex_Type.__name__ = "Integer32"
_Hm2AgentRadiusAccountingServerIndex_Object = MibTableColumn
hm2AgentRadiusAccountingServerIndex = _Hm2AgentRadiusAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 1),
    _Hm2AgentRadiusAccountingServerIndex_Type()
)
hm2AgentRadiusAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServerIndex.setStatus("current")
_Hm2AgentRadiusAccountingServerAddress_Type = InetAddress
_Hm2AgentRadiusAccountingServerAddress_Object = MibTableColumn
hm2AgentRadiusAccountingServerAddress = _Hm2AgentRadiusAccountingServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 2),
    _Hm2AgentRadiusAccountingServerAddress_Type()
)
hm2AgentRadiusAccountingServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServerAddress.setStatus("deprecated")
_Hm2AgentRadiusAccountingServerAddressType_Type = InetAddressType
_Hm2AgentRadiusAccountingServerAddressType_Object = MibTableColumn
hm2AgentRadiusAccountingServerAddressType = _Hm2AgentRadiusAccountingServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 3),
    _Hm2AgentRadiusAccountingServerAddressType_Type()
)
hm2AgentRadiusAccountingServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServerAddressType.setStatus("deprecated")


class _Hm2AgentRadiusAccountingPort_Type(Unsigned32):
    """Custom type hm2AgentRadiusAccountingPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentRadiusAccountingPort_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusAccountingPort_Object = MibTableColumn
hm2AgentRadiusAccountingPort = _Hm2AgentRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 4),
    _Hm2AgentRadiusAccountingPort_Type()
)
hm2AgentRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingPort.setStatus("current")


class _Hm2AgentRadiusAccountingSecret_Type(DisplayString):
    """Custom type hm2AgentRadiusAccountingSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_Hm2AgentRadiusAccountingSecret_Type.__name__ = "DisplayString"
_Hm2AgentRadiusAccountingSecret_Object = MibTableColumn
hm2AgentRadiusAccountingSecret = _Hm2AgentRadiusAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 5),
    _Hm2AgentRadiusAccountingSecret_Type()
)
hm2AgentRadiusAccountingSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingSecret.setStatus("current")
_Hm2AgentRadiusAccountingStatus_Type = RowStatus
_Hm2AgentRadiusAccountingStatus_Object = MibTableColumn
hm2AgentRadiusAccountingStatus = _Hm2AgentRadiusAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 6),
    _Hm2AgentRadiusAccountingStatus_Type()
)
hm2AgentRadiusAccountingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingStatus.setStatus("current")


class _Hm2AgentRadiusAccountingServerName_Type(DisplayString):
    """Custom type hm2AgentRadiusAccountingServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2AgentRadiusAccountingServerName_Type.__name__ = "DisplayString"
_Hm2AgentRadiusAccountingServerName_Object = MibTableColumn
hm2AgentRadiusAccountingServerName = _Hm2AgentRadiusAccountingServerName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 7),
    _Hm2AgentRadiusAccountingServerName_Type()
)
hm2AgentRadiusAccountingServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServerName.setStatus("current")
_Hm2AgentRadiusAccountingServerAddrType_Type = InetAddressType
_Hm2AgentRadiusAccountingServerAddrType_Object = MibTableColumn
hm2AgentRadiusAccountingServerAddrType = _Hm2AgentRadiusAccountingServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 248),
    _Hm2AgentRadiusAccountingServerAddrType_Type()
)
hm2AgentRadiusAccountingServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServerAddrType.setStatus("current")
_Hm2AgentRadiusAccountingServerAddr_Type = InetAddress
_Hm2AgentRadiusAccountingServerAddr_Object = MibTableColumn
hm2AgentRadiusAccountingServerAddr = _Hm2AgentRadiusAccountingServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 6, 1, 249),
    _Hm2AgentRadiusAccountingServerAddr_Type()
)
hm2AgentRadiusAccountingServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServerAddr.setStatus("current")


class _Hm2AgentRadiusServerIndexNextValid_Type(Integer32):
    """Custom type hm2AgentRadiusServerIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_Hm2AgentRadiusServerIndexNextValid_Type.__name__ = "Integer32"
_Hm2AgentRadiusServerIndexNextValid_Object = MibScalar
hm2AgentRadiusServerIndexNextValid = _Hm2AgentRadiusServerIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 7),
    _Hm2AgentRadiusServerIndexNextValid_Type()
)
hm2AgentRadiusServerIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerIndexNextValid.setStatus("current")
_Hm2AgentRadiusServerConfigTable_Object = MibTable
hm2AgentRadiusServerConfigTable = _Hm2AgentRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hm2AgentRadiusServerConfigTable.setStatus("current")
_Hm2AgentRadiusServerConfigEntry_Object = MibTableRow
hm2AgentRadiusServerConfigEntry = _Hm2AgentRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1)
)
hm2AgentRadiusServerConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-RADIUS-MIB", "hm2AgentRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentRadiusServerConfigEntry.setStatus("current")


class _Hm2AgentRadiusServerIndex_Type(Integer32):
    """Custom type hm2AgentRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hm2AgentRadiusServerIndex_Type.__name__ = "Integer32"
_Hm2AgentRadiusServerIndex_Object = MibTableColumn
hm2AgentRadiusServerIndex = _Hm2AgentRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 1),
    _Hm2AgentRadiusServerIndex_Type()
)
hm2AgentRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerIndex.setStatus("current")
_Hm2AgentRadiusServerAddressType_Type = InetAddressType
_Hm2AgentRadiusServerAddressType_Object = MibTableColumn
hm2AgentRadiusServerAddressType = _Hm2AgentRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 3),
    _Hm2AgentRadiusServerAddressType_Type()
)
hm2AgentRadiusServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerAddressType.setStatus("deprecated")


class _Hm2AgentRadiusServerPort_Type(Unsigned32):
    """Custom type hm2AgentRadiusServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentRadiusServerPort_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusServerPort_Object = MibTableColumn
hm2AgentRadiusServerPort = _Hm2AgentRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 4),
    _Hm2AgentRadiusServerPort_Type()
)
hm2AgentRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerPort.setStatus("current")


class _Hm2AgentRadiusServerSecret_Type(DisplayString):
    """Custom type hm2AgentRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_Hm2AgentRadiusServerSecret_Type.__name__ = "DisplayString"
_Hm2AgentRadiusServerSecret_Object = MibTableColumn
hm2AgentRadiusServerSecret = _Hm2AgentRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 5),
    _Hm2AgentRadiusServerSecret_Type()
)
hm2AgentRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerSecret.setStatus("current")
_Hm2AgentRadiusServerPrimaryMode_Type = HmEnabledStatus
_Hm2AgentRadiusServerPrimaryMode_Object = MibTableColumn
hm2AgentRadiusServerPrimaryMode = _Hm2AgentRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 6),
    _Hm2AgentRadiusServerPrimaryMode_Type()
)
hm2AgentRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerPrimaryMode.setStatus("current")


class _Hm2AgentRadiusServerCurrentMode_Type(Integer32):
    """Custom type hm2AgentRadiusServerCurrentMode based on Integer32"""
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


_Hm2AgentRadiusServerCurrentMode_Type.__name__ = "Integer32"
_Hm2AgentRadiusServerCurrentMode_Object = MibTableColumn
hm2AgentRadiusServerCurrentMode = _Hm2AgentRadiusServerCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 7),
    _Hm2AgentRadiusServerCurrentMode_Type()
)
hm2AgentRadiusServerCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerCurrentMode.setStatus("current")
_Hm2AgentRadiusServerMsgAuth_Type = HmEnabledStatus
_Hm2AgentRadiusServerMsgAuth_Object = MibTableColumn
hm2AgentRadiusServerMsgAuth = _Hm2AgentRadiusServerMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 8),
    _Hm2AgentRadiusServerMsgAuth_Type()
)
hm2AgentRadiusServerMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerMsgAuth.setStatus("current")
_Hm2AgentRadiusServerRowStatus_Type = RowStatus
_Hm2AgentRadiusServerRowStatus_Object = MibTableColumn
hm2AgentRadiusServerRowStatus = _Hm2AgentRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 9),
    _Hm2AgentRadiusServerRowStatus_Type()
)
hm2AgentRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerRowStatus.setStatus("current")


class _Hm2AgentRadiusServerName_Type(DisplayString):
    """Custom type hm2AgentRadiusServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2AgentRadiusServerName_Type.__name__ = "DisplayString"
_Hm2AgentRadiusServerName_Object = MibTableColumn
hm2AgentRadiusServerName = _Hm2AgentRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 10),
    _Hm2AgentRadiusServerName_Type()
)
hm2AgentRadiusServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerName.setStatus("current")
_Hm2AgentRadiusServerInetAddress_Type = InetAddress
_Hm2AgentRadiusServerInetAddress_Object = MibTableColumn
hm2AgentRadiusServerInetAddress = _Hm2AgentRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 11),
    _Hm2AgentRadiusServerInetAddress_Type()
)
hm2AgentRadiusServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerInetAddress.setStatus("deprecated")


class _Hm2AgentRadiusServerTimeout_Type(Unsigned32):
    """Custom type hm2AgentRadiusServerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Hm2AgentRadiusServerTimeout_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusServerTimeout_Object = MibTableColumn
hm2AgentRadiusServerTimeout = _Hm2AgentRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 12),
    _Hm2AgentRadiusServerTimeout_Type()
)
hm2AgentRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerTimeout.setStatus("current")


class _Hm2AgentRadiusServerRetransmit_Type(Unsigned32):
    """Custom type hm2AgentRadiusServerRetransmit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2AgentRadiusServerRetransmit_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusServerRetransmit_Object = MibTableColumn
hm2AgentRadiusServerRetransmit = _Hm2AgentRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 13),
    _Hm2AgentRadiusServerRetransmit_Type()
)
hm2AgentRadiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerRetransmit.setStatus("current")


class _Hm2AgentRadiusServerDeadtime_Type(Unsigned32):
    """Custom type hm2AgentRadiusServerDeadtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Hm2AgentRadiusServerDeadtime_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusServerDeadtime_Object = MibTableColumn
hm2AgentRadiusServerDeadtime = _Hm2AgentRadiusServerDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 14),
    _Hm2AgentRadiusServerDeadtime_Type()
)
hm2AgentRadiusServerDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerDeadtime.setStatus("current")
_Hm2AgentRadiusServerSourceIPAddr_Type = IpAddress
_Hm2AgentRadiusServerSourceIPAddr_Object = MibTableColumn
hm2AgentRadiusServerSourceIPAddr = _Hm2AgentRadiusServerSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 15),
    _Hm2AgentRadiusServerSourceIPAddr_Type()
)
hm2AgentRadiusServerSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerSourceIPAddr.setStatus("current")


class _Hm2AgentRadiusServerPriority_Type(Unsigned32):
    """Custom type hm2AgentRadiusServerPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentRadiusServerPriority_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusServerPriority_Object = MibTableColumn
hm2AgentRadiusServerPriority = _Hm2AgentRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 16),
    _Hm2AgentRadiusServerPriority_Type()
)
hm2AgentRadiusServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerPriority.setStatus("current")


class _Hm2AgentRadiusServerUsageType_Type(Integer32):
    """Custom type hm2AgentRadiusServerUsageType based on Integer32"""
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
        *(("all", 1),
          ("dot1x", 3),
          ("login", 2))
    )


_Hm2AgentRadiusServerUsageType_Type.__name__ = "Integer32"
_Hm2AgentRadiusServerUsageType_Object = MibTableColumn
hm2AgentRadiusServerUsageType = _Hm2AgentRadiusServerUsageType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 17),
    _Hm2AgentRadiusServerUsageType_Type()
)
hm2AgentRadiusServerUsageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerUsageType.setStatus("current")
_Hm2AgentRadiusServerInetAddrType_Type = InetAddressType
_Hm2AgentRadiusServerInetAddrType_Object = MibTableColumn
hm2AgentRadiusServerInetAddrType = _Hm2AgentRadiusServerInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 248),
    _Hm2AgentRadiusServerInetAddrType_Type()
)
hm2AgentRadiusServerInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerInetAddrType.setStatus("current")
_Hm2AgentRadiusServerInetAddr_Type = InetAddress
_Hm2AgentRadiusServerInetAddr_Object = MibTableColumn
hm2AgentRadiusServerInetAddr = _Hm2AgentRadiusServerInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 8, 1, 249),
    _Hm2AgentRadiusServerInetAddr_Type()
)
hm2AgentRadiusServerInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentRadiusServerInetAddr.setStatus("current")
_Hm2AgentRadiusAuthenticationServers_Type = Unsigned32
_Hm2AgentRadiusAuthenticationServers_Object = MibScalar
hm2AgentRadiusAuthenticationServers = _Hm2AgentRadiusAuthenticationServers_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 9),
    _Hm2AgentRadiusAuthenticationServers_Type()
)
hm2AgentRadiusAuthenticationServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusAuthenticationServers.setStatus("current")
_Hm2AgentRadiusAccountingServers_Type = Unsigned32
_Hm2AgentRadiusAccountingServers_Object = MibScalar
hm2AgentRadiusAccountingServers = _Hm2AgentRadiusAccountingServers_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 10),
    _Hm2AgentRadiusAccountingServers_Type()
)
hm2AgentRadiusAccountingServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusAccountingServers.setStatus("current")
_Hm2AgentRadiusNamedAuthenticationServerGroups_Type = Unsigned32
_Hm2AgentRadiusNamedAuthenticationServerGroups_Object = MibScalar
hm2AgentRadiusNamedAuthenticationServerGroups = _Hm2AgentRadiusNamedAuthenticationServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 11),
    _Hm2AgentRadiusNamedAuthenticationServerGroups_Type()
)
hm2AgentRadiusNamedAuthenticationServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusNamedAuthenticationServerGroups.setStatus("current")
_Hm2AgentRadiusNamedAccountingServerGroups_Type = Unsigned32
_Hm2AgentRadiusNamedAccountingServerGroups_Object = MibScalar
hm2AgentRadiusNamedAccountingServerGroups = _Hm2AgentRadiusNamedAccountingServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 12),
    _Hm2AgentRadiusNamedAccountingServerGroups_Type()
)
hm2AgentRadiusNamedAccountingServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentRadiusNamedAccountingServerGroups.setStatus("current")


class _Hm2AgentRadiusDeadTime_Type(Unsigned32):
    """Custom type hm2AgentRadiusDeadTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Hm2AgentRadiusDeadTime_Type.__name__ = "Unsigned32"
_Hm2AgentRadiusDeadTime_Object = MibScalar
hm2AgentRadiusDeadTime = _Hm2AgentRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 13),
    _Hm2AgentRadiusDeadTime_Type()
)
hm2AgentRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusDeadTime.setStatus("current")


class _Hm2AgentRadiusSourceIPAddr_Type(IpAddress):
    """Custom type hm2AgentRadiusSourceIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_Hm2AgentRadiusSourceIPAddr_Object = MibScalar
hm2AgentRadiusSourceIPAddr = _Hm2AgentRadiusSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 15),
    _Hm2AgentRadiusSourceIPAddr_Type()
)
hm2AgentRadiusSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusSourceIPAddr.setStatus("current")


class _Hm2AgentRadiusNasIpAddress_Type(IpAddress):
    """Custom type hm2AgentRadiusNasIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_Hm2AgentRadiusNasIpAddress_Object = MibScalar
hm2AgentRadiusNasIpAddress = _Hm2AgentRadiusNasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 16),
    _Hm2AgentRadiusNasIpAddress_Type()
)
hm2AgentRadiusNasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusNasIpAddress.setStatus("current")


class _Hm2AgentAuthorizationNetworkRadiusMode_Type(HmEnabledStatus):
    """Custom type hm2AgentAuthorizationNetworkRadiusMode based on HmEnabledStatus"""


_Hm2AgentAuthorizationNetworkRadiusMode_Object = MibScalar
hm2AgentAuthorizationNetworkRadiusMode = _Hm2AgentAuthorizationNetworkRadiusMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 17),
    _Hm2AgentAuthorizationNetworkRadiusMode_Type()
)
hm2AgentAuthorizationNetworkRadiusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentAuthorizationNetworkRadiusMode.setStatus("current")


class _Hm2AgentRadiusSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentRadiusSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentRadiusSourceInterface_Object = MibScalar
hm2AgentRadiusSourceInterface = _Hm2AgentRadiusSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 8, 1, 18),
    _Hm2AgentRadiusSourceInterface_Type()
)
hm2AgentRadiusSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentRadiusSourceInterface.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-RADIUS-MIB",
    **{"hm2PlatformRadius": hm2PlatformRadius,
       "hm2AgentRadiusConfigGroup": hm2AgentRadiusConfigGroup,
       "hm2AgentRadiusMaxTransmit": hm2AgentRadiusMaxTransmit,
       "hm2AgentRadiusTimeout": hm2AgentRadiusTimeout,
       "hm2AgentRadiusAccountingMode": hm2AgentRadiusAccountingMode,
       "hm2AgentRadiusStatsClear": hm2AgentRadiusStatsClear,
       "hm2AgentRadiusAccountingIndexNextValid": hm2AgentRadiusAccountingIndexNextValid,
       "hm2AgentRadiusAccountingConfigTable": hm2AgentRadiusAccountingConfigTable,
       "hm2AgentRadiusAccountingConfigEntry": hm2AgentRadiusAccountingConfigEntry,
       "hm2AgentRadiusAccountingServerIndex": hm2AgentRadiusAccountingServerIndex,
       "hm2AgentRadiusAccountingServerAddress": hm2AgentRadiusAccountingServerAddress,
       "hm2AgentRadiusAccountingServerAddressType": hm2AgentRadiusAccountingServerAddressType,
       "hm2AgentRadiusAccountingPort": hm2AgentRadiusAccountingPort,
       "hm2AgentRadiusAccountingSecret": hm2AgentRadiusAccountingSecret,
       "hm2AgentRadiusAccountingStatus": hm2AgentRadiusAccountingStatus,
       "hm2AgentRadiusAccountingServerName": hm2AgentRadiusAccountingServerName,
       "hm2AgentRadiusAccountingServerAddrType": hm2AgentRadiusAccountingServerAddrType,
       "hm2AgentRadiusAccountingServerAddr": hm2AgentRadiusAccountingServerAddr,
       "hm2AgentRadiusServerIndexNextValid": hm2AgentRadiusServerIndexNextValid,
       "hm2AgentRadiusServerConfigTable": hm2AgentRadiusServerConfigTable,
       "hm2AgentRadiusServerConfigEntry": hm2AgentRadiusServerConfigEntry,
       "hm2AgentRadiusServerIndex": hm2AgentRadiusServerIndex,
       "hm2AgentRadiusServerAddressType": hm2AgentRadiusServerAddressType,
       "hm2AgentRadiusServerPort": hm2AgentRadiusServerPort,
       "hm2AgentRadiusServerSecret": hm2AgentRadiusServerSecret,
       "hm2AgentRadiusServerPrimaryMode": hm2AgentRadiusServerPrimaryMode,
       "hm2AgentRadiusServerCurrentMode": hm2AgentRadiusServerCurrentMode,
       "hm2AgentRadiusServerMsgAuth": hm2AgentRadiusServerMsgAuth,
       "hm2AgentRadiusServerRowStatus": hm2AgentRadiusServerRowStatus,
       "hm2AgentRadiusServerName": hm2AgentRadiusServerName,
       "hm2AgentRadiusServerInetAddress": hm2AgentRadiusServerInetAddress,
       "hm2AgentRadiusServerTimeout": hm2AgentRadiusServerTimeout,
       "hm2AgentRadiusServerRetransmit": hm2AgentRadiusServerRetransmit,
       "hm2AgentRadiusServerDeadtime": hm2AgentRadiusServerDeadtime,
       "hm2AgentRadiusServerSourceIPAddr": hm2AgentRadiusServerSourceIPAddr,
       "hm2AgentRadiusServerPriority": hm2AgentRadiusServerPriority,
       "hm2AgentRadiusServerUsageType": hm2AgentRadiusServerUsageType,
       "hm2AgentRadiusServerInetAddrType": hm2AgentRadiusServerInetAddrType,
       "hm2AgentRadiusServerInetAddr": hm2AgentRadiusServerInetAddr,
       "hm2AgentRadiusAuthenticationServers": hm2AgentRadiusAuthenticationServers,
       "hm2AgentRadiusAccountingServers": hm2AgentRadiusAccountingServers,
       "hm2AgentRadiusNamedAuthenticationServerGroups": hm2AgentRadiusNamedAuthenticationServerGroups,
       "hm2AgentRadiusNamedAccountingServerGroups": hm2AgentRadiusNamedAccountingServerGroups,
       "hm2AgentRadiusDeadTime": hm2AgentRadiusDeadTime,
       "hm2AgentRadiusSourceIPAddr": hm2AgentRadiusSourceIPAddr,
       "hm2AgentRadiusNasIpAddress": hm2AgentRadiusNasIpAddress,
       "hm2AgentAuthorizationNetworkRadiusMode": hm2AgentAuthorizationNetworkRadiusMode,
       "hm2AgentRadiusSourceInterface": hm2AgentRadiusSourceInterface}
)
