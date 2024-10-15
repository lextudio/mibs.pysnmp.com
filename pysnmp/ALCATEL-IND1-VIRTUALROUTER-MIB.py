# SNMP MIB module (ALCATEL-IND1-VIRTUALROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-VIRTUALROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:19 2024
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

(routingIND1Vrf,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Vrf")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1VirtualRouterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1)
)
alcatelIND1VirtualRouterMIB.setRevisions(
        ("2008-03-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBObjects = _AlcatelIND1VirtualRouterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1)
)
_AlaVirtualRouterConfig_ObjectIdentity = ObjectIdentity
alaVirtualRouterConfig = _AlaVirtualRouterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1)
)
_AlaVirtualRouterNameTable_Object = MibTable
alaVirtualRouterNameTable = _AlaVirtualRouterNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaVirtualRouterNameTable.setStatus("current")
_AlaVirtualRouterNameEntry_Object = MibTableRow
alaVirtualRouterNameEntry = _AlaVirtualRouterNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1)
)
alaVirtualRouterNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"),
)
if mibBuilder.loadTexts:
    alaVirtualRouterNameEntry.setStatus("current")


class _AlaVirtualRouterName_Type(SnmpAdminString):
    """Custom type alaVirtualRouterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlaVirtualRouterName_Type.__name__ = "SnmpAdminString"
_AlaVirtualRouterName_Object = MibTableColumn
alaVirtualRouterName = _AlaVirtualRouterName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1),
    _AlaVirtualRouterName_Type()
)
alaVirtualRouterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVirtualRouterName.setStatus("current")
_AlaVirtualRouterNameIndex_Type = Integer32
_AlaVirtualRouterNameIndex_Object = MibTableColumn
alaVirtualRouterNameIndex = _AlaVirtualRouterNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2),
    _AlaVirtualRouterNameIndex_Type()
)
alaVirtualRouterNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterNameIndex.setStatus("current")
_AlaVirtualRouterNameRowStatus_Type = RowStatus
_AlaVirtualRouterNameRowStatus_Object = MibTableColumn
alaVirtualRouterNameRowStatus = _AlaVirtualRouterNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3),
    _AlaVirtualRouterNameRowStatus_Type()
)
alaVirtualRouterNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVirtualRouterNameRowStatus.setStatus("current")


class _AlaVirtualRouterProfile_Type(SnmpAdminString):
    """Custom type alaVirtualRouterProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlaVirtualRouterProfile_Type.__name__ = "SnmpAdminString"
_AlaVirtualRouterProfile_Object = MibTableColumn
alaVirtualRouterProfile = _AlaVirtualRouterProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 4),
    _AlaVirtualRouterProfile_Type()
)
alaVirtualRouterProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVirtualRouterProfile.setStatus("current")
_AlaVirtualRouterMaxRouteMaps_Type = Integer32
_AlaVirtualRouterMaxRouteMaps_Object = MibTableColumn
alaVirtualRouterMaxRouteMaps = _AlaVirtualRouterMaxRouteMaps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 5),
    _AlaVirtualRouterMaxRouteMaps_Type()
)
alaVirtualRouterMaxRouteMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterMaxRouteMaps.setStatus("current")
_AlaVirtualRouterMaxSequences_Type = Integer32
_AlaVirtualRouterMaxSequences_Object = MibTableColumn
alaVirtualRouterMaxSequences = _AlaVirtualRouterMaxSequences_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 6),
    _AlaVirtualRouterMaxSequences_Type()
)
alaVirtualRouterMaxSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterMaxSequences.setStatus("current")
_AlaVirtualRouterMaxTlvs_Type = Integer32
_AlaVirtualRouterMaxTlvs_Object = MibTableColumn
alaVirtualRouterMaxTlvs = _AlaVirtualRouterMaxTlvs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 7),
    _AlaVirtualRouterMaxTlvs_Type()
)
alaVirtualRouterMaxTlvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterMaxTlvs.setStatus("current")
_AlaVirtualRouterMaxAccessLists_Type = Integer32
_AlaVirtualRouterMaxAccessLists_Object = MibTableColumn
alaVirtualRouterMaxAccessLists = _AlaVirtualRouterMaxAccessLists_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 8),
    _AlaVirtualRouterMaxAccessLists_Type()
)
alaVirtualRouterMaxAccessLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterMaxAccessLists.setStatus("current")
_AlaVirtualRouterMaxAddressBlocks_Type = Integer32
_AlaVirtualRouterMaxAddressBlocks_Object = MibTableColumn
alaVirtualRouterMaxAddressBlocks = _AlaVirtualRouterMaxAddressBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 9),
    _AlaVirtualRouterMaxAddressBlocks_Type()
)
alaVirtualRouterMaxAddressBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterMaxAddressBlocks.setStatus("current")
_AlaVirtualRouterMaxMatchInterfaces_Type = Integer32
_AlaVirtualRouterMaxMatchInterfaces_Object = MibTableColumn
alaVirtualRouterMaxMatchInterfaces = _AlaVirtualRouterMaxMatchInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 10),
    _AlaVirtualRouterMaxMatchInterfaces_Type()
)
alaVirtualRouterMaxMatchInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVirtualRouterMaxMatchInterfaces.setStatus("current")


