# SNMP MIB module (EFFICIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EFFICIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:40 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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

_Efficient_ObjectIdentity = ObjectIdentity
efficient = _Efficient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1)
)
_Modem5010_ObjectIdentity = ObjectIdentity
modem5010 = _Modem5010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 5010)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 5010, 1)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 5010, 2)
)
_Atu_R_ObjectIdentity = ObjectIdentity
atu_R = _Atu_R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 5010, 2, 1)
)
_Atu_C_ObjectIdentity = ObjectIdentity
atu_C = _Atu_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 5010, 2, 2)
)
_Modem5621_ObjectIdentity = ObjectIdentity
modem5621 = _Modem5621_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 5621)
)
_Iad8600_ObjectIdentity = ObjectIdentity
iad8600 = _Iad8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 1, 8600)
)
_Mib_extensions_ObjectIdentity = ObjectIdentity
mib_extensions = _Mib_extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2)
)
_MibRouter5660_ObjectIdentity = ObjectIdentity
mibRouter5660 = _MibRouter5660_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 1)
)
_MibIad8600_ObjectIdentity = ObjectIdentity
mibIad8600 = _MibIad8600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2)
)
_Iad8600Info_ObjectIdentity = ObjectIdentity
iad8600Info = _Iad8600Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 1)
)
_Iad8600Voice_ObjectIdentity = ObjectIdentity
iad8600Voice = _Iad8600Voice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 2)
)
_Iad8600Data_ObjectIdentity = ObjectIdentity
iad8600Data = _Iad8600Data_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 3)
)
_Iad8600DataPppAuth_ObjectIdentity = ObjectIdentity
iad8600DataPppAuth = _Iad8600DataPppAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 3, 1)
)
_Iad8600DataPppAuthUsername_Type = DisplayString
_Iad8600DataPppAuthUsername_Object = MibScalar
iad8600DataPppAuthUsername = _Iad8600DataPppAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 3, 1, 1),
    _Iad8600DataPppAuthUsername_Type()
)
iad8600DataPppAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600DataPppAuthUsername.setStatus("mandatory")
_Iad8600DataPppAuthPassword_Type = DisplayString
_Iad8600DataPppAuthPassword_Object = MibScalar
iad8600DataPppAuthPassword = _Iad8600DataPppAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 3, 1, 2),
    _Iad8600DataPppAuthPassword_Type()
)
iad8600DataPppAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600DataPppAuthPassword.setStatus("mandatory")
_Iad8600Wan_ObjectIdentity = ObjectIdentity
iad8600Wan = _Iad8600Wan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 4)
)
_Iad8600System_ObjectIdentity = ObjectIdentity
iad8600System = _Iad8600System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5)
)
_Iad8600SystemCommunity_ObjectIdentity = ObjectIdentity
iad8600SystemCommunity = _Iad8600SystemCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 1)
)
_Iad8600SystemGetCommunityString_Type = DisplayString
_Iad8600SystemGetCommunityString_Object = MibScalar
iad8600SystemGetCommunityString = _Iad8600SystemGetCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 1, 1),
    _Iad8600SystemGetCommunityString_Type()
)
iad8600SystemGetCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600SystemGetCommunityString.setStatus("mandatory")
_Iad8600SystemTrapDest_ObjectIdentity = ObjectIdentity
iad8600SystemTrapDest = _Iad8600SystemTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2)
)


class _Iad8600SystemTrapDestAddr1_Type(IpAddress):
    """Custom type iad8600SystemTrapDestAddr1 based on IpAddress"""
    defaultValue = 0


_Iad8600SystemTrapDestAddr1_Object = MibScalar
iad8600SystemTrapDestAddr1 = _Iad8600SystemTrapDestAddr1_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 1),
    _Iad8600SystemTrapDestAddr1_Type()
)
iad8600SystemTrapDestAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600SystemTrapDestAddr1.setStatus("mandatory")


class _Iad8600SystemTrapDestAddr2_Type(IpAddress):
    """Custom type iad8600SystemTrapDestAddr2 based on IpAddress"""
    defaultValue = 0


_Iad8600SystemTrapDestAddr2_Object = MibScalar
iad8600SystemTrapDestAddr2 = _Iad8600SystemTrapDestAddr2_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 2),
    _Iad8600SystemTrapDestAddr2_Type()
)
iad8600SystemTrapDestAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600SystemTrapDestAddr2.setStatus("mandatory")


class _Iad8600SystemTrapDestAddr3_Type(IpAddress):
    """Custom type iad8600SystemTrapDestAddr3 based on IpAddress"""
    defaultValue = 0


_Iad8600SystemTrapDestAddr3_Object = MibScalar
iad8600SystemTrapDestAddr3 = _Iad8600SystemTrapDestAddr3_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 3),
    _Iad8600SystemTrapDestAddr3_Type()
)
iad8600SystemTrapDestAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600SystemTrapDestAddr3.setStatus("mandatory")


class _Iad8600SystemTrapDestAddr4_Type(IpAddress):
    """Custom type iad8600SystemTrapDestAddr4 based on IpAddress"""
    defaultValue = 0


