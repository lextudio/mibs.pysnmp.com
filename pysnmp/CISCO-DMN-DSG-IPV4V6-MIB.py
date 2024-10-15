# SNMP MIB module (CISCO-DMN-DSG-IPV4V6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-IPV4V6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:26 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGIPv4v6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25)
)
ciscoDSGIPv4v6.setRevisions(
        ("2012-03-20 11:00",
         "2010-08-30 11:00",
         "2010-04-30 05:00",
         "2010-04-12 05:00",
         "2010-03-22 05:00",
         "2009-12-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpV4v6Table_ObjectIdentity = ObjectIdentity
ipV4v6Table = _IpV4v6Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2)
)
_MacInfoTable_Object = MibTable
macInfoTable = _MacInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 1)
)
if mibBuilder.loadTexts:
    macInfoTable.setStatus("current")
_MacInfoEntry_Object = MibTableRow
macInfoEntry = _MacInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 1, 1)
)
macInfoEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-IPV4V6-MIB", "macInfoMacIndex"),
)
if mibBuilder.loadTexts:
    macInfoEntry.setStatus("current")


class _MacInfoMacIndex_Type(Integer32):
    """Custom type macInfoMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MacInfoMacIndex_Type.__name__ = "Integer32"
_MacInfoMacIndex_Object = MibTableColumn
macInfoMacIndex = _MacInfoMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 1, 1, 1),
    _MacInfoMacIndex_Type()
)
macInfoMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macInfoMacIndex.setStatus("current")


class _MacInfoMacAddr_Type(DisplayString):
    """Custom type macInfoMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_MacInfoMacAddr_Type.__name__ = "DisplayString"
_MacInfoMacAddr_Object = MibTableColumn
macInfoMacAddr = _MacInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 1, 1, 2),
    _MacInfoMacAddr_Type()
)
macInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macInfoMacAddr.setStatus("current")
_IpConfigTable_Object = MibTable
ipConfigTable = _IpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2)
)
if mibBuilder.loadTexts:
    ipConfigTable.setStatus("current")
_IpConfigEntry_Object = MibTableRow
ipConfigEntry = _IpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1)
)
ipConfigEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-IPV4V6-MIB", "ipConfigPortIdKey"),
)
if mibBuilder.loadTexts:
    ipConfigEntry.setStatus("current")


class _IpConfigPortIdKey_Type(Integer32):
    """Custom type ipConfigPortIdKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IpConfigPortIdKey_Type.__name__ = "Integer32"
_IpConfigPortIdKey_Object = MibTableColumn
ipConfigPortIdKey = _IpConfigPortIdKey_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 1),
    _IpConfigPortIdKey_Type()
)
ipConfigPortIdKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipConfigPortIdKey.setStatus("current")


class _IpConfigName_Type(DisplayString):
    """Custom type ipConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_IpConfigName_Type.__name__ = "DisplayString"
_IpConfigName_Object = MibTableColumn
ipConfigName = _IpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 2),
    _IpConfigName_Type()
)
ipConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigName.setStatus("current")
_IpConfigCurIPAddressV4_Type = IpAddress
_IpConfigCurIPAddressV4_Object = MibTableColumn
ipConfigCurIPAddressV4 = _IpConfigCurIPAddressV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 3),
    _IpConfigCurIPAddressV4_Type()
)
ipConfigCurIPAddressV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigCurIPAddressV4.setStatus("current")


class _IpConfigCurNetworkMaskV4_Type(Integer32):
    """Custom type ipConfigCurNetworkMaskV4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 30),
    )


_IpConfigCurNetworkMaskV4_Type.__name__ = "Integer32"
_IpConfigCurNetworkMaskV4_Object = MibTableColumn
ipConfigCurNetworkMaskV4 = _IpConfigCurNetworkMaskV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 4),
    _IpConfigCurNetworkMaskV4_Type()
)
ipConfigCurNetworkMaskV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigCurNetworkMaskV4.setStatus("current")
_IpConfigCurDefaultGatewayV4_Type = IpAddress
_IpConfigCurDefaultGatewayV4_Object = MibTableColumn
ipConfigCurDefaultGatewayV4 = _IpConfigCurDefaultGatewayV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 5),
    _IpConfigCurDefaultGatewayV4_Type()
)
ipConfigCurDefaultGatewayV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigCurDefaultGatewayV4.setStatus("current")


class _IpConfigV4V6Flag_Type(Integer32):
    """Custom type ipConfigV4V6Flag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipV4", 1),
          ("ipV6", 2))
    )


