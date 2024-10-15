# SNMP MIB module (CISCO-DLC-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DLC-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:09 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDlcSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SAP(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class SdlcAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDlcSwitchMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDlcSwitchMIBObjects = _CiscoDlcSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1)
)
_FrasBnnSdlc_ObjectIdentity = ObjectIdentity
frasBnnSdlc = _FrasBnnSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1)
)
_FrasBnnSdlcConTable_Object = MibTable
frasBnnSdlcConTable = _FrasBnnSdlcConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1)
)
if mibBuilder.loadTexts:
    frasBnnSdlcConTable.setStatus("current")
_FrasBnnSdlcConEntry_Object = MibTableRow
frasBnnSdlcConEntry = _FrasBnnSdlcConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1)
)
frasBnnSdlcConEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DLC-SWITCH-MIB", "bnnSdlcConAddress"),
)
if mibBuilder.loadTexts:
    frasBnnSdlcConEntry.setStatus("current")
_BnnSdlcConAddress_Type = SdlcAddress
_BnnSdlcConAddress_Object = MibTableColumn
bnnSdlcConAddress = _BnnSdlcConAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 1),
    _BnnSdlcConAddress_Type()
)
bnnSdlcConAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnnSdlcConAddress.setStatus("current")


class _BnnSdlcConState_Type(Integer32):
    """Custom type bnnSdlcConState based on Integer32"""
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
        *(("connrqsent", 4),
          ("connrspsent", 7),
          ("connrspwait", 6),
          ("contacted", 8),
          ("discwait", 9),
          ("reset", 1),
          ("sigstnwait", 5),
          ("testSent", 2),
          ("xidexchg", 3))
    )


_BnnSdlcConState_Type.__name__ = "Integer32"
_BnnSdlcConState_Object = MibTableColumn
bnnSdlcConState = _BnnSdlcConState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 2),
    _BnnSdlcConState_Type()
)
bnnSdlcConState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnSdlcConState.setStatus("current")