_Iad8600SystemTrapDestAddr4_Object = MibScalar
iad8600SystemTrapDestAddr4 = _Iad8600SystemTrapDestAddr4_Object(
    (1, 3, 6, 1, 4, 1, 763, 2, 2, 5, 2, 4),
    _Iad8600SystemTrapDestAddr4_Type()
)
iad8600SystemTrapDestAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iad8600SystemTrapDestAddr4.setStatus("mandatory")
_XMIB_ObjectIdentity = ObjectIdentity
xMIB = _XMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3)
)
_Modem_ObjectIdentity = ObjectIdentity
modem = _Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 1)
)
_ModemClearCounters_Type = Integer32
_ModemClearCounters_Object = MibScalar
modemClearCounters = _ModemClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 1),
    _ModemClearCounters_Type()
)
modemClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemClearCounters.setStatus("current")
_ModemPartNumber_Type = DisplayString
_ModemPartNumber_Object = MibScalar
modemPartNumber = _ModemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 2),
    _ModemPartNumber_Type()
)
modemPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemPartNumber.setStatus("current")
_ModemConfigPartNumber_Type = DisplayString
_ModemConfigPartNumber_Object = MibScalar
modemConfigPartNumber = _ModemConfigPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 3),
    _ModemConfigPartNumber_Type()
)
modemConfigPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemConfigPartNumber.setStatus("current")
_ModemBuildNumber_Type = DisplayString
_ModemBuildNumber_Object = MibScalar
modemBuildNumber = _ModemBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 4),
    _ModemBuildNumber_Type()
)
modemBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemBuildNumber.setStatus("current")
_ModemFirmwareVersion1_Type = DisplayString
_ModemFirmwareVersion1_Object = MibScalar
modemFirmwareVersion1 = _ModemFirmwareVersion1_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 5),
    _ModemFirmwareVersion1_Type()
)
modemFirmwareVersion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemFirmwareVersion1.setStatus("current")
_ModemFirmwareVersion2_Type = DisplayString
_ModemFirmwareVersion2_Object = MibScalar
modemFirmwareVersion2 = _ModemFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 6),
    _ModemFirmwareVersion2_Type()
)
modemFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemFirmwareVersion2.setStatus("current")
_ModemFirmwareVersion3_Type = DisplayString
_ModemFirmwareVersion3_Object = MibScalar
modemFirmwareVersion3 = _ModemFirmwareVersion3_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 7),
    _ModemFirmwareVersion3_Type()
)
modemFirmwareVersion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemFirmwareVersion3.setStatus("current")


class _ModemReboot_Type(Integer32):
    """Custom type modemReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 1),
          ("save", 0))
    )


_ModemReboot_Type.__name__ = "Integer32"
_ModemReboot_Object = MibScalar
modemReboot = _ModemReboot_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 8),
    _ModemReboot_Type()
)
modemReboot.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    modemReboot.setStatus("current")


class _ModemIsBridge_Type(Integer32):
    """Custom type modemIsBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("brtr", 3),
          ("rtr", 2))
    )


_ModemIsBridge_Type.__name__ = "Integer32"
_ModemIsBridge_Object = MibScalar
modemIsBridge = _ModemIsBridge_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 9),
    _ModemIsBridge_Type()
)
modemIsBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIsBridge.setStatus("current")


class _ModemNVRAMVersion_Type(OctetString):
    """Custom type modemNVRAMVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ModemNVRAMVersion_Type.__name__ = "OctetString"
_ModemNVRAMVersion_Object = MibScalar
modemNVRAMVersion = _ModemNVRAMVersion_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 10),
    _ModemNVRAMVersion_Type()
)
modemNVRAMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemNVRAMVersion.setStatus("current")
_ModemMacAddress_Type = MacAddress
_ModemMacAddress_Object = MibScalar
modemMacAddress = _ModemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 11),
    _ModemMacAddress_Type()
)
modemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemMacAddress.setStatus("current")
_ModemLANIpAddress_Type = IpAddress
_ModemLANIpAddress_Object = MibScalar
modemLANIpAddress = _ModemLANIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 12),
    _ModemLANIpAddress_Type()
)
modemLANIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemLANIpAddress.setStatus("current")
_ModemLANMask_Type = IpAddress
_ModemLANMask_Object = MibScalar
modemLANMask = _ModemLANMask_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 1, 13),
    _ModemLANMask_Type()
)
modemLANMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemLANMask.setStatus("current")
_Adsl_ObjectIdentity = ObjectIdentity
adsl = _Adsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 2)
)
_AdslTrainedPath_Type = DisplayString
_AdslTrainedPath_Object = MibScalar
adslTrainedPath = _AdslTrainedPath_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 2, 1),
    _AdslTrainedPath_Type()
)
adslTrainedPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslTrainedPath.setStatus("current")
_AdslTrainedMode_Type = DisplayString
_AdslTrainedMode_Object = MibScalar
adslTrainedMode = _AdslTrainedMode_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 2, 2),
    _AdslTrainedMode_Type()
)
adslTrainedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslTrainedMode.setStatus("current")
_Atm_ObjectIdentity = ObjectIdentity
atm = _Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 3)
)
_AtmVcl2_Table_Object = MibTable
atmVcl2_Table = _AtmVcl2_Table_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1)
)
if mibBuilder.loadTexts:
    atmVcl2_Table.setStatus("mandatory")
_AtmVclEntry2_Object = MibTableRow
atmVclEntry2 = _AtmVclEntry2_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1)
)
atmVclEntry2.setIndexNames(
    (0, "EFFICIENT-MIB", "ifIndex"),
    (0, "EFFICIENT-MIB", "ifIndex"),
    (0, "EFFICIENT-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmVclEntry2.setStatus("mandatory")


class _AtmVcl2Vpi_Type(Integer32):
    """Custom type atmVcl2Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmVcl2Vpi_Type.__name__ = "Integer32"
