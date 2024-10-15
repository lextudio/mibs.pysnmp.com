# SNMP MIB module (ADTRAN-AOS-3G) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-3G
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:03 2024
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

(adGenAOSConformance,
 adGenAOSWan) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSWan")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenAOS3GMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 6, 2)
)
adGenAOS3GMib.setRevisions(
        ("2010-01-05 00:00",
         "2010-01-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOS3G_ObjectIdentity = ObjectIdentity
adGenAOS3G = _AdGenAOS3G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2)
)
_AdGenAOS3GTraps_ObjectIdentity = ObjectIdentity
adGenAOS3GTraps = _AdGenAOS3GTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0)
)
if mibBuilder.loadTexts:
    adGenAOS3GTraps.setStatus("current")
_AdGenAOS3GTable_Object = MibTable
adGenAOS3GTable = _AdGenAOS3GTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOS3GTable.setStatus("current")
_AdGenAOS3GEntry_Object = MibTableRow
adGenAOS3GEntry = _AdGenAOS3GEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1)
)
adGenAOS3GEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAOS3GEntry.setStatus("current")
_AdGenAOS3GNetworkAccessID_Type = DisplayString
_AdGenAOS3GNetworkAccessID_Object = MibTableColumn
adGenAOS3GNetworkAccessID = _AdGenAOS3GNetworkAccessID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 1),
    _AdGenAOS3GNetworkAccessID_Type()
)
adGenAOS3GNetworkAccessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GNetworkAccessID.setStatus("current")


class _AdGenAOS3GHASS_Type(Bits):
    """Custom type adGenAOS3GHASS based on Bits"""
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 0))
    )

_AdGenAOS3GHASS_Type.__name__ = "Bits"
_AdGenAOS3GHASS_Object = MibTableColumn
adGenAOS3GHASS = _AdGenAOS3GHASS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 2),
    _AdGenAOS3GHASS_Type()
)
adGenAOS3GHASS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GHASS.setStatus("current")
_AdGenAOS3GHASPI_Type = Unsigned32
_AdGenAOS3GHASPI_Object = MibTableColumn
adGenAOS3GHASPI = _AdGenAOS3GHASPI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 3),
    _AdGenAOS3GHASPI_Type()
)
adGenAOS3GHASPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GHASPI.setStatus("current")


class _AdGenAOS3GAAASS_Type(Bits):
    """Custom type adGenAOS3GAAASS based on Bits"""
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 0))
    )

_AdGenAOS3GAAASS_Type.__name__ = "Bits"
_AdGenAOS3GAAASS_Object = MibTableColumn
adGenAOS3GAAASS = _AdGenAOS3GAAASS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 4),
    _AdGenAOS3GAAASS_Type()
)
adGenAOS3GAAASS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GAAASS.setStatus("current")
_AdGenAOS3GAAASPI_Type = Unsigned32
_AdGenAOS3GAAASPI_Object = MibTableColumn
adGenAOS3GAAASPI = _AdGenAOS3GAAASPI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 5),
    _AdGenAOS3GAAASPI_Type()
)
adGenAOS3GAAASPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GAAASPI.setStatus("current")


class _AdGenAOS3GReverseTunneling_Type(Bits):
    """Custom type adGenAOS3GReverseTunneling based on Bits"""
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 0))
    )