_IpConfigV4V6Flag_Type.__name__ = "Integer32"
_IpConfigV4V6Flag_Object = MibTableColumn
ipConfigV4V6Flag = _IpConfigV4V6Flag_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 6),
    _IpConfigV4V6Flag_Type()
)
ipConfigV4V6Flag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipConfigV4V6Flag.setStatus("current")


class _IpConfigPortMode_Type(Integer32):
    """Custom type ipConfigPortMode based on Integer32"""
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
        *(("auto", 1),
          ("fd10", 3),
          ("fd100", 5),
          ("fd1000", 7),
          ("hd10", 2),
          ("hd100", 4),
          ("hd1000", 6))
    )


_IpConfigPortMode_Type.__name__ = "Integer32"
_IpConfigPortMode_Object = MibTableColumn
ipConfigPortMode = _IpConfigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 7),
    _IpConfigPortMode_Type()
)
ipConfigPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigPortMode.setStatus("current")


class _EthStatusLink_Type(DisplayString):
    """Custom type ethStatusLink based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthStatusLink_Type.__name__ = "DisplayString"
_EthStatusLink_Object = MibTableColumn
ethStatusLink = _EthStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 11),
    _EthStatusLink_Type()
)
ethStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatusLink.setStatus("current")


class _EthStatusSpeed_Type(DisplayString):
    """Custom type ethStatusSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthStatusSpeed_Type.__name__ = "DisplayString"
_EthStatusSpeed_Object = MibTableColumn
ethStatusSpeed = _EthStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 12),
    _EthStatusSpeed_Type()
)
ethStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatusSpeed.setStatus("current")


class _EthStatusDuplex_Type(DisplayString):
    """Custom type ethStatusDuplex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthStatusDuplex_Type.__name__ = "DisplayString"
_EthStatusDuplex_Object = MibTableColumn
ethStatusDuplex = _EthStatusDuplex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 13),
    _EthStatusDuplex_Type()
)
ethStatusDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatusDuplex.setStatus("current")


class _EthStatusXover_Type(DisplayString):
    """Custom type ethStatusXover based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthStatusXover_Type.__name__ = "DisplayString"
_EthStatusXover_Object = MibTableColumn
ethStatusXover = _EthStatusXover_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 2, 1, 14),
    _EthStatusXover_Type()
)
ethStatusXover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethStatusXover.setStatus("current")
_EthBackupTable_Object = MibTable
ethBackupTable = _EthBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3)
)
if mibBuilder.loadTexts:
    ethBackupTable.setStatus("current")
_EthBackupEntry_Object = MibTableRow
ethBackupEntry = _EthBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3, 1)
)
ethBackupEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-IPV4V6-MIB", "ethBackupIndex"),
)
if mibBuilder.loadTexts:
    ethBackupEntry.setStatus("current")


class _EthBackupIndex_Type(Integer32):
    """Custom type ethBackupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EthBackupIndex_Type.__name__ = "Integer32"
_EthBackupIndex_Object = MibTableColumn
ethBackupIndex = _EthBackupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3, 1, 1),
    _EthBackupIndex_Type()
)
ethBackupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBackupIndex.setStatus("current")


class _EthBackupMode_Type(Integer32):
    """Custom type ethBackupMode based on Integer32"""
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
        *(("backupPrimaryData1", 2),
          ("backupPrimaryData2", 3),
          ("manualData1", 4),
          ("manualData2", 5),
          ("mirroring", 1))
    )


_EthBackupMode_Type.__name__ = "Integer32"
_EthBackupMode_Object = MibTableColumn
ethBackupMode = _EthBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3, 1, 2),
    _EthBackupMode_Type()
)
ethBackupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBackupMode.setStatus("current")


class _EthBackupDirection_Type(Integer32):
    """Custom type ethBackupDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_EthBackupDirection_Type.__name__ = "Integer32"
_EthBackupDirection_Object = MibTableColumn
ethBackupDirection = _EthBackupDirection_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3, 1, 3),
    _EthBackupDirection_Type()
)
ethBackupDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBackupDirection.setStatus("current")


class _EthBackupDelayForward_Type(Integer32):
    """Custom type ethBackupDelayForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EthBackupDelayForward_Type.__name__ = "Integer32"
_EthBackupDelayForward_Object = MibTableColumn
ethBackupDelayForward = _EthBackupDelayForward_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3, 1, 4),
    _EthBackupDelayForward_Type()
)
ethBackupDelayForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBackupDelayForward.setStatus("current")


class _EthBackupDelayBack_Type(Integer32):
    """Custom type ethBackupDelayBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_EthBackupDelayBack_Type.__name__ = "Integer32"
