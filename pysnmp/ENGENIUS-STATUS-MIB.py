# SNMP MIB module (ENGENIUS-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENGENIUS-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:36 2024
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
 TimeTicks,
 Unsigned32,
 dod,
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
    "dod",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

engeniusstatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 3)
)
engeniusstatus.setRevisions(
        ("1905-11-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Engenius_ObjectIdentity = ObjectIdentity
engenius = _Engenius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125)
)
_WirelessCBStatus_ObjectIdentity = ObjectIdentity
wirelessCBStatus = _WirelessCBStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1)
)
_CbConnectionStatus_Type = OctetString
_CbConnectionStatus_Object = MibScalar
cbConnectionStatus = _CbConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 1),
    _CbConnectionStatus_Type()
)
cbConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbConnectionStatus.setStatus("mandatory")
_CbSignalStrength_Type = OctetString
_CbSignalStrength_Object = MibScalar
cbSignalStrength = _CbSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 2),
    _CbSignalStrength_Type()
)
cbSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbSignalStrength.setStatus("mandatory")
_CbCurrentTxRate_Type = OctetString
_CbCurrentTxRate_Object = MibScalar
cbCurrentTxRate = _CbCurrentTxRate_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 3),
    _CbCurrentTxRate_Type()
)
cbCurrentTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCurrentTxRate.setStatus("mandatory")
_CbCurrentChannel_Type = OctetString
_CbCurrentChannel_Object = MibScalar
cbCurrentChannel = _CbCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 4),
    _CbCurrentChannel_Type()
)
cbCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbCurrentChannel.setStatus("mandatory")
_CbEssid_Type = OctetString
_CbEssid_Object = MibScalar
cbEssid = _CbEssid_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 5),
    _CbEssid_Type()
)
cbEssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEssid.setStatus("mandatory")
_CbTxPower_Type = OctetString
_CbTxPower_Object = MibScalar
cbTxPower = _CbTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 6),
    _CbTxPower_Type()
)
cbTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbTxPower.setStatus("mandatory")
_CbIpAddress_Type = OctetString
_CbIpAddress_Object = MibScalar
cbIpAddress = _CbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 1, 7),
    _CbIpAddress_Type()
)
cbIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbIpAddress.setStatus("mandatory")
_WirelessAPStatus_ObjectIdentity = ObjectIdentity
wirelessAPStatus = _WirelessAPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2)
)
_ApSsidProfile_1_Type = OctetString
_ApSsidProfile_1_Object = MibScalar
apSsidProfile_1 = _ApSsidProfile_1_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 1),
    _ApSsidProfile_1_Type()
)
apSsidProfile_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidProfile_1.setStatus("mandatory")
_ApSsidProfile_2_Type = OctetString
_ApSsidProfile_2_Object = MibScalar
apSsidProfile_2 = _ApSsidProfile_2_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 2),
    _ApSsidProfile_2_Type()
)
apSsidProfile_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidProfile_2.setStatus("mandatory")
_ApSsidProfile_3_Type = OctetString
_ApSsidProfile_3_Object = MibScalar
apSsidProfile_3 = _ApSsidProfile_3_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 3),
    _ApSsidProfile_3_Type()
)
apSsidProfile_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidProfile_3.setStatus("mandatory")
_ApSsidProfile_4_Type = OctetString
_ApSsidProfile_4_Object = MibScalar
apSsidProfile_4 = _ApSsidProfile_4_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 4),
    _ApSsidProfile_4_Type()
)
apSsidProfile_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSsidProfile_4.setStatus("mandatory")
_ApWlanMode_Type = OctetString
_ApWlanMode_Object = MibScalar
apWlanMode = _ApWlanMode_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 5),
    _ApWlanMode_Type()
)
apWlanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanMode.setStatus("mandatory")
_ApCurrentChannel_Type = OctetString
_ApCurrentChannel_Object = MibScalar
apCurrentChannel = _ApCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 6),
    _ApCurrentChannel_Type()
)
apCurrentChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCurrentChannel.setStatus("mandatory")
_ApTxPower_Type = OctetString
_ApTxPower_Object = MibScalar
apTxPower = _ApTxPower_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 7),
    _ApTxPower_Type()
)
apTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTxPower.setStatus("mandatory")
_ApIpAddress_Type = OctetString
_ApIpAddress_Object = MibScalar
apIpAddress = _ApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 2, 8),
    _ApIpAddress_Type()
)
apIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpAddress.setStatus("mandatory")
_IfCBStatus_ObjectIdentity = ObjectIdentity
ifCBStatus = _IfCBStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3)
)
_CbAth0_RxPackets_Type = OctetString
_CbAth0_RxPackets_Object = MibScalar
cbAth0_RxPackets = _CbAth0_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 1),
    _CbAth0_RxPackets_Type()
)
cbAth0_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAth0_RxPackets.setStatus("mandatory")
_CbAth0_RxBytes_Type = OctetString
_CbAth0_RxBytes_Object = MibScalar
cbAth0_RxBytes = _CbAth0_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 2),
    _CbAth0_RxBytes_Type()
)
cbAth0_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAth0_RxBytes.setStatus("mandatory")
_CbAth0_RxErrors_Type = OctetString
_CbAth0_RxErrors_Object = MibScalar
cbAth0_RxErrors = _CbAth0_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 3),
    _CbAth0_RxErrors_Type()
)
cbAth0_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAth0_RxErrors.setStatus("mandatory")
_CbAth0_TxPackets_Type = OctetString
_CbAth0_TxPackets_Object = MibScalar
cbAth0_TxPackets = _CbAth0_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 4),
    _CbAth0_TxPackets_Type()
)
cbAth0_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAth0_TxPackets.setStatus("mandatory")
_CbAth0_TxBytes_Type = OctetString
_CbAth0_TxBytes_Object = MibScalar
cbAth0_TxBytes = _CbAth0_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 5),
    _CbAth0_TxBytes_Type()
)
cbAth0_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAth0_TxBytes.setStatus("mandatory")
_CbAth0_TxErrors_Type = OctetString
_CbAth0_TxErrors_Object = MibScalar
cbAth0_TxErrors = _CbAth0_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 6),
    _CbAth0_TxErrors_Type()
)
cbAth0_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbAth0_TxErrors.setStatus("mandatory")
_CbBr0_RxPackets_Type = OctetString
_CbBr0_RxPackets_Object = MibScalar
cbBr0_RxPackets = _CbBr0_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 7),
    _CbBr0_RxPackets_Type()
)
cbBr0_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbBr0_RxPackets.setStatus("mandatory")
_CbBr0_RxBytes_Type = OctetString
_CbBr0_RxBytes_Object = MibScalar
cbBr0_RxBytes = _CbBr0_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 8),
    _CbBr0_RxBytes_Type()
)
cbBr0_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbBr0_RxBytes.setStatus("mandatory")
_CbBr0_RxErrors_Type = OctetString
_CbBr0_RxErrors_Object = MibScalar
cbBr0_RxErrors = _CbBr0_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 9),
    _CbBr0_RxErrors_Type()
)
cbBr0_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbBr0_RxErrors.setStatus("mandatory")
_CbBr0_TxPackets_Type = OctetString
_CbBr0_TxPackets_Object = MibScalar
cbBr0_TxPackets = _CbBr0_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 10),
    _CbBr0_TxPackets_Type()
)
cbBr0_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbBr0_TxPackets.setStatus("mandatory")
_CbBr0_TxBytes_Type = OctetString
_CbBr0_TxBytes_Object = MibScalar
cbBr0_TxBytes = _CbBr0_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 11),
    _CbBr0_TxBytes_Type()
)
cbBr0_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbBr0_TxBytes.setStatus("mandatory")
_CbBr0_TxErrors_Type = OctetString
_CbBr0_TxErrors_Object = MibScalar
cbBr0_TxErrors = _CbBr0_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 12),
    _CbBr0_TxErrors_Type()
)
cbBr0_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbBr0_TxErrors.setStatus("mandatory")
_CbEth0_RxPackets_Type = OctetString
_CbEth0_RxPackets_Object = MibScalar
cbEth0_RxPackets = _CbEth0_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 13),
    _CbEth0_RxPackets_Type()
)
cbEth0_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEth0_RxPackets.setStatus("mandatory")
_CbEth0_RxBytes_Type = OctetString
_CbEth0_RxBytes_Object = MibScalar
cbEth0_RxBytes = _CbEth0_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 14),
    _CbEth0_RxBytes_Type()
)
cbEth0_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEth0_RxBytes.setStatus("mandatory")
_CbEth0_RxErrors_Type = OctetString
_CbEth0_RxErrors_Object = MibScalar
cbEth0_RxErrors = _CbEth0_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 15),
    _CbEth0_RxErrors_Type()
)
cbEth0_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEth0_RxErrors.setStatus("mandatory")
_CbEth0_TxPackets_Type = OctetString
_CbEth0_TxPackets_Object = MibScalar
cbEth0_TxPackets = _CbEth0_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 16),
    _CbEth0_TxPackets_Type()
)
cbEth0_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEth0_TxPackets.setStatus("mandatory")
_CbEth0_TxBytes_Type = OctetString
_CbEth0_TxBytes_Object = MibScalar
cbEth0_TxBytes = _CbEth0_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 17),
    _CbEth0_TxBytes_Type()
)
cbEth0_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEth0_TxBytes.setStatus("mandatory")
_CbEth0_TxErrors_Type = OctetString
_CbEth0_TxErrors_Object = MibScalar
cbEth0_TxErrors = _CbEth0_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 3, 18),
    _CbEth0_TxErrors_Type()
)
cbEth0_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEth0_TxErrors.setStatus("mandatory")
_IfAPStatus_ObjectIdentity = ObjectIdentity
ifAPStatus = _IfAPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4)
)
_ApAth1_RxPackets_Type = OctetString
_ApAth1_RxPackets_Object = MibScalar
apAth1_RxPackets = _ApAth1_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 1),
    _ApAth1_RxPackets_Type()
)
apAth1_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1_RxPackets.setStatus("mandatory")
_ApAth1_RxBytes_Type = OctetString
_ApAth1_RxBytes_Object = MibScalar
apAth1_RxBytes = _ApAth1_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 2),
    _ApAth1_RxBytes_Type()
)
apAth1_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1_RxBytes.setStatus("mandatory")
_ApAth1_RxErrors_Type = OctetString
_ApAth1_RxErrors_Object = MibScalar
apAth1_RxErrors = _ApAth1_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 3),
    _ApAth1_RxErrors_Type()
)
apAth1_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1_RxErrors.setStatus("mandatory")
_ApAth1_TxPackets_Type = OctetString
_ApAth1_TxPackets_Object = MibScalar
apAth1_TxPackets = _ApAth1_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 4),
    _ApAth1_TxPackets_Type()
)
apAth1_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1_TxPackets.setStatus("mandatory")
_ApAth1_TxBytes_Type = OctetString
_ApAth1_TxBytes_Object = MibScalar
apAth1_TxBytes = _ApAth1_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 5),
    _ApAth1_TxBytes_Type()
)
apAth1_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1_TxBytes.setStatus("mandatory")
_ApAth1_TxErrors_Type = OctetString
_ApAth1_TxErrors_Object = MibScalar
apAth1_TxErrors = _ApAth1_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 6),
    _ApAth1_TxErrors_Type()
)
apAth1_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1_TxErrors.setStatus("mandatory")
_ApAth2_RxPackets_Type = OctetString
_ApAth2_RxPackets_Object = MibScalar
apAth2_RxPackets = _ApAth2_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 7),
    _ApAth2_RxPackets_Type()
)
apAth2_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2_RxPackets.setStatus("mandatory")
_ApAth2_RxBytes_Type = OctetString
_ApAth2_RxBytes_Object = MibScalar
apAth2_RxBytes = _ApAth2_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 8),
    _ApAth2_RxBytes_Type()
)
apAth2_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2_RxBytes.setStatus("mandatory")
_ApAth2_RxErrors_Type = OctetString
_ApAth2_RxErrors_Object = MibScalar
apAth2_RxErrors = _ApAth2_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 9),
    _ApAth2_RxErrors_Type()
)
apAth2_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2_RxErrors.setStatus("mandatory")
_ApAth2_TxPackets_Type = OctetString
_ApAth2_TxPackets_Object = MibScalar
apAth2_TxPackets = _ApAth2_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 10),
    _ApAth2_TxPackets_Type()
)
apAth2_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2_TxPackets.setStatus("mandatory")
_ApAth2_TxBytes_Type = OctetString
_ApAth2_TxBytes_Object = MibScalar
apAth2_TxBytes = _ApAth2_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 11),
    _ApAth2_TxBytes_Type()
)
apAth2_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2_TxBytes.setStatus("mandatory")
_ApAth2_TxErrors_Type = OctetString
_ApAth2_TxErrors_Object = MibScalar
apAth2_TxErrors = _ApAth2_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 12),
    _ApAth2_TxErrors_Type()
)
apAth2_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2_TxErrors.setStatus("mandatory")
_ApAth3_RxPackets_Type = OctetString
_ApAth3_RxPackets_Object = MibScalar
apAth3_RxPackets = _ApAth3_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 13),
    _ApAth3_RxPackets_Type()
)
apAth3_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3_RxPackets.setStatus("mandatory")
_ApAth3_RxBytes_Type = OctetString
_ApAth3_RxBytes_Object = MibScalar
apAth3_RxBytes = _ApAth3_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 14),
    _ApAth3_RxBytes_Type()
)
apAth3_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3_RxBytes.setStatus("mandatory")
_ApAth3_RxErrors_Type = OctetString
_ApAth3_RxErrors_Object = MibScalar
apAth3_RxErrors = _ApAth3_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 15),
    _ApAth3_RxErrors_Type()
)
apAth3_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3_RxErrors.setStatus("mandatory")
_ApAth3_TxPackets_Type = OctetString
_ApAth3_TxPackets_Object = MibScalar
apAth3_TxPackets = _ApAth3_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 16),
    _ApAth3_TxPackets_Type()
)
apAth3_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3_TxPackets.setStatus("mandatory")
_ApAth3_TxBytes_Type = OctetString
_ApAth3_TxBytes_Object = MibScalar
apAth3_TxBytes = _ApAth3_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 17),
    _ApAth3_TxBytes_Type()
)
apAth3_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3_TxBytes.setStatus("mandatory")
_ApAth3_TxErrors_Type = OctetString
_ApAth3_TxErrors_Object = MibScalar
apAth3_TxErrors = _ApAth3_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 18),
    _ApAth3_TxErrors_Type()
)
apAth3_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3_TxErrors.setStatus("mandatory")
_ApAth4_RxPackets_Type = OctetString
_ApAth4_RxPackets_Object = MibScalar
apAth4_RxPackets = _ApAth4_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 19),
    _ApAth4_RxPackets_Type()
)
apAth4_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4_RxPackets.setStatus("mandatory")
_ApAth4_RxBytes_Type = OctetString
_ApAth4_RxBytes_Object = MibScalar
apAth4_RxBytes = _ApAth4_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 20),
    _ApAth4_RxBytes_Type()
)
apAth4_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4_RxBytes.setStatus("mandatory")
_ApAth4_RxErrors_Type = OctetString
_ApAth4_RxErrors_Object = MibScalar
apAth4_RxErrors = _ApAth4_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 21),
    _ApAth4_RxErrors_Type()
)
apAth4_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4_RxErrors.setStatus("mandatory")
_ApAth4_TxPackets_Type = OctetString
_ApAth4_TxPackets_Object = MibScalar
apAth4_TxPackets = _ApAth4_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 22),
    _ApAth4_TxPackets_Type()
)
apAth4_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4_TxPackets.setStatus("mandatory")
_ApAth4_TxBytes_Type = OctetString
_ApAth4_TxBytes_Object = MibScalar
apAth4_TxBytes = _ApAth4_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 23),
    _ApAth4_TxBytes_Type()
)
apAth4_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4_TxBytes.setStatus("mandatory")
_ApAth4_TxErrors_Type = OctetString
_ApAth4_TxErrors_Object = MibScalar
apAth4_TxErrors = _ApAth4_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 24),
    _ApAth4_TxErrors_Type()
)
apAth4_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4_TxErrors.setStatus("mandatory")
_ApAth1V_RxPackets_Type = OctetString
_ApAth1V_RxPackets_Object = MibScalar
apAth1V_RxPackets = _ApAth1V_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 25),
    _ApAth1V_RxPackets_Type()
)
apAth1V_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1V_RxPackets.setStatus("mandatory")
_ApAth1V_RxBytes_Type = OctetString
_ApAth1V_RxBytes_Object = MibScalar
apAth1V_RxBytes = _ApAth1V_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 26),
    _ApAth1V_RxBytes_Type()
)
apAth1V_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1V_RxBytes.setStatus("mandatory")
_ApAth1V_RxErrors_Type = OctetString
_ApAth1V_RxErrors_Object = MibScalar
apAth1V_RxErrors = _ApAth1V_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 27),
    _ApAth1V_RxErrors_Type()
)
apAth1V_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1V_RxErrors.setStatus("mandatory")
_ApAth1V_TxPackets_Type = OctetString
_ApAth1V_TxPackets_Object = MibScalar
apAth1V_TxPackets = _ApAth1V_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 28),
    _ApAth1V_TxPackets_Type()
)
apAth1V_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1V_TxPackets.setStatus("mandatory")
_ApAth1V_TxBytes_Type = OctetString
_ApAth1V_TxBytes_Object = MibScalar
apAth1V_TxBytes = _ApAth1V_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 29),
    _ApAth1V_TxBytes_Type()
)
apAth1V_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1V_TxBytes.setStatus("mandatory")
_ApAth1V_TxErrors_Type = OctetString
_ApAth1V_TxErrors_Object = MibScalar
apAth1V_TxErrors = _ApAth1V_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 30),
    _ApAth1V_TxErrors_Type()
)
apAth1V_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth1V_TxErrors.setStatus("mandatory")
_ApAth2V_RxPackets_Type = OctetString
_ApAth2V_RxPackets_Object = MibScalar
apAth2V_RxPackets = _ApAth2V_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 31),
    _ApAth2V_RxPackets_Type()
)
apAth2V_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2V_RxPackets.setStatus("mandatory")
_ApAth2V_RxBytes_Type = OctetString
_ApAth2V_RxBytes_Object = MibScalar
apAth2V_RxBytes = _ApAth2V_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 32),
    _ApAth2V_RxBytes_Type()
)
apAth2V_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2V_RxBytes.setStatus("mandatory")
_ApAth2V_RxErrors_Type = OctetString
_ApAth2V_RxErrors_Object = MibScalar
apAth2V_RxErrors = _ApAth2V_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 33),
    _ApAth2V_RxErrors_Type()
)
apAth2V_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2V_RxErrors.setStatus("mandatory")
_ApAth2V_TxPackets_Type = OctetString
_ApAth2V_TxPackets_Object = MibScalar
apAth2V_TxPackets = _ApAth2V_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 34),
    _ApAth2V_TxPackets_Type()
)
apAth2V_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2V_TxPackets.setStatus("mandatory")
_ApAth2V_TxBytes_Type = OctetString
_ApAth2V_TxBytes_Object = MibScalar
apAth2V_TxBytes = _ApAth2V_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 35),
    _ApAth2V_TxBytes_Type()
)
apAth2V_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2V_TxBytes.setStatus("mandatory")
_ApAth2V_TxErrors_Type = OctetString
_ApAth2V_TxErrors_Object = MibScalar
apAth2V_TxErrors = _ApAth2V_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 36),
    _ApAth2V_TxErrors_Type()
)
apAth2V_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth2V_TxErrors.setStatus("mandatory")
_ApAth3V_RxPackets_Type = OctetString
_ApAth3V_RxPackets_Object = MibScalar
apAth3V_RxPackets = _ApAth3V_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 37),
    _ApAth3V_RxPackets_Type()
)
apAth3V_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3V_RxPackets.setStatus("mandatory")
_ApAth3V_RxBytes_Type = OctetString
_ApAth3V_RxBytes_Object = MibScalar
apAth3V_RxBytes = _ApAth3V_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 38),
    _ApAth3V_RxBytes_Type()
)
apAth3V_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3V_RxBytes.setStatus("mandatory")
_ApAth3V_RxErrors_Type = OctetString
_ApAth3V_RxErrors_Object = MibScalar
apAth3V_RxErrors = _ApAth3V_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 39),
    _ApAth3V_RxErrors_Type()
)
apAth3V_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3V_RxErrors.setStatus("mandatory")
_ApAth3V_TxPackets_Type = OctetString
_ApAth3V_TxPackets_Object = MibScalar
apAth3V_TxPackets = _ApAth3V_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 40),
    _ApAth3V_TxPackets_Type()
)
apAth3V_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3V_TxPackets.setStatus("mandatory")
_ApAth3V_TxBytes_Type = OctetString
_ApAth3V_TxBytes_Object = MibScalar
apAth3V_TxBytes = _ApAth3V_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 41),
    _ApAth3V_TxBytes_Type()
)
apAth3V_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3V_TxBytes.setStatus("mandatory")
_ApAth3V_TxErrors_Type = OctetString
_ApAth3V_TxErrors_Object = MibScalar
apAth3V_TxErrors = _ApAth3V_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 42),
    _ApAth3V_TxErrors_Type()
)
apAth3V_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth3V_TxErrors.setStatus("mandatory")
_ApAth4V_RxPackets_Type = OctetString
_ApAth4V_RxPackets_Object = MibScalar
apAth4V_RxPackets = _ApAth4V_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 43),
    _ApAth4V_RxPackets_Type()
)
apAth4V_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4V_RxPackets.setStatus("mandatory")
_ApAth4V_RxBytes_Type = OctetString
_ApAth4V_RxBytes_Object = MibScalar
apAth4V_RxBytes = _ApAth4V_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 44),
    _ApAth4V_RxBytes_Type()
)
apAth4V_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4V_RxBytes.setStatus("mandatory")
_ApAth4V_RxErrors_Type = OctetString
_ApAth4V_RxErrors_Object = MibScalar
apAth4V_RxErrors = _ApAth4V_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 45),
    _ApAth4V_RxErrors_Type()
)
apAth4V_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4V_RxErrors.setStatus("mandatory")
_ApAth4V_TxPackets_Type = OctetString
_ApAth4V_TxPackets_Object = MibScalar
apAth4V_TxPackets = _ApAth4V_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 46),
    _ApAth4V_TxPackets_Type()
)
apAth4V_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4V_TxPackets.setStatus("mandatory")
_ApAth4V_TxBytes_Type = OctetString
_ApAth4V_TxBytes_Object = MibScalar
apAth4V_TxBytes = _ApAth4V_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 47),
    _ApAth4V_TxBytes_Type()
)
apAth4V_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4V_TxBytes.setStatus("mandatory")
_ApAth4V_TxErrors_Type = OctetString
_ApAth4V_TxErrors_Object = MibScalar
apAth4V_TxErrors = _ApAth4V_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 48),
    _ApAth4V_TxErrors_Type()
)
apAth4V_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAth4V_TxErrors.setStatus("mandatory")
_ApBr0_RxPackets_Type = OctetString
_ApBr0_RxPackets_Object = MibScalar
apBr0_RxPackets = _ApBr0_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 49),
    _ApBr0_RxPackets_Type()
)
apBr0_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr0_RxPackets.setStatus("mandatory")
_ApBr0_RxBytes_Type = OctetString
_ApBr0_RxBytes_Object = MibScalar
apBr0_RxBytes = _ApBr0_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 50),
    _ApBr0_RxBytes_Type()
)
apBr0_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr0_RxBytes.setStatus("mandatory")
_ApBr0_RxErrors_Type = OctetString
_ApBr0_RxErrors_Object = MibScalar
apBr0_RxErrors = _ApBr0_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 51),
    _ApBr0_RxErrors_Type()
)
apBr0_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr0_RxErrors.setStatus("mandatory")
_ApBr0_TxPackets_Type = OctetString
_ApBr0_TxPackets_Object = MibScalar
apBr0_TxPackets = _ApBr0_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 52),
    _ApBr0_TxPackets_Type()
)
apBr0_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr0_TxPackets.setStatus("mandatory")
_ApBr0_TxBytes_Type = OctetString
_ApBr0_TxBytes_Object = MibScalar
apBr0_TxBytes = _ApBr0_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 53),
    _ApBr0_TxBytes_Type()
)
apBr0_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr0_TxBytes.setStatus("mandatory")
_ApBr0_TxErrors_Type = OctetString
_ApBr0_TxErrors_Object = MibScalar
apBr0_TxErrors = _ApBr0_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 54),
    _ApBr0_TxErrors_Type()
)
apBr0_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr0_TxErrors.setStatus("mandatory")
_ApBr1_RxPackets_Type = OctetString
_ApBr1_RxPackets_Object = MibScalar
apBr1_RxPackets = _ApBr1_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 55),
    _ApBr1_RxPackets_Type()
)
apBr1_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr1_RxPackets.setStatus("mandatory")
_ApBr1_RxBytes_Type = OctetString
_ApBr1_RxBytes_Object = MibScalar
apBr1_RxBytes = _ApBr1_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 56),
    _ApBr1_RxBytes_Type()
)
apBr1_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr1_RxBytes.setStatus("mandatory")
_ApBr1_RxErrors_Type = OctetString
_ApBr1_RxErrors_Object = MibScalar
apBr1_RxErrors = _ApBr1_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 57),
    _ApBr1_RxErrors_Type()
)
apBr1_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr1_RxErrors.setStatus("mandatory")
_ApBr1_TxPackets_Type = OctetString
_ApBr1_TxPackets_Object = MibScalar
apBr1_TxPackets = _ApBr1_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 58),
    _ApBr1_TxPackets_Type()
)
apBr1_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr1_TxPackets.setStatus("mandatory")
_ApBr1_TxBytes_Type = OctetString
_ApBr1_TxBytes_Object = MibScalar
apBr1_TxBytes = _ApBr1_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 59),
    _ApBr1_TxBytes_Type()
)
apBr1_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr1_TxBytes.setStatus("mandatory")
_ApBr1_TxErrors_Type = OctetString
_ApBr1_TxErrors_Object = MibScalar
apBr1_TxErrors = _ApBr1_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 60),
    _ApBr1_TxErrors_Type()
)
apBr1_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr1_TxErrors.setStatus("mandatory")
_ApBr2_RxPackets_Type = OctetString
_ApBr2_RxPackets_Object = MibScalar
apBr2_RxPackets = _ApBr2_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 61),
    _ApBr2_RxPackets_Type()
)
apBr2_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr2_RxPackets.setStatus("mandatory")
_ApBr2_RxBytes_Type = OctetString
_ApBr2_RxBytes_Object = MibScalar
apBr2_RxBytes = _ApBr2_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 62),
    _ApBr2_RxBytes_Type()
)
apBr2_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr2_RxBytes.setStatus("mandatory")
_ApBr2_RxErrors_Type = OctetString
_ApBr2_RxErrors_Object = MibScalar
apBr2_RxErrors = _ApBr2_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 63),
    _ApBr2_RxErrors_Type()
)
apBr2_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr2_RxErrors.setStatus("mandatory")
_ApBr2_TxPackets_Type = OctetString
_ApBr2_TxPackets_Object = MibScalar
apBr2_TxPackets = _ApBr2_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 64),
    _ApBr2_TxPackets_Type()
)
apBr2_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr2_TxPackets.setStatus("mandatory")
_ApBr2_TxBytes_Type = OctetString
_ApBr2_TxBytes_Object = MibScalar
apBr2_TxBytes = _ApBr2_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 65),
    _ApBr2_TxBytes_Type()
)
apBr2_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr2_TxBytes.setStatus("mandatory")
_ApBr2_TxErrors_Type = OctetString
_ApBr2_TxErrors_Object = MibScalar
apBr2_TxErrors = _ApBr2_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 66),
    _ApBr2_TxErrors_Type()
)
apBr2_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr2_TxErrors.setStatus("mandatory")
_ApBr3_RxPackets_Type = OctetString
_ApBr3_RxPackets_Object = MibScalar
apBr3_RxPackets = _ApBr3_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 67),
    _ApBr3_RxPackets_Type()
)
apBr3_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr3_RxPackets.setStatus("mandatory")
_ApBr3_RxBytes_Type = OctetString
_ApBr3_RxBytes_Object = MibScalar
apBr3_RxBytes = _ApBr3_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 68),
    _ApBr3_RxBytes_Type()
)
apBr3_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr3_RxBytes.setStatus("mandatory")
_ApBr3_RxErrors_Type = OctetString
_ApBr3_RxErrors_Object = MibScalar
apBr3_RxErrors = _ApBr3_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 69),
    _ApBr3_RxErrors_Type()
)
apBr3_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr3_RxErrors.setStatus("mandatory")
_ApBr3_TxPackets_Type = OctetString
_ApBr3_TxPackets_Object = MibScalar
apBr3_TxPackets = _ApBr3_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 70),
    _ApBr3_TxPackets_Type()
)
apBr3_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr3_TxPackets.setStatus("mandatory")
_ApBr3_TxBytes_Type = OctetString
_ApBr3_TxBytes_Object = MibScalar
apBr3_TxBytes = _ApBr3_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 71),
    _ApBr3_TxBytes_Type()
)
apBr3_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr3_TxBytes.setStatus("mandatory")
_ApBr3_TxErrors_Type = OctetString
_ApBr3_TxErrors_Object = MibScalar
apBr3_TxErrors = _ApBr3_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 72),
    _ApBr3_TxErrors_Type()
)
apBr3_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr3_TxErrors.setStatus("mandatory")
_ApBr4_RxPackets_Type = OctetString
_ApBr4_RxPackets_Object = MibScalar
apBr4_RxPackets = _ApBr4_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 73),
    _ApBr4_RxPackets_Type()
)
apBr4_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr4_RxPackets.setStatus("mandatory")
_ApBr4_RxBytes_Type = OctetString
_ApBr4_RxBytes_Object = MibScalar
apBr4_RxBytes = _ApBr4_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 74),
    _ApBr4_RxBytes_Type()
)
apBr4_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr4_RxBytes.setStatus("mandatory")
_ApBr4_RxErrors_Type = OctetString
_ApBr4_RxErrors_Object = MibScalar
apBr4_RxErrors = _ApBr4_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 75),
    _ApBr4_RxErrors_Type()
)
apBr4_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr4_RxErrors.setStatus("mandatory")
_ApBr4_TxPackets_Type = OctetString
_ApBr4_TxPackets_Object = MibScalar
apBr4_TxPackets = _ApBr4_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 76),
    _ApBr4_TxPackets_Type()
)
apBr4_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr4_TxPackets.setStatus("mandatory")
_ApBr4_TxBytes_Type = OctetString
_ApBr4_TxBytes_Object = MibScalar
apBr4_TxBytes = _ApBr4_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 77),
    _ApBr4_TxBytes_Type()
)
apBr4_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr4_TxBytes.setStatus("mandatory")
_ApBr4_TxErrors_Type = OctetString
_ApBr4_TxErrors_Object = MibScalar
apBr4_TxErrors = _ApBr4_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 78),
    _ApBr4_TxErrors_Type()
)
apBr4_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBr4_TxErrors.setStatus("mandatory")
_ApEth0_RxPackets_Type = OctetString
_ApEth0_RxPackets_Object = MibScalar
apEth0_RxPackets = _ApEth0_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 79),
    _ApEth0_RxPackets_Type()
)
apEth0_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0_RxPackets.setStatus("mandatory")
_ApEth0_RxBytes_Type = OctetString
_ApEth0_RxBytes_Object = MibScalar
apEth0_RxBytes = _ApEth0_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 80),
    _ApEth0_RxBytes_Type()
)
apEth0_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0_RxBytes.setStatus("mandatory")
_ApEth0_RxErrors_Type = OctetString
_ApEth0_RxErrors_Object = MibScalar
apEth0_RxErrors = _ApEth0_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 81),
    _ApEth0_RxErrors_Type()
)
apEth0_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0_RxErrors.setStatus("mandatory")
_ApEth0_TxPackets_Type = OctetString
_ApEth0_TxPackets_Object = MibScalar
apEth0_TxPackets = _ApEth0_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 82),
    _ApEth0_TxPackets_Type()
)
apEth0_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0_TxPackets.setStatus("mandatory")
_ApEth0_TxBytes_Type = OctetString
_ApEth0_TxBytes_Object = MibScalar
apEth0_TxBytes = _ApEth0_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 83),
    _ApEth0_TxBytes_Type()
)
apEth0_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0_TxBytes.setStatus("mandatory")
_ApEth0_TxErrors_Type = OctetString
_ApEth0_TxErrors_Object = MibScalar
apEth0_TxErrors = _ApEth0_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 84),
    _ApEth0_TxErrors_Type()
)
apEth0_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0_TxErrors.setStatus("mandatory")
_ApEth0V1_RxPackets_Type = OctetString
_ApEth0V1_RxPackets_Object = MibScalar
apEth0V1_RxPackets = _ApEth0V1_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 85),
    _ApEth0V1_RxPackets_Type()
)
apEth0V1_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V1_RxPackets.setStatus("mandatory")
_ApEth0V1_RxBytes_Type = OctetString
_ApEth0V1_RxBytes_Object = MibScalar
apEth0V1_RxBytes = _ApEth0V1_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 86),
    _ApEth0V1_RxBytes_Type()
)
apEth0V1_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V1_RxBytes.setStatus("mandatory")
_ApEth0V1_RxErrors_Type = OctetString
_ApEth0V1_RxErrors_Object = MibScalar
apEth0V1_RxErrors = _ApEth0V1_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 87),
    _ApEth0V1_RxErrors_Type()
)
apEth0V1_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V1_RxErrors.setStatus("mandatory")
_ApEth0V1_TxPackets_Type = OctetString
_ApEth0V1_TxPackets_Object = MibScalar
apEth0V1_TxPackets = _ApEth0V1_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 88),
    _ApEth0V1_TxPackets_Type()
)
apEth0V1_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V1_TxPackets.setStatus("mandatory")
_ApEth0V1_TxBytes_Type = OctetString
_ApEth0V1_TxBytes_Object = MibScalar
apEth0V1_TxBytes = _ApEth0V1_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 89),
    _ApEth0V1_TxBytes_Type()
)
apEth0V1_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V1_TxBytes.setStatus("mandatory")
_ApEth0V1_TxErrors_Type = OctetString
_ApEth0V1_TxErrors_Object = MibScalar
apEth0V1_TxErrors = _ApEth0V1_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 90),
    _ApEth0V1_TxErrors_Type()
)
apEth0V1_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V1_TxErrors.setStatus("mandatory")
_ApEth0V2_RxPackets_Type = OctetString
_ApEth0V2_RxPackets_Object = MibScalar
apEth0V2_RxPackets = _ApEth0V2_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 91),
    _ApEth0V2_RxPackets_Type()
)
apEth0V2_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V2_RxPackets.setStatus("mandatory")
_ApEth0V2_RxBytes_Type = OctetString
_ApEth0V2_RxBytes_Object = MibScalar
apEth0V2_RxBytes = _ApEth0V2_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 92),
    _ApEth0V2_RxBytes_Type()
)
apEth0V2_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V2_RxBytes.setStatus("mandatory")
_ApEth0V2_RxErrors_Type = OctetString
_ApEth0V2_RxErrors_Object = MibScalar
apEth0V2_RxErrors = _ApEth0V2_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 93),
    _ApEth0V2_RxErrors_Type()
)
apEth0V2_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V2_RxErrors.setStatus("mandatory")
_ApEth0V2_TxPackets_Type = OctetString
_ApEth0V2_TxPackets_Object = MibScalar
apEth0V2_TxPackets = _ApEth0V2_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 94),
    _ApEth0V2_TxPackets_Type()
)
apEth0V2_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V2_TxPackets.setStatus("mandatory")
_ApEth0V2_TxBytes_Type = OctetString
_ApEth0V2_TxBytes_Object = MibScalar
apEth0V2_TxBytes = _ApEth0V2_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 95),
    _ApEth0V2_TxBytes_Type()
)
apEth0V2_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V2_TxBytes.setStatus("mandatory")
_ApEth0V2_TxErrors_Type = OctetString
_ApEth0V2_TxErrors_Object = MibScalar
apEth0V2_TxErrors = _ApEth0V2_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 96),
    _ApEth0V2_TxErrors_Type()
)
apEth0V2_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V2_TxErrors.setStatus("mandatory")
_ApEth0V3_RxPackets_Type = OctetString
_ApEth0V3_RxPackets_Object = MibScalar
apEth0V3_RxPackets = _ApEth0V3_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 97),
    _ApEth0V3_RxPackets_Type()
)
apEth0V3_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V3_RxPackets.setStatus("mandatory")
_ApEth0V3_RxBytes_Type = OctetString
_ApEth0V3_RxBytes_Object = MibScalar
apEth0V3_RxBytes = _ApEth0V3_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 98),
    _ApEth0V3_RxBytes_Type()
)
apEth0V3_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V3_RxBytes.setStatus("mandatory")
_ApEth0V3_RxErrors_Type = OctetString
_ApEth0V3_RxErrors_Object = MibScalar
apEth0V3_RxErrors = _ApEth0V3_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 99),
    _ApEth0V3_RxErrors_Type()
)
apEth0V3_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V3_RxErrors.setStatus("mandatory")
_ApEth0V3_TxPackets_Type = OctetString
_ApEth0V3_TxPackets_Object = MibScalar
apEth0V3_TxPackets = _ApEth0V3_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 100),
    _ApEth0V3_TxPackets_Type()
)
apEth0V3_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V3_TxPackets.setStatus("mandatory")
_ApEth0V3_TxBytes_Type = OctetString
_ApEth0V3_TxBytes_Object = MibScalar
apEth0V3_TxBytes = _ApEth0V3_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 101),
    _ApEth0V3_TxBytes_Type()
)
apEth0V3_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V3_TxBytes.setStatus("mandatory")
_ApEth0V3_TxErrors_Type = OctetString
_ApEth0V3_TxErrors_Object = MibScalar
apEth0V3_TxErrors = _ApEth0V3_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 102),
    _ApEth0V3_TxErrors_Type()
)
apEth0V3_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V3_TxErrors.setStatus("mandatory")
_ApEth0V4_RxPackets_Type = OctetString
_ApEth0V4_RxPackets_Object = MibScalar
apEth0V4_RxPackets = _ApEth0V4_RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 103),
    _ApEth0V4_RxPackets_Type()
)
apEth0V4_RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V4_RxPackets.setStatus("mandatory")
_ApEth0V4_RxBytes_Type = OctetString
_ApEth0V4_RxBytes_Object = MibScalar
apEth0V4_RxBytes = _ApEth0V4_RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 104),
    _ApEth0V4_RxBytes_Type()
)
apEth0V4_RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V4_RxBytes.setStatus("mandatory")
_ApEth0V4_RxErrors_Type = OctetString
_ApEth0V4_RxErrors_Object = MibScalar
apEth0V4_RxErrors = _ApEth0V4_RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 105),
    _ApEth0V4_RxErrors_Type()
)
apEth0V4_RxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V4_RxErrors.setStatus("mandatory")
_ApEth0V4_TxPackets_Type = OctetString
_ApEth0V4_TxPackets_Object = MibScalar
apEth0V4_TxPackets = _ApEth0V4_TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 106),
    _ApEth0V4_TxPackets_Type()
)
apEth0V4_TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V4_TxPackets.setStatus("mandatory")
_ApEth0V4_TxBytes_Type = OctetString
_ApEth0V4_TxBytes_Object = MibScalar
apEth0V4_TxBytes = _ApEth0V4_TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 107),
    _ApEth0V4_TxBytes_Type()
)
apEth0V4_TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V4_TxBytes.setStatus("mandatory")
_ApEth0V4_TxErrors_Type = OctetString
_ApEth0V4_TxErrors_Object = MibScalar
apEth0V4_TxErrors = _ApEth0V4_TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 14125, 3, 4, 108),
    _ApEth0V4_TxErrors_Type()
)
apEth0V4_TxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEth0V4_TxErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENGENIUS-STATUS-MIB",
    **{"engenius": engenius,
       "engeniusstatus": engeniusstatus,
       "wirelessCBStatus": wirelessCBStatus,
       "cbConnectionStatus": cbConnectionStatus,
       "cbSignalStrength": cbSignalStrength,
       "cbCurrentTxRate": cbCurrentTxRate,
       "cbCurrentChannel": cbCurrentChannel,
       "cbEssid": cbEssid,
       "cbTxPower": cbTxPower,
       "cbIpAddress": cbIpAddress,
       "wirelessAPStatus": wirelessAPStatus,
       "apSsidProfile_1": apSsidProfile_1,
       "apSsidProfile_2": apSsidProfile_2,
       "apSsidProfile_3": apSsidProfile_3,
       "apSsidProfile_4": apSsidProfile_4,
       "apWlanMode": apWlanMode,
       "apCurrentChannel": apCurrentChannel,
       "apTxPower": apTxPower,
       "apIpAddress": apIpAddress,
       "ifCBStatus": ifCBStatus,
       "cbAth0_RxPackets": cbAth0_RxPackets,
       "cbAth0_RxBytes": cbAth0_RxBytes,
       "cbAth0_RxErrors": cbAth0_RxErrors,
       "cbAth0_TxPackets": cbAth0_TxPackets,
       "cbAth0_TxBytes": cbAth0_TxBytes,
       "cbAth0_TxErrors": cbAth0_TxErrors,
       "cbBr0_RxPackets": cbBr0_RxPackets,
       "cbBr0_RxBytes": cbBr0_RxBytes,
       "cbBr0_RxErrors": cbBr0_RxErrors,
       "cbBr0_TxPackets": cbBr0_TxPackets,
       "cbBr0_TxBytes": cbBr0_TxBytes,
       "cbBr0_TxErrors": cbBr0_TxErrors,
       "cbEth0_RxPackets": cbEth0_RxPackets,
       "cbEth0_RxBytes": cbEth0_RxBytes,
       "cbEth0_RxErrors": cbEth0_RxErrors,
       "cbEth0_TxPackets": cbEth0_TxPackets,
       "cbEth0_TxBytes": cbEth0_TxBytes,
       "cbEth0_TxErrors": cbEth0_TxErrors,
       "ifAPStatus": ifAPStatus,
       "apAth1_RxPackets": apAth1_RxPackets,
       "apAth1_RxBytes": apAth1_RxBytes,
       "apAth1_RxErrors": apAth1_RxErrors,
       "apAth1_TxPackets": apAth1_TxPackets,
       "apAth1_TxBytes": apAth1_TxBytes,
       "apAth1_TxErrors": apAth1_TxErrors,
       "apAth2_RxPackets": apAth2_RxPackets,
       "apAth2_RxBytes": apAth2_RxBytes,
       "apAth2_RxErrors": apAth2_RxErrors,
       "apAth2_TxPackets": apAth2_TxPackets,
       "apAth2_TxBytes": apAth2_TxBytes,
       "apAth2_TxErrors": apAth2_TxErrors,
       "apAth3_RxPackets": apAth3_RxPackets,
       "apAth3_RxBytes": apAth3_RxBytes,
       "apAth3_RxErrors": apAth3_RxErrors,
       "apAth3_TxPackets": apAth3_TxPackets,
       "apAth3_TxBytes": apAth3_TxBytes,
       "apAth3_TxErrors": apAth3_TxErrors,
       "apAth4_RxPackets": apAth4_RxPackets,
       "apAth4_RxBytes": apAth4_RxBytes,
       "apAth4_RxErrors": apAth4_RxErrors,
       "apAth4_TxPackets": apAth4_TxPackets,
       "apAth4_TxBytes": apAth4_TxBytes,
       "apAth4_TxErrors": apAth4_TxErrors,
       "apAth1V_RxPackets": apAth1V_RxPackets,
       "apAth1V_RxBytes": apAth1V_RxBytes,
       "apAth1V_RxErrors": apAth1V_RxErrors,
       "apAth1V_TxPackets": apAth1V_TxPackets,
       "apAth1V_TxBytes": apAth1V_TxBytes,
       "apAth1V_TxErrors": apAth1V_TxErrors,
       "apAth2V_RxPackets": apAth2V_RxPackets,
       "apAth2V_RxBytes": apAth2V_RxBytes,
       "apAth2V_RxErrors": apAth2V_RxErrors,
       "apAth2V_TxPackets": apAth2V_TxPackets,
       "apAth2V_TxBytes": apAth2V_TxBytes,
       "apAth2V_TxErrors": apAth2V_TxErrors,
       "apAth3V_RxPackets": apAth3V_RxPackets,
       "apAth3V_RxBytes": apAth3V_RxBytes,
       "apAth3V_RxErrors": apAth3V_RxErrors,
       "apAth3V_TxPackets": apAth3V_TxPackets,
       "apAth3V_TxBytes": apAth3V_TxBytes,
       "apAth3V_TxErrors": apAth3V_TxErrors,
       "apAth4V_RxPackets": apAth4V_RxPackets,
       "apAth4V_RxBytes": apAth4V_RxBytes,
       "apAth4V_RxErrors": apAth4V_RxErrors,
       "apAth4V_TxPackets": apAth4V_TxPackets,
       "apAth4V_TxBytes": apAth4V_TxBytes,
       "apAth4V_TxErrors": apAth4V_TxErrors,
       "apBr0_RxPackets": apBr0_RxPackets,
       "apBr0_RxBytes": apBr0_RxBytes,
       "apBr0_RxErrors": apBr0_RxErrors,
       "apBr0_TxPackets": apBr0_TxPackets,
       "apBr0_TxBytes": apBr0_TxBytes,
       "apBr0_TxErrors": apBr0_TxErrors,
       "apBr1_RxPackets": apBr1_RxPackets,
       "apBr1_RxBytes": apBr1_RxBytes,
       "apBr1_RxErrors": apBr1_RxErrors,
       "apBr1_TxPackets": apBr1_TxPackets,
       "apBr1_TxBytes": apBr1_TxBytes,
       "apBr1_TxErrors": apBr1_TxErrors,
       "apBr2_RxPackets": apBr2_RxPackets,
       "apBr2_RxBytes": apBr2_RxBytes,
       "apBr2_RxErrors": apBr2_RxErrors,
       "apBr2_TxPackets": apBr2_TxPackets,
       "apBr2_TxBytes": apBr2_TxBytes,
       "apBr2_TxErrors": apBr2_TxErrors,
       "apBr3_RxPackets": apBr3_RxPackets,
       "apBr3_RxBytes": apBr3_RxBytes,
       "apBr3_RxErrors": apBr3_RxErrors,
       "apBr3_TxPackets": apBr3_TxPackets,
       "apBr3_TxBytes": apBr3_TxBytes,
       "apBr3_TxErrors": apBr3_TxErrors,
       "apBr4_RxPackets": apBr4_RxPackets,
       "apBr4_RxBytes": apBr4_RxBytes,
       "apBr4_RxErrors": apBr4_RxErrors,
       "apBr4_TxPackets": apBr4_TxPackets,
       "apBr4_TxBytes": apBr4_TxBytes,
       "apBr4_TxErrors": apBr4_TxErrors,
       "apEth0_RxPackets": apEth0_RxPackets,
       "apEth0_RxBytes": apEth0_RxBytes,
       "apEth0_RxErrors": apEth0_RxErrors,
       "apEth0_TxPackets": apEth0_TxPackets,
       "apEth0_TxBytes": apEth0_TxBytes,
       "apEth0_TxErrors": apEth0_TxErrors,
       "apEth0V1_RxPackets": apEth0V1_RxPackets,
       "apEth0V1_RxBytes": apEth0V1_RxBytes,
       "apEth0V1_RxErrors": apEth0V1_RxErrors,
       "apEth0V1_TxPackets": apEth0V1_TxPackets,
       "apEth0V1_TxBytes": apEth0V1_TxBytes,
       "apEth0V1_TxErrors": apEth0V1_TxErrors,
       "apEth0V2_RxPackets": apEth0V2_RxPackets,
       "apEth0V2_RxBytes": apEth0V2_RxBytes,
       "apEth0V2_RxErrors": apEth0V2_RxErrors,
       "apEth0V2_TxPackets": apEth0V2_TxPackets,
       "apEth0V2_TxBytes": apEth0V2_TxBytes,
       "apEth0V2_TxErrors": apEth0V2_TxErrors,
       "apEth0V3_RxPackets": apEth0V3_RxPackets,
       "apEth0V3_RxBytes": apEth0V3_RxBytes,
       "apEth0V3_RxErrors": apEth0V3_RxErrors,
       "apEth0V3_TxPackets": apEth0V3_TxPackets,
       "apEth0V3_TxBytes": apEth0V3_TxBytes,
       "apEth0V3_TxErrors": apEth0V3_TxErrors,
       "apEth0V4_RxPackets": apEth0V4_RxPackets,
       "apEth0V4_RxBytes": apEth0V4_RxBytes,
       "apEth0V4_RxErrors": apEth0V4_RxErrors,
       "apEth0V4_TxPackets": apEth0V4_TxPackets,
       "apEth0V4_TxBytes": apEth0V4_TxBytes,
       "apEth0V4_TxErrors": apEth0V4_TxErrors}
)
