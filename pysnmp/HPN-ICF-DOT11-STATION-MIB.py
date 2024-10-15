# SNMP MIB module (HPN-ICF-DOT11-STATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-STATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:55 2024
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

(HpnicfDot11AKMType,
 HpnicfDot11AssocFailType,
 HpnicfDot11AuthenType,
 HpnicfDot11AuthorFailType,
 HpnicfDot11ChannelScopeType,
 HpnicfDot11CipherType,
 HpnicfDot11ObjectIDType,
 HpnicfDot11RadioScopeType,
 HpnicfDot11RadioType,
 HpnicfDot11RadioType2,
 HpnicfDot11SSIDEncryptModeType,
 HpnicfDot11SSIDStringType,
 HpnicfDot11SecIEStatusType,
 hpnicfDot11) = mibBuilder.importSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    "HpnicfDot11AKMType",
    "HpnicfDot11AssocFailType",
    "HpnicfDot11AuthenType",
    "HpnicfDot11AuthorFailType",
    "HpnicfDot11ChannelScopeType",
    "HpnicfDot11CipherType",
    "HpnicfDot11ObjectIDType",
    "HpnicfDot11RadioScopeType",
    "HpnicfDot11RadioType",
    "HpnicfDot11RadioType2",
    "HpnicfDot11SSIDEncryptModeType",
    "HpnicfDot11SSIDStringType",
    "HpnicfDot11SecIEStatusType",
    "hpnicfDot11")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfDot11STATION = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3)
)
hpnicfDot11STATION.setRevisions(
        ("2010-09-02 18:00",
         "2010-02-23 18:00",
         "2009-12-01 18:00",
         "2009-08-07 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-11-07 17:30",
         "2008-02-25 18:00",
         "2007-12-21 18:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11StationMtGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11StationMtGroup = _HpnicfDot11StationMtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1)
)
_HpnicfDot11StationAssociateTable_Object = MibTable
hpnicfDot11StationAssociateTable = _HpnicfDot11StationAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAssociateTable.setStatus("current")
_HpnicfDot11StationAssociateEntry_Object = MibTableRow
hpnicfDot11StationAssociateEntry = _HpnicfDot11StationAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1)
)
hpnicfDot11StationAssociateEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAssociateEntry.setStatus("current")
_HpnicfDot11StationMAC_Type = MacAddress
_HpnicfDot11StationMAC_Object = MibTableColumn
hpnicfDot11StationMAC = _HpnicfDot11StationMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 1),
    _HpnicfDot11StationMAC_Type()
)
hpnicfDot11StationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11StationMAC.setStatus("current")
_HpnicfDot11StationIPAddress_Type = IpAddress
_HpnicfDot11StationIPAddress_Object = MibTableColumn
hpnicfDot11StationIPAddress = _HpnicfDot11StationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 2),
    _HpnicfDot11StationIPAddress_Type()
)
hpnicfDot11StationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationIPAddress.setStatus("current")
_HpnicfDot11StationUserName_Type = OctetString
_HpnicfDot11StationUserName_Object = MibTableColumn
hpnicfDot11StationUserName = _HpnicfDot11StationUserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 3),
    _HpnicfDot11StationUserName_Type()
)
hpnicfDot11StationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationUserName.setStatus("current")
_HpnicfDot11StationTxRateSet_Type = OctetString
_HpnicfDot11StationTxRateSet_Object = MibTableColumn
hpnicfDot11StationTxRateSet = _HpnicfDot11StationTxRateSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 4),
    _HpnicfDot11StationTxRateSet_Type()
)
hpnicfDot11StationTxRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxRateSet.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxRateSet.setUnits("Mbps")
_HpnicfDot11StationUpTime_Type = Unsigned32
_HpnicfDot11StationUpTime_Object = MibTableColumn
hpnicfDot11StationUpTime = _HpnicfDot11StationUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 5),
    _HpnicfDot11StationUpTime_Type()
)
hpnicfDot11StationUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationUpTime.setUnits("second")
_HpnicfDot11StationSignalStrength_Type = Integer32
_HpnicfDot11StationSignalStrength_Object = MibTableColumn
hpnicfDot11StationSignalStrength = _HpnicfDot11StationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 6),
    _HpnicfDot11StationSignalStrength_Type()
)
hpnicfDot11StationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationSignalStrength.setUnits("dBm")
_HpnicfDot11StationRSSI_Type = Integer32
_HpnicfDot11StationRSSI_Object = MibTableColumn
hpnicfDot11StationRSSI = _HpnicfDot11StationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 7),
    _HpnicfDot11StationRSSI_Type()
)
hpnicfDot11StationRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRSSI.setStatus("current")
_HpnicfDot11StationChannel_Type = HpnicfDot11ChannelScopeType
_HpnicfDot11StationChannel_Object = MibTableColumn
hpnicfDot11StationChannel = _HpnicfDot11StationChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 8),
    _HpnicfDot11StationChannel_Type()
)
hpnicfDot11StationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationChannel.setStatus("current")


