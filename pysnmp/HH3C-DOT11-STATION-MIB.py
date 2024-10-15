# SNMP MIB module (HH3C-DOT11-STATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-STATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:56 2024
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

(Hh3cDot11AKMType,
 Hh3cDot11AssocFailType,
 Hh3cDot11AuthenType,
 Hh3cDot11AuthorFailType,
 Hh3cDot11ChannelScopeType,
 Hh3cDot11CipherType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11RadioScopeType,
 Hh3cDot11RadioType,
 Hh3cDot11SSIDEncryptModeType,
 Hh3cDot11SSIDStringType,
 Hh3cDot11SecIEStatusType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11AKMType",
    "Hh3cDot11AssocFailType",
    "Hh3cDot11AuthenType",
    "Hh3cDot11AuthorFailType",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11CipherType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11RadioType",
    "Hh3cDot11SSIDEncryptModeType",
    "Hh3cDot11SSIDStringType",
    "Hh3cDot11SecIEStatusType",
    "hh3cDot11")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDot11STATION = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3)
)
hh3cDot11STATION.setRevisions(
        ("2010-09-02 18:00",
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

_Hh3cDot11StationMtGroup_ObjectIdentity = ObjectIdentity
hh3cDot11StationMtGroup = _Hh3cDot11StationMtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1)
)
_Hh3cDot11StationAssociateTable_Object = MibTable
hh3cDot11StationAssociateTable = _Hh3cDot11StationAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11StationAssociateTable.setStatus("current")
_Hh3cDot11StationAssociateEntry_Object = MibTableRow
hh3cDot11StationAssociateEntry = _Hh3cDot11StationAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1)
)
hh3cDot11StationAssociateEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationAssociateEntry.setStatus("current")
_Hh3cDot11StationMAC_Type = MacAddress
_Hh3cDot11StationMAC_Object = MibTableColumn
hh3cDot11StationMAC = _Hh3cDot11StationMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 1),
    _Hh3cDot11StationMAC_Type()
)
hh3cDot11StationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11StationMAC.setStatus("current")
_Hh3cDot11StationIPAddress_Type = IpAddress
_Hh3cDot11StationIPAddress_Object = MibTableColumn
hh3cDot11StationIPAddress = _Hh3cDot11StationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 2),
    _Hh3cDot11StationIPAddress_Type()
)
hh3cDot11StationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationIPAddress.setStatus("current")
_Hh3cDot11StationUserName_Type = OctetString
_Hh3cDot11StationUserName_Object = MibTableColumn
hh3cDot11StationUserName = _Hh3cDot11StationUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 3),
    _Hh3cDot11StationUserName_Type()
)
hh3cDot11StationUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUserName.setStatus("current")
_Hh3cDot11StationTxRateSet_Type = OctetString
_Hh3cDot11StationTxRateSet_Object = MibTableColumn
hh3cDot11StationTxRateSet = _Hh3cDot11StationTxRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 4),
    _Hh3cDot11StationTxRateSet_Type()
)
hh3cDot11StationTxRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRateSet.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRateSet.setUnits("Mbps")
_Hh3cDot11StationUpTime_Type = Unsigned32
_Hh3cDot11StationUpTime_Object = MibTableColumn
hh3cDot11StationUpTime = _Hh3cDot11StationUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 5),
    _Hh3cDot11StationUpTime_Type()
)
hh3cDot11StationUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationUpTime.setUnits("second")
_Hh3cDot11StationSignalStrength_Type = Integer32
_Hh3cDot11StationSignalStrength_Object = MibTableColumn
hh3cDot11StationSignalStrength = _Hh3cDot11StationSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 6),
    _Hh3cDot11StationSignalStrength_Type()
)
hh3cDot11StationSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationSignalStrength.setUnits("dBm")
_Hh3cDot11StationRSSI_Type = Integer32
_Hh3cDot11StationRSSI_Object = MibTableColumn
hh3cDot11StationRSSI = _Hh3cDot11StationRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 7),
    _Hh3cDot11StationRSSI_Type()
)
hh3cDot11StationRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRSSI.setStatus("current")
_Hh3cDot11StationChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11StationChannel_Object = MibTableColumn
hh3cDot11StationChannel = _Hh3cDot11StationChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 8),
    _Hh3cDot11StationChannel_Type()
)
hh3cDot11StationChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationChannel.setStatus("current")


class _Hh3cDot11StationPowerSaveMode_Type(Integer32):
    """Custom type hh3cDot11StationPowerSaveMode based on Integer32"""
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