class _AlaVirtualRouterNoAutoLoadVrrp_Type(TruthValue):
    """Custom type alaVirtualRouterNoAutoLoadVrrp based on TruthValue"""


_AlaVirtualRouterNoAutoLoadVrrp_Object = MibTableColumn
alaVirtualRouterNoAutoLoadVrrp = _AlaVirtualRouterNoAutoLoadVrrp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 11),
    _AlaVirtualRouterNoAutoLoadVrrp_Type()
)
alaVirtualRouterNoAutoLoadVrrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVirtualRouterNoAutoLoadVrrp.setStatus("current")
_AlaVrConfigTable_Object = MibTable
alaVrConfigTable = _AlaVrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaVrConfigTable.setStatus("current")
_AlaVrConfigEntry_Object = MibTableRow
alaVrConfigEntry = _AlaVrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1)
)
alaVrConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigIndex"),
)
if mibBuilder.loadTexts:
    alaVrConfigEntry.setStatus("current")


class _AlaVrConfigIndex_Type(Integer32):
    """Custom type alaVrConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaVrConfigIndex_Type.__name__ = "Integer32"
_AlaVrConfigIndex_Object = MibTableColumn
alaVrConfigIndex = _AlaVrConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 1),
    _AlaVrConfigIndex_Type()
)
alaVrConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVrConfigIndex.setStatus("current")


class _AlaVrConfigRipStatus_Type(Integer32):
    """Custom type alaVrConfigRipStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigRipStatus_Type.__name__ = "Integer32"
_AlaVrConfigRipStatus_Object = MibTableColumn
alaVrConfigRipStatus = _AlaVrConfigRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 2),
    _AlaVrConfigRipStatus_Type()
)
alaVrConfigRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigRipStatus.setStatus("current")


class _AlaVrConfigOspfStatus_Type(Integer32):
    """Custom type alaVrConfigOspfStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigOspfStatus_Type.__name__ = "Integer32"
_AlaVrConfigOspfStatus_Object = MibTableColumn
alaVrConfigOspfStatus = _AlaVrConfigOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 3),
    _AlaVrConfigOspfStatus_Type()
)
alaVrConfigOspfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigOspfStatus.setStatus("current")


class _AlaVrConfigIsisStatus_Type(Integer32):
    """Custom type alaVrConfigIsisStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigIsisStatus_Type.__name__ = "Integer32"
_AlaVrConfigIsisStatus_Object = MibTableColumn
alaVrConfigIsisStatus = _AlaVrConfigIsisStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 4),
    _AlaVrConfigIsisStatus_Type()
)
alaVrConfigIsisStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigIsisStatus.setStatus("current")