class _BnnSdlcConDlci_Type(Integer32):
    """Custom type bnnSdlcConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_BnnSdlcConDlci_Type.__name__ = "Integer32"
_BnnSdlcConDlci_Object = MibTableColumn
bnnSdlcConDlci = _BnnSdlcConDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 3),
    _BnnSdlcConDlci_Type()
)
bnnSdlcConDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnSdlcConDlci.setStatus("current")
_BnnSdlcConFRInterface_Type = InterfaceIndexOrZero
_BnnSdlcConFRInterface_Object = MibTableColumn
bnnSdlcConFRInterface = _BnnSdlcConFRInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 4),
    _BnnSdlcConFRInterface_Type()
)
bnnSdlcConFRInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnSdlcConFRInterface.setStatus("current")
_BnnSdlcConLocalSap_Type = SAP
_BnnSdlcConLocalSap_Object = MibTableColumn
bnnSdlcConLocalSap = _BnnSdlcConLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 5),
    _BnnSdlcConLocalSap_Type()
)
bnnSdlcConLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnSdlcConLocalSap.setStatus("current")
_BnnSdlcConRemoteSap_Type = SAP
_BnnSdlcConRemoteSap_Object = MibTableColumn
bnnSdlcConRemoteSap = _BnnSdlcConRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 6),
    _BnnSdlcConRemoteSap_Type()
)
bnnSdlcConRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnSdlcConRemoteSap.setStatus("current")
_FrasBnnLlc_ObjectIdentity = ObjectIdentity
frasBnnLlc = _FrasBnnLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2)
)
_FrasBnnLlcConTable_Object = MibTable
frasBnnLlcConTable = _FrasBnnLlcConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1)
)
if mibBuilder.loadTexts:
    frasBnnLlcConTable.setStatus("current")
_FrasBnnLlcConEntry_Object = MibTableRow
frasBnnLlcConEntry = _FrasBnnLlcConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1)
)
frasBnnLlcConEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DLC-SWITCH-MIB", "bnnLlcConDeviceMacAddress"),
    (0, "CISCO-DLC-SWITCH-MIB", "bnnLlcConLanLocalSap"),
    (0, "CISCO-DLC-SWITCH-MIB", "bnnLlcConLanRemoteSap"),
)
if mibBuilder.loadTexts:
    frasBnnLlcConEntry.setStatus("current")
_BnnLlcConDeviceMacAddress_Type = MacAddress
_BnnLlcConDeviceMacAddress_Object = MibTableColumn
bnnLlcConDeviceMacAddress = _BnnLlcConDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 1),
    _BnnLlcConDeviceMacAddress_Type()
)
bnnLlcConDeviceMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnnLlcConDeviceMacAddress.setStatus("current")
_BnnLlcConLanLocalSap_Type = SAP
_BnnLlcConLanLocalSap_Object = MibTableColumn
bnnLlcConLanLocalSap = _BnnLlcConLanLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 2),
    _BnnLlcConLanLocalSap_Type()
)
bnnLlcConLanLocalSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnnLlcConLanLocalSap.setStatus("current")
_BnnLlcConLanRemoteSap_Type = SAP
_BnnLlcConLanRemoteSap_Object = MibTableColumn
bnnLlcConLanRemoteSap = _BnnLlcConLanRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 3),
    _BnnLlcConLanRemoteSap_Type()
)
bnnLlcConLanRemoteSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bnnLlcConLanRemoteSap.setStatus("current")
_BnnLlcConLanInterface_Type = InterfaceIndexOrZero
_BnnLlcConLanInterface_Object = MibTableColumn
bnnLlcConLanInterface = _BnnLlcConLanInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 4),
    _BnnLlcConLanInterface_Type()
)
bnnLlcConLanInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnLlcConLanInterface.setStatus("current")


class _BnnLlcConDlci_Type(Integer32):
    """Custom type bnnLlcConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_BnnLlcConDlci_Type.__name__ = "Integer32"
_BnnLlcConDlci_Object = MibTableColumn
bnnLlcConDlci = _BnnLlcConDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 5),
    _BnnLlcConDlci_Type()
)
bnnLlcConDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnLlcConDlci.setStatus("current")


class _BnnLlcConState_Type(Integer32):
    """Custom type bnnLlcConState based on Integer32"""
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
        *(("connrqsent", 4),
          ("connrspsent", 7),
          ("connrspwait", 6),
          ("contacted", 8),
          ("discwait", 9),
          ("reset", 1),
          ("sigstnwait", 5),
          ("testSent", 2),
          ("xidexchg", 3))
    )


_BnnLlcConState_Type.__name__ = "Integer32"
_BnnLlcConState_Object = MibTableColumn
bnnLlcConState = _BnnLlcConState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 6),
    _BnnLlcConState_Type()
)
bnnLlcConState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnLlcConState.setStatus("current")
_BnnLlcConLocalMacAddress_Type = MacAddress
_BnnLlcConLocalMacAddress_Object = MibTableColumn
bnnLlcConLocalMacAddress = _BnnLlcConLocalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 7),
    _BnnLlcConLocalMacAddress_Type()
)
bnnLlcConLocalMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnLlcConLocalMacAddress.setStatus("current")
_BnnLlcConFrLocalSap_Type = SAP
_BnnLlcConFrLocalSap_Object = MibTableColumn
bnnLlcConFrLocalSap = _BnnLlcConFrLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 8),
    _BnnLlcConFrLocalSap_Type()
)
bnnLlcConFrLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnLlcConFrLocalSap.setStatus("current")
_BnnLlcConFrRemoteSap_Type = SAP
_BnnLlcConFrRemoteSap_Object = MibTableColumn
bnnLlcConFrRemoteSap = _BnnLlcConFrRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 9),
    _BnnLlcConFrRemoteSap_Type()
)
bnnLlcConFrRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnnLlcConFrRemoteSap.setStatus("current")
_FrasBanSdlc_ObjectIdentity = ObjectIdentity
frasBanSdlc = _FrasBanSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3)
)
_FrasBanSdlcConTable_Object = MibTable
frasBanSdlcConTable = _FrasBanSdlcConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1)
)
if mibBuilder.loadTexts:
    frasBanSdlcConTable.setStatus("current")