_Hh3cDot11StationPowerSaveMode_Type.__name__ = "Integer32"
_Hh3cDot11StationPowerSaveMode_Object = MibTableColumn
hh3cDot11StationPowerSaveMode = _Hh3cDot11StationPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 9),
    _Hh3cDot11StationPowerSaveMode_Type()
)
hh3cDot11StationPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationPowerSaveMode.setStatus("current")
_Hh3cDot11StationAid_Type = Integer32
_Hh3cDot11StationAid_Object = MibTableColumn
hh3cDot11StationAid = _Hh3cDot11StationAid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 10),
    _Hh3cDot11StationAid_Type()
)
hh3cDot11StationAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAid.setStatus("current")
_Hh3cDot11StationVlanId_Type = Integer32
_Hh3cDot11StationVlanId_Object = MibTableColumn
hh3cDot11StationVlanId = _Hh3cDot11StationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 11),
    _Hh3cDot11StationVlanId_Type()
)
hh3cDot11StationVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationVlanId.setStatus("current")
_Hh3cDot11StationSSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11StationSSIDName_Object = MibTableColumn
hh3cDot11StationSSIDName = _Hh3cDot11StationSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 12),
    _Hh3cDot11StationSSIDName_Type()
)
hh3cDot11StationSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSSIDName.setStatus("current")
_Hh3cDot11StationAuthenMode_Type = Hh3cDot11AuthenType
_Hh3cDot11StationAuthenMode_Object = MibTableColumn
hh3cDot11StationAuthenMode = _Hh3cDot11StationAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 13),
    _Hh3cDot11StationAuthenMode_Type()
)
hh3cDot11StationAuthenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthenMode.setStatus("current")
_Hh3cDot11StationAKMMode_Type = Hh3cDot11AKMType
_Hh3cDot11StationAKMMode_Object = MibTableColumn
hh3cDot11StationAKMMode = _Hh3cDot11StationAKMMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 14),
    _Hh3cDot11StationAKMMode_Type()
)
hh3cDot11StationAKMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAKMMode.setStatus("current")
_Hh3cDot11StationSecurityCiphers_Type = Hh3cDot11CipherType
_Hh3cDot11StationSecurityCiphers_Object = MibTableColumn
hh3cDot11StationSecurityCiphers = _Hh3cDot11StationSecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 15),
    _Hh3cDot11StationSecurityCiphers_Type()
)
hh3cDot11StationSecurityCiphers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSecurityCiphers.setStatus("current")


class _Hh3cDot11StationSSIDEncryptMode_Type(Hh3cDot11SSIDEncryptModeType):
    """Custom type hh3cDot11StationSSIDEncryptMode based on Hh3cDot11SSIDEncryptModeType"""


_Hh3cDot11StationSSIDEncryptMode_Object = MibTableColumn
hh3cDot11StationSSIDEncryptMode = _Hh3cDot11StationSSIDEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 16),
    _Hh3cDot11StationSSIDEncryptMode_Type()
)
hh3cDot11StationSSIDEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSSIDEncryptMode.setStatus("current")
_Hh3cDot11StationRxSNR_Type = Integer32
_Hh3cDot11StationRxSNR_Object = MibTableColumn
hh3cDot11StationRxSNR = _Hh3cDot11StationRxSNR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 17),
    _Hh3cDot11StationRxSNR_Type()
)
hh3cDot11StationRxSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSNR.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSNR.setUnits("One Percent")
_Hh3cDot11StationTxRate_Type = Integer32
_Hh3cDot11StationTxRate_Object = MibTableColumn
hh3cDot11StationTxRate = _Hh3cDot11StationTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 18),
    _Hh3cDot11StationTxRate_Type()
)
hh3cDot11StationTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRate.setUnits("Mbps")
_Hh3cDot11StationRxRate_Type = Integer32
_Hh3cDot11StationRxRate_Object = MibTableColumn
hh3cDot11StationRxRate = _Hh3cDot11StationRxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 19),
    _Hh3cDot11StationRxRate_Type()
)
hh3cDot11StationRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRate.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRate.setUnits("Mbps")