class _AlaVrConfigBgpStatus_Type(Integer32):
    """Custom type alaVrConfigBgpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigBgpStatus_Type.__name__ = "Integer32"
_AlaVrConfigBgpStatus_Object = MibTableColumn
alaVrConfigBgpStatus = _AlaVrConfigBgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 5),
    _AlaVrConfigBgpStatus_Type()
)
alaVrConfigBgpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigBgpStatus.setStatus("current")


class _AlaVrConfigPimStatus_Type(Integer32):
    """Custom type alaVrConfigPimStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigPimStatus_Type.__name__ = "Integer32"
_AlaVrConfigPimStatus_Object = MibTableColumn
alaVrConfigPimStatus = _AlaVrConfigPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 6),
    _AlaVrConfigPimStatus_Type()
)
alaVrConfigPimStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigPimStatus.setStatus("current")


class _AlaVrConfigDvmrpStatus_Type(Integer32):
    """Custom type alaVrConfigDvmrpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigDvmrpStatus_Type.__name__ = "Integer32"
_AlaVrConfigDvmrpStatus_Object = MibTableColumn
alaVrConfigDvmrpStatus = _AlaVrConfigDvmrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 7),
    _AlaVrConfigDvmrpStatus_Type()
)
alaVrConfigDvmrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigDvmrpStatus.setStatus("current")


class _AlaVrConfigRipngStatus_Type(Integer32):
    """Custom type alaVrConfigRipngStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigRipngStatus_Type.__name__ = "Integer32"
_AlaVrConfigRipngStatus_Object = MibTableColumn
alaVrConfigRipngStatus = _AlaVrConfigRipngStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 8),
    _AlaVrConfigRipngStatus_Type()
)
alaVrConfigRipngStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigRipngStatus.setStatus("current")


class _AlaVrConfigOspf3Status_Type(Integer32):
    """Custom type alaVrConfigOspf3Status based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigOspf3Status_Type.__name__ = "Integer32"
_AlaVrConfigOspf3Status_Object = MibTableColumn
alaVrConfigOspf3Status = _AlaVrConfigOspf3Status_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 9),
    _AlaVrConfigOspf3Status_Type()
)
alaVrConfigOspf3Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigOspf3Status.setStatus("current")


class _AlaVrConfigMplsLdpStatus_Type(Integer32):
    """Custom type alaVrConfigMplsLdpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigMplsLdpStatus_Type.__name__ = "Integer32"
_AlaVrConfigMplsLdpStatus_Object = MibTableColumn
alaVrConfigMplsLdpStatus = _AlaVrConfigMplsLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 10),
    _AlaVrConfigMplsLdpStatus_Type()
)
alaVrConfigMplsLdpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVrConfigMplsLdpStatus.setStatus("current")