class _HpnicfDot11StationPowerSaveMode_Type(Integer32):
    """Custom type hpnicfDot11StationPowerSaveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_HpnicfDot11StationPowerSaveMode_Type.__name__ = "Integer32"
_HpnicfDot11StationPowerSaveMode_Object = MibTableColumn
hpnicfDot11StationPowerSaveMode = _HpnicfDot11StationPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 9),
    _HpnicfDot11StationPowerSaveMode_Type()
)
hpnicfDot11StationPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationPowerSaveMode.setStatus("current")
_HpnicfDot11StationAid_Type = Integer32
_HpnicfDot11StationAid_Object = MibTableColumn
hpnicfDot11StationAid = _HpnicfDot11StationAid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 10),
    _HpnicfDot11StationAid_Type()
)
hpnicfDot11StationAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAid.setStatus("current")
_HpnicfDot11StationVlanId_Type = Integer32
_HpnicfDot11StationVlanId_Object = MibTableColumn
hpnicfDot11StationVlanId = _HpnicfDot11StationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 11),
    _HpnicfDot11StationVlanId_Type()
)
hpnicfDot11StationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationVlanId.setStatus("current")
_HpnicfDot11StationSSIDName_Type = HpnicfDot11SSIDStringType
_HpnicfDot11StationSSIDName_Object = MibTableColumn
hpnicfDot11StationSSIDName = _HpnicfDot11StationSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 12),
    _HpnicfDot11StationSSIDName_Type()
)
hpnicfDot11StationSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSSIDName.setStatus("current")
_HpnicfDot11StationAuthenMode_Type = HpnicfDot11AuthenType
_HpnicfDot11StationAuthenMode_Object = MibTableColumn
hpnicfDot11StationAuthenMode = _HpnicfDot11StationAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 13),
    _HpnicfDot11StationAuthenMode_Type()
)
hpnicfDot11StationAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthenMode.setStatus("current")
_HpnicfDot11StationAKMMode_Type = HpnicfDot11AKMType
_HpnicfDot11StationAKMMode_Object = MibTableColumn
hpnicfDot11StationAKMMode = _HpnicfDot11StationAKMMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 14),
    _HpnicfDot11StationAKMMode_Type()
)
hpnicfDot11StationAKMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAKMMode.setStatus("current")
_HpnicfDot11StationSecurityCiphers_Type = HpnicfDot11CipherType
_HpnicfDot11StationSecurityCiphers_Object = MibTableColumn
hpnicfDot11StationSecurityCiphers = _HpnicfDot11StationSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 15),
    _HpnicfDot11StationSecurityCiphers_Type()
)
hpnicfDot11StationSecurityCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSecurityCiphers.setStatus("current")


class _HpnicfDot11StationSSIDEncryptMode_Type(HpnicfDot11SSIDEncryptModeType):
    """Custom type hpnicfDot11StationSSIDEncryptMode based on HpnicfDot11SSIDEncryptModeType"""


_HpnicfDot11StationSSIDEncryptMode_Object = MibTableColumn
hpnicfDot11StationSSIDEncryptMode = _HpnicfDot11StationSSIDEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 16),
    _HpnicfDot11StationSSIDEncryptMode_Type()
)
hpnicfDot11StationSSIDEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSSIDEncryptMode.setStatus("current")
_HpnicfDot11StationRxSNR_Type = Integer32
_HpnicfDot11StationRxSNR_Object = MibTableColumn
hpnicfDot11StationRxSNR = _HpnicfDot11StationRxSNR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 17),
    _HpnicfDot11StationRxSNR_Type()
)
hpnicfDot11StationRxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxSNR.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxSNR.setUnits("One Percent")
_HpnicfDot11StationTxRate_Type = Integer32
_HpnicfDot11StationTxRate_Object = MibTableColumn
hpnicfDot11StationTxRate = _HpnicfDot11StationTxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 18),
    _HpnicfDot11StationTxRate_Type()
)
hpnicfDot11StationTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxRate.setUnits("Mbps")
_HpnicfDot11StationRxRate_Type = Integer32
_HpnicfDot11StationRxRate_Object = MibTableColumn
hpnicfDot11StationRxRate = _HpnicfDot11StationRxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 19),
    _HpnicfDot11StationRxRate_Type()
)
hpnicfDot11StationRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxRate.setUnits("Mbps")


class _HpnicfDot11StationVendorName_Type(OctetString):
    """Custom type hpnicfDot11StationVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfDot11StationVendorName_Type.__name__ = "OctetString"
_HpnicfDot11StationVendorName_Object = MibTableColumn
hpnicfDot11StationVendorName = _HpnicfDot11StationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 20),
    _HpnicfDot11StationVendorName_Type()
)
hpnicfDot11StationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationVendorName.setStatus("current")
_HpnicfDot11StationRadioMode_Type = HpnicfDot11RadioType
_HpnicfDot11StationRadioMode_Object = MibTableColumn
hpnicfDot11StationRadioMode = _HpnicfDot11StationRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 21),
    _HpnicfDot11StationRadioMode_Type()
)
hpnicfDot11StationRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRadioMode.setStatus("current")
_HpnicfDot11StationRxNoise_Type = Integer32
_HpnicfDot11StationRxNoise_Object = MibTableColumn
hpnicfDot11StationRxNoise = _HpnicfDot11StationRxNoise_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 22),
    _HpnicfDot11StationRxNoise_Type()
)
hpnicfDot11StationRxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxNoise.setStatus("current")
_HpnicfDot11StationMACAddress_Type = MacAddress
_HpnicfDot11StationMACAddress_Object = MibTableColumn
hpnicfDot11StationMACAddress = _HpnicfDot11StationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 23),
    _HpnicfDot11StationMACAddress_Type()
)
hpnicfDot11StationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationMACAddress.setStatus("current")
_HpnicfDot11StationTxSpeed_Type = Integer32
_HpnicfDot11StationTxSpeed_Object = MibTableColumn
hpnicfDot11StationTxSpeed = _HpnicfDot11StationTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 24),
    _HpnicfDot11StationTxSpeed_Type()
)
hpnicfDot11StationTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxSpeed.setUnits("byte/s")
_HpnicfDot11StationRxSpeed_Type = Integer32
_HpnicfDot11StationRxSpeed_Object = MibTableColumn
hpnicfDot11StationRxSpeed = _HpnicfDot11StationRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 25),
    _HpnicfDot11StationRxSpeed_Type()
)
hpnicfDot11StationRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxSpeed.setUnits("byte/s")