class _Hh3cDot11StationVendorName_Type(OctetString):
    """Custom type hh3cDot11StationVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11StationVendorName_Type.__name__ = "OctetString"
_Hh3cDot11StationVendorName_Object = MibTableColumn
hh3cDot11StationVendorName = _Hh3cDot11StationVendorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 20),
    _Hh3cDot11StationVendorName_Type()
)
hh3cDot11StationVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationVendorName.setStatus("current")
_Hh3cDot11StationRadioMode_Type = Hh3cDot11RadioType
_Hh3cDot11StationRadioMode_Object = MibTableColumn
hh3cDot11StationRadioMode = _Hh3cDot11StationRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 21),
    _Hh3cDot11StationRadioMode_Type()
)
hh3cDot11StationRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRadioMode.setStatus("current")
_Hh3cDot11StationRxNoise_Type = Integer32
_Hh3cDot11StationRxNoise_Object = MibTableColumn
hh3cDot11StationRxNoise = _Hh3cDot11StationRxNoise_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 22),
    _Hh3cDot11StationRxNoise_Type()
)
hh3cDot11StationRxNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxNoise.setStatus("current")
_Hh3cDot11StationMACAddress_Type = MacAddress
_Hh3cDot11StationMACAddress_Object = MibTableColumn
hh3cDot11StationMACAddress = _Hh3cDot11StationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 23),
    _Hh3cDot11StationMACAddress_Type()
)
hh3cDot11StationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationMACAddress.setStatus("current")
_Hh3cDot11StationTxSpeed_Type = Integer32
_Hh3cDot11StationTxSpeed_Object = MibTableColumn
hh3cDot11StationTxSpeed = _Hh3cDot11StationTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 24),
    _Hh3cDot11StationTxSpeed_Type()
)
hh3cDot11StationTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxSpeed.setUnits("byte/s")
_Hh3cDot11StationRxSpeed_Type = Integer32
_Hh3cDot11StationRxSpeed_Object = MibTableColumn
hh3cDot11StationRxSpeed = _Hh3cDot11StationRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 25),
    _Hh3cDot11StationRxSpeed_Type()
)
hh3cDot11StationRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxSpeed.setUnits("byte/s")


class _Hh3cDot11StationWmmMode_Type(Integer32):
    """Custom type hh3cDot11StationWmmMode based on Integer32"""
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


_Hh3cDot11StationWmmMode_Type.__name__ = "Integer32"
_Hh3cDot11StationWmmMode_Object = MibTableColumn
hh3cDot11StationWmmMode = _Hh3cDot11StationWmmMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 26),
    _Hh3cDot11StationWmmMode_Type()
)
hh3cDot11StationWmmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationWmmMode.setStatus("current")
_Hh3cDot11StationSecIEStatus_Type = Hh3cDot11SecIEStatusType
_Hh3cDot11StationSecIEStatus_Object = MibTableColumn
hh3cDot11StationSecIEStatus = _Hh3cDot11StationSecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 27),
    _Hh3cDot11StationSecIEStatus_Type()
)
hh3cDot11StationSecIEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSecIEStatus.setStatus("current")
_Hh3cDot11StationUpTimeTicks_Type = TimeTicks
_Hh3cDot11StationUpTimeTicks_Object = MibTableColumn
hh3cDot11StationUpTimeTicks = _Hh3cDot11StationUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 1, 1, 28),
    _Hh3cDot11StationUpTimeTicks_Type()
)
hh3cDot11StationUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationUpTimeTicks.setStatus("current")
_Hh3cDot11StationAPRelationTable_Object = MibTable
hh3cDot11StationAPRelationTable = _Hh3cDot11StationAPRelationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11StationAPRelationTable.setStatus("current")
_Hh3cDot11StationAPRelationEntry_Object = MibTableRow
hh3cDot11StationAPRelationEntry = _Hh3cDot11StationAPRelationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1)
)
hh3cDot11StationAPRelationEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationAPRelationEntry.setStatus("current")
_Hh3cDot11CurrAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11CurrAPID_Object = MibTableColumn
hh3cDot11CurrAPID = _Hh3cDot11CurrAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 1),
    _Hh3cDot11CurrAPID_Type()
)
hh3cDot11CurrAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrAPID.setStatus("current")
_Hh3cDot11CurrRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11CurrRadioID_Object = MibTableColumn
hh3cDot11CurrRadioID = _Hh3cDot11CurrRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 2),
    _Hh3cDot11CurrRadioID_Type()
)
hh3cDot11CurrRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrRadioID.setStatus("current")
_Hh3cDot11CurrWlanID_Type = Integer32
_Hh3cDot11CurrWlanID_Object = MibTableColumn
hh3cDot11CurrWlanID = _Hh3cDot11CurrWlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 2, 1, 3),
    _Hh3cDot11CurrWlanID_Type()
)
hh3cDot11CurrWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrWlanID.setStatus("current")
_Hh3cDot11StationStatisTable_Object = MibTable
hh3cDot11StationStatisTable = _Hh3cDot11StationStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11StationStatisTable.setStatus("current")
_Hh3cDot11StationStatisEntry_Object = MibTableRow
hh3cDot11StationStatisEntry = _Hh3cDot11StationStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1)
)
hh3cDot11StationStatisEntry.setIndexNames(
    (0, "HH3C-DOT11-STATION-MIB", "hh3cDot11StationMAC"),
)
if mibBuilder.loadTexts:
    hh3cDot11StationStatisEntry.setStatus("current")
_Hh3cDot11StationRxFrameCnt_Type = Counter32
_Hh3cDot11StationRxFrameCnt_Object = MibTableColumn
hh3cDot11StationRxFrameCnt = _Hh3cDot11StationRxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 1),
    _Hh3cDot11StationRxFrameCnt_Type()
)
hh3cDot11StationRxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFrameCnt.setStatus("current")
_Hh3cDot11StationTxFrameCnt_Type = Counter32
_Hh3cDot11StationTxFrameCnt_Object = MibTableColumn
hh3cDot11StationTxFrameCnt = _Hh3cDot11StationTxFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 2),
    _Hh3cDot11StationTxFrameCnt_Type()
)
hh3cDot11StationTxFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxFrameCnt.setStatus("current")
_Hh3cDot11StationDropFrameCnt_Type = Counter32
_Hh3cDot11StationDropFrameCnt_Object = MibTableColumn
hh3cDot11StationDropFrameCnt = _Hh3cDot11StationDropFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 3),
    _Hh3cDot11StationDropFrameCnt_Type()
)
hh3cDot11StationDropFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationDropFrameCnt.setStatus("current")
_Hh3cDot11StationRxFrameBytes_Type = Counter64
_Hh3cDot11StationRxFrameBytes_Object = MibTableColumn
hh3cDot11StationRxFrameBytes = _Hh3cDot11StationRxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 4),
    _Hh3cDot11StationRxFrameBytes_Type()
)
hh3cDot11StationRxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFrameBytes.setUnits("bytes")
_Hh3cDot11StationTxFrameBytes_Type = Counter64
_Hh3cDot11StationTxFrameBytes_Object = MibTableColumn
hh3cDot11StationTxFrameBytes = _Hh3cDot11StationTxFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 5),
    _Hh3cDot11StationTxFrameBytes_Type()
)
hh3cDot11StationTxFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationTxFrameBytes.setUnits("bytes")
_Hh3cDot11StationDropFrameBytes_Type = Counter64
_Hh3cDot11StationDropFrameBytes_Object = MibTableColumn
hh3cDot11StationDropFrameBytes = _Hh3cDot11StationDropFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 6),
    _Hh3cDot11StationDropFrameBytes_Type()
)
hh3cDot11StationDropFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationDropFrameBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationDropFrameBytes.setUnits("bytes")
_Hh3cDot11StationRxRetryPkts_Type = Counter32
_Hh3cDot11StationRxRetryPkts_Object = MibTableColumn
hh3cDot11StationRxRetryPkts = _Hh3cDot11StationRxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 7),
    _Hh3cDot11StationRxRetryPkts_Type()
)
hh3cDot11StationRxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRetryPkts.setStatus("current")
_Hh3cDot11StationTxRetryPkts_Type = Counter32
_Hh3cDot11StationTxRetryPkts_Object = MibTableColumn
hh3cDot11StationTxRetryPkts = _Hh3cDot11StationTxRetryPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 8),
    _Hh3cDot11StationTxRetryPkts_Type()
)
hh3cDot11StationTxRetryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRetryPkts.setStatus("current")
_Hh3cDot11StationRxRetryBytes_Type = Counter64
_Hh3cDot11StationRxRetryBytes_Object = MibTableColumn
hh3cDot11StationRxRetryBytes = _Hh3cDot11StationRxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 9),
    _Hh3cDot11StationRxRetryBytes_Type()
)
hh3cDot11StationRxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxRetryBytes.setStatus("current")
_Hh3cDot11StationTxRetryBytes_Type = Counter64
_Hh3cDot11StationTxRetryBytes_Object = MibTableColumn
hh3cDot11StationTxRetryBytes = _Hh3cDot11StationTxRetryBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 10),
    _Hh3cDot11StationTxRetryBytes_Type()
)
hh3cDot11StationTxRetryBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxRetryBytes.setStatus("current")
_Hh3cDot11StationThroughput_Type = Counter64
_Hh3cDot11StationThroughput_Object = MibTableColumn
hh3cDot11StationThroughput = _Hh3cDot11StationThroughput_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 11),
    _Hh3cDot11StationThroughput_Type()
)
hh3cDot11StationThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationThroughput.setUnits("bytes")
_Hh3cDot11StationSuccessTxCnt_Type = Counter32
_Hh3cDot11StationSuccessTxCnt_Object = MibTableColumn
hh3cDot11StationSuccessTxCnt = _Hh3cDot11StationSuccessTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 12),
    _Hh3cDot11StationSuccessTxCnt_Type()
)
hh3cDot11StationSuccessTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSuccessTxCnt.setStatus("current")
_Hh3cDot11StationSuccessTxDataCnt_Type = Counter32
_Hh3cDot11StationSuccessTxDataCnt_Object = MibTableColumn
hh3cDot11StationSuccessTxDataCnt = _Hh3cDot11StationSuccessTxDataCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 13),
    _Hh3cDot11StationSuccessTxDataCnt_Type()
)
hh3cDot11StationSuccessTxDataCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationSuccessTxDataCnt.setStatus("current")
_Hh3cDot11StationRxDataFrameCnt_Type = Counter32
_Hh3cDot11StationRxDataFrameCnt_Object = MibTableColumn
hh3cDot11StationRxDataFrameCnt = _Hh3cDot11StationRxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 14),
    _Hh3cDot11StationRxDataFrameCnt_Type()
)
hh3cDot11StationRxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxDataFrameCnt.setStatus("current")
_Hh3cDot11StationTxDataFrameCnt_Type = Counter32
_Hh3cDot11StationTxDataFrameCnt_Object = MibTableColumn
hh3cDot11StationTxDataFrameCnt = _Hh3cDot11StationTxDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 15),
    _Hh3cDot11StationTxDataFrameCnt_Type()
)
hh3cDot11StationTxDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxDataFrameCnt.setStatus("current")
_Hh3cDot11StationRxDataFrameBytes_Type = Counter64
_Hh3cDot11StationRxDataFrameBytes_Object = MibTableColumn
hh3cDot11StationRxDataFrameBytes = _Hh3cDot11StationRxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 16),
    _Hh3cDot11StationRxDataFrameBytes_Type()
)
hh3cDot11StationRxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxDataFrameBytes.setStatus("current")
_Hh3cDot11StationTxDataFrameBytes_Type = Counter64
_Hh3cDot11StationTxDataFrameBytes_Object = MibTableColumn
hh3cDot11StationTxDataFrameBytes = _Hh3cDot11StationTxDataFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 17),
    _Hh3cDot11StationTxDataFrameBytes_Type()
)
hh3cDot11StationTxDataFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationTxDataFrameBytes.setStatus("current")
_Hh3cDot11StationRxFragCnt_Type = Counter32
_Hh3cDot11StationRxFragCnt_Object = MibTableColumn
hh3cDot11StationRxFragCnt = _Hh3cDot11StationRxFragCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 18),
    _Hh3cDot11StationRxFragCnt_Type()
)
hh3cDot11StationRxFragCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationRxFragCnt.setStatus("current")
_Hh3cDot11StaRxErrDataFrameCnt_Type = Counter64
_Hh3cDot11StaRxErrDataFrameCnt_Object = MibTableColumn
hh3cDot11StaRxErrDataFrameCnt = _Hh3cDot11StaRxErrDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 19),
    _Hh3cDot11StaRxErrDataFrameCnt_Type()
)
hh3cDot11StaRxErrDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaRxErrDataFrameCnt.setStatus("current")
_Hh3cDot11StaTxRetryDataFrameCnt_Type = Counter64
_Hh3cDot11StaTxRetryDataFrameCnt_Object = MibTableColumn
hh3cDot11StaTxRetryDataFrameCnt = _Hh3cDot11StaTxRetryDataFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 1, 3, 1, 20),
    _Hh3cDot11StaTxRetryDataFrameCnt_Type()
)
hh3cDot11StaTxRetryDataFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StaTxRetryDataFrameCnt.setStatus("current")
_Hh3cDot11StationNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11StationNotifyGroup = _Hh3cDot11StationNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2)
)
_Hh3cDot11StationTraps_ObjectIdentity = ObjectIdentity
hh3cDot11StationTraps = _Hh3cDot11StationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0)
)
_Hh3cDot11StationTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11StationTrapVarObjects = _Hh3cDot11StationTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1)
)
_Hh3cDot11StationTrapBSSID_Type = MacAddress
_Hh3cDot11StationTrapBSSID_Object = MibScalar
hh3cDot11StationTrapBSSID = _Hh3cDot11StationTrapBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 1),
    _Hh3cDot11StationTrapBSSID_Type()
)
hh3cDot11StationTrapBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapBSSID.setStatus("current")
_Hh3cDot11StationTrapStaMAC_Type = MacAddress
_Hh3cDot11StationTrapStaMAC_Object = MibScalar
hh3cDot11StationTrapStaMAC = _Hh3cDot11StationTrapStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 2),
    _Hh3cDot11StationTrapStaMAC_Type()
)
hh3cDot11StationTrapStaMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationTrapStaMAC.setStatus("current")
_Hh3cDot11StationSessionStartTime_Type = DateAndTime
_Hh3cDot11StationSessionStartTime_Object = MibScalar
hh3cDot11StationSessionStartTime = _Hh3cDot11StationSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 3),
    _Hh3cDot11StationSessionStartTime_Type()
)
hh3cDot11StationSessionStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationSessionStartTime.setStatus("current")
_Hh3cDot11StationAssocFailCause_Type = Hh3cDot11AssocFailType
_Hh3cDot11StationAssocFailCause_Object = MibScalar
hh3cDot11StationAssocFailCause = _Hh3cDot11StationAssocFailCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 4),
    _Hh3cDot11StationAssocFailCause_Type()
)
hh3cDot11StationAssocFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocFailCause.setStatus("current")
_Hh3cDot11StationAuthorFailCause_Type = Hh3cDot11AuthorFailType
_Hh3cDot11StationAuthorFailCause_Object = MibScalar
hh3cDot11StationAuthorFailCause = _Hh3cDot11StationAuthorFailCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 5),
    _Hh3cDot11StationAuthorFailCause_Type()
)
hh3cDot11StationAuthorFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthorFailCause.setStatus("current")


class _Hh3cDot11StationFailCauseDesc_Type(OctetString):
    """Custom type hh3cDot11StationFailCauseDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11StationFailCauseDesc_Type.__name__ = "OctetString"