_EthBackupDelayBack_Object = MibTableColumn
ethBackupDelayBack = _EthBackupDelayBack_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 3, 1, 5),
    _EthBackupDelayBack_Type()
)
ethBackupDelayBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBackupDelayBack.setStatus("current")
_EthBackupStatusTable_Object = MibTable
ethBackupStatusTable = _EthBackupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 4)
)
if mibBuilder.loadTexts:
    ethBackupStatusTable.setStatus("current")
_EthBackupStatusEntry_Object = MibTableRow
ethBackupStatusEntry = _EthBackupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 4, 1)
)
ethBackupStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-IPV4V6-MIB", "ethBackupStatusIndex"),
)
if mibBuilder.loadTexts:
    ethBackupStatusEntry.setStatus("current")


class _EthBackupStatusIndex_Type(Integer32):
    """Custom type ethBackupStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EthBackupStatusIndex_Type.__name__ = "Integer32"
_EthBackupStatusIndex_Object = MibTableColumn
ethBackupStatusIndex = _EthBackupStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 4, 1, 1),
    _EthBackupStatusIndex_Type()
)
ethBackupStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBackupStatusIndex.setStatus("current")


class _EthBackupStatusPortsInUse_Type(DisplayString):
    """Custom type ethBackupStatusPortsInUse based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthBackupStatusPortsInUse_Type.__name__ = "DisplayString"
_EthBackupStatusPortsInUse_Object = MibTableColumn
ethBackupStatusPortsInUse = _EthBackupStatusPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 4, 1, 2),
    _EthBackupStatusPortsInUse_Type()
)
ethBackupStatusPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBackupStatusPortsInUse.setStatus("current")


class _EthBackupStatusChangeReason_Type(DisplayString):
    """Custom type ethBackupStatusChangeReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EthBackupStatusChangeReason_Type.__name__ = "DisplayString"
_EthBackupStatusChangeReason_Object = MibTableColumn
ethBackupStatusChangeReason = _EthBackupStatusChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 4, 1, 3),
    _EthBackupStatusChangeReason_Type()
)
ethBackupStatusChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBackupStatusChangeReason.setStatus("current")


class _EthBackupStatusChangeDateTime_Type(DisplayString):
    """Custom type ethBackupStatusChangeDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_EthBackupStatusChangeDateTime_Type.__name__ = "DisplayString"
_EthBackupStatusChangeDateTime_Object = MibTableColumn
ethBackupStatusChangeDateTime = _EthBackupStatusChangeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 25, 2, 4, 1, 4),
    _EthBackupStatusChangeDateTime_Type()
)
ethBackupStatusChangeDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBackupStatusChangeDateTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-IPV4V6-MIB",
    **{"ciscoDSGIPv4v6": ciscoDSGIPv4v6,
       "ipV4v6Table": ipV4v6Table,
       "macInfoTable": macInfoTable,
       "macInfoEntry": macInfoEntry,
       "macInfoMacIndex": macInfoMacIndex,
       "macInfoMacAddr": macInfoMacAddr,
       "ipConfigTable": ipConfigTable,
       "ipConfigEntry": ipConfigEntry,
       "ipConfigPortIdKey": ipConfigPortIdKey,
       "ipConfigName": ipConfigName,
       "ipConfigCurIPAddressV4": ipConfigCurIPAddressV4,
       "ipConfigCurNetworkMaskV4": ipConfigCurNetworkMaskV4,
       "ipConfigCurDefaultGatewayV4": ipConfigCurDefaultGatewayV4,
       "ipConfigV4V6Flag": ipConfigV4V6Flag,
       "ipConfigPortMode": ipConfigPortMode,
       "ethStatusLink": ethStatusLink,
       "ethStatusSpeed": ethStatusSpeed,
       "ethStatusDuplex": ethStatusDuplex,
       "ethStatusXover": ethStatusXover,
       "ethBackupTable": ethBackupTable,
       "ethBackupEntry": ethBackupEntry,
       "ethBackupIndex": ethBackupIndex,
       "ethBackupMode": ethBackupMode,
       "ethBackupDirection": ethBackupDirection,
       "ethBackupDelayForward": ethBackupDelayForward,
       "ethBackupDelayBack": ethBackupDelayBack,
       "ethBackupStatusTable": ethBackupStatusTable,
       "ethBackupStatusEntry": ethBackupStatusEntry,
       "ethBackupStatusIndex": ethBackupStatusIndex,
       "ethBackupStatusPortsInUse": ethBackupStatusPortsInUse,
       "ethBackupStatusChangeReason": ethBackupStatusChangeReason,
       "ethBackupStatusChangeDateTime": ethBackupStatusChangeDateTime}
)
