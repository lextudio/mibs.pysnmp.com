# SNMP MIB module (NETFINITYMANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETFINITYMANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:45 2024
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

(dmiMibs,) = mibBuilder.importSymbols(
    "NETFINITYSERVICES-MIB",
    "dmiMibs")

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



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiDate(OctetString):
    """Custom type DmiDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )





class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetFinityManagerMIB_ObjectIdentity = ObjectIdentity
netFinityManagerMIB = _NetFinityManagerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3)
)
_DmtfGroups2_ObjectIdentity = ObjectIdentity
dmtfGroups2 = _DmtfGroups2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1)
)
_TComponentid2_Object = MibTable
tComponentid2 = _TComponentid2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid2.setStatus("mandatory")
_EComponentid2_Object = MibTableRow
eComponentid2 = _EComponentid2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 1, 1)
)
eComponentid2.setIndexNames(
    (0, "NETFINITYMANAGER-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid2.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_TRemoteSystems_Object = MibTable
tRemoteSystems = _TRemoteSystems_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11)
)
if mibBuilder.loadTexts:
    tRemoteSystems.setStatus("mandatory")
_ERemoteSystems_Object = MibTableRow
eRemoteSystems = _ERemoteSystems_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1)
)
eRemoteSystems.setIndexNames(
    (0, "NETFINITYMANAGER-MIB", "DmiComponentIndex"),
    (0, "NETFINITYMANAGER-MIB", "a11SystemTag"),
)
if mibBuilder.loadTexts:
    eRemoteSystems.setStatus("mandatory")
_A11SystemTag_Type = DmiInteger
_A11SystemTag_Object = MibTableColumn
a11SystemTag = _A11SystemTag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 1),
    _A11SystemTag_Type()
)
a11SystemTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemTag.setStatus("mandatory")
_A11SystemName_Type = DmiDisplaystring
_A11SystemName_Object = MibTableColumn
a11SystemName = _A11SystemName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 2),
    _A11SystemName_Type()
)
a11SystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemName.setStatus("mandatory")
_A11ProtocolName_Type = DmiDisplaystring
_A11ProtocolName_Object = MibTableColumn
a11ProtocolName = _A11ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 3),
    _A11ProtocolName_Type()
)
a11ProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11ProtocolName.setStatus("mandatory")
_A11NetworkAddress_Type = DmiDisplaystring
_A11NetworkAddress_Object = MibTableColumn
a11NetworkAddress = _A11NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 4),
    _A11NetworkAddress_Type()
)
a11NetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11NetworkAddress.setStatus("mandatory")


class _A11SystemState_Type(Integer32):
    """Custom type a11SystemState based on Integer32"""
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
        *(("vOff-line", 0),
          ("vOff-lineWithErrorCondition", 2),
          ("vOn-line", 1),
          ("vOn-lineWithErrorCondition", 3))
    )


_A11SystemState_Type.__name__ = "Integer32"
_A11SystemState_Object = MibTableColumn
a11SystemState = _A11SystemState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 5),
    _A11SystemState_Type()
)
a11SystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemState.setStatus("mandatory")


class _A11Server_Type(Integer32):
    """Custom type a11Server based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A11Server_Type.__name__ = "Integer32"
_A11Server_Object = MibTableColumn
a11Server = _A11Server_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 6),
    _A11Server_Type()
)
a11Server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Server.setStatus("mandatory")


class _A11Manager_Type(Integer32):
    """Custom type a11Manager based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A11Manager_Type.__name__ = "Integer32"
_A11Manager_Object = MibTableColumn
a11Manager = _A11Manager_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 7),
    _A11Manager_Type()
)
a11Manager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Manager.setStatus("mandatory")


class _A11OperatingSystemType_Type(Integer32):
    """Custom type a11OperatingSystemType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("vBanyanVines", 6),
          ("vIbmAix", 5),
          ("vIbmOs2", 1),
          ("vIbmPc-dos", 7),
          ("vMicrosoftWindows", 2),
          ("vMicrosoftWindows95", 11),
          ("vMicrosoftWindowsNt", 4),
          ("vNovellNetware", 3),
          ("vScoXenix", 8),
          ("vUnixSystemV", 9),
          ("vUnknown", 0))
    )


