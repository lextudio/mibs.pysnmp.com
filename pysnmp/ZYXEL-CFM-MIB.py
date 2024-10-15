# SNMP MIB module (ZYXEL-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:29 2024
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

(dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TDomain",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelCfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelCfmSetup_ObjectIdentity = ObjectIdentity
zyxelCfmSetup = _ZyxelCfmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1)
)
_ZyCfmState_Type = EnabledStatus
_ZyCfmState_Object = MibScalar
zyCfmState = _ZyCfmState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 1),
    _ZyCfmState_Type()
)
zyCfmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmState.setStatus("current")
_ZyxelCfmMibObjects_ObjectIdentity = ObjectIdentity
zyxelCfmMibObjects = _ZyxelCfmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 2)
)
_ZyCfmMgmtIpAddressDomain_Type = TDomain
_ZyCfmMgmtIpAddressDomain_Object = MibScalar
zyCfmMgmtIpAddressDomain = _ZyCfmMgmtIpAddressDomain_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 2, 1),
    _ZyCfmMgmtIpAddressDomain_Type()
)
zyCfmMgmtIpAddressDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmMgmtIpAddressDomain.setStatus("current")
_ZyCfmMgmtIpAddress_Type = IpAddress
_ZyCfmMgmtIpAddress_Object = MibScalar
zyCfmMgmtIpAddress = _ZyCfmMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 2, 2),
    _ZyCfmMgmtIpAddress_Type()
)
zyCfmMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmMgmtIpAddress.setStatus("current")
_ZyxelCfmMepTable_Object = MibTable
zyxelCfmMepTable = _ZyxelCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelCfmMepTable.setStatus("current")
_ZyxelCfmMepEntry_Object = MibTableRow
zyxelCfmMepEntry = _ZyxelCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 2, 3, 1)
)
zyxelCfmMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    zyxelCfmMepEntry.setStatus("current")


class _ZyCfmMepTransmitLbmDataTlvSize_Type(Unsigned32):
    """Custom type zyCfmMepTransmitLbmDataTlvSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_ZyCfmMepTransmitLbmDataTlvSize_Type.__name__ = "Unsigned32"
_ZyCfmMepTransmitLbmDataTlvSize_Object = MibTableColumn
zyCfmMepTransmitLbmDataTlvSize = _ZyCfmMepTransmitLbmDataTlvSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 1, 2, 3, 1, 1),
    _ZyCfmMepTransmitLbmDataTlvSize_Type()
)
zyCfmMepTransmitLbmDataTlvSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmMepTransmitLbmDataTlvSize.setStatus("current")
_ZyxelCfmStatus_ObjectIdentity = ObjectIdentity
zyxelCfmStatus = _ZyxelCfmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 2)
)
_ZyCfmLinkTraceClear_Type = EnabledStatus
_ZyCfmLinkTraceClear_Object = MibScalar
zyCfmLinkTraceClear = _ZyCfmLinkTraceClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 2, 1),
    _ZyCfmLinkTraceClear_Type()
)
zyCfmLinkTraceClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmLinkTraceClear.setStatus("current")
_ZyCfmMepCcmDbClear_Type = EnabledStatus
_ZyCfmMepCcmDbClear_Object = MibScalar
zyCfmMepCcmDbClear = _ZyCfmMepCcmDbClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 2, 2),
    _ZyCfmMepCcmDbClear_Type()
)
zyCfmMepCcmDbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmMepCcmDbClear.setStatus("current")
_ZyCfmMepDefectsClear_Type = EnabledStatus
_ZyCfmMepDefectsClear_Object = MibScalar
zyCfmMepDefectsClear = _ZyCfmMepDefectsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 2, 3),
    _ZyCfmMepDefectsClear_Type()
)
zyCfmMepDefectsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmMepDefectsClear.setStatus("current")
_ZyCfmMipCcmDbClear_Type = EnabledStatus
_ZyCfmMipCcmDbClear_Object = MibScalar
zyCfmMipCcmDbClear = _ZyCfmMipCcmDbClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 13, 2, 4),
    _ZyCfmMipCcmDbClear_Type()
)
zyCfmMipCcmDbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyCfmMipCcmDbClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-CFM-MIB",
    **{"zyxelCfm": zyxelCfm,
       "zyxelCfmSetup": zyxelCfmSetup,
       "zyCfmState": zyCfmState,
       "zyxelCfmMibObjects": zyxelCfmMibObjects,
       "zyCfmMgmtIpAddressDomain": zyCfmMgmtIpAddressDomain,
       "zyCfmMgmtIpAddress": zyCfmMgmtIpAddress,
       "zyxelCfmMepTable": zyxelCfmMepTable,
       "zyxelCfmMepEntry": zyxelCfmMepEntry,
       "zyCfmMepTransmitLbmDataTlvSize": zyCfmMepTransmitLbmDataTlvSize,
       "zyxelCfmStatus": zyxelCfmStatus,
       "zyCfmLinkTraceClear": zyCfmLinkTraceClear,
       "zyCfmMepCcmDbClear": zyCfmMepCcmDbClear,
       "zyCfmMepDefectsClear": zyCfmMepDefectsClear,
       "zyCfmMipCcmDbClear": zyCfmMipCcmDbClear}
)