_Hh3cDot11StationFailCauseDesc_Object = MibScalar
hh3cDot11StationFailCauseDesc = _Hh3cDot11StationFailCauseDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 6),
    _Hh3cDot11StationFailCauseDesc_Type()
)
hh3cDot11StationFailCauseDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationFailCauseDesc.setStatus("current")
_Hh3cDot11StationSessionDuration_Type = Unsigned32
_Hh3cDot11StationSessionDuration_Object = MibScalar
hh3cDot11StationSessionDuration = _Hh3cDot11StationSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 7),
    _Hh3cDot11StationSessionDuration_Type()
)
hh3cDot11StationSessionDuration.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationSessionDuration.setUnits("second")
_Hh3cDot11StationRoamingTime_Type = Unsigned32
_Hh3cDot11StationRoamingTime_Object = MibScalar
hh3cDot11StationRoamingTime = _Hh3cDot11StationRoamingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 8),
    _Hh3cDot11StationRoamingTime_Type()
)
hh3cDot11StationRoamingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationRoamingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StationRoamingTime.setUnits("second")
_Hh3cDot11StationACIPAddress_Type = IpAddress
_Hh3cDot11StationACIPAddress_Object = MibScalar
hh3cDot11StationACIPAddress = _Hh3cDot11StationACIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 9),
    _Hh3cDot11StationACIPAddress_Type()
)
hh3cDot11StationACIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationACIPAddress.setStatus("current")
_Hh3cDot11StationAPName_Type = OctetString
_Hh3cDot11StationAPName_Object = MibScalar
hh3cDot11StationAPName = _Hh3cDot11StationAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 10),
    _Hh3cDot11StationAPName_Type()
)
hh3cDot11StationAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAPName.setStatus("current")
_Hh3cDot11StationBSSID_Type = MacAddress
_Hh3cDot11StationBSSID_Object = MibScalar
hh3cDot11StationBSSID = _Hh3cDot11StationBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 11),
    _Hh3cDot11StationBSSID_Type()
)
hh3cDot11StationBSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationBSSID.setStatus("current")
_Hh3cDot11StaDisconnectReason_Type = OctetString
_Hh3cDot11StaDisconnectReason_Object = MibScalar
hh3cDot11StaDisconnectReason = _Hh3cDot11StaDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 12),
    _Hh3cDot11StaDisconnectReason_Type()
)
hh3cDot11StaDisconnectReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StaDisconnectReason.setStatus("current")