_A11OperatingSystemType_Type.__name__ = "Integer32"
_A11OperatingSystemType_Object = MibTableColumn
a11OperatingSystemType = _A11OperatingSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 8),
    _A11OperatingSystemType_Type()
)
a11OperatingSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11OperatingSystemType.setStatus("mandatory")
_A11OsMajorVersion_Type = DmiInteger
_A11OsMajorVersion_Object = MibTableColumn
a11OsMajorVersion = _A11OsMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 9),
    _A11OsMajorVersion_Type()
)
a11OsMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11OsMajorVersion.setStatus("mandatory")
_A11OsMinorVersion_Type = DmiInteger
_A11OsMinorVersion_Object = MibTableColumn
a11OsMinorVersion = _A11OsMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 10),
    _A11OsMinorVersion_Type()
)
a11OsMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11OsMinorVersion.setStatus("mandatory")
_A11SystemModelId_Type = DmiOctetstring
_A11SystemModelId_Object = MibTableColumn
a11SystemModelId = _A11SystemModelId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 11),
    _A11SystemModelId_Type()
)
a11SystemModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemModelId.setStatus("mandatory")
_A11SystemModelName_Type = DmiDisplaystring
_A11SystemModelName_Object = MibTableColumn
a11SystemModelName = _A11SystemModelName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 12),
    _A11SystemModelName_Type()
)
a11SystemModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemModelName.setStatus("mandatory")


class _A11SystemOn_lineNotify_Type(Integer32):
    """Custom type a11SystemOn_lineNotify based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 255),
          ("vNoDefault", 254),
          ("vSev0", 0),
          ("vSev1", 1),
          ("vSev2", 2),
          ("vSev3", 3),
          ("vSev4", 4),
          ("vSev5", 5),
          ("vSev6", 6),
          ("vSev7", 7))
    )


_A11SystemOn_lineNotify_Type.__name__ = "Integer32"
_A11SystemOn_lineNotify_Object = MibScalar
a11SystemOn_lineNotify = _A11SystemOn_lineNotify_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 13),
    _A11SystemOn_lineNotify_Type()
)
a11SystemOn_lineNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemOn_lineNotify.setStatus("mandatory")


class _A11SystemOff_lineNotify_Type(Integer32):
    """Custom type a11SystemOff_lineNotify based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 255),
          ("vNoDefault", 254),
          ("vSev0", 0),
          ("vSev1", 1),
          ("vSev2", 2),
          ("vSev3", 3),
          ("vSev4", 4),
          ("vSev5", 5),
          ("vSev6", 6),
          ("vSev7", 7))
    )


_A11SystemOff_lineNotify_Type.__name__ = "Integer32"
_A11SystemOff_lineNotify_Object = MibScalar
a11SystemOff_lineNotify = _A11SystemOff_lineNotify_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 14),
    _A11SystemOff_lineNotify_Type()
)
a11SystemOff_lineNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11SystemOff_lineNotify.setStatus("mandatory")
_A11PresenceCheckInterval_Type = DmiInteger
_A11PresenceCheckInterval_Object = MibTableColumn
a11PresenceCheckInterval = _A11PresenceCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 15),
    _A11PresenceCheckInterval_Type()
)
a11PresenceCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11PresenceCheckInterval.setStatus("mandatory")
_A11MacAddress_Type = DmiOctetstring
_A11MacAddress_Object = MibTableColumn
a11MacAddress = _A11MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 11, 1, 16),
    _A11MacAddress_Type()
)
a11MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11MacAddress.setStatus("mandatory")
_TRemoteSystemGroups_Object = MibTable
tRemoteSystemGroups = _TRemoteSystemGroups_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12)
)
if mibBuilder.loadTexts:
    tRemoteSystemGroups.setStatus("mandatory")