_FrasBanSdlcConEntry_Object = MibTableRow
frasBanSdlcConEntry = _FrasBanSdlcConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1)
)
frasBanSdlcConEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DLC-SWITCH-MIB", "banSdlcConAddress"),
    (0, "CISCO-DLC-SWITCH-MIB", "banSdlcConBanDlciMac"),
)
if mibBuilder.loadTexts:
    frasBanSdlcConEntry.setStatus("current")
_BanSdlcConLocalInterface_Type = InterfaceIndexOrZero
_BanSdlcConLocalInterface_Object = MibTableColumn
banSdlcConLocalInterface = _BanSdlcConLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 1),
    _BanSdlcConLocalInterface_Type()
)
banSdlcConLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConLocalInterface.setStatus("current")
_BanSdlcConAddress_Type = SdlcAddress
_BanSdlcConAddress_Object = MibTableColumn
banSdlcConAddress = _BanSdlcConAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 2),
    _BanSdlcConAddress_Type()
)
banSdlcConAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConAddress.setStatus("current")
_BanSdlcConBanDlciMac_Type = MacAddress
_BanSdlcConBanDlciMac_Object = MibTableColumn
banSdlcConBanDlciMac = _BanSdlcConBanDlciMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 3),
    _BanSdlcConBanDlciMac_Type()
)
banSdlcConBanDlciMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConBanDlciMac.setStatus("current")