class _HpnicfDot11StationWmmMode_Type(Integer32):
    """Custom type hpnicfDot11StationWmmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonwmm", 2),
          ("wmm", 1))
    )


_HpnicfDot11StationWmmMode_Type.__name__ = "Integer32"
_HpnicfDot11StationWmmMode_Object = MibTableColumn
hpnicfDot11StationWmmMode = _HpnicfDot11StationWmmMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 26),
    _HpnicfDot11StationWmmMode_Type()
)
hpnicfDot11StationWmmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationWmmMode.setStatus("current")
_HpnicfDot11StationSecIEStatus_Type = HpnicfDot11SecIEStatusType
_HpnicfDot11StationSecIEStatus_Object = MibTableColumn
hpnicfDot11StationSecIEStatus = _HpnicfDot11StationSecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 27),
    _HpnicfDot11StationSecIEStatus_Type()
)
hpnicfDot11StationSecIEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSecIEStatus.setStatus("current")
_HpnicfDot11StationUpTimeTicks_Type = TimeTicks
_HpnicfDot11StationUpTimeTicks_Object = MibTableColumn
hpnicfDot11StationUpTimeTicks = _HpnicfDot11StationUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 28),
    _HpnicfDot11StationUpTimeTicks_Type()
)
hpnicfDot11StationUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationUpTimeTicks.setStatus("current")
_HpnicfDot11StationRadioMode2_Type = HpnicfDot11RadioType2
_HpnicfDot11StationRadioMode2_Object = MibTableColumn
hpnicfDot11StationRadioMode2 = _HpnicfDot11StationRadioMode2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 29),
    _HpnicfDot11StationRadioMode2_Type()
)
hpnicfDot11StationRadioMode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRadioMode2.setStatus("current")
_HpnicfDot11StationAssTime_Type = DateAndTime
_HpnicfDot11StationAssTime_Object = MibTableColumn
hpnicfDot11StationAssTime = _HpnicfDot11StationAssTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 30),
    _HpnicfDot11StationAssTime_Type()
)
hpnicfDot11StationAssTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAssTime.setStatus("current")


class _HpnicfDot11StationUserAuthType_Type(Integer32):
    """Custom type hpnicfDot11StationUserAuthType based on Integer32"""
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
        *(("associateAuth", 3),
          ("authFree", 2),
          ("macAuth", 4),
          ("portalAuth", 1))
    )


_HpnicfDot11StationUserAuthType_Type.__name__ = "Integer32"
_HpnicfDot11StationUserAuthType_Object = MibTableColumn
hpnicfDot11StationUserAuthType = _HpnicfDot11StationUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 31),
    _HpnicfDot11StationUserAuthType_Type()
)
hpnicfDot11StationUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationUserAuthType.setStatus("current")
_HpnicfDot11StationRfPingTest_Type = TruthValue
_HpnicfDot11StationRfPingTest_Object = MibTableColumn
hpnicfDot11StationRfPingTest = _HpnicfDot11StationRfPingTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 32),
    _HpnicfDot11StationRfPingTest_Type()
)
hpnicfDot11StationRfPingTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingTest.setStatus("current")
_HpnicfDot11StationMaxRate_Type = Integer32
_HpnicfDot11StationMaxRate_Object = MibTableColumn
hpnicfDot11StationMaxRate = _HpnicfDot11StationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 33),
    _HpnicfDot11StationMaxRate_Type()
)
hpnicfDot11StationMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationMaxRate.setUnits("Mbps")


class _HpnicfDot11StationPowerSaveModeCM_Type(Integer32):
    """Custom type hpnicfDot11StationPowerSaveModeCM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("powersave", 1))
    )


_HpnicfDot11StationPowerSaveModeCM_Type.__name__ = "Integer32"
_HpnicfDot11StationPowerSaveModeCM_Object = MibTableColumn
hpnicfDot11StationPowerSaveModeCM = _HpnicfDot11StationPowerSaveModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 34),
    _HpnicfDot11StationPowerSaveModeCM_Type()
)
hpnicfDot11StationPowerSaveModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationPowerSaveModeCM.setStatus("current")


class _HpnicfDot11StationAuthenModeCM_Type(Integer32):
    """Custom type hpnicfDot11StationAuthenModeCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_HpnicfDot11StationAuthenModeCM_Type.__name__ = "Integer32"
_HpnicfDot11StationAuthenModeCM_Object = MibTableColumn
hpnicfDot11StationAuthenModeCM = _HpnicfDot11StationAuthenModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 35),
    _HpnicfDot11StationAuthenModeCM_Type()
)
hpnicfDot11StationAuthenModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthenModeCM.setStatus("current")


class _HpnicfDot11StationAKMModeCM_Type(Integer32):
    """Custom type hpnicfDot11StationAKMModeCM based on Integer32"""
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
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wlanex", 3))
    )


_HpnicfDot11StationAKMModeCM_Type.__name__ = "Integer32"
_HpnicfDot11StationAKMModeCM_Object = MibTableColumn
hpnicfDot11StationAKMModeCM = _HpnicfDot11StationAKMModeCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 36),
    _HpnicfDot11StationAKMModeCM_Type()
)
hpnicfDot11StationAKMModeCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationAKMModeCM.setStatus("current")


class _HpnicfDot11StationSecurityCiphersCM_Type(Integer32):
    """Custom type hpnicfDot11StationSecurityCiphersCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aesccmp", 4),
          ("none", 0),
          ("tkip", 3),
          ("wep104", 2),
          ("wep40", 1),
          ("wpisms4", 5))
    )


_HpnicfDot11StationSecurityCiphersCM_Type.__name__ = "Integer32"
_HpnicfDot11StationSecurityCiphersCM_Object = MibTableColumn
hpnicfDot11StationSecurityCiphersCM = _HpnicfDot11StationSecurityCiphersCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 37),
    _HpnicfDot11StationSecurityCiphersCM_Type()
)
hpnicfDot11StationSecurityCiphersCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSecurityCiphersCM.setStatus("current")


class _HpnicfDot11StationSecIEStatusCM_Type(Integer32):
    """Custom type hpnicfDot11StationSecIEStatusCM based on Integer32"""
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
        *(("none", 0),
          ("wlanex", 3),
          ("wpa", 1),
          ("wpa2", 2))
    )