_AtmVcl2Vpi_Object = MibTableColumn
atmVcl2Vpi = _AtmVcl2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 1),
    _AtmVcl2Vpi_Type()
)
atmVcl2Vpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcl2Vpi.setStatus("optional")


class _AtmVcl2Vci_Type(Integer32):
    """Custom type atmVcl2Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmVcl2Vci_Type.__name__ = "Integer32"
_AtmVcl2Vci_Object = MibTableColumn
atmVcl2Vci = _AtmVcl2Vci_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 2),
    _AtmVcl2Vci_Type()
)
atmVcl2Vci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVcl2Vci.setStatus("optional")


class _AtmVcl2Protocol_Type(Integer32):
    """Custom type atmVcl2Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("bridged1483", 1),
          ("none", 0),
          ("pppoallc", 4),
          ("pppoavcmux", 2),
          ("pppoe", 8),
          ("routed1483", 2048))
    )


_AtmVcl2Protocol_Type.__name__ = "Integer32"
_AtmVcl2Protocol_Object = MibTableColumn
atmVcl2Protocol = _AtmVcl2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 3),
    _AtmVcl2Protocol_Type()
)
atmVcl2Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2Protocol.setStatus("current")
_AtmVcl2RxRate_Type = Gauge32
_AtmVcl2RxRate_Object = MibTableColumn
atmVcl2RxRate = _AtmVcl2RxRate_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 4),
    _AtmVcl2RxRate_Type()
)
atmVcl2RxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2RxRate.setStatus("current")
if mibBuilder.loadTexts:
    atmVcl2RxRate.setUnits("bps")
_AtmVcl2TxRate_Type = Gauge32
_AtmVcl2TxRate_Object = MibTableColumn
atmVcl2TxRate = _AtmVcl2TxRate_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 5),
    _AtmVcl2TxRate_Type()
)
atmVcl2TxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2TxRate.setStatus("current")
if mibBuilder.loadTexts:
    atmVcl2TxRate.setUnits("bps")
_AtmVcl2TxPDUs_Type = Gauge32
_AtmVcl2TxPDUs_Object = MibTableColumn
atmVcl2TxPDUs = _AtmVcl2TxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 6),
    _AtmVcl2TxPDUs_Type()
)
atmVcl2TxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2TxPDUs.setStatus("current")
if mibBuilder.loadTexts:
    atmVcl2TxPDUs.setUnits("PDUs")
_AtmVcl2RxPDUs_Type = Gauge32
_AtmVcl2RxPDUs_Object = MibTableColumn
atmVcl2RxPDUs = _AtmVcl2RxPDUs_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 7),
    _AtmVcl2RxPDUs_Type()
)
atmVcl2RxPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2RxPDUs.setStatus("current")
if mibBuilder.loadTexts:
    atmVcl2RxPDUs.setUnits("PDUs")
_AtmVcl2TxErrs_Type = Gauge32
_AtmVcl2TxErrs_Object = MibTableColumn
atmVcl2TxErrs = _AtmVcl2TxErrs_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 8),
    _AtmVcl2TxErrs_Type()
)
atmVcl2TxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2TxErrs.setStatus("current")
if mibBuilder.loadTexts:
    atmVcl2TxErrs.setUnits("PDUs")
_AtmVcl2RxErrs_Type = Gauge32
_AtmVcl2RxErrs_Object = MibTableColumn
atmVcl2RxErrs = _AtmVcl2RxErrs_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 9),
    _AtmVcl2RxErrs_Type()
)
atmVcl2RxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2RxErrs.setStatus("current")
if mibBuilder.loadTexts:
    atmVcl2RxErrs.setUnits("PDUs")