_AdGenAOS3GReverseTunneling_Type.__name__ = "Bits"
_AdGenAOS3GReverseTunneling_Object = MibTableColumn
adGenAOS3GReverseTunneling = _AdGenAOS3GReverseTunneling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 6),
    _AdGenAOS3GReverseTunneling_Type()
)
adGenAOS3GReverseTunneling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GReverseTunneling.setStatus("current")
_AdGenAOS3GHomeAddress_Type = IpAddress
_AdGenAOS3GHomeAddress_Object = MibTableColumn
adGenAOS3GHomeAddress = _AdGenAOS3GHomeAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 7),
    _AdGenAOS3GHomeAddress_Type()
)
adGenAOS3GHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GHomeAddress.setStatus("current")
_AdGenAOS3GPrimaryHomeAddress_Type = IpAddress
_AdGenAOS3GPrimaryHomeAddress_Object = MibTableColumn
adGenAOS3GPrimaryHomeAddress = _AdGenAOS3GPrimaryHomeAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 8),
    _AdGenAOS3GPrimaryHomeAddress_Type()
)
adGenAOS3GPrimaryHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GPrimaryHomeAddress.setStatus("current")
_AdGenAOS3GSecHomeAddress_Type = IpAddress
_AdGenAOS3GSecHomeAddress_Object = MibTableColumn
adGenAOS3GSecHomeAddress = _AdGenAOS3GSecHomeAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 9),
    _AdGenAOS3GSecHomeAddress_Type()
)
adGenAOS3GSecHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GSecHomeAddress.setStatus("current")
_AdGenAOS3GRSSI_Type = Integer32
_AdGenAOS3GRSSI_Object = MibTableColumn
adGenAOS3GRSSI = _AdGenAOS3GRSSI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 10),
    _AdGenAOS3GRSSI_Type()
)
adGenAOS3GRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GRSSI.setStatus("current")
_AdGenAOS3GECIO_Type = DisplayString
_AdGenAOS3GECIO_Object = MibTableColumn
adGenAOS3GECIO = _AdGenAOS3GECIO_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 11),
    _AdGenAOS3GECIO_Type()
)
adGenAOS3GECIO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GECIO.setStatus("current")
_AdGenAOS3GPnOffset_Type = Integer32
_AdGenAOS3GPnOffset_Object = MibTableColumn
adGenAOS3GPnOffset = _AdGenAOS3GPnOffset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 12),
    _AdGenAOS3GPnOffset_Type()
)
adGenAOS3GPnOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GPnOffset.setStatus("current")
_AdGenAOS3GServiceType_Type = DisplayString
_AdGenAOS3GServiceType_Object = MibTableColumn
adGenAOS3GServiceType = _AdGenAOS3GServiceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 13),
    _AdGenAOS3GServiceType_Type()
)
adGenAOS3GServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GServiceType.setStatus("current")


class _AdGenAOS3GServiceTypePreference_Type(Integer32):
    """Custom type adGenAOS3GServiceTypePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("mode1xEVDO", 10),
          ("mode1xRTT", 9),
          ("modeAUTO", 4))
    )


_AdGenAOS3GServiceTypePreference_Type.__name__ = "Integer32"
_AdGenAOS3GServiceTypePreference_Object = MibTableColumn
adGenAOS3GServiceTypePreference = _AdGenAOS3GServiceTypePreference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 14),
    _AdGenAOS3GServiceTypePreference_Type()
)
adGenAOS3GServiceTypePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOS3GServiceTypePreference.setStatus("current")
_AdGenAOS3GConnectionState_Type = DisplayString
_AdGenAOS3GConnectionState_Object = MibTableColumn
adGenAOS3GConnectionState = _AdGenAOS3GConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 15),
    _AdGenAOS3GConnectionState_Type()
)
adGenAOS3GConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GConnectionState.setStatus("current")
_AdGenAOS3GECIOIntegerValue_Type = Integer32
_AdGenAOS3GECIOIntegerValue_Object = MibTableColumn
adGenAOS3GECIOIntegerValue = _AdGenAOS3GECIOIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 1, 1, 16),
    _AdGenAOS3GECIOIntegerValue_Type()
)
adGenAOS3GECIOIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GECIOIntegerValue.setStatus("current")
_AdGenAOS3GHardwareDataTable_Object = MibTable
adGenAOS3GHardwareDataTable = _AdGenAOS3GHardwareDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2)
)
if mibBuilder.loadTexts:
    adGenAOS3GHardwareDataTable.setStatus("current")
_AdGenAOS3GHardwareDataEntry_Object = MibTableRow
adGenAOS3GHardwareDataEntry = _AdGenAOS3GHardwareDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1)
)
adGenAOS3GHardwareDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAOS3GHardwareDataEntry.setStatus("current")
_AdGenAOS3GSystemID_Type = Unsigned32
_AdGenAOS3GSystemID_Object = MibTableColumn
adGenAOS3GSystemID = _AdGenAOS3GSystemID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 1),
    _AdGenAOS3GSystemID_Type()
)
adGenAOS3GSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GSystemID.setStatus("current")
_AdGenAOS3GNetworkID_Type = DisplayString
_AdGenAOS3GNetworkID_Object = MibTableColumn
adGenAOS3GNetworkID = _AdGenAOS3GNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 2),
    _AdGenAOS3GNetworkID_Type()
)
adGenAOS3GNetworkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GNetworkID.setStatus("current")
_AdGenAOS3GPrefferedRoamList_Type = Unsigned32
_AdGenAOS3GPrefferedRoamList_Object = MibTableColumn
adGenAOS3GPrefferedRoamList = _AdGenAOS3GPrefferedRoamList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 3),
    _AdGenAOS3GPrefferedRoamList_Type()
)
adGenAOS3GPrefferedRoamList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GPrefferedRoamList.setStatus("current")
_AdGenAOS3GMobileDirNumber_Type = DisplayString
_AdGenAOS3GMobileDirNumber_Object = MibTableColumn
adGenAOS3GMobileDirNumber = _AdGenAOS3GMobileDirNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 4),
    _AdGenAOS3GMobileDirNumber_Type()
)
adGenAOS3GMobileDirNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GMobileDirNumber.setStatus("current")
_AdGenAOS3GESN_Type = DisplayString
_AdGenAOS3GESN_Object = MibTableColumn
adGenAOS3GESN = _AdGenAOS3GESN_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 5),
    _AdGenAOS3GESN_Type()
)
adGenAOS3GESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GESN.setStatus("current")
_AdGenAOS3GMobileStationID_Type = DisplayString
_AdGenAOS3GMobileStationID_Object = MibTableColumn
adGenAOS3GMobileStationID = _AdGenAOS3GMobileStationID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 6),
    _AdGenAOS3GMobileStationID_Type()
)
adGenAOS3GMobileStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GMobileStationID.setStatus("current")
_AdGenAOS3GHardwareVersion_Type = DisplayString
_AdGenAOS3GHardwareVersion_Object = MibTableColumn
adGenAOS3GHardwareVersion = _AdGenAOS3GHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 7),
    _AdGenAOS3GHardwareVersion_Type()
)
adGenAOS3GHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GHardwareVersion.setStatus("current")
_AdGenAOS3GFirmwareVersion_Type = DisplayString
_AdGenAOS3GFirmwareVersion_Object = MibTableColumn
adGenAOS3GFirmwareVersion = _AdGenAOS3GFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 2, 1, 8),
    _AdGenAOS3GFirmwareVersion_Type()
)
adGenAOS3GFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOS3GFirmwareVersion.setStatus("current")
_AdGenAOS3GThresholdDataTable_Object = MibTable
adGenAOS3GThresholdDataTable = _AdGenAOS3GThresholdDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3)
)
if mibBuilder.loadTexts:
    adGenAOS3GThresholdDataTable.setStatus("current")
_AdGenAOS3GThresholdDataEntry_Object = MibTableRow
adGenAOS3GThresholdDataEntry = _AdGenAOS3GThresholdDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1)
)
adGenAOS3GThresholdDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAOS3GThresholdDataEntry.setStatus("current")


class _AdGenAOS3GEnableTraps_Type(Integer32):
    """Custom type adGenAOS3GEnableTraps based on Integer32"""
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


_AdGenAOS3GEnableTraps_Type.__name__ = "Integer32"
_AdGenAOS3GEnableTraps_Object = MibTableColumn
adGenAOS3GEnableTraps = _AdGenAOS3GEnableTraps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 1),
    _AdGenAOS3GEnableTraps_Type()
)
adGenAOS3GEnableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOS3GEnableTraps.setStatus("current")


class _AdGenAOS3GRSSIThreshold_Type(Integer32):
    """Custom type adGenAOS3GRSSIThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_AdGenAOS3GRSSIThreshold_Type.__name__ = "Integer32"