_HpnicfDot11StationSecIEStatusCM_Type.__name__ = "Integer32"
_HpnicfDot11StationSecIEStatusCM_Object = MibTableColumn
hpnicfDot11StationSecIEStatusCM = _HpnicfDot11StationSecIEStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 1, 1, 38),
    _HpnicfDot11StationSecIEStatusCM_Type()
)
hpnicfDot11StationSecIEStatusCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSecIEStatusCM.setStatus("current")
_HpnicfDot11StationAPRelationTable_Object = MibTable
hpnicfDot11StationAPRelationTable = _HpnicfDot11StationAPRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAPRelationTable.setStatus("current")
_HpnicfDot11StationAPRelationEntry_Object = MibTableRow
hpnicfDot11StationAPRelationEntry = _HpnicfDot11StationAPRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 2, 1)
)
hpnicfDot11StationAPRelationEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAPRelationEntry.setStatus("current")
_HpnicfDot11CurrAPID_Type = HpnicfDot11ObjectIDType
_HpnicfDot11CurrAPID_Object = MibTableColumn
hpnicfDot11CurrAPID = _HpnicfDot11CurrAPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 2, 1, 1),
    _HpnicfDot11CurrAPID_Type()
)
hpnicfDot11CurrAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAPID.setStatus("current")
_HpnicfDot11CurrRadioID_Type = HpnicfDot11RadioScopeType
_HpnicfDot11CurrRadioID_Object = MibTableColumn
hpnicfDot11CurrRadioID = _HpnicfDot11CurrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 2, 1, 2),
    _HpnicfDot11CurrRadioID_Type()
)
hpnicfDot11CurrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrRadioID.setStatus("current")
_HpnicfDot11CurrWlanID_Type = Integer32
_HpnicfDot11CurrWlanID_Object = MibTableColumn
hpnicfDot11CurrWlanID = _HpnicfDot11CurrWlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 2, 1, 3),
    _HpnicfDot11CurrWlanID_Type()
)
hpnicfDot11CurrWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrWlanID.setStatus("current")
_HpnicfDot11CurrAntennaID_Type = Integer32
_HpnicfDot11CurrAntennaID_Object = MibTableColumn
hpnicfDot11CurrAntennaID = _HpnicfDot11CurrAntennaID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 2, 1, 4),
    _HpnicfDot11CurrAntennaID_Type()
)
hpnicfDot11CurrAntennaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11CurrAntennaID.setStatus("current")
_HpnicfDot11StationStatisTable_Object = MibTable
hpnicfDot11StationStatisTable = _HpnicfDot11StationStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDot11StationStatisTable.setStatus("current")
_HpnicfDot11StationStatisEntry_Object = MibTableRow
hpnicfDot11StationStatisEntry = _HpnicfDot11StationStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1)
)
hpnicfDot11StationStatisEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StationStatisEntry.setStatus("current")
_HpnicfDot11StationRxFrameCnt_Type = Counter32
_HpnicfDot11StationRxFrameCnt_Object = MibTableColumn
hpnicfDot11StationRxFrameCnt = _HpnicfDot11StationRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 1),
    _HpnicfDot11StationRxFrameCnt_Type()
)
hpnicfDot11StationRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxFrameCnt.setStatus("current")
_HpnicfDot11StationTxFrameCnt_Type = Counter32
_HpnicfDot11StationTxFrameCnt_Object = MibTableColumn
hpnicfDot11StationTxFrameCnt = _HpnicfDot11StationTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 2),
    _HpnicfDot11StationTxFrameCnt_Type()
)
hpnicfDot11StationTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxFrameCnt.setStatus("current")
_HpnicfDot11StationDropFrameCnt_Type = Counter32
_HpnicfDot11StationDropFrameCnt_Object = MibTableColumn
hpnicfDot11StationDropFrameCnt = _HpnicfDot11StationDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 3),
    _HpnicfDot11StationDropFrameCnt_Type()
)
hpnicfDot11StationDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationDropFrameCnt.setStatus("current")
_HpnicfDot11StationRxFrameBytes_Type = Counter64
_HpnicfDot11StationRxFrameBytes_Object = MibTableColumn
hpnicfDot11StationRxFrameBytes = _HpnicfDot11StationRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 4),
    _HpnicfDot11StationRxFrameBytes_Type()
)
hpnicfDot11StationRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxFrameBytes.setUnits("bytes")
_HpnicfDot11StationTxFrameBytes_Type = Counter64
_HpnicfDot11StationTxFrameBytes_Object = MibTableColumn
hpnicfDot11StationTxFrameBytes = _HpnicfDot11StationTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 5),
    _HpnicfDot11StationTxFrameBytes_Type()
)
hpnicfDot11StationTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxFrameBytes.setUnits("bytes")
_HpnicfDot11StationDropFrameBytes_Type = Counter64
_HpnicfDot11StationDropFrameBytes_Object = MibTableColumn
hpnicfDot11StationDropFrameBytes = _HpnicfDot11StationDropFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 6),
    _HpnicfDot11StationDropFrameBytes_Type()
)
hpnicfDot11StationDropFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationDropFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationDropFrameBytes.setUnits("bytes")
_HpnicfDot11StationRxRetryPkts_Type = Counter32
_HpnicfDot11StationRxRetryPkts_Object = MibTableColumn
hpnicfDot11StationRxRetryPkts = _HpnicfDot11StationRxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 7),
    _HpnicfDot11StationRxRetryPkts_Type()
)
hpnicfDot11StationRxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxRetryPkts.setStatus("current")
_HpnicfDot11StationTxRetryPkts_Type = Counter32
_HpnicfDot11StationTxRetryPkts_Object = MibTableColumn
hpnicfDot11StationTxRetryPkts = _HpnicfDot11StationTxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 8),
    _HpnicfDot11StationTxRetryPkts_Type()
)
hpnicfDot11StationTxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxRetryPkts.setStatus("current")
_HpnicfDot11StationRxRetryBytes_Type = Counter64
_HpnicfDot11StationRxRetryBytes_Object = MibTableColumn
hpnicfDot11StationRxRetryBytes = _HpnicfDot11StationRxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 9),
    _HpnicfDot11StationRxRetryBytes_Type()
)
hpnicfDot11StationRxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxRetryBytes.setStatus("current")
_HpnicfDot11StationTxRetryBytes_Type = Counter64
_HpnicfDot11StationTxRetryBytes_Object = MibTableColumn
hpnicfDot11StationTxRetryBytes = _HpnicfDot11StationTxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 10),
    _HpnicfDot11StationTxRetryBytes_Type()
)
hpnicfDot11StationTxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxRetryBytes.setStatus("current")
_HpnicfDot11StationThroughput_Type = Counter64
_HpnicfDot11StationThroughput_Object = MibTableColumn
hpnicfDot11StationThroughput = _HpnicfDot11StationThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 11),
    _HpnicfDot11StationThroughput_Type()
)
hpnicfDot11StationThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationThroughput.setUnits("bytes")
_HpnicfDot11StationSuccessTxCnt_Type = Counter32
_HpnicfDot11StationSuccessTxCnt_Object = MibTableColumn
hpnicfDot11StationSuccessTxCnt = _HpnicfDot11StationSuccessTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 12),
    _HpnicfDot11StationSuccessTxCnt_Type()
)
hpnicfDot11StationSuccessTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSuccessTxCnt.setStatus("current")
_HpnicfDot11StationSuccessTxDataCnt_Type = Counter32
_HpnicfDot11StationSuccessTxDataCnt_Object = MibTableColumn
hpnicfDot11StationSuccessTxDataCnt = _HpnicfDot11StationSuccessTxDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 13),
    _HpnicfDot11StationSuccessTxDataCnt_Type()
)
hpnicfDot11StationSuccessTxDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationSuccessTxDataCnt.setStatus("current")
_HpnicfDot11StationRxDataFrameCnt_Type = Counter32
_HpnicfDot11StationRxDataFrameCnt_Object = MibTableColumn
hpnicfDot11StationRxDataFrameCnt = _HpnicfDot11StationRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 14),
    _HpnicfDot11StationRxDataFrameCnt_Type()
)
hpnicfDot11StationRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxDataFrameCnt.setStatus("current")
_HpnicfDot11StationTxDataFrameCnt_Type = Counter32
_HpnicfDot11StationTxDataFrameCnt_Object = MibTableColumn
hpnicfDot11StationTxDataFrameCnt = _HpnicfDot11StationTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 15),
    _HpnicfDot11StationTxDataFrameCnt_Type()
)
hpnicfDot11StationTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxDataFrameCnt.setStatus("current")
_HpnicfDot11StationRxDataFrameBytes_Type = Counter64
_HpnicfDot11StationRxDataFrameBytes_Object = MibTableColumn
hpnicfDot11StationRxDataFrameBytes = _HpnicfDot11StationRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 16),
    _HpnicfDot11StationRxDataFrameBytes_Type()
)
hpnicfDot11StationRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxDataFrameBytes.setStatus("current")
_HpnicfDot11StationTxDataFrameBytes_Type = Counter64
_HpnicfDot11StationTxDataFrameBytes_Object = MibTableColumn
hpnicfDot11StationTxDataFrameBytes = _HpnicfDot11StationTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 17),
    _HpnicfDot11StationTxDataFrameBytes_Type()
)
hpnicfDot11StationTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationTxDataFrameBytes.setStatus("current")
_HpnicfDot11StationRxFragCnt_Type = Counter32
_HpnicfDot11StationRxFragCnt_Object = MibTableColumn
hpnicfDot11StationRxFragCnt = _HpnicfDot11StationRxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 18),
    _HpnicfDot11StationRxFragCnt_Type()
)
hpnicfDot11StationRxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRxFragCnt.setStatus("current")
_HpnicfDot11StaRxErrDataFrameCnt_Type = Counter64
_HpnicfDot11StaRxErrDataFrameCnt_Object = MibTableColumn
hpnicfDot11StaRxErrDataFrameCnt = _HpnicfDot11StaRxErrDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 19),
    _HpnicfDot11StaRxErrDataFrameCnt_Type()
)
hpnicfDot11StaRxErrDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StaRxErrDataFrameCnt.setStatus("current")
_HpnicfDot11StaTxRetryDataFrameCnt_Type = Counter64
_HpnicfDot11StaTxRetryDataFrameCnt_Object = MibTableColumn
hpnicfDot11StaTxRetryDataFrameCnt = _HpnicfDot11StaTxRetryDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 20),
    _HpnicfDot11StaTxRetryDataFrameCnt_Type()
)
hpnicfDot11StaTxRetryDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StaTxRetryDataFrameCnt.setStatus("current")
_HpnicfDot11StaTxDataRatePkts_Type = OctetString
_HpnicfDot11StaTxDataRatePkts_Object = MibTableColumn
hpnicfDot11StaTxDataRatePkts = _HpnicfDot11StaTxDataRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 21),
    _HpnicfDot11StaTxDataRatePkts_Type()
)
hpnicfDot11StaTxDataRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StaTxDataRatePkts.setStatus("current")
_HpnicfDot11StaRxDataRatePkts_Type = OctetString
_HpnicfDot11StaRxDataRatePkts_Object = MibTableColumn
hpnicfDot11StaRxDataRatePkts = _HpnicfDot11StaRxDataRatePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 22),
    _HpnicfDot11StaRxDataRatePkts_Type()
)
hpnicfDot11StaRxDataRatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StaRxDataRatePkts.setStatus("current")
_HpnicfDot11StaTxSignalStrengthPkts_Type = OctetString
_HpnicfDot11StaTxSignalStrengthPkts_Object = MibTableColumn
hpnicfDot11StaTxSignalStrengthPkts = _HpnicfDot11StaTxSignalStrengthPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 3, 1, 23),
    _HpnicfDot11StaTxSignalStrengthPkts_Type()
)
hpnicfDot11StaTxSignalStrengthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StaTxSignalStrengthPkts.setStatus("current")
_HpnicfDot11StationRfPingTable_Object = MibTable
hpnicfDot11StationRfPingTable = _HpnicfDot11StationRfPingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingTable.setStatus("current")
_HpnicfDot11StationRfPingEntry_Object = MibTableRow
hpnicfDot11StationRfPingEntry = _HpnicfDot11StationRfPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1)
)
hpnicfDot11StationRfPingEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationMAC"),
    (0, "HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationRfPingIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingEntry.setStatus("current")


class _HpnicfDot11StationRfPingIndex_Type(Integer32):
    """Custom type hpnicfDot11StationRfPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214783647),
    )


_HpnicfDot11StationRfPingIndex_Type.__name__ = "Integer32"
_HpnicfDot11StationRfPingIndex_Object = MibTableColumn
hpnicfDot11StationRfPingIndex = _HpnicfDot11StationRfPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 1),
    _HpnicfDot11StationRfPingIndex_Type()
)
hpnicfDot11StationRfPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingIndex.setStatus("current")
_HpnicfDot11StationRfPingRate_Type = OctetString
_HpnicfDot11StationRfPingRate_Object = MibTableColumn
hpnicfDot11StationRfPingRate = _HpnicfDot11StationRfPingRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 2),
    _HpnicfDot11StationRfPingRate_Type()
)
hpnicfDot11StationRfPingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRate.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRate.setUnits("Mbps")
_HpnicfDot11StationRfPingTxCnt_Type = Integer32
_HpnicfDot11StationRfPingTxCnt_Object = MibTableColumn
hpnicfDot11StationRfPingTxCnt = _HpnicfDot11StationRfPingTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 3),
    _HpnicfDot11StationRfPingTxCnt_Type()
)
hpnicfDot11StationRfPingTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingTxCnt.setStatus("current")
_HpnicfDot11StationRfPingRxCnt_Type = Integer32
_HpnicfDot11StationRfPingRxCnt_Object = MibTableColumn
hpnicfDot11StationRfPingRxCnt = _HpnicfDot11StationRfPingRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 4),
    _HpnicfDot11StationRfPingRxCnt_Type()
)
hpnicfDot11StationRfPingRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRxCnt.setStatus("current")
_HpnicfDot11StationRfPingRssi_Type = Integer32
_HpnicfDot11StationRfPingRssi_Object = MibTableColumn
hpnicfDot11StationRfPingRssi = _HpnicfDot11StationRfPingRssi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 5),
    _HpnicfDot11StationRfPingRssi_Type()
)
hpnicfDot11StationRfPingRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRssi.setStatus("current")
_HpnicfDot11StationRfPingRetries_Type = Integer32
_HpnicfDot11StationRfPingRetries_Object = MibTableColumn
hpnicfDot11StationRfPingRetries = _HpnicfDot11StationRfPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 6),
    _HpnicfDot11StationRfPingRetries_Type()
)
hpnicfDot11StationRfPingRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRetries.setStatus("current")
_HpnicfDot11StationRfPingRtt_Type = Integer32
_HpnicfDot11StationRfPingRtt_Object = MibTableColumn
hpnicfDot11StationRfPingRtt = _HpnicfDot11StationRfPingRtt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 1, 4, 1, 7),
    _HpnicfDot11StationRfPingRtt_Type()
)
hpnicfDot11StationRfPingRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRtt.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRfPingRtt.setUnits("ms")
_HpnicfDot11StationNotifyGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11StationNotifyGroup = _HpnicfDot11StationNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2)
)
_HpnicfDot11StationTraps_ObjectIdentity = ObjectIdentity
hpnicfDot11StationTraps = _HpnicfDot11StationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0)
)
_HpnicfDot11StationTrapVarObjects_ObjectIdentity = ObjectIdentity
hpnicfDot11StationTrapVarObjects = _HpnicfDot11StationTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1)
)
_HpnicfDot11StationTrapBSSID_Type = MacAddress
_HpnicfDot11StationTrapBSSID_Object = MibScalar
hpnicfDot11StationTrapBSSID = _HpnicfDot11StationTrapBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 1),
    _HpnicfDot11StationTrapBSSID_Type()
)
hpnicfDot11StationTrapBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationTrapBSSID.setStatus("current")
_HpnicfDot11StationTrapStaMAC_Type = MacAddress
_HpnicfDot11StationTrapStaMAC_Object = MibScalar
hpnicfDot11StationTrapStaMAC = _HpnicfDot11StationTrapStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 2),
    _HpnicfDot11StationTrapStaMAC_Type()
)
hpnicfDot11StationTrapStaMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationTrapStaMAC.setStatus("current")
_HpnicfDot11StationSessionStartTime_Type = DateAndTime
_HpnicfDot11StationSessionStartTime_Object = MibScalar
hpnicfDot11StationSessionStartTime = _HpnicfDot11StationSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 3),
    _HpnicfDot11StationSessionStartTime_Type()
)
hpnicfDot11StationSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationSessionStartTime.setStatus("current")
_HpnicfDot11StationAssocFailCause_Type = HpnicfDot11AssocFailType
_HpnicfDot11StationAssocFailCause_Object = MibScalar
hpnicfDot11StationAssocFailCause = _HpnicfDot11StationAssocFailCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 4),
    _HpnicfDot11StationAssocFailCause_Type()
)
hpnicfDot11StationAssocFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationAssocFailCause.setStatus("current")
_HpnicfDot11StationAuthorFailCause_Type = HpnicfDot11AuthorFailType
_HpnicfDot11StationAuthorFailCause_Object = MibScalar
hpnicfDot11StationAuthorFailCause = _HpnicfDot11StationAuthorFailCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 5),
    _HpnicfDot11StationAuthorFailCause_Type()
)
hpnicfDot11StationAuthorFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthorFailCause.setStatus("current")


class _HpnicfDot11StationFailCauseDesc_Type(OctetString):
    """Custom type hpnicfDot11StationFailCauseDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDot11StationFailCauseDesc_Type.__name__ = "OctetString"
_HpnicfDot11StationFailCauseDesc_Object = MibScalar
hpnicfDot11StationFailCauseDesc = _HpnicfDot11StationFailCauseDesc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 6),
    _HpnicfDot11StationFailCauseDesc_Type()
)
hpnicfDot11StationFailCauseDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationFailCauseDesc.setStatus("current")
_HpnicfDot11StationSessionDuration_Type = Unsigned32
_HpnicfDot11StationSessionDuration_Object = MibScalar
hpnicfDot11StationSessionDuration = _HpnicfDot11StationSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 7),
    _HpnicfDot11StationSessionDuration_Type()
)
hpnicfDot11StationSessionDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationSessionDuration.setUnits("second")
_HpnicfDot11StationRoamingTime_Type = Unsigned32
_HpnicfDot11StationRoamingTime_Object = MibScalar
hpnicfDot11StationRoamingTime = _HpnicfDot11StationRoamingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 8),
    _HpnicfDot11StationRoamingTime_Type()
)
hpnicfDot11StationRoamingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationRoamingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDot11StationRoamingTime.setUnits("second")
_HpnicfDot11StationACIPAddress_Type = IpAddress
_HpnicfDot11StationACIPAddress_Object = MibScalar
hpnicfDot11StationACIPAddress = _HpnicfDot11StationACIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 9),
    _HpnicfDot11StationACIPAddress_Type()
)
hpnicfDot11StationACIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationACIPAddress.setStatus("current")
_HpnicfDot11StationAPName_Type = OctetString
_HpnicfDot11StationAPName_Object = MibScalar
hpnicfDot11StationAPName = _HpnicfDot11StationAPName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 10),
    _HpnicfDot11StationAPName_Type()
)
hpnicfDot11StationAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationAPName.setStatus("current")
_HpnicfDot11StationBSSID_Type = MacAddress
_HpnicfDot11StationBSSID_Object = MibScalar
hpnicfDot11StationBSSID = _HpnicfDot11StationBSSID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 11),
    _HpnicfDot11StationBSSID_Type()
)
hpnicfDot11StationBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationBSSID.setStatus("current")
_HpnicfDot11StaDisconnectReason_Type = OctetString
_HpnicfDot11StaDisconnectReason_Object = MibScalar
hpnicfDot11StaDisconnectReason = _HpnicfDot11StaDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 12),
    _HpnicfDot11StaDisconnectReason_Type()
)
hpnicfDot11StaDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StaDisconnectReason.setStatus("current")