class _Hh3cDot11StationAuthMode_Type(Integer32):
    """Custom type hh3cDot11StationAuthMode based on Integer32"""
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


_Hh3cDot11StationAuthMode_Type.__name__ = "Integer32"
_Hh3cDot11StationAuthMode_Object = MibScalar
hh3cDot11StationAuthMode = _Hh3cDot11StationAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 13),
    _Hh3cDot11StationAuthMode_Type()
)
hh3cDot11StationAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationAuthMode.setStatus("current")
_Hh3cDot11StationACIPv6Add_Type = OctetString
_Hh3cDot11StationACIPv6Add_Object = MibScalar
hh3cDot11StationACIPv6Add = _Hh3cDot11StationACIPv6Add_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 1, 14),
    _Hh3cDot11StationACIPv6Add_Type()
)
hh3cDot11StationACIPv6Add.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11StationACIPv6Add.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11StationMICErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 1)
)
hh3cDot11StationMICErrorTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationMICErrorTrap.setStatus(
        "current"
    )

hh3cDot11StationAuthenErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 2)
)
hh3cDot11StationAuthenErrorTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthenMode"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAKMMode"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuthenErrorTrap.setStatus(
        "current"
    )

hh3cDot11StationAuthorFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 3)
)
hh3cDot11StationAuthorFailTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthorFailCause"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationFailCauseDesc"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAuthMode"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuthorFailTrap.setStatus(
        "current"
    )