class _AlaVrConfigVrrpStatus_Type(Integer32):
    """Custom type alaVrConfigVrrpStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loaded", 1),
          ("loading", 3),
          ("notloaded", 2))
    )


_AlaVrConfigVrrpStatus_Type.__name__ = "Integer32"
_AlaVrConfigVrrpStatus_Object = MibTableColumn
alaVrConfigVrrpStatus = _AlaVrConfigVrrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 11),
    _AlaVrConfigVrrpStatus_Type()
)
alaVrConfigVrrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVrConfigVrrpStatus.setStatus("current")
_AlaVirtualRouterProfileTable_Object = MibTable
alaVirtualRouterProfileTable = _AlaVirtualRouterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaVirtualRouterProfileTable.setStatus("current")
_AlaVirtualRouterProfileEntry_Object = MibTableRow
alaVirtualRouterProfileEntry = _AlaVirtualRouterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1)
)
alaVirtualRouterProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileName"),
)
if mibBuilder.loadTexts:
    alaVirtualRouterProfileEntry.setStatus("current")
_AlaVirtualRouterProfileName_Type = SnmpAdminString
_AlaVirtualRouterProfileName_Object = MibTableColumn
alaVirtualRouterProfileName = _AlaVirtualRouterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 1),
    _AlaVirtualRouterProfileName_Type()
)
alaVirtualRouterProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileName.setStatus("current")
_AlaVirtualRouterProfileMaxRouteMaps_Type = Integer32
_AlaVirtualRouterProfileMaxRouteMaps_Object = MibTableColumn
alaVirtualRouterProfileMaxRouteMaps = _AlaVirtualRouterProfileMaxRouteMaps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 2),
    _AlaVirtualRouterProfileMaxRouteMaps_Type()
)
alaVirtualRouterProfileMaxRouteMaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileMaxRouteMaps.setStatus("current")
_AlaVirtualRouterProfileMaxSequences_Type = Integer32
_AlaVirtualRouterProfileMaxSequences_Object = MibTableColumn
alaVirtualRouterProfileMaxSequences = _AlaVirtualRouterProfileMaxSequences_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 3),
    _AlaVirtualRouterProfileMaxSequences_Type()
)
alaVirtualRouterProfileMaxSequences.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileMaxSequences.setStatus("current")
_AlaVirtualRouterProfileMaxTlvs_Type = Integer32
_AlaVirtualRouterProfileMaxTlvs_Object = MibTableColumn
alaVirtualRouterProfileMaxTlvs = _AlaVirtualRouterProfileMaxTlvs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 4),
    _AlaVirtualRouterProfileMaxTlvs_Type()
)
alaVirtualRouterProfileMaxTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileMaxTlvs.setStatus("current")
_AlaVirtualRouterProfileMaxAccessLists_Type = Integer32
_AlaVirtualRouterProfileMaxAccessLists_Object = MibTableColumn
alaVirtualRouterProfileMaxAccessLists = _AlaVirtualRouterProfileMaxAccessLists_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 5),
    _AlaVirtualRouterProfileMaxAccessLists_Type()
)
alaVirtualRouterProfileMaxAccessLists.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileMaxAccessLists.setStatus("current")
_AlaVirtualRouterProfileMaxAddressBlocks_Type = Integer32
_AlaVirtualRouterProfileMaxAddressBlocks_Object = MibTableColumn
alaVirtualRouterProfileMaxAddressBlocks = _AlaVirtualRouterProfileMaxAddressBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 6),
    _AlaVirtualRouterProfileMaxAddressBlocks_Type()
)
alaVirtualRouterProfileMaxAddressBlocks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileMaxAddressBlocks.setStatus("current")
_AlaVirtualRouterProfileMaxMatchInterfaces_Type = Integer32
_AlaVirtualRouterProfileMaxMatchInterfaces_Object = MibTableColumn
alaVirtualRouterProfileMaxMatchInterfaces = _AlaVirtualRouterProfileMaxMatchInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 7),
    _AlaVirtualRouterProfileMaxMatchInterfaces_Type()
)
alaVirtualRouterProfileMaxMatchInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVirtualRouterProfileMaxMatchInterfaces.setStatus("current")
_AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBConformance = _AlcatelIND1VirtualRouterMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2)
)
_AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBCompliances = _AlcatelIND1VirtualRouterMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 1)
)
_AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VirtualRouterMIBGroups = _AlcatelIND1VirtualRouterMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 2)
)

# Managed Objects groups

alaVirtualRouterConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 2, 1)
)
alaVirtualRouterConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfile"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxRouteMaps"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxSequences"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxTlvs"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxAccessLists"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxAddressBlocks"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxMatchInterfaces"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNoAutoLoadVrrp"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigRipStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigOspfStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigIsisStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigBgpStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigPimStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigDvmrpStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigRipngStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigOspf3Status"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigMplsLdpStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigVrrpStatus"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxRouteMaps"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxSequences"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxTlvs"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxAccessLists"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxAddressBlocks"),
        ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxMatchInterfaces"))
)
if mibBuilder.loadTexts:
    alaVirtualRouterConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaVirtualRouterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaVirtualRouterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-VIRTUALROUTER-MIB",
    **{"alcatelIND1VirtualRouterMIB": alcatelIND1VirtualRouterMIB,
       "alcatelIND1VirtualRouterMIBObjects": alcatelIND1VirtualRouterMIBObjects,
       "alaVirtualRouterConfig": alaVirtualRouterConfig,
       "alaVirtualRouterNameTable": alaVirtualRouterNameTable,
       "alaVirtualRouterNameEntry": alaVirtualRouterNameEntry,
       "alaVirtualRouterName": alaVirtualRouterName,
       "alaVirtualRouterNameIndex": alaVirtualRouterNameIndex,
       "alaVirtualRouterNameRowStatus": alaVirtualRouterNameRowStatus,
       "alaVirtualRouterProfile": alaVirtualRouterProfile,
       "alaVirtualRouterMaxRouteMaps": alaVirtualRouterMaxRouteMaps,
       "alaVirtualRouterMaxSequences": alaVirtualRouterMaxSequences,
       "alaVirtualRouterMaxTlvs": alaVirtualRouterMaxTlvs,
       "alaVirtualRouterMaxAccessLists": alaVirtualRouterMaxAccessLists,
       "alaVirtualRouterMaxAddressBlocks": alaVirtualRouterMaxAddressBlocks,
       "alaVirtualRouterMaxMatchInterfaces": alaVirtualRouterMaxMatchInterfaces,
       "alaVirtualRouterNoAutoLoadVrrp": alaVirtualRouterNoAutoLoadVrrp,
       "alaVrConfigTable": alaVrConfigTable,
       "alaVrConfigEntry": alaVrConfigEntry,
       "alaVrConfigIndex": alaVrConfigIndex,
       "alaVrConfigRipStatus": alaVrConfigRipStatus,
       "alaVrConfigOspfStatus": alaVrConfigOspfStatus,
       "alaVrConfigIsisStatus": alaVrConfigIsisStatus,
       "alaVrConfigBgpStatus": alaVrConfigBgpStatus,
       "alaVrConfigPimStatus": alaVrConfigPimStatus,
       "alaVrConfigDvmrpStatus": alaVrConfigDvmrpStatus,
       "alaVrConfigRipngStatus": alaVrConfigRipngStatus,
       "alaVrConfigOspf3Status": alaVrConfigOspf3Status,
       "alaVrConfigMplsLdpStatus": alaVrConfigMplsLdpStatus,
       "alaVrConfigVrrpStatus": alaVrConfigVrrpStatus,
       "alaVirtualRouterProfileTable": alaVirtualRouterProfileTable,
       "alaVirtualRouterProfileEntry": alaVirtualRouterProfileEntry,
       "alaVirtualRouterProfileName": alaVirtualRouterProfileName,
       "alaVirtualRouterProfileMaxRouteMaps": alaVirtualRouterProfileMaxRouteMaps,
       "alaVirtualRouterProfileMaxSequences": alaVirtualRouterProfileMaxSequences,
       "alaVirtualRouterProfileMaxTlvs": alaVirtualRouterProfileMaxTlvs,
       "alaVirtualRouterProfileMaxAccessLists": alaVirtualRouterProfileMaxAccessLists,
       "alaVirtualRouterProfileMaxAddressBlocks": alaVirtualRouterProfileMaxAddressBlocks,
       "alaVirtualRouterProfileMaxMatchInterfaces": alaVirtualRouterProfileMaxMatchInterfaces,
       "alcatelIND1VirtualRouterMIBConformance": alcatelIND1VirtualRouterMIBConformance,
       "alcatelIND1VirtualRouterMIBCompliances": alcatelIND1VirtualRouterMIBCompliances,
       "alaVirtualRouterCompliance": alaVirtualRouterCompliance,
       "alcatelIND1VirtualRouterMIBGroups": alcatelIND1VirtualRouterMIBGroups,
       "alaVirtualRouterConfigMIBGroup": alaVirtualRouterConfigMIBGroup}
)