class _BanSdlcConDlci_Type(Integer32):
    """Custom type banSdlcConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_BanSdlcConDlci_Type.__name__ = "Integer32"
_BanSdlcConDlci_Object = MibTableColumn
banSdlcConDlci = _BanSdlcConDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 4),
    _BanSdlcConDlci_Type()
)
banSdlcConDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConDlci.setStatus("current")


class _BanSdlcConState_Type(Integer32):
    """Custom type banSdlcConState based on Integer32"""
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
        *(("connrqsent", 4),
          ("connrspsent", 7),
          ("connrspwait", 6),
          ("contacted", 8),
          ("discwait", 9),
          ("reset", 1),
          ("sigstnwait", 5),
          ("testSent", 2),
          ("xidexchg", 3))
    )


_BanSdlcConState_Type.__name__ = "Integer32"
_BanSdlcConState_Object = MibTableColumn
banSdlcConState = _BanSdlcConState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 5),
    _BanSdlcConState_Type()
)
banSdlcConState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConState.setStatus("current")
_BanSdlcConVmac_Type = MacAddress
_BanSdlcConVmac_Object = MibTableColumn
banSdlcConVmac = _BanSdlcConVmac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 6),
    _BanSdlcConVmac_Type()
)
banSdlcConVmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConVmac.setStatus("current")
_BanSdlcConBniAddress_Type = MacAddress
_BanSdlcConBniAddress_Object = MibTableColumn
banSdlcConBniAddress = _BanSdlcConBniAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 7),
    _BanSdlcConBniAddress_Type()
)
banSdlcConBniAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConBniAddress.setStatus("current")
_BanSdlcConFrLocalSap_Type = SAP
_BanSdlcConFrLocalSap_Object = MibTableColumn
banSdlcConFrLocalSap = _BanSdlcConFrLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 8),
    _BanSdlcConFrLocalSap_Type()
)
banSdlcConFrLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConFrLocalSap.setStatus("current")
_BanSdlcConFrRemoteSap_Type = SAP
_BanSdlcConFrRemoteSap_Object = MibTableColumn
banSdlcConFrRemoteSap = _BanSdlcConFrRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 9),
    _BanSdlcConFrRemoteSap_Type()
)
banSdlcConFrRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banSdlcConFrRemoteSap.setStatus("current")
_FrasBanLlc_ObjectIdentity = ObjectIdentity
frasBanLlc = _FrasBanLlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4)
)
_FrasBanLlcConTable_Object = MibTable
frasBanLlcConTable = _FrasBanLlcConTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1)
)
if mibBuilder.loadTexts:
    frasBanLlcConTable.setStatus("current")
_FrasBanLlcConEntry_Object = MibTableRow
frasBanLlcConEntry = _FrasBanLlcConEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1)
)
frasBanLlcConEntry.setIndexNames(
    (0, "CISCO-DLC-SWITCH-MIB", "banLlcEndstnLocalMac"),
    (0, "CISCO-DLC-SWITCH-MIB", "banLlcConLocalSap"),
    (0, "CISCO-DLC-SWITCH-MIB", "banLlcConRemoteSap"),
    (0, "CISCO-DLC-SWITCH-MIB", "banLlcBanDlciMac"),
)
if mibBuilder.loadTexts:
    frasBanLlcConEntry.setStatus("current")
_BanLlcEndstnLocalMac_Type = MacAddress
_BanLlcEndstnLocalMac_Object = MibTableColumn
banLlcEndstnLocalMac = _BanLlcEndstnLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 1),
    _BanLlcEndstnLocalMac_Type()
)
banLlcEndstnLocalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcEndstnLocalMac.setStatus("current")
_BanLlcBanDlciMac_Type = MacAddress
_BanLlcBanDlciMac_Object = MibTableColumn
banLlcBanDlciMac = _BanLlcBanDlciMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 2),
    _BanLlcBanDlciMac_Type()
)
banLlcBanDlciMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcBanDlciMac.setStatus("current")
_BanLlcConLocalSap_Type = SAP
_BanLlcConLocalSap_Object = MibTableColumn
banLlcConLocalSap = _BanLlcConLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 3),
    _BanLlcConLocalSap_Type()
)
banLlcConLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConLocalSap.setStatus("current")
_BanLlcConRemoteSap_Type = SAP
_BanLlcConRemoteSap_Object = MibTableColumn
banLlcConRemoteSap = _BanLlcConRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 4),
    _BanLlcConRemoteSap_Type()
)
banLlcConRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConRemoteSap.setStatus("current")


class _BanLlcConDlci_Type(Integer32):
    """Custom type banLlcConDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_BanLlcConDlci_Type.__name__ = "Integer32"
_BanLlcConDlci_Object = MibTableColumn
banLlcConDlci = _BanLlcConDlci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 5),
    _BanLlcConDlci_Type()
)
banLlcConDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConDlci.setStatus("current")


class _BanLlcConState_Type(Integer32):
    """Custom type banLlcConState based on Integer32"""
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
        *(("connrqsent", 4),
          ("connrspsent", 7),
          ("connrspwait", 6),
          ("contacted", 8),
          ("discwait", 9),
          ("reset", 1),
          ("sigstnwait", 5),
          ("testSent", 2),
          ("xidexchg", 3))
    )