_ERemoteSystemGroups_Object = MibTableRow
eRemoteSystemGroups = _ERemoteSystemGroups_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1)
)
eRemoteSystemGroups.setIndexNames(
    (0, "NETFINITYMANAGER-MIB", "DmiComponentIndex"),
    (0, "NETFINITYMANAGER-MIB", "a12GroupTag"),
)
if mibBuilder.loadTexts:
    eRemoteSystemGroups.setStatus("mandatory")
_A12GroupTag_Type = DmiInteger
_A12GroupTag_Object = MibTableColumn
a12GroupTag = _A12GroupTag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 1),
    _A12GroupTag_Type()
)
a12GroupTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12GroupTag.setStatus("mandatory")
_A12GroupName_Type = DmiDisplaystring
_A12GroupName_Object = MibTableColumn
a12GroupName = _A12GroupName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 2),
    _A12GroupName_Type()
)
a12GroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12GroupName.setStatus("mandatory")


class _A12RequiredKeywordsCombination_Type(Integer32):
    """Custom type a12RequiredKeywordsCombination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vAllKeywordsMustMatch", 0),
          ("vAnyOfTheKeywordsMayMatch", 1),
          ("vExactlyOneOfTheKeywordsMustMatch", 2))
    )


_A12RequiredKeywordsCombination_Type.__name__ = "Integer32"
_A12RequiredKeywordsCombination_Object = MibTableColumn
a12RequiredKeywordsCombination = _A12RequiredKeywordsCombination_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 3),
    _A12RequiredKeywordsCombination_Type()
)
a12RequiredKeywordsCombination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12RequiredKeywordsCombination.setStatus("mandatory")
_A12Keywords_Type = DmiDisplaystring
_A12Keywords_Object = MibTableColumn
a12Keywords = _A12Keywords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 4),
    _A12Keywords_Type()
)
a12Keywords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12Keywords.setStatus("mandatory")


class _A12SystemOn_lineNotifyDefault_Type(Integer32):
    """Custom type a12SystemOn_lineNotifyDefault based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 255),
          ("vNoDefault", 254),
          ("vSev0", 0),
          ("vSev1", 1),
          ("vSev2", 2),
          ("vSev3", 3),
          ("vSev4", 4),
          ("vSev5", 5),
          ("vSev6", 6),
          ("vSev7", 7))
    )


_A12SystemOn_lineNotifyDefault_Type.__name__ = "Integer32"
_A12SystemOn_lineNotifyDefault_Object = MibScalar
a12SystemOn_lineNotifyDefault = _A12SystemOn_lineNotifyDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 5),
    _A12SystemOn_lineNotifyDefault_Type()
)
a12SystemOn_lineNotifyDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SystemOn_lineNotifyDefault.setStatus("mandatory")