_AdGenAOS3GRSSIThreshold_Object = MibTableColumn
adGenAOS3GRSSIThreshold = _AdGenAOS3GRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 2),
    _AdGenAOS3GRSSIThreshold_Type()
)
adGenAOS3GRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOS3GRSSIThreshold.setStatus("current")


class _AdGenAOS3GECIOThreshold_Type(Integer32):
    """Custom type adGenAOS3GECIOThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_AdGenAOS3GECIOThreshold_Type.__name__ = "Integer32"
_AdGenAOS3GECIOThreshold_Object = MibTableColumn
adGenAOS3GECIOThreshold = _AdGenAOS3GECIOThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 3, 1, 3),
    _AdGenAOS3GECIOThreshold_Type()
)
adGenAOS3GECIOThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOS3GECIOThreshold.setStatus("current")
_AdGenAOS3GConformance_ObjectIdentity = ObjectIdentity
adGenAOS3GConformance = _AdGenAOS3GConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9)
)
_AdGenAOS3GGroup_ObjectIdentity = ObjectIdentity
adGenAOS3GGroup = _AdGenAOS3GGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1)
)
_AdGenAOS3GCompliances_ObjectIdentity = ObjectIdentity
adGenAOS3GCompliances = _AdGenAOS3GCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 2)
)

# Managed Objects groups

adGenAOS3GTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 1)
)
adGenAOS3GTableGroup.setObjects(
      *(("ADTRAN-AOS-3G", "adGenAOS3GNetworkAccessID"),
        ("ADTRAN-AOS-3G", "adGenAOS3GHASS"),
        ("ADTRAN-AOS-3G", "adGenAOS3GHASPI"),
        ("ADTRAN-AOS-3G", "adGenAOS3GAAASS"),
        ("ADTRAN-AOS-3G", "adGenAOS3GAAASPI"),
        ("ADTRAN-AOS-3G", "adGenAOS3GReverseTunneling"),
        ("ADTRAN-AOS-3G", "adGenAOS3GHomeAddress"),
        ("ADTRAN-AOS-3G", "adGenAOS3GPrimaryHomeAddress"),
        ("ADTRAN-AOS-3G", "adGenAOS3GSecHomeAddress"),
        ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"),
        ("ADTRAN-AOS-3G", "adGenAOS3GECIO"),
        ("ADTRAN-AOS-3G", "adGenAOS3GPnOffset"),
        ("ADTRAN-AOS-3G", "adGenAOS3GServiceType"),
        ("ADTRAN-AOS-3G", "adGenAOS3GServiceTypePreference"),
        ("ADTRAN-AOS-3G", "adGenAOS3GConnectionState"),
        ("ADTRAN-AOS-3G", "adGenAOS3GECIOIntegerValue"))
)
if mibBuilder.loadTexts:
    adGenAOS3GTableGroup.setStatus("current")

adGenAOS3GHardwareDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 2)
)
adGenAOS3GHardwareDataGroup.setObjects(
      *(("ADTRAN-AOS-3G", "adGenAOS3GSystemID"),
        ("ADTRAN-AOS-3G", "adGenAOS3GNetworkID"),
        ("ADTRAN-AOS-3G", "adGenAOS3GPrefferedRoamList"),
        ("ADTRAN-AOS-3G", "adGenAOS3GMobileDirNumber"),
        ("ADTRAN-AOS-3G", "adGenAOS3GESN"),
        ("ADTRAN-AOS-3G", "adGenAOS3GMobileStationID"),
        ("ADTRAN-AOS-3G", "adGenAOS3GHardwareVersion"),
        ("ADTRAN-AOS-3G", "adGenAOS3GFirmwareVersion"))
)
if mibBuilder.loadTexts:
    adGenAOS3GHardwareDataGroup.setStatus("current")

adGenAOS3GThresholdDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 3)
)
adGenAOS3GThresholdDataGroup.setObjects(
      *(("ADTRAN-AOS-3G", "adGenAOS3GEnableTraps"),
        ("ADTRAN-AOS-3G", "adGenAOS3GRSSIThreshold"),
        ("ADTRAN-AOS-3G", "adGenAOS3GECIOThreshold"))
)
if mibBuilder.loadTexts:
    adGenAOS3GThresholdDataGroup.setStatus("current")


# Notification objects

rssiDataRangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 1)
)
rssiDataRangeAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"))
)
if mibBuilder.loadTexts:
    rssiDataRangeAlarm.setStatus(
        "current"
    )

ecioDataRangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 2)
)
ecioDataRangeAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-AOS-3G", "adGenAOS3GECIO"))
)
if mibBuilder.loadTexts:
    ecioDataRangeAlarm.setStatus(
        "current"
    )

rssiDataRangeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 3)
)
rssiDataRangeClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-AOS-3G", "adGenAOS3GRSSI"))
)
if mibBuilder.loadTexts:
    rssiDataRangeClear.setStatus(
        "current"
    )

ecioDataRangeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 4)
)
ecioDataRangeClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-AOS-3G", "adGenAOS3GECIO"))
)
if mibBuilder.loadTexts:
    ecioDataRangeClear.setStatus(
        "current"
    )

configValueSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 5)
)
configValueSet.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    configValueSet.setStatus(
        "current"
    )

modemResetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 6)
)
modemResetAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    modemResetAlarm.setStatus(
        "current"
    )

serviceTypeChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 7)
)
serviceTypeChangeAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-AOS-3G", "adGenAOS3GServiceType"))
)
if mibBuilder.loadTexts:
    serviceTypeChangeAlarm.setStatus(
        "current"
    )

connectionStateDownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 6, 2, 0, 8)
)
connectionStateDownAlarm.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    connectionStateDownAlarm.setStatus(
        "current"
    )


# Notifications groups

adGenAOS3GTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 1, 4)
)
adGenAOS3GTrapGroup.setObjects(
      *(("ADTRAN-AOS-3G", "rssiDataRangeAlarm"),
        ("ADTRAN-AOS-3G", "ecioDataRangeAlarm"),
        ("ADTRAN-AOS-3G", "rssiDataRangeClear"),
        ("ADTRAN-AOS-3G", "ecioDataRangeClear"),
        ("ADTRAN-AOS-3G", "configValueSet"),
        ("ADTRAN-AOS-3G", "modemResetAlarm"),
        ("ADTRAN-AOS-3G", "serviceTypeChangeAlarm"),
        ("ADTRAN-AOS-3G", "connectionStateDownAlarm"))
)
if mibBuilder.loadTexts:
    adGenAOS3GTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOS3GFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 9, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOS3GFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-3G",
    **{"adGenAOS3G": adGenAOS3G,
       "adGenAOS3GTraps": adGenAOS3GTraps,
       "rssiDataRangeAlarm": rssiDataRangeAlarm,
       "ecioDataRangeAlarm": ecioDataRangeAlarm,
       "rssiDataRangeClear": rssiDataRangeClear,
       "ecioDataRangeClear": ecioDataRangeClear,
       "configValueSet": configValueSet,
       "modemResetAlarm": modemResetAlarm,
       "serviceTypeChangeAlarm": serviceTypeChangeAlarm,
       "connectionStateDownAlarm": connectionStateDownAlarm,
       "adGenAOS3GTable": adGenAOS3GTable,
       "adGenAOS3GEntry": adGenAOS3GEntry,
       "adGenAOS3GNetworkAccessID": adGenAOS3GNetworkAccessID,
       "adGenAOS3GHASS": adGenAOS3GHASS,
       "adGenAOS3GHASPI": adGenAOS3GHASPI,
       "adGenAOS3GAAASS": adGenAOS3GAAASS,
       "adGenAOS3GAAASPI": adGenAOS3GAAASPI,
       "adGenAOS3GReverseTunneling": adGenAOS3GReverseTunneling,
       "adGenAOS3GHomeAddress": adGenAOS3GHomeAddress,
       "adGenAOS3GPrimaryHomeAddress": adGenAOS3GPrimaryHomeAddress,
       "adGenAOS3GSecHomeAddress": adGenAOS3GSecHomeAddress,
       "adGenAOS3GRSSI": adGenAOS3GRSSI,
       "adGenAOS3GECIO": adGenAOS3GECIO,
       "adGenAOS3GPnOffset": adGenAOS3GPnOffset,
       "adGenAOS3GServiceType": adGenAOS3GServiceType,
       "adGenAOS3GServiceTypePreference": adGenAOS3GServiceTypePreference,
       "adGenAOS3GConnectionState": adGenAOS3GConnectionState,
       "adGenAOS3GECIOIntegerValue": adGenAOS3GECIOIntegerValue,
       "adGenAOS3GHardwareDataTable": adGenAOS3GHardwareDataTable,
       "adGenAOS3GHardwareDataEntry": adGenAOS3GHardwareDataEntry,
       "adGenAOS3GSystemID": adGenAOS3GSystemID,
       "adGenAOS3GNetworkID": adGenAOS3GNetworkID,
       "adGenAOS3GPrefferedRoamList": adGenAOS3GPrefferedRoamList,
       "adGenAOS3GMobileDirNumber": adGenAOS3GMobileDirNumber,
       "adGenAOS3GESN": adGenAOS3GESN,
       "adGenAOS3GMobileStationID": adGenAOS3GMobileStationID,
       "adGenAOS3GHardwareVersion": adGenAOS3GHardwareVersion,
       "adGenAOS3GFirmwareVersion": adGenAOS3GFirmwareVersion,
       "adGenAOS3GThresholdDataTable": adGenAOS3GThresholdDataTable,
       "adGenAOS3GThresholdDataEntry": adGenAOS3GThresholdDataEntry,
       "adGenAOS3GEnableTraps": adGenAOS3GEnableTraps,
       "adGenAOS3GRSSIThreshold": adGenAOS3GRSSIThreshold,
       "adGenAOS3GECIOThreshold": adGenAOS3GECIOThreshold,
       "adGenAOS3GConformance": adGenAOS3GConformance,
       "adGenAOS3GGroup": adGenAOS3GGroup,
       "adGenAOS3GTableGroup": adGenAOS3GTableGroup,
       "adGenAOS3GHardwareDataGroup": adGenAOS3GHardwareDataGroup,
       "adGenAOS3GThresholdDataGroup": adGenAOS3GThresholdDataGroup,
       "adGenAOS3GTrapGroup": adGenAOS3GTrapGroup,
       "adGenAOS3GCompliances": adGenAOS3GCompliances,
       "adGenAOS3GFullCompliance": adGenAOS3GFullCompliance,
       "adGenAOS3GMib": adGenAOS3GMib}
)