_BanLlcConState_Type.__name__ = "Integer32"
_BanLlcConState_Object = MibTableColumn
banLlcConState = _BanLlcConState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 6),
    _BanLlcConState_Type()
)
banLlcConState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConState.setStatus("current")
_BanLlcConFrInterface_Type = InterfaceIndexOrZero
_BanLlcConFrInterface_Object = MibTableColumn
banLlcConFrInterface = _BanLlcConFrInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 7),
    _BanLlcConFrInterface_Type()
)
banLlcConFrInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConFrInterface.setStatus("current")
_BanLlcBniAddress_Type = MacAddress
_BanLlcBniAddress_Object = MibTableColumn
banLlcBniAddress = _BanLlcBniAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 8),
    _BanLlcBniAddress_Type()
)
banLlcBniAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcBniAddress.setStatus("current")
_BanLlcConFrLocalSap_Type = SAP
_BanLlcConFrLocalSap_Object = MibTableColumn
banLlcConFrLocalSap = _BanLlcConFrLocalSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 9),
    _BanLlcConFrLocalSap_Type()
)
banLlcConFrLocalSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConFrLocalSap.setStatus("current")
_BanLlcConFrRemoteSap_Type = SAP
_BanLlcConFrRemoteSap_Object = MibTableColumn
banLlcConFrRemoteSap = _BanLlcConFrRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 10),
    _BanLlcConFrRemoteSap_Type()
)
banLlcConFrRemoteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    banLlcConFrRemoteSap.setStatus("current")
_CiscoDlcSwitchConformance_ObjectIdentity = ObjectIdentity
ciscoDlcSwitchConformance = _CiscoDlcSwitchConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2)
)
_CiscoDlcSwitchCompliances_ObjectIdentity = ObjectIdentity
ciscoDlcSwitchCompliances = _CiscoDlcSwitchCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 1)
)
_CiscoDlcSwitchGroups_ObjectIdentity = ObjectIdentity
ciscoDlcSwitchGroups = _CiscoDlcSwitchGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2)
)

# Managed Objects groups

frasBnnSdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 1)
)
frasBnnSdlcGroup.setObjects(
      *(("CISCO-DLC-SWITCH-MIB", "bnnSdlcConState"),
        ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConDlci"),
        ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConFRInterface"),
        ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConLocalSap"),
        ("CISCO-DLC-SWITCH-MIB", "bnnSdlcConRemoteSap"))
)
if mibBuilder.loadTexts:
    frasBnnSdlcGroup.setStatus("current")

frasBnnLlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 2)
)
frasBnnLlcGroup.setObjects(
      *(("CISCO-DLC-SWITCH-MIB", "bnnLlcConLanInterface"),
        ("CISCO-DLC-SWITCH-MIB", "bnnLlcConDlci"),
        ("CISCO-DLC-SWITCH-MIB", "bnnLlcConState"),
        ("CISCO-DLC-SWITCH-MIB", "bnnLlcConLocalMacAddress"),
        ("CISCO-DLC-SWITCH-MIB", "bnnLlcConFrLocalSap"),
        ("CISCO-DLC-SWITCH-MIB", "bnnLlcConFrRemoteSap"))
)
if mibBuilder.loadTexts:
    frasBnnLlcGroup.setStatus("current")

frasBanSdlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 3)
)
frasBanSdlcGroup.setObjects(
      *(("CISCO-DLC-SWITCH-MIB", "banSdlcConLocalInterface"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConAddress"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConBanDlciMac"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConDlci"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConState"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConVmac"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConBniAddress"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConFrLocalSap"),
        ("CISCO-DLC-SWITCH-MIB", "banSdlcConFrRemoteSap"))
)
if mibBuilder.loadTexts:
    frasBanSdlcGroup.setStatus("current")

frasBanLlcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 4)
)
frasBanLlcGroup.setObjects(
      *(("CISCO-DLC-SWITCH-MIB", "banLlcEndstnLocalMac"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcBanDlciMac"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConDlci"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConLocalSap"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConRemoteSap"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConState"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConFrInterface"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcBniAddress"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConFrLocalSap"),
        ("CISCO-DLC-SWITCH-MIB", "banLlcConFrRemoteSap"))
)
if mibBuilder.loadTexts:
    frasBanLlcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDlcSwitchCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDlcSwitchCoreCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DLC-SWITCH-MIB",
    **{"SAP": SAP,
       "SdlcAddress": SdlcAddress,
       "ciscoDlcSwitchMIB": ciscoDlcSwitchMIB,
       "ciscoDlcSwitchMIBObjects": ciscoDlcSwitchMIBObjects,
       "frasBnnSdlc": frasBnnSdlc,
       "frasBnnSdlcConTable": frasBnnSdlcConTable,
       "frasBnnSdlcConEntry": frasBnnSdlcConEntry,
       "bnnSdlcConAddress": bnnSdlcConAddress,
       "bnnSdlcConState": bnnSdlcConState,
       "bnnSdlcConDlci": bnnSdlcConDlci,
       "bnnSdlcConFRInterface": bnnSdlcConFRInterface,
       "bnnSdlcConLocalSap": bnnSdlcConLocalSap,
       "bnnSdlcConRemoteSap": bnnSdlcConRemoteSap,
       "frasBnnLlc": frasBnnLlc,
       "frasBnnLlcConTable": frasBnnLlcConTable,
       "frasBnnLlcConEntry": frasBnnLlcConEntry,
       "bnnLlcConDeviceMacAddress": bnnLlcConDeviceMacAddress,
       "bnnLlcConLanLocalSap": bnnLlcConLanLocalSap,
       "bnnLlcConLanRemoteSap": bnnLlcConLanRemoteSap,
       "bnnLlcConLanInterface": bnnLlcConLanInterface,
       "bnnLlcConDlci": bnnLlcConDlci,
       "bnnLlcConState": bnnLlcConState,
       "bnnLlcConLocalMacAddress": bnnLlcConLocalMacAddress,
       "bnnLlcConFrLocalSap": bnnLlcConFrLocalSap,
       "bnnLlcConFrRemoteSap": bnnLlcConFrRemoteSap,
       "frasBanSdlc": frasBanSdlc,
       "frasBanSdlcConTable": frasBanSdlcConTable,
       "frasBanSdlcConEntry": frasBanSdlcConEntry,
       "banSdlcConLocalInterface": banSdlcConLocalInterface,
       "banSdlcConAddress": banSdlcConAddress,
       "banSdlcConBanDlciMac": banSdlcConBanDlciMac,
       "banSdlcConDlci": banSdlcConDlci,
       "banSdlcConState": banSdlcConState,
       "banSdlcConVmac": banSdlcConVmac,
       "banSdlcConBniAddress": banSdlcConBniAddress,
       "banSdlcConFrLocalSap": banSdlcConFrLocalSap,
       "banSdlcConFrRemoteSap": banSdlcConFrRemoteSap,
       "frasBanLlc": frasBanLlc,
       "frasBanLlcConTable": frasBanLlcConTable,
       "frasBanLlcConEntry": frasBanLlcConEntry,
       "banLlcEndstnLocalMac": banLlcEndstnLocalMac,
       "banLlcBanDlciMac": banLlcBanDlciMac,
       "banLlcConLocalSap": banLlcConLocalSap,
       "banLlcConRemoteSap": banLlcConRemoteSap,
       "banLlcConDlci": banLlcConDlci,
       "banLlcConState": banLlcConState,
       "banLlcConFrInterface": banLlcConFrInterface,
       "banLlcBniAddress": banLlcBniAddress,
       "banLlcConFrLocalSap": banLlcConFrLocalSap,
       "banLlcConFrRemoteSap": banLlcConFrRemoteSap,
       "ciscoDlcSwitchConformance": ciscoDlcSwitchConformance,
       "ciscoDlcSwitchCompliances": ciscoDlcSwitchCompliances,
       "ciscoDlcSwitchCoreCompliance": ciscoDlcSwitchCoreCompliance,
       "ciscoDlcSwitchGroups": ciscoDlcSwitchGroups,
       "frasBnnSdlcGroup": frasBnnSdlcGroup,
       "frasBnnLlcGroup": frasBnnLlcGroup,
       "frasBanSdlcGroup": frasBanSdlcGroup,
       "frasBanLlcGroup": frasBanLlcGroup}
)