class _A12SystemOff_lineNotifyDefault_Type(Integer32):
    """Custom type a12SystemOff_lineNotifyDefault based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("vDisabled", 255),
          ("vNoDefault", 254),
          ("vSev0", 0),
          ("vSev1", 1),
          ("vSev2", 2),
          ("vSev3", 3),
          ("vSev4", 4),
          ("vSev5", 5),
          ("vSev6", 6),
          ("vSev7", 7))
    )


_A12SystemOff_lineNotifyDefault_Type.__name__ = "Integer32"
_A12SystemOff_lineNotifyDefault_Object = MibScalar
a12SystemOff_lineNotifyDefault = _A12SystemOff_lineNotifyDefault_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 6),
    _A12SystemOff_lineNotifyDefault_Type()
)
a12SystemOff_lineNotifyDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12SystemOff_lineNotifyDefault.setStatus("mandatory")
_A12DefaultPresenceCheckInterval_Type = DmiInteger
_A12DefaultPresenceCheckInterval_Object = MibTableColumn
a12DefaultPresenceCheckInterval = _A12DefaultPresenceCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 7),
    _A12DefaultPresenceCheckInterval_Type()
)
a12DefaultPresenceCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12DefaultPresenceCheckInterval.setStatus("mandatory")
_A12DiscoveryStartFlag_Type = DmiInteger
_A12DiscoveryStartFlag_Object = MibTableColumn
a12DiscoveryStartFlag = _A12DiscoveryStartFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 12, 1, 8),
    _A12DiscoveryStartFlag_Type()
)
a12DiscoveryStartFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a12DiscoveryStartFlag.setStatus("mandatory")
_TRemoteSystemGroupMap_Object = MibTable
tRemoteSystemGroupMap = _TRemoteSystemGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 13)
)
if mibBuilder.loadTexts:
    tRemoteSystemGroupMap.setStatus("mandatory")
_ERemoteSystemGroupMap_Object = MibTableRow
eRemoteSystemGroupMap = _ERemoteSystemGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 13, 1)
)
eRemoteSystemGroupMap.setIndexNames(
    (0, "NETFINITYMANAGER-MIB", "DmiComponentIndex"),
    (0, "NETFINITYMANAGER-MIB", "a13SystemTag"),
    (0, "NETFINITYMANAGER-MIB", "a13GroupTag"),
)
if mibBuilder.loadTexts:
    eRemoteSystemGroupMap.setStatus("mandatory")
_A13SystemTag_Type = DmiInteger
_A13SystemTag_Object = MibTableColumn
a13SystemTag = _A13SystemTag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 13, 1, 1),
    _A13SystemTag_Type()
)
a13SystemTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13SystemTag.setStatus("mandatory")
_A13GroupTag_Type = DmiInteger
_A13GroupTag_Object = MibTableColumn
a13GroupTag = _A13GroupTag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 71, 200, 3, 1, 13, 1, 2),
    _A13GroupTag_Type()
)
a13GroupTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13GroupTag.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETFINITYMANAGER-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiDate": DmiDate,
       "DmiComponentIndex": DmiComponentIndex,
       "netFinityManagerMIB": netFinityManagerMIB,
       "dmtfGroups2": dmtfGroups2,
       "tComponentid2": tComponentid2,
       "eComponentid2": eComponentid2,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "tRemoteSystems": tRemoteSystems,
       "eRemoteSystems": eRemoteSystems,
       "a11SystemTag": a11SystemTag,
       "a11SystemName": a11SystemName,
       "a11ProtocolName": a11ProtocolName,
       "a11NetworkAddress": a11NetworkAddress,
       "a11SystemState": a11SystemState,
       "a11Server": a11Server,
       "a11Manager": a11Manager,
       "a11OperatingSystemType": a11OperatingSystemType,
       "a11OsMajorVersion": a11OsMajorVersion,
       "a11OsMinorVersion": a11OsMinorVersion,
       "a11SystemModelId": a11SystemModelId,
       "a11SystemModelName": a11SystemModelName,
       "a11SystemOn-lineNotify": a11SystemOn_lineNotify,
       "a11SystemOff-lineNotify": a11SystemOff_lineNotify,
       "a11PresenceCheckInterval": a11PresenceCheckInterval,
       "a11MacAddress": a11MacAddress,
       "tRemoteSystemGroups": tRemoteSystemGroups,
       "eRemoteSystemGroups": eRemoteSystemGroups,
       "a12GroupTag": a12GroupTag,
       "a12GroupName": a12GroupName,
       "a12RequiredKeywordsCombination": a12RequiredKeywordsCombination,
       "a12Keywords": a12Keywords,
       "a12SystemOn-lineNotifyDefault": a12SystemOn_lineNotifyDefault,
       "a12SystemOff-lineNotifyDefault": a12SystemOff_lineNotifyDefault,
       "a12DefaultPresenceCheckInterval": a12DefaultPresenceCheckInterval,
       "a12DiscoveryStartFlag": a12DiscoveryStartFlag,
       "tRemoteSystemGroupMap": tRemoteSystemGroupMap,
       "eRemoteSystemGroupMap": eRemoteSystemGroupMap,
       "a13SystemTag": a13SystemTag,
       "a13GroupTag": a13GroupTag}
)