_AtmVcl2PCR_Type = Integer32
_AtmVcl2PCR_Object = MibTableColumn
atmVcl2PCR = _AtmVcl2PCR_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 10),
    _AtmVcl2PCR_Type()
)
atmVcl2PCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmVcl2PCR.setStatus("current")
_AtmVcl2SCR_Type = Integer32
_AtmVcl2SCR_Object = MibTableColumn
atmVcl2SCR = _AtmVcl2SCR_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 11),
    _AtmVcl2SCR_Type()
)
atmVcl2SCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2SCR.setStatus("current")
_AtmVcl2RxSdu_Type = Integer32
_AtmVcl2RxSdu_Object = MibTableColumn
atmVcl2RxSdu = _AtmVcl2RxSdu_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 12),
    _AtmVcl2RxSdu_Type()
)
atmVcl2RxSdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2RxSdu.setStatus("current")
_AtmVcl2TxSdu_Type = Integer32
_AtmVcl2TxSdu_Object = MibTableColumn
atmVcl2TxSdu = _AtmVcl2TxSdu_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 3, 1, 1, 13),
    _AtmVcl2TxSdu_Type()
)
atmVcl2TxSdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcl2TxSdu.setStatus("current")
_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 4)
)
_PppConnect_Type = Integer32
_PppConnect_Object = MibTableColumn
pppConnect = _PppConnect_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 1),
    _PppConnect_Type()
)
pppConnect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pppConnect.setStatus("current")
_PppDisconnect_Type = Integer32
_PppDisconnect_Object = MibScalar
pppDisconnect = _PppDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 2),
    _PppDisconnect_Type()
)
pppDisconnect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pppDisconnect.setStatus("current")
_PppTable_Object = MibTable
pppTable = _PppTable_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3)
)
if mibBuilder.loadTexts:
    pppTable.setStatus("mandatory")
_PppEntry_Object = MibTableRow
pppEntry = _PppEntry_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1)
)
pppEntry.setIndexNames(
    (0, "EFFICIENT-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppEntry.setStatus("mandatory")
_PppLCPState_Type = DisplayString
_PppLCPState_Object = MibTableColumn
pppLCPState = _PppLCPState_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 1),
    _PppLCPState_Type()
)
pppLCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCPState.setStatus("current")
_PppIPCPState_Type = DisplayString
_PppIPCPState_Object = MibTableColumn
pppIPCPState = _PppIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 2),
    _PppIPCPState_Type()
)
pppIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIPCPState.setStatus("current")
_PppAUTHState_Type = DisplayString
_PppAUTHState_Object = MibTableColumn
pppAUTHState = _PppAUTHState_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 3),
    _PppAUTHState_Type()
)
pppAUTHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppAUTHState.setStatus("current")
_PppLCPOldState_Type = DisplayString
_PppLCPOldState_Object = MibTableColumn
pppLCPOldState = _PppLCPOldState_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 4),
    _PppLCPOldState_Type()
)
pppLCPOldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppLCPOldState.setStatus("current")
_PppIPCPOldState_Type = DisplayString
_PppIPCPOldState_Object = MibTableColumn
pppIPCPOldState = _PppIPCPOldState_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 5),
    _PppIPCPOldState_Type()
)
pppIPCPOldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppIPCPOldState.setStatus("current")
_PppAUTHOldState_Type = DisplayString
_PppAUTHOldState_Object = MibTableColumn
pppAUTHOldState = _PppAUTHOldState_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 3, 1, 6),
    _PppAUTHOldState_Type()
)
pppAUTHOldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppAUTHOldState.setStatus("current")
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 4)
)
_PppoeTable_Object = MibTable
pppoeTable = _PppoeTable_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    pppoeTable.setStatus("mandatory")
_PppoeEntry_Object = MibTableRow
pppoeEntry = _PppoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1, 1)
)
pppoeEntry.setIndexNames(
    (0, "EFFICIENT-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppoeEntry.setStatus("mandatory")
_PppoeAccessConcentratorName_Type = DisplayString
_PppoeAccessConcentratorName_Object = MibTableColumn
pppoeAccessConcentratorName = _PppoeAccessConcentratorName_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1, 1, 1),
    _PppoeAccessConcentratorName_Type()
)
pppoeAccessConcentratorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeAccessConcentratorName.setStatus("current")
_PppoeServiceName_Type = DisplayString
_PppoeServiceName_Object = MibTableColumn
pppoeServiceName = _PppoeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 4, 4, 1, 1, 2),
    _PppoeServiceName_Type()
)
pppoeServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeServiceName.setStatus("current")
_Nvram_ObjectIdentity = ObjectIdentity
nvram = _Nvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 5)
)
_Nvsys_ObjectIdentity = ObjectIdentity
nvsys = _Nvsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 1)
)
_Nvatm_ObjectIdentity = ObjectIdentity
nvatm = _Nvatm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2)
)
_NvatmVccTable_Object = MibTable
nvatmVccTable = _NvatmVccTable_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    nvatmVccTable.setStatus("mandatory")
_NvatmVccEntry_Object = MibTableRow
nvatmVccEntry = _NvatmVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1)
)
nvatmVccEntry.setIndexNames(
    (0, "EFFICIENT-MIB", "vccIndex"),
)
if mibBuilder.loadTexts:
    nvatmVccEntry.setStatus("mandatory")


class _VccIndex_Type(Integer32):
    """Custom type vccIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VccIndex_Type.__name__ = "Integer32"
_VccIndex_Object = MibTableColumn
vccIndex = _VccIndex_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 1),
    _VccIndex_Type()
)
vccIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vccIndex.setStatus("current")


class _NvatmVccVpi_Type(Integer32):
    """Custom type nvatmVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NvatmVccVpi_Type.__name__ = "Integer32"
_NvatmVccVpi_Object = MibTableColumn
nvatmVccVpi = _NvatmVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 2),
    _NvatmVccVpi_Type()
)
nvatmVccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvatmVccVpi.setStatus("optional")