hh3cDot11StationAssocFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 4)
)
hh3cDot11StationAssocFailTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAssocFailCause"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationFailCauseDesc"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAssocFailTrap.setStatus(
        "current"
    )

hh3cDot11StationDeAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 5)
)
hh3cDot11StationDeAssocTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationDeAssocTrap.setStatus(
        "current"
    )

hh3cDot11StationAuthorSuccTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 6)
)
hh3cDot11StationAuthorSuccTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionStartTime"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationAuthorSuccTrap.setStatus(
        "current"
    )

hh3cDot11StationRoamingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 7)
)
hh3cDot11StationRoamingTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationUserName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationRoamingTime"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationACIPAddress"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationACIPv6Add"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationRoamingTrap.setStatus(
        "current"
    )

hh3cDot11StationDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 3, 2, 0, 8)
)
hh3cDot11StationDisconnectTrap.setObjects(
      *(("HH3C-DOT11-STATION-MIB", "hh3cDot11StationAPName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationBSSID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSSIDName"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationSessionDuration"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationVlanId"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrAPID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11CurrRadioID"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StaDisconnectReason"),
        ("HH3C-DOT11-STATION-MIB", "hh3cDot11StationTrapStaMAC"))
)
if mibBuilder.loadTexts:
    hh3cDot11StationDisconnectTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-STATION-MIB",
    **{"hh3cDot11STATION": hh3cDot11STATION,
       "hh3cDot11StationMtGroup": hh3cDot11StationMtGroup,
       "hh3cDot11StationAssociateTable": hh3cDot11StationAssociateTable,
       "hh3cDot11StationAssociateEntry": hh3cDot11StationAssociateEntry,
       "hh3cDot11StationMAC": hh3cDot11StationMAC,
       "hh3cDot11StationIPAddress": hh3cDot11StationIPAddress,
       "hh3cDot11StationUserName": hh3cDot11StationUserName,
       "hh3cDot11StationTxRateSet": hh3cDot11StationTxRateSet,
       "hh3cDot11StationUpTime": hh3cDot11StationUpTime,
       "hh3cDot11StationSignalStrength": hh3cDot11StationSignalStrength,
       "hh3cDot11StationRSSI": hh3cDot11StationRSSI,
       "hh3cDot11StationChannel": hh3cDot11StationChannel,
       "hh3cDot11StationPowerSaveMode": hh3cDot11StationPowerSaveMode,
       "hh3cDot11StationAid": hh3cDot11StationAid,
       "hh3cDot11StationVlanId": hh3cDot11StationVlanId,
       "hh3cDot11StationSSIDName": hh3cDot11StationSSIDName,
       "hh3cDot11StationAuthenMode": hh3cDot11StationAuthenMode,
       "hh3cDot11StationAKMMode": hh3cDot11StationAKMMode,
       "hh3cDot11StationSecurityCiphers": hh3cDot11StationSecurityCiphers,
       "hh3cDot11StationSSIDEncryptMode": hh3cDot11StationSSIDEncryptMode,
       "hh3cDot11StationRxSNR": hh3cDot11StationRxSNR,
       "hh3cDot11StationTxRate": hh3cDot11StationTxRate,
       "hh3cDot11StationRxRate": hh3cDot11StationRxRate,
       "hh3cDot11StationVendorName": hh3cDot11StationVendorName,
       "hh3cDot11StationRadioMode": hh3cDot11StationRadioMode,
       "hh3cDot11StationRxNoise": hh3cDot11StationRxNoise,
       "hh3cDot11StationMACAddress": hh3cDot11StationMACAddress,
       "hh3cDot11StationTxSpeed": hh3cDot11StationTxSpeed,
       "hh3cDot11StationRxSpeed": hh3cDot11StationRxSpeed,
       "hh3cDot11StationWmmMode": hh3cDot11StationWmmMode,
       "hh3cDot11StationSecIEStatus": hh3cDot11StationSecIEStatus,
       "hh3cDot11StationUpTimeTicks": hh3cDot11StationUpTimeTicks,
       "hh3cDot11StationAPRelationTable": hh3cDot11StationAPRelationTable,
       "hh3cDot11StationAPRelationEntry": hh3cDot11StationAPRelationEntry,
       "hh3cDot11CurrAPID": hh3cDot11CurrAPID,
       "hh3cDot11CurrRadioID": hh3cDot11CurrRadioID,
       "hh3cDot11CurrWlanID": hh3cDot11CurrWlanID,
       "hh3cDot11StationStatisTable": hh3cDot11StationStatisTable,
       "hh3cDot11StationStatisEntry": hh3cDot11StationStatisEntry,
       "hh3cDot11StationRxFrameCnt": hh3cDot11StationRxFrameCnt,
       "hh3cDot11StationTxFrameCnt": hh3cDot11StationTxFrameCnt,
       "hh3cDot11StationDropFrameCnt": hh3cDot11StationDropFrameCnt,
       "hh3cDot11StationRxFrameBytes": hh3cDot11StationRxFrameBytes,
       "hh3cDot11StationTxFrameBytes": hh3cDot11StationTxFrameBytes,
       "hh3cDot11StationDropFrameBytes": hh3cDot11StationDropFrameBytes,
       "hh3cDot11StationRxRetryPkts": hh3cDot11StationRxRetryPkts,
       "hh3cDot11StationTxRetryPkts": hh3cDot11StationTxRetryPkts,
       "hh3cDot11StationRxRetryBytes": hh3cDot11StationRxRetryBytes,
       "hh3cDot11StationTxRetryBytes": hh3cDot11StationTxRetryBytes,
       "hh3cDot11StationThroughput": hh3cDot11StationThroughput,
       "hh3cDot11StationSuccessTxCnt": hh3cDot11StationSuccessTxCnt,
       "hh3cDot11StationSuccessTxDataCnt": hh3cDot11StationSuccessTxDataCnt,
       "hh3cDot11StationRxDataFrameCnt": hh3cDot11StationRxDataFrameCnt,
       "hh3cDot11StationTxDataFrameCnt": hh3cDot11StationTxDataFrameCnt,
       "hh3cDot11StationRxDataFrameBytes": hh3cDot11StationRxDataFrameBytes,
       "hh3cDot11StationTxDataFrameBytes": hh3cDot11StationTxDataFrameBytes,
       "hh3cDot11StationRxFragCnt": hh3cDot11StationRxFragCnt,
       "hh3cDot11StaRxErrDataFrameCnt": hh3cDot11StaRxErrDataFrameCnt,
       "hh3cDot11StaTxRetryDataFrameCnt": hh3cDot11StaTxRetryDataFrameCnt,
       "hh3cDot11StationNotifyGroup": hh3cDot11StationNotifyGroup,
       "hh3cDot11StationTraps": hh3cDot11StationTraps,
       "hh3cDot11StationMICErrorTrap": hh3cDot11StationMICErrorTrap,
       "hh3cDot11StationAuthenErrorTrap": hh3cDot11StationAuthenErrorTrap,
       "hh3cDot11StationAuthorFailTrap": hh3cDot11StationAuthorFailTrap,
       "hh3cDot11StationAssocFailTrap": hh3cDot11StationAssocFailTrap,
       "hh3cDot11StationDeAssocTrap": hh3cDot11StationDeAssocTrap,
       "hh3cDot11StationAuthorSuccTrap": hh3cDot11StationAuthorSuccTrap,
       "hh3cDot11StationRoamingTrap": hh3cDot11StationRoamingTrap,
       "hh3cDot11StationDisconnectTrap": hh3cDot11StationDisconnectTrap,
       "hh3cDot11StationTrapVarObjects": hh3cDot11StationTrapVarObjects,
       "hh3cDot11StationTrapBSSID": hh3cDot11StationTrapBSSID,
       "hh3cDot11StationTrapStaMAC": hh3cDot11StationTrapStaMAC,
       "hh3cDot11StationSessionStartTime": hh3cDot11StationSessionStartTime,
       "hh3cDot11StationAssocFailCause": hh3cDot11StationAssocFailCause,
       "hh3cDot11StationAuthorFailCause": hh3cDot11StationAuthorFailCause,
       "hh3cDot11StationFailCauseDesc": hh3cDot11StationFailCauseDesc,
       "hh3cDot11StationSessionDuration": hh3cDot11StationSessionDuration,
       "hh3cDot11StationRoamingTime": hh3cDot11StationRoamingTime,
       "hh3cDot11StationACIPAddress": hh3cDot11StationACIPAddress,
       "hh3cDot11StationAPName": hh3cDot11StationAPName,
       "hh3cDot11StationBSSID": hh3cDot11StationBSSID,
       "hh3cDot11StaDisconnectReason": hh3cDot11StaDisconnectReason,
       "hh3cDot11StationAuthMode": hh3cDot11StationAuthMode,
       "hh3cDot11StationACIPv6Add": hh3cDot11StationACIPv6Add}
)