class _HpnicfDot11StationAuthMode_Type(Integer32):
    """Custom type hpnicfDot11StationAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 1),
          ("sharedkey", 2))
    )


_HpnicfDot11StationAuthMode_Type.__name__ = "Integer32"
_HpnicfDot11StationAuthMode_Object = MibScalar
hpnicfDot11StationAuthMode = _HpnicfDot11StationAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 13),
    _HpnicfDot11StationAuthMode_Type()
)
hpnicfDot11StationAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthMode.setStatus("current")
_HpnicfDot11StationACIPv6Add_Type = OctetString
_HpnicfDot11StationACIPv6Add_Object = MibScalar
hpnicfDot11StationACIPv6Add = _HpnicfDot11StationACIPv6Add_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 14),
    _HpnicfDot11StationACIPv6Add_Type()
)
hpnicfDot11StationACIPv6Add.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationACIPv6Add.setStatus("current")
_HpnicfDot11UserName_Type = OctetString
_HpnicfDot11UserName_Object = MibScalar
hpnicfDot11UserName = _HpnicfDot11UserName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 15),
    _HpnicfDot11UserName_Type()
)
hpnicfDot11UserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11UserName.setStatus("current")
_HpnicfDot11StationTrapAPMacAddress_Type = MacAddress
_HpnicfDot11StationTrapAPMacAddress_Object = MibScalar
hpnicfDot11StationTrapAPMacAddress = _HpnicfDot11StationTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 1, 16),
    _HpnicfDot11StationTrapAPMacAddress_Type()
)
hpnicfDot11StationTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDot11StationTrapAPMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDot11StationMICErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 1)
)
hpnicfDot11StationMICErrorTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapBSSID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationMICErrorTrap.setStatus(
        "current"
    )

hpnicfDot11StationAuthenErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 2)
)
hpnicfDot11StationAuthenErrorTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapBSSID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAuthenMode"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAKMMode"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthenErrorTrap.setStatus(
        "current"
    )

hpnicfDot11StationAuthorFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 3)
)
hpnicfDot11StationAuthorFailTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationUserName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAuthorFailCause"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationFailCauseDesc"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationBSSID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAuthMode"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthorFailTrap.setStatus(
        "current"
    )

hpnicfDot11StationAssocFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 4)
)
hpnicfDot11StationAssocFailTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAssocFailCause"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationFailCauseDesc"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAssocFailTrap.setStatus(
        "current"
    )

hpnicfDot11StationDeAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 5)
)
hpnicfDot11StationDeAssocTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationUserName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationVlanId"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSessionDuration"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAPName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationDeAssocTrap.setStatus(
        "current"
    )

hpnicfDot11StationAuthorSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 6)
)
hpnicfDot11StationAuthorSuccTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationUserName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationVlanId"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSessionStartTime"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAPName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationAuthorSuccTrap.setStatus(
        "current"
    )

hpnicfDot11StationRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 7)
)
hpnicfDot11StationRoamingTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationUserName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationVlanId"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationRoamingTime"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationACIPAddress"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationACIPv6Add"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationRoamingTrap.setStatus(
        "current"
    )

hpnicfDot11StationDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 8)
)
hpnicfDot11StationDisconnectTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAPName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationBSSID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSSIDName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationSessionDuration"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationVlanId"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrAPID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11CurrRadioID"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StaDisconnectReason"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    hpnicfDot11StationDisconnectTrap.setStatus(
        "current"
    )

hpnicfDot11UserDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 3, 2, 0, 9)
)
hpnicfDot11UserDisconnectTrap.setObjects(
      *(("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationAPName"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11StationTrapStaMAC"),
        ("HPN-ICF-DOT11-STATION-MIB", "hpnicfDot11UserName"))
)
if mibBuilder.loadTexts:
    hpnicfDot11UserDisconnectTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-STATION-MIB",
    **{"hpnicfDot11STATION": hpnicfDot11STATION,
       "hpnicfDot11StationMtGroup": hpnicfDot11StationMtGroup,
       "hpnicfDot11StationAssociateTable": hpnicfDot11StationAssociateTable,
       "hpnicfDot11StationAssociateEntry": hpnicfDot11StationAssociateEntry,
       "hpnicfDot11StationMAC": hpnicfDot11StationMAC,
       "hpnicfDot11StationIPAddress": hpnicfDot11StationIPAddress,
       "hpnicfDot11StationUserName": hpnicfDot11StationUserName,
       "hpnicfDot11StationTxRateSet": hpnicfDot11StationTxRateSet,
       "hpnicfDot11StationUpTime": hpnicfDot11StationUpTime,
       "hpnicfDot11StationSignalStrength": hpnicfDot11StationSignalStrength,
       "hpnicfDot11StationRSSI": hpnicfDot11StationRSSI,
       "hpnicfDot11StationChannel": hpnicfDot11StationChannel,
       "hpnicfDot11StationPowerSaveMode": hpnicfDot11StationPowerSaveMode,
       "hpnicfDot11StationAid": hpnicfDot11StationAid,
       "hpnicfDot11StationVlanId": hpnicfDot11StationVlanId,
       "hpnicfDot11StationSSIDName": hpnicfDot11StationSSIDName,
       "hpnicfDot11StationAuthenMode": hpnicfDot11StationAuthenMode,
       "hpnicfDot11StationAKMMode": hpnicfDot11StationAKMMode,
       "hpnicfDot11StationSecurityCiphers": hpnicfDot11StationSecurityCiphers,
       "hpnicfDot11StationSSIDEncryptMode": hpnicfDot11StationSSIDEncryptMode,
       "hpnicfDot11StationRxSNR": hpnicfDot11StationRxSNR,
       "hpnicfDot11StationTxRate": hpnicfDot11StationTxRate,
       "hpnicfDot11StationRxRate": hpnicfDot11StationRxRate,
       "hpnicfDot11StationVendorName": hpnicfDot11StationVendorName,
       "hpnicfDot11StationRadioMode": hpnicfDot11StationRadioMode,
       "hpnicfDot11StationRxNoise": hpnicfDot11StationRxNoise,
       "hpnicfDot11StationMACAddress": hpnicfDot11StationMACAddress,
       "hpnicfDot11StationTxSpeed": hpnicfDot11StationTxSpeed,
       "hpnicfDot11StationRxSpeed": hpnicfDot11StationRxSpeed,
       "hpnicfDot11StationWmmMode": hpnicfDot11StationWmmMode,
       "hpnicfDot11StationSecIEStatus": hpnicfDot11StationSecIEStatus,
       "hpnicfDot11StationUpTimeTicks": hpnicfDot11StationUpTimeTicks,
       "hpnicfDot11StationRadioMode2": hpnicfDot11StationRadioMode2,
       "hpnicfDot11StationAssTime": hpnicfDot11StationAssTime,
       "hpnicfDot11StationUserAuthType": hpnicfDot11StationUserAuthType,
       "hpnicfDot11StationRfPingTest": hpnicfDot11StationRfPingTest,
       "hpnicfDot11StationMaxRate": hpnicfDot11StationMaxRate,
       "hpnicfDot11StationPowerSaveModeCM": hpnicfDot11StationPowerSaveModeCM,
       "hpnicfDot11StationAuthenModeCM": hpnicfDot11StationAuthenModeCM,
       "hpnicfDot11StationAKMModeCM": hpnicfDot11StationAKMModeCM,
       "hpnicfDot11StationSecurityCiphersCM": hpnicfDot11StationSecurityCiphersCM,
       "hpnicfDot11StationSecIEStatusCM": hpnicfDot11StationSecIEStatusCM,
       "hpnicfDot11StationAPRelationTable": hpnicfDot11StationAPRelationTable,
       "hpnicfDot11StationAPRelationEntry": hpnicfDot11StationAPRelationEntry,
       "hpnicfDot11CurrAPID": hpnicfDot11CurrAPID,
       "hpnicfDot11CurrRadioID": hpnicfDot11CurrRadioID,
       "hpnicfDot11CurrWlanID": hpnicfDot11CurrWlanID,
       "hpnicfDot11CurrAntennaID": hpnicfDot11CurrAntennaID,
       "hpnicfDot11StationStatisTable": hpnicfDot11StationStatisTable,
       "hpnicfDot11StationStatisEntry": hpnicfDot11StationStatisEntry,
       "hpnicfDot11StationRxFrameCnt": hpnicfDot11StationRxFrameCnt,
       "hpnicfDot11StationTxFrameCnt": hpnicfDot11StationTxFrameCnt,
       "hpnicfDot11StationDropFrameCnt": hpnicfDot11StationDropFrameCnt,
       "hpnicfDot11StationRxFrameBytes": hpnicfDot11StationRxFrameBytes,
       "hpnicfDot11StationTxFrameBytes": hpnicfDot11StationTxFrameBytes,
       "hpnicfDot11StationDropFrameBytes": hpnicfDot11StationDropFrameBytes,
       "hpnicfDot11StationRxRetryPkts": hpnicfDot11StationRxRetryPkts,
       "hpnicfDot11StationTxRetryPkts": hpnicfDot11StationTxRetryPkts,
       "hpnicfDot11StationRxRetryBytes": hpnicfDot11StationRxRetryBytes,
       "hpnicfDot11StationTxRetryBytes": hpnicfDot11StationTxRetryBytes,
       "hpnicfDot11StationThroughput": hpnicfDot11StationThroughput,
       "hpnicfDot11StationSuccessTxCnt": hpnicfDot11StationSuccessTxCnt,
       "hpnicfDot11StationSuccessTxDataCnt": hpnicfDot11StationSuccessTxDataCnt,
       "hpnicfDot11StationRxDataFrameCnt": hpnicfDot11StationRxDataFrameCnt,
       "hpnicfDot11StationTxDataFrameCnt": hpnicfDot11StationTxDataFrameCnt,
       "hpnicfDot11StationRxDataFrameBytes": hpnicfDot11StationRxDataFrameBytes,
       "hpnicfDot11StationTxDataFrameBytes": hpnicfDot11StationTxDataFrameBytes,
       "hpnicfDot11StationRxFragCnt": hpnicfDot11StationRxFragCnt,
       "hpnicfDot11StaRxErrDataFrameCnt": hpnicfDot11StaRxErrDataFrameCnt,
       "hpnicfDot11StaTxRetryDataFrameCnt": hpnicfDot11StaTxRetryDataFrameCnt,
       "hpnicfDot11StaTxDataRatePkts": hpnicfDot11StaTxDataRatePkts,
       "hpnicfDot11StaRxDataRatePkts": hpnicfDot11StaRxDataRatePkts,
       "hpnicfDot11StaTxSignalStrengthPkts": hpnicfDot11StaTxSignalStrengthPkts,
       "hpnicfDot11StationRfPingTable": hpnicfDot11StationRfPingTable,
       "hpnicfDot11StationRfPingEntry": hpnicfDot11StationRfPingEntry,
       "hpnicfDot11StationRfPingIndex": hpnicfDot11StationRfPingIndex,
       "hpnicfDot11StationRfPingRate": hpnicfDot11StationRfPingRate,
       "hpnicfDot11StationRfPingTxCnt": hpnicfDot11StationRfPingTxCnt,
       "hpnicfDot11StationRfPingRxCnt": hpnicfDot11StationRfPingRxCnt,
       "hpnicfDot11StationRfPingRssi": hpnicfDot11StationRfPingRssi,
       "hpnicfDot11StationRfPingRetries": hpnicfDot11StationRfPingRetries,
       "hpnicfDot11StationRfPingRtt": hpnicfDot11StationRfPingRtt,
       "hpnicfDot11StationNotifyGroup": hpnicfDot11StationNotifyGroup,
       "hpnicfDot11StationTraps": hpnicfDot11StationTraps,
       "hpnicfDot11StationMICErrorTrap": hpnicfDot11StationMICErrorTrap,
       "hpnicfDot11StationAuthenErrorTrap": hpnicfDot11StationAuthenErrorTrap,
       "hpnicfDot11StationAuthorFailTrap": hpnicfDot11StationAuthorFailTrap,
       "hpnicfDot11StationAssocFailTrap": hpnicfDot11StationAssocFailTrap,
       "hpnicfDot11StationDeAssocTrap": hpnicfDot11StationDeAssocTrap,
       "hpnicfDot11StationAuthorSuccTrap": hpnicfDot11StationAuthorSuccTrap,
       "hpnicfDot11StationRoamingTrap": hpnicfDot11StationRoamingTrap,
       "hpnicfDot11StationDisconnectTrap": hpnicfDot11StationDisconnectTrap,
       "hpnicfDot11UserDisconnectTrap": hpnicfDot11UserDisconnectTrap,
       "hpnicfDot11StationTrapVarObjects": hpnicfDot11StationTrapVarObjects,
       "hpnicfDot11StationTrapBSSID": hpnicfDot11StationTrapBSSID,
       "hpnicfDot11StationTrapStaMAC": hpnicfDot11StationTrapStaMAC,
       "hpnicfDot11StationSessionStartTime": hpnicfDot11StationSessionStartTime,
       "hpnicfDot11StationAssocFailCause": hpnicfDot11StationAssocFailCause,
       "hpnicfDot11StationAuthorFailCause": hpnicfDot11StationAuthorFailCause,
       "hpnicfDot11StationFailCauseDesc": hpnicfDot11StationFailCauseDesc,
       "hpnicfDot11StationSessionDuration": hpnicfDot11StationSessionDuration,
       "hpnicfDot11StationRoamingTime": hpnicfDot11StationRoamingTime,
       "hpnicfDot11StationACIPAddress": hpnicfDot11StationACIPAddress,
       "hpnicfDot11StationAPName": hpnicfDot11StationAPName,
       "hpnicfDot11StationBSSID": hpnicfDot11StationBSSID,
       "hpnicfDot11StaDisconnectReason": hpnicfDot11StaDisconnectReason,
       "hpnicfDot11StationAuthMode": hpnicfDot11StationAuthMode,
       "hpnicfDot11StationACIPv6Add": hpnicfDot11StationACIPv6Add,
       "hpnicfDot11UserName": hpnicfDot11UserName,
       "hpnicfDot11StationTrapAPMacAddress": hpnicfDot11StationTrapAPMacAddress}
)