class _NvatmVccVci_Type(Integer32):
    """Custom type nvatmVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvatmVccVci_Type.__name__ = "Integer32"
_NvatmVccVci_Object = MibTableColumn
nvatmVccVci = _NvatmVccVci_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 3),
    _NvatmVccVci_Type()
)
nvatmVccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvatmVccVci.setStatus("optional")


class _NvatmVccAalType_Type(Integer32):
    """Custom type nvatmVccAalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NvatmVccAalType_Type.__name__ = "Integer32"
_NvatmVccAalType_Object = MibTableColumn
nvatmVccAalType = _NvatmVccAalType_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 4),
    _NvatmVccAalType_Type()
)
nvatmVccAalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvatmVccAalType.setStatus("current")


class _NvatmVccEncType_Type(Integer32):
    """Custom type nvatmVccEncType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vcm", 2))
    )


_NvatmVccEncType_Type.__name__ = "Integer32"
_NvatmVccEncType_Object = MibTableColumn
nvatmVccEncType = _NvatmVccEncType_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 1, 1, 5),
    _NvatmVccEncType_Type()
)
nvatmVccEncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvatmVccEncType.setStatus("current")
_NvatmVccPoeTable_Object = MibTable
nvatmVccPoeTable = _NvatmVccPoeTable_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    nvatmVccPoeTable.setStatus("mandatory")
_NvatmVccPoeEntry_Object = MibTableRow
nvatmVccPoeEntry = _NvatmVccPoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1)
)
nvatmVccPoeEntry.setIndexNames(
    (0, "EFFICIENT-MIB", "vccIndex"),
    (0, "EFFICIENT-MIB", "poeIndex"),
)
if mibBuilder.loadTexts:
    nvatmVccPoeEntry.setStatus("mandatory")


class _VccIndex2_Type(Integer32):
    """Custom type vccIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VccIndex2_Type.__name__ = "Integer32"
_VccIndex2_Object = MibScalar
vccIndex2 = _VccIndex2_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 1),
    _VccIndex2_Type()
)
vccIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vccIndex2.setStatus("current")


class _PoeIndex_Type(Integer32):
    """Custom type poeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PoeIndex_Type.__name__ = "Integer32"
_PoeIndex_Object = MibTableColumn
poeIndex = _PoeIndex_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 2),
    _PoeIndex_Type()
)
poeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    poeIndex.setStatus("current")
_PppUsrUsername_Type = DisplayString
_PppUsrUsername_Object = MibTableColumn
pppUsrUsername = _PppUsrUsername_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 3),
    _PppUsrUsername_Type()
)
pppUsrUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppUsrUsername.setStatus("current")
_PppUsrPassword_Type = DisplayString
_PppUsrPassword_Object = MibTableColumn
pppUsrPassword = _PppUsrPassword_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 2, 2, 1, 4),
    _PppUsrPassword_Type()
)
pppUsrPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppUsrPassword.setStatus("current")
_Nvwlan_ObjectIdentity = ObjectIdentity
nvwlan = _Nvwlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3)
)
_NvwlanMacAddress_Type = MacAddress
_NvwlanMacAddress_Object = MibScalar
nvwlanMacAddress = _NvwlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 1),
    _NvwlanMacAddress_Type()
)
nvwlanMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanMacAddress.setStatus("current")
_NvwlanChannel_Type = Integer32
_NvwlanChannel_Object = MibScalar
nvwlanChannel = _NvwlanChannel_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 2),
    _NvwlanChannel_Type()
)
nvwlanChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanChannel.setStatus("current")
_NvwlanSsid_Type = OctetString
_NvwlanSsid_Object = MibScalar
nvwlanSsid = _NvwlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 3),
    _NvwlanSsid_Type()
)
nvwlanSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanSsid.setStatus("current")


class _NvwlanSecurity_Type(Integer32):
    """Custom type nvwlanSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("w128", 2),
          ("w64", 1),
          ("wpa", 3))
    )


_NvwlanSecurity_Type.__name__ = "Integer32"
_NvwlanSecurity_Object = MibScalar
nvwlanSecurity = _NvwlanSecurity_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 4),
    _NvwlanSecurity_Type()
)
nvwlanSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanSecurity.setStatus("current")


class _NvwlanKey_Type(Integer32):
    """Custom type nvwlanKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NvwlanKey_Type.__name__ = "Integer32"
_NvwlanKey_Object = MibScalar
nvwlanKey = _NvwlanKey_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 5),
    _NvwlanKey_Type()
)
nvwlanKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanKey.setStatus("current")
_NvwlanK64_1_Type = OctetString
_NvwlanK64_1_Object = MibScalar
nvwlanK64_1 = _NvwlanK64_1_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 6),
    _NvwlanK64_1_Type()
)
nvwlanK64_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanK64_1.setStatus("current")
_NvwlanK64_2_Type = OctetString
_NvwlanK64_2_Object = MibScalar
nvwlanK64_2 = _NvwlanK64_2_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 7),
    _NvwlanK64_2_Type()
)
nvwlanK64_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanK64_2.setStatus("current")
_NvwlanK64_3_Type = OctetString
_NvwlanK64_3_Object = MibScalar
nvwlanK64_3 = _NvwlanK64_3_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 8),
    _NvwlanK64_3_Type()
)
nvwlanK64_3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanK64_3.setStatus("current")
_NvwlanK64_4_Type = OctetString
_NvwlanK64_4_Object = MibScalar
nvwlanK64_4 = _NvwlanK64_4_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 9),
    _NvwlanK64_4_Type()
)
nvwlanK64_4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanK64_4.setStatus("current")
_NvwlanK128_Type = OctetString
_NvwlanK128_Object = MibScalar
nvwlanK128 = _NvwlanK128_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 10),
    _NvwlanK128_Type()
)
nvwlanK128.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanK128.setStatus("current")


class _NvwlanWpaAlgorithm_Type(Integer32):
    """Custom type nvwlanWpaAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkip", 0))
    )


_NvwlanWpaAlgorithm_Type.__name__ = "Integer32"
_NvwlanWpaAlgorithm_Object = MibScalar
nvwlanWpaAlgorithm = _NvwlanWpaAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 11),
    _NvwlanWpaAlgorithm_Type()
)
nvwlanWpaAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanWpaAlgorithm.setStatus("current")
_NvwlanWpaKey_Type = OctetString
_NvwlanWpaKey_Object = MibScalar
nvwlanWpaKey = _NvwlanWpaKey_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 12),
    _NvwlanWpaKey_Type()
)
nvwlanWpaKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanWpaKey.setStatus("current")
_NvwlanWpaRenewal_Type = Integer32
_NvwlanWpaRenewal_Object = MibScalar
nvwlanWpaRenewal = _NvwlanWpaRenewal_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 13),
    _NvwlanWpaRenewal_Type()
)
nvwlanWpaRenewal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanWpaRenewal.setStatus("current")
if mibBuilder.loadTexts:
    nvwlanWpaRenewal.setUnits("seconds")


class _NvwlanRate_Type(Integer32):
    """Custom type nvwlanRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("r1", 11),
          ("r11", 7),
          ("r12", 6),
          ("r18", 5),
          ("r2", 10),
          ("r24", 4),
          ("r36", 3),
          ("r48", 2),
          ("r5", 9),
          ("r54", 1),
          ("r9", 8))
    )


_NvwlanRate_Type.__name__ = "Integer32"
_NvwlanRate_Object = MibScalar
nvwlanRate = _NvwlanRate_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 14),
    _NvwlanRate_Type()
)
nvwlanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanRate.setStatus("current")
_NvwlanRts_Type = Integer32
_NvwlanRts_Object = MibScalar
nvwlanRts = _NvwlanRts_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 15),
    _NvwlanRts_Type()
)
nvwlanRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanRts.setStatus("current")
_NvwlanFragmentation_Type = Integer32
_NvwlanFragmentation_Object = MibScalar
nvwlanFragmentation = _NvwlanFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 16),
    _NvwlanFragmentation_Type()
)
nvwlanFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanFragmentation.setStatus("current")
_NvwlanLocale_Type = Integer32
_NvwlanLocale_Object = MibScalar
nvwlanLocale = _NvwlanLocale_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 17),
    _NvwlanLocale_Type()
)
nvwlanLocale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanLocale.setStatus("current")


class _NvwlanEnableFilters_Type(Integer32):
    """Custom type nvwlanEnableFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NvwlanEnableFilters_Type.__name__ = "Integer32"
_NvwlanEnableFilters_Object = MibScalar
nvwlanEnableFilters = _NvwlanEnableFilters_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 18),
    _NvwlanEnableFilters_Type()
)
nvwlanEnableFilters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanEnableFilters.setStatus("current")


class _NvwlanFilterIsDeny_Type(Integer32):
    """Custom type nvwlanFilterIsDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NvwlanFilterIsDeny_Type.__name__ = "Integer32"
_NvwlanFilterIsDeny_Object = MibScalar
nvwlanFilterIsDeny = _NvwlanFilterIsDeny_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 19),
    _NvwlanFilterIsDeny_Type()
)
nvwlanFilterIsDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanFilterIsDeny.setStatus("current")


class _NvwlanDisableSsidBroadcast_Type(Integer32):
    """Custom type nvwlanDisableSsidBroadcast based on Integer32"""
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


_NvwlanDisableSsidBroadcast_Type.__name__ = "Integer32"
_NvwlanDisableSsidBroadcast_Object = MibScalar
nvwlanDisableSsidBroadcast = _NvwlanDisableSsidBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 20),
    _NvwlanDisableSsidBroadcast_Type()
)
nvwlanDisableSsidBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanDisableSsidBroadcast.setStatus("current")


class _NvwlanDisabled_Type(Integer32):
    """Custom type nvwlanDisabled based on Integer32"""
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


_NvwlanDisabled_Type.__name__ = "Integer32"
_NvwlanDisabled_Object = MibScalar
nvwlanDisabled = _NvwlanDisabled_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 21),
    _NvwlanDisabled_Type()
)
nvwlanDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanDisabled.setStatus("current")


class _NvwlanSharedKeyAuth_Type(Integer32):
    """Custom type nvwlanSharedKeyAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NvwlanSharedKeyAuth_Type.__name__ = "Integer32"
_NvwlanSharedKeyAuth_Object = MibScalar
nvwlanSharedKeyAuth = _NvwlanSharedKeyAuth_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 22),
    _NvwlanSharedKeyAuth_Type()
)
nvwlanSharedKeyAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanSharedKeyAuth.setStatus("current")


class _NvwlanInitialSetup_Type(Integer32):
    """Custom type nvwlanInitialSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NvwlanInitialSetup_Type.__name__ = "Integer32"
_NvwlanInitialSetup_Object = MibScalar
nvwlanInitialSetup = _NvwlanInitialSetup_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 23),
    _NvwlanInitialSetup_Type()
)
nvwlanInitialSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanInitialSetup.setStatus("current")
_NvwlanFiltTable_Object = MibTable
nvwlanFiltTable = _NvwlanFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24)
)
if mibBuilder.loadTexts:
    nvwlanFiltTable.setStatus("mandatory")
_NvwlanFiltEntry_Object = MibTableRow
nvwlanFiltEntry = _NvwlanFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1)
)
nvwlanFiltEntry.setIndexNames(
    (0, "EFFICIENT-MIB", "filtIndex"),
)
if mibBuilder.loadTexts:
    nvwlanFiltEntry.setStatus("mandatory")


class _FiltIndex_Type(Integer32):
    """Custom type filtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_FiltIndex_Type.__name__ = "Integer32"
_FiltIndex_Object = MibTableColumn
filtIndex = _FiltIndex_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1, 1),
    _FiltIndex_Type()
)
filtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filtIndex.setStatus("current")
_NvwlanFiltUsername_Type = DisplayString
_NvwlanFiltUsername_Object = MibTableColumn
nvwlanFiltUsername = _NvwlanFiltUsername_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1, 2),
    _NvwlanFiltUsername_Type()
)
nvwlanFiltUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanFiltUsername.setStatus("current")
_NvwlanFiltMac_Type = MacAddress
_NvwlanFiltMac_Object = MibTableColumn
nvwlanFiltMac = _NvwlanFiltMac_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 3, 24, 1, 3),
    _NvwlanFiltMac_Type()
)
nvwlanFiltMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvwlanFiltMac.setStatus("current")
_Nvsntp_ObjectIdentity = ObjectIdentity
nvsntp = _Nvsntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 4)
)
_NvSntpPrimaryServer_Type = DisplayString
_NvSntpPrimaryServer_Object = MibScalar
nvSntpPrimaryServer = _NvSntpPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 4, 1),
    _NvSntpPrimaryServer_Type()
)
nvSntpPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvSntpPrimaryServer.setStatus("current")
_NvSntpBackupServer_Type = DisplayString
_NvSntpBackupServer_Object = MibScalar
nvSntpBackupServer = _NvSntpBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 4, 2),
    _NvSntpBackupServer_Type()
)
nvSntpBackupServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvSntpBackupServer.setStatus("current")
_NvSntpTimezone_Type = Integer32
_NvSntpTimezone_Object = MibScalar
nvSntpTimezone = _NvSntpTimezone_Object(
    (1, 3, 6, 1, 4, 1, 763, 3, 5, 4, 3),
    _NvSntpTimezone_Type()
)
nvSntpTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvSntpTimezone.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EFFICIENT-MIB",
    **{"efficient": efficient,
       "product": product,
       "modem5010": modem5010,
       "bridge": bridge,
       "router": router,
       "atu-R": atu_R,
       "atu-C": atu_C,
       "modem5621": modem5621,
       "iad8600": iad8600,
       "mib-extensions": mib_extensions,
       "mibRouter5660": mibRouter5660,
       "mibIad8600": mibIad8600,
       "iad8600Info": iad8600Info,
       "iad8600Voice": iad8600Voice,
       "iad8600Data": iad8600Data,
       "iad8600DataPppAuth": iad8600DataPppAuth,
       "iad8600DataPppAuthUsername": iad8600DataPppAuthUsername,
       "iad8600DataPppAuthPassword": iad8600DataPppAuthPassword,
       "iad8600Wan": iad8600Wan,
       "iad8600System": iad8600System,
       "iad8600SystemCommunity": iad8600SystemCommunity,
       "iad8600SystemGetCommunityString": iad8600SystemGetCommunityString,
       "iad8600SystemTrapDest": iad8600SystemTrapDest,
       "iad8600SystemTrapDestAddr1": iad8600SystemTrapDestAddr1,
       "iad8600SystemTrapDestAddr2": iad8600SystemTrapDestAddr2,
       "iad8600SystemTrapDestAddr3": iad8600SystemTrapDestAddr3,
       "iad8600SystemTrapDestAddr4": iad8600SystemTrapDestAddr4,
       "xMIB": xMIB,
       "modem": modem,
       "modemClearCounters": modemClearCounters,
       "modemPartNumber": modemPartNumber,
       "modemConfigPartNumber": modemConfigPartNumber,
       "modemBuildNumber": modemBuildNumber,
       "modemFirmwareVersion1": modemFirmwareVersion1,
       "modemFirmwareVersion2": modemFirmwareVersion2,
       "modemFirmwareVersion3": modemFirmwareVersion3,
       "modemReboot": modemReboot,
       "modemIsBridge": modemIsBridge,
       "modemNVRAMVersion": modemNVRAMVersion,
       "modemMacAddress": modemMacAddress,
       "modemLANIpAddress": modemLANIpAddress,
       "modemLANMask": modemLANMask,
       "adsl": adsl,
       "adslTrainedPath": adslTrainedPath,
       "adslTrainedMode": adslTrainedMode,
       "atm": atm,
       "atmVcl2-Table": atmVcl2_Table,
       "atmVclEntry2": atmVclEntry2,
       "atmVcl2Vpi": atmVcl2Vpi,
       "atmVcl2Vci": atmVcl2Vci,
       "atmVcl2Protocol": atmVcl2Protocol,
       "atmVcl2RxRate": atmVcl2RxRate,
       "atmVcl2TxRate": atmVcl2TxRate,
       "atmVcl2TxPDUs": atmVcl2TxPDUs,
       "atmVcl2RxPDUs": atmVcl2RxPDUs,
       "atmVcl2TxErrs": atmVcl2TxErrs,
       "atmVcl2RxErrs": atmVcl2RxErrs,
       "atmVcl2PCR": atmVcl2PCR,
       "atmVcl2SCR": atmVcl2SCR,
       "atmVcl2RxSdu": atmVcl2RxSdu,
       "atmVcl2TxSdu": atmVcl2TxSdu,
       "ppp": ppp,
       "pppConnect": pppConnect,
       "pppDisconnect": pppDisconnect,
       "pppTable": pppTable,
       "pppEntry": pppEntry,
       "pppLCPState": pppLCPState,
       "pppIPCPState": pppIPCPState,
       "pppAUTHState": pppAUTHState,
       "pppLCPOldState": pppLCPOldState,
       "pppIPCPOldState": pppIPCPOldState,
       "pppAUTHOldState": pppAUTHOldState,
       "pppoe": pppoe,
       "pppoeTable": pppoeTable,
       "pppoeEntry": pppoeEntry,
       "pppoeAccessConcentratorName": pppoeAccessConcentratorName,
       "pppoeServiceName": pppoeServiceName,
       "nvram": nvram,
       "nvsys": nvsys,
       "nvatm": nvatm,
       "nvatmVccTable": nvatmVccTable,
       "nvatmVccEntry": nvatmVccEntry,
       "vccIndex": vccIndex,
       "nvatmVccVpi": nvatmVccVpi,
       "nvatmVccVci": nvatmVccVci,
       "nvatmVccAalType": nvatmVccAalType,
       "nvatmVccEncType": nvatmVccEncType,
       "nvatmVccPoeTable": nvatmVccPoeTable,
       "nvatmVccPoeEntry": nvatmVccPoeEntry,
       "vccIndex2": vccIndex2,
       "poeIndex": poeIndex,
       "pppUsrUsername": pppUsrUsername,
       "pppUsrPassword": pppUsrPassword,
       "nvwlan": nvwlan,
       "nvwlanMacAddress": nvwlanMacAddress,
       "nvwlanChannel": nvwlanChannel,
       "nvwlanSsid": nvwlanSsid,
       "nvwlanSecurity": nvwlanSecurity,
       "nvwlanKey": nvwlanKey,
       "nvwlanK64-1": nvwlanK64_1,
       "nvwlanK64-2": nvwlanK64_2,
       "nvwlanK64-3": nvwlanK64_3,
       "nvwlanK64-4": nvwlanK64_4,
       "nvwlanK128": nvwlanK128,
       "nvwlanWpaAlgorithm": nvwlanWpaAlgorithm,
       "nvwlanWpaKey": nvwlanWpaKey,
       "nvwlanWpaRenewal": nvwlanWpaRenewal,
       "nvwlanRate": nvwlanRate,
       "nvwlanRts": nvwlanRts,
       "nvwlanFragmentation": nvwlanFragmentation,
       "nvwlanLocale": nvwlanLocale,
       "nvwlanEnableFilters": nvwlanEnableFilters,
       "nvwlanFilterIsDeny": nvwlanFilterIsDeny,
       "nvwlanDisableSsidBroadcast": nvwlanDisableSsidBroadcast,
       "nvwlanDisabled": nvwlanDisabled,
       "nvwlanSharedKeyAuth": nvwlanSharedKeyAuth,
       "nvwlanInitialSetup": nvwlanInitialSetup,
       "nvwlanFiltTable": nvwlanFiltTable,
       "nvwlanFiltEntry": nvwlanFiltEntry,
       "filtIndex": filtIndex,
       "nvwlanFiltUsername": nvwlanFiltUsername,
       "nvwlanFiltMac": nvwlanFiltMac,
       "nvsntp": nvsntp,
       "nvSntpPrimaryServer": nvSntpPrimaryServer,
       "nvSntpBackupServer": nvSntpBackupServer,
       "nvSntpTimezone": nvSntpTimezone}
)
