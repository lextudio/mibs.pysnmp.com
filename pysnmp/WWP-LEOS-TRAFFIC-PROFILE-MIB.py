# SNMP MIB module (WWP-LEOS-TRAFFIC-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-TRAFFIC-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:13 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosTrafficProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27)
)
wwpLeosTrafficProfileMIB.setRevisions(
        ("2011-07-07 00:00",
         "2011-03-27 17:00",
         "2009-08-25 17:00",
         "2008-11-14 17:00",
         "2008-07-28 17:00",
         "2008-06-28 17:00",
         "2008-06-16 17:00",
         "2008-06-13 17:00",
         "2008-06-04 17:00",
         "2008-05-21 17:00",
         "2008-05-15 17:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosTrafficProfileObjects_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileObjects = _WwpLeosTrafficProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1)
)
_WwpLeosTrafficProfile_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfile = _WwpLeosTrafficProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1)
)
_WwpLeosTrafficProfileGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileGlobalAttrs = _WwpLeosTrafficProfileGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 1)
)


class _WwpLeosTrafficProfileGlobalState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileGlobalState based on Integer32"""
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


_WwpLeosTrafficProfileGlobalState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileGlobalState_Object = MibScalar
wwpLeosTrafficProfileGlobalState = _WwpLeosTrafficProfileGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 1, 1),
    _WwpLeosTrafficProfileGlobalState_Type()
)
wwpLeosTrafficProfileGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileGlobalState.setStatus("current")


class _WwpLeosTrafficProfileGlobalMeterProvisioningState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileGlobalMeterProvisioningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eir", 2),
          ("pir", 1))
    )


_WwpLeosTrafficProfileGlobalMeterProvisioningState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileGlobalMeterProvisioningState_Object = MibScalar
wwpLeosTrafficProfileGlobalMeterProvisioningState = _WwpLeosTrafficProfileGlobalMeterProvisioningState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 1, 2),
    _WwpLeosTrafficProfileGlobalMeterProvisioningState_Type()
)
wwpLeosTrafficProfileGlobalMeterProvisioningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileGlobalMeterProvisioningState.setStatus("current")
_WwpLeosTrafficProfilePortTable_Object = MibTable
wwpLeosTrafficProfilePortTable = _WwpLeosTrafficProfilePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfilePortTable.setStatus("current")
_WwpLeosTrafficProfilePortEntry_Object = MibTableRow
wwpLeosTrafficProfilePortEntry = _WwpLeosTrafficProfilePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1)
)
wwpLeosTrafficProfilePortEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfilePortEntry.setStatus("current")


class _WwpLeosTrafficProfilePort_Type(Integer32):
    """Custom type wwpLeosTrafficProfilePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTrafficProfilePort_Type.__name__ = "Integer32"
_WwpLeosTrafficProfilePort_Object = MibTableColumn
wwpLeosTrafficProfilePort = _WwpLeosTrafficProfilePort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 1),
    _WwpLeosTrafficProfilePort_Type()
)
wwpLeosTrafficProfilePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfilePort.setStatus("current")


class _WwpLeosTrafficProfileAdminState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileAdminState based on Integer32"""
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


_WwpLeosTrafficProfileAdminState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileAdminState_Object = MibTableColumn
wwpLeosTrafficProfileAdminState = _WwpLeosTrafficProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 2),
    _WwpLeosTrafficProfileAdminState_Type()
)
wwpLeosTrafficProfileAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileAdminState.setStatus("current")


class _WwpLeosTrafficProfileOperState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileOperState based on Integer32"""
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


_WwpLeosTrafficProfileOperState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileOperState_Object = MibTableColumn
wwpLeosTrafficProfileOperState = _WwpLeosTrafficProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 3),
    _WwpLeosTrafficProfileOperState_Type()
)
wwpLeosTrafficProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileOperState.setStatus("current")


class _WwpLeosTrafficProfileMode_Type(Integer32):
    """Custom type wwpLeosTrafficProfileMode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 15),
          ("cascadedDot1dPri", 1),
          ("cascadedDscp", 2),
          ("cascadedIpPrec", 3),
          ("hierarchicalPort", 13),
          ("hierarchicalVlan", 12),
          ("none", 14),
          ("stdDiffServ", 5),
          ("stdDot1", 4),
          ("stdDscp", 8),
          ("stdIpPrec", 6),
          ("stdVlan", 7),
          ("stdVlanDot1DPri", 9),
          ("stdVlanDscp", 11),
          ("stdVlanIpp", 10))
    )


_WwpLeosTrafficProfileMode_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileMode_Object = MibTableColumn
wwpLeosTrafficProfileMode = _WwpLeosTrafficProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 4),
    _WwpLeosTrafficProfileMode_Type()
)
wwpLeosTrafficProfileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMode.setStatus("current")


class _WwpLeosTrafficProfileNonConformCascadedProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileNonConformCascadedProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deprecated", 4),
          ("drop", 0),
          ("profile1", 1),
          ("profile2", 2),
          ("profile3", 3))
    )


_WwpLeosTrafficProfileNonConformCascadedProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileNonConformCascadedProfile_Object = MibTableColumn
wwpLeosTrafficProfileNonConformCascadedProfile = _WwpLeosTrafficProfileNonConformCascadedProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 5),
    _WwpLeosTrafficProfileNonConformCascadedProfile_Type()
)
wwpLeosTrafficProfileNonConformCascadedProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileNonConformCascadedProfile.setStatus("deprecated")


class _WwpLeosTrafficProfileNonConformStdProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileNonConformStdProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosTrafficProfileNonConformStdProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileNonConformStdProfile_Object = MibTableColumn
wwpLeosTrafficProfileNonConformStdProfile = _WwpLeosTrafficProfileNonConformStdProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 6),
    _WwpLeosTrafficProfileNonConformStdProfile_Type()
)
wwpLeosTrafficProfileNonConformStdProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileNonConformStdProfile.setStatus("current")


class _WwpLeosTrafficProfileArpCascadedProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileArpCascadedProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 0),
          ("deprecated", 4),
          ("profile1", 1),
          ("profile2", 2),
          ("profile3", 3))
    )


_WwpLeosTrafficProfileArpCascadedProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileArpCascadedProfile_Object = MibTableColumn
wwpLeosTrafficProfileArpCascadedProfile = _WwpLeosTrafficProfileArpCascadedProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 7),
    _WwpLeosTrafficProfileArpCascadedProfile_Type()
)
wwpLeosTrafficProfileArpCascadedProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileArpCascadedProfile.setStatus("deprecated")


class _WwpLeosTrafficProfileArpStdProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileArpStdProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosTrafficProfileArpStdProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileArpStdProfile_Object = MibTableColumn
wwpLeosTrafficProfileArpStdProfile = _WwpLeosTrafficProfileArpStdProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 8),
    _WwpLeosTrafficProfileArpStdProfile_Type()
)
wwpLeosTrafficProfileArpStdProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileArpStdProfile.setStatus("current")


class _WwpLeosTrafficProfileMeterPool_Type(Integer32):
    """Custom type wwpLeosTrafficProfileMeterPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosTrafficProfileMeterPool_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileMeterPool_Object = MibTableColumn
wwpLeosTrafficProfileMeterPool = _WwpLeosTrafficProfileMeterPool_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 9),
    _WwpLeosTrafficProfileMeterPool_Type()
)
wwpLeosTrafficProfileMeterPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPool.setStatus("current")


class _WwpLeosTrafficProfileClassifierMode_Type(Integer32):
    """Custom type wwpLeosTrafficProfileClassifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 1),
          ("wide", 2))
    )


_WwpLeosTrafficProfileClassifierMode_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileClassifierMode_Object = MibTableColumn
wwpLeosTrafficProfileClassifierMode = _WwpLeosTrafficProfileClassifierMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 2, 1, 10),
    _WwpLeosTrafficProfileClassifierMode_Type()
)
wwpLeosTrafficProfileClassifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileClassifierMode.setStatus("current")
_WwpLeosTrafficProfileCascadedTable_Object = MibTable
wwpLeosTrafficProfileCascadedTable = _WwpLeosTrafficProfileCascadedTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTable.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedEntry_Object = MibTableRow
wwpLeosTrafficProfileCascadedEntry = _WwpLeosTrafficProfileCascadedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 3, 1)
)
wwpLeosTrafficProfileCascadedEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileCascadedIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedEntry.setStatus("deprecated")


class _WwpLeosTrafficProfileCascadedIndx_Type(Integer32):
    """Custom type wwpLeosTrafficProfileCascadedIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WwpLeosTrafficProfileCascadedIndx_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileCascadedIndx_Object = MibTableColumn
wwpLeosTrafficProfileCascadedIndx = _WwpLeosTrafficProfileCascadedIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 3, 1, 1),
    _WwpLeosTrafficProfileCascadedIndx_Type()
)
wwpLeosTrafficProfileCascadedIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedIndx.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedCir_Type = Integer32
_WwpLeosTrafficProfileCascadedCir_Object = MibTableColumn
wwpLeosTrafficProfileCascadedCir = _WwpLeosTrafficProfileCascadedCir_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 3, 1, 2),
    _WwpLeosTrafficProfileCascadedCir_Type()
)
wwpLeosTrafficProfileCascadedCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedCir.setStatus("deprecated")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedCir.setUnits("kbps")
_WwpLeosTrafficProfileCascadedPir_Type = Integer32
_WwpLeosTrafficProfileCascadedPir_Object = MibTableColumn
wwpLeosTrafficProfileCascadedPir = _WwpLeosTrafficProfileCascadedPir_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 3, 1, 3),
    _WwpLeosTrafficProfileCascadedPir_Type()
)
wwpLeosTrafficProfileCascadedPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedPir.setStatus("deprecated")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedPir.setUnits("kbps")
_WwpLeosTrafficProfileCascadedStatus_Type = RowStatus
_WwpLeosTrafficProfileCascadedStatus_Object = MibTableColumn
wwpLeosTrafficProfileCascadedStatus = _WwpLeosTrafficProfileCascadedStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 3, 1, 5),
    _WwpLeosTrafficProfileCascadedStatus_Type()
)
wwpLeosTrafficProfileCascadedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedStatus.setStatus("deprecated")
_WwpLeosTrafficProfileStdTable_Object = MibTable
wwpLeosTrafficProfileStdTable = _WwpLeosTrafficProfileStdTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTable.setStatus("current")
_WwpLeosTrafficProfileStdEntry_Object = MibTableRow
wwpLeosTrafficProfileStdEntry = _WwpLeosTrafficProfileStdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1)
)
wwpLeosTrafficProfileStdEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdEntry.setStatus("current")


class _WwpLeosTrafficProfileStdIndx_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosTrafficProfileStdIndx_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdIndx_Object = MibTableColumn
wwpLeosTrafficProfileStdIndx = _WwpLeosTrafficProfileStdIndx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 1),
    _WwpLeosTrafficProfileStdIndx_Type()
)
wwpLeosTrafficProfileStdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIndx.setStatus("current")
_WwpLeosTrafficProfileStdCir_Type = Integer32
_WwpLeosTrafficProfileStdCir_Object = MibTableColumn
wwpLeosTrafficProfileStdCir = _WwpLeosTrafficProfileStdCir_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 2),
    _WwpLeosTrafficProfileStdCir_Type()
)
wwpLeosTrafficProfileStdCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdCir.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdCir.setUnits("kbps")
_WwpLeosTrafficProfileStdPir_Type = Integer32
_WwpLeosTrafficProfileStdPir_Object = MibTableColumn
wwpLeosTrafficProfileStdPir = _WwpLeosTrafficProfileStdPir_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 3),
    _WwpLeosTrafficProfileStdPir_Type()
)
wwpLeosTrafficProfileStdPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPir.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPir.setUnits("kbps")


class _WwpLeosTrafficProfileStdName_Type(DisplayString):
    """Custom type wwpLeosTrafficProfileStdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeosTrafficProfileStdName_Type.__name__ = "DisplayString"
_WwpLeosTrafficProfileStdName_Object = MibTableColumn
wwpLeosTrafficProfileStdName = _WwpLeosTrafficProfileStdName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 4),
    _WwpLeosTrafficProfileStdName_Type()
)
wwpLeosTrafficProfileStdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdName.setStatus("current")
_WwpLeosTrafficProfileStdStatus_Type = RowStatus
_WwpLeosTrafficProfileStdStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdStatus = _WwpLeosTrafficProfileStdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 5),
    _WwpLeosTrafficProfileStdStatus_Type()
)
wwpLeosTrafficProfileStdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdStatus.setStatus("current")


class _WwpLeosTrafficProfileStdVlan_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WwpLeosTrafficProfileStdVlan_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdVlan_Object = MibTableColumn
wwpLeosTrafficProfileStdVlan = _WwpLeosTrafficProfileStdVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 6),
    _WwpLeosTrafficProfileStdVlan_Type()
)
wwpLeosTrafficProfileStdVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlan.setStatus("current")


class _WwpLeosTrafficProfileStdCbs_Type(Unsigned32):
    """Custom type wwpLeosTrafficProfileStdCbs based on Unsigned32"""
    defaultValue = 2


_WwpLeosTrafficProfileStdCbs_Object = MibTableColumn
wwpLeosTrafficProfileStdCbs = _WwpLeosTrafficProfileStdCbs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 7),
    _WwpLeosTrafficProfileStdCbs_Type()
)
wwpLeosTrafficProfileStdCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdCbs.setStatus("current")


class _WwpLeosTrafficProfileStdEbs_Type(Unsigned32):
    """Custom type wwpLeosTrafficProfileStdEbs based on Unsigned32"""
    defaultValue = 2


_WwpLeosTrafficProfileStdEbs_Object = MibTableColumn
wwpLeosTrafficProfileStdEbs = _WwpLeosTrafficProfileStdEbs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 8),
    _WwpLeosTrafficProfileStdEbs_Type()
)
wwpLeosTrafficProfileStdEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdEbs.setStatus("current")


class _WwpLeosTrafficProfileStdDscpRemarkPolicy_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdDscpRemarkPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("leave", 1))
    )


_WwpLeosTrafficProfileStdDscpRemarkPolicy_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdDscpRemarkPolicy_Object = MibTableColumn
wwpLeosTrafficProfileStdDscpRemarkPolicy = _WwpLeosTrafficProfileStdDscpRemarkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 9),
    _WwpLeosTrafficProfileStdDscpRemarkPolicy_Type()
)
wwpLeosTrafficProfileStdDscpRemarkPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDscpRemarkPolicy.setStatus("current")


class _WwpLeosTrafficProfileStdFixedDscp_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdFixedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosTrafficProfileStdFixedDscp_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdFixedDscp_Object = MibTableColumn
wwpLeosTrafficProfileStdFixedDscp = _WwpLeosTrafficProfileStdFixedDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 10),
    _WwpLeosTrafficProfileStdFixedDscp_Type()
)
wwpLeosTrafficProfileStdFixedDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdFixedDscp.setStatus("current")


class _WwpLeosTrafficProfileStdUnsetVlan_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdUnsetVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unset", 1))
    )


_WwpLeosTrafficProfileStdUnsetVlan_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdUnsetVlan_Object = MibTableColumn
wwpLeosTrafficProfileStdUnsetVlan = _WwpLeosTrafficProfileStdUnsetVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 11),
    _WwpLeosTrafficProfileStdUnsetVlan_Type()
)
wwpLeosTrafficProfileStdUnsetVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdUnsetVlan.setStatus("current")


class _WwpLeosTrafficProfileStdDefaultProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdDefaultProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WwpLeosTrafficProfileStdDefaultProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdDefaultProfile_Object = MibTableColumn
wwpLeosTrafficProfileStdDefaultProfile = _WwpLeosTrafficProfileStdDefaultProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 12),
    _WwpLeosTrafficProfileStdDefaultProfile_Type()
)
wwpLeosTrafficProfileStdDefaultProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDefaultProfile.setStatus("current")


class _WwpLeosTrafficeProfileStdDrop_Type(Integer32):
    """Custom type wwpLeosTrafficeProfileStdDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WwpLeosTrafficeProfileStdDrop_Type.__name__ = "Integer32"
_WwpLeosTrafficeProfileStdDrop_Object = MibTableColumn
wwpLeosTrafficeProfileStdDrop = _WwpLeosTrafficeProfileStdDrop_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 13),
    _WwpLeosTrafficeProfileStdDrop_Type()
)
wwpLeosTrafficeProfileStdDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficeProfileStdDrop.setStatus("current")
_WwpLeosTrafficProfileStdParentIndex_Type = Integer32
_WwpLeosTrafficProfileStdParentIndex_Object = MibTableColumn
wwpLeosTrafficProfileStdParentIndex = _WwpLeosTrafficProfileStdParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 14),
    _WwpLeosTrafficProfileStdParentIndex_Type()
)
wwpLeosTrafficProfileStdParentIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdParentIndex.setStatus("current")


class _WwpLeosTrafficProfileStdChildMode_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdChildMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dot1dPri", 1),
          ("dscp", 3),
          ("ipprec", 2),
          ("none", 99),
          ("vlan", 4),
          ("vlanCos", 5))
    )


_WwpLeosTrafficProfileStdChildMode_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdChildMode_Object = MibTableColumn
wwpLeosTrafficProfileStdChildMode = _WwpLeosTrafficProfileStdChildMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 15),
    _WwpLeosTrafficProfileStdChildMode_Type()
)
wwpLeosTrafficProfileStdChildMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdChildMode.setStatus("current")


class _WwpLeosTrafficProfileStdStatsMonitor_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdStatsMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileStdStatsMonitor_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdStatsMonitor_Object = MibTableColumn
wwpLeosTrafficProfileStdStatsMonitor = _WwpLeosTrafficProfileStdStatsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 16),
    _WwpLeosTrafficProfileStdStatsMonitor_Type()
)
wwpLeosTrafficProfileStdStatsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdStatsMonitor.setStatus("current")


class _WwpLeosTrafficProfileStdUntaggedState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdUntaggedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileStdUntaggedState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdUntaggedState_Object = MibTableColumn
wwpLeosTrafficProfileStdUntaggedState = _WwpLeosTrafficProfileStdUntaggedState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 17),
    _WwpLeosTrafficProfileStdUntaggedState_Type()
)
wwpLeosTrafficProfileStdUntaggedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdUntaggedState.setStatus("current")


class _WwpLeosTrafficProfileStdVs_Type(DisplayString):
    """Custom type wwpLeosTrafficProfileStdVs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeosTrafficProfileStdVs_Type.__name__ = "DisplayString"
_WwpLeosTrafficProfileStdVs_Object = MibTableColumn
wwpLeosTrafficProfileStdVs = _WwpLeosTrafficProfileStdVs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 18),
    _WwpLeosTrafficProfileStdVs_Type()
)
wwpLeosTrafficProfileStdVs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVs.setStatus("current")


class _WwpLeosTrafficProfileStdRemarkColorPolicy_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdRemarkColorPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greenRemarkToYellow", 3),
          ("leave", 1),
          ("yellowRemarkToGreen", 2))
    )


_WwpLeosTrafficProfileStdRemarkColorPolicy_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdRemarkColorPolicy_Object = MibTableColumn
wwpLeosTrafficProfileStdRemarkColorPolicy = _WwpLeosTrafficProfileStdRemarkColorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 19),
    _WwpLeosTrafficProfileStdRemarkColorPolicy_Type()
)
wwpLeosTrafficProfileStdRemarkColorPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdRemarkColorPolicy.setStatus("current")


class _WwpLeosTrafficProfileStdRemarkRcosPolicy_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdRemarkRcosPolicy based on Integer32"""
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
        *(("leave", 1),
          ("remarkBoth", 4),
          ("remarkGreen", 2),
          ("remarkYellow", 3))
    )


_WwpLeosTrafficProfileStdRemarkRcosPolicy_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdRemarkRcosPolicy_Object = MibTableColumn
wwpLeosTrafficProfileStdRemarkRcosPolicy = _WwpLeosTrafficProfileStdRemarkRcosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 20),
    _WwpLeosTrafficProfileStdRemarkRcosPolicy_Type()
)
wwpLeosTrafficProfileStdRemarkRcosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdRemarkRcosPolicy.setStatus("current")


class _WwpLeosTrafficProfileStdYellowRemarkRcos_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdYellowRemarkRcos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTrafficProfileStdYellowRemarkRcos_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdYellowRemarkRcos_Object = MibTableColumn
wwpLeosTrafficProfileStdYellowRemarkRcos = _WwpLeosTrafficProfileStdYellowRemarkRcos_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 21),
    _WwpLeosTrafficProfileStdYellowRemarkRcos_Type()
)
wwpLeosTrafficProfileStdYellowRemarkRcos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdYellowRemarkRcos.setStatus("current")


class _WwpLeosTrafficProfileStdGreenRemarkRcos_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdGreenRemarkRcos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTrafficProfileStdGreenRemarkRcos_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdGreenRemarkRcos_Object = MibTableColumn
wwpLeosTrafficProfileStdGreenRemarkRcos = _WwpLeosTrafficProfileStdGreenRemarkRcos_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 22),
    _WwpLeosTrafficProfileStdGreenRemarkRcos_Type()
)
wwpLeosTrafficProfileStdGreenRemarkRcos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdGreenRemarkRcos.setStatus("current")


class _WwpLeosTrafficProfileStdIngressColorAware_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdIngressColorAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileStdIngressColorAware_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdIngressColorAware_Object = MibTableColumn
wwpLeosTrafficProfileStdIngressColorAware = _WwpLeosTrafficProfileStdIngressColorAware_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 23),
    _WwpLeosTrafficProfileStdIngressColorAware_Type()
)
wwpLeosTrafficProfileStdIngressColorAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIngressColorAware.setStatus("current")
_WwpLeosTrafficProfileStdEir_Type = Integer32
_WwpLeosTrafficProfileStdEir_Object = MibTableColumn
wwpLeosTrafficProfileStdEir = _WwpLeosTrafficProfileStdEir_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 4, 1, 24),
    _WwpLeosTrafficProfileStdEir_Type()
)
wwpLeosTrafficProfileStdEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdEir.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdEir.setUnits("kbps")
_WwpLeosTrafficProfileStdDot1dTable_Object = MibTable
wwpLeosTrafficProfileStdDot1dTable = _WwpLeosTrafficProfileStdDot1dTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDot1dTable.setStatus("current")
_WwpLeosTrafficProfileStdDot1dEntry_Object = MibTableRow
wwpLeosTrafficProfileStdDot1dEntry = _WwpLeosTrafficProfileStdDot1dEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 5, 1)
)
wwpLeosTrafficProfileStdDot1dEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdDot1d"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDot1dEntry.setStatus("current")


class _WwpLeosTrafficProfileStdDot1d_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdDot1d based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTrafficProfileStdDot1d_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdDot1d_Object = MibTableColumn
wwpLeosTrafficProfileStdDot1d = _WwpLeosTrafficProfileStdDot1d_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 5, 1, 1),
    _WwpLeosTrafficProfileStdDot1d_Type()
)
wwpLeosTrafficProfileStdDot1d.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDot1d.setStatus("current")


class _WwpLeosTrafficProfileStdDot1dToProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdDot1dToProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosTrafficProfileStdDot1dToProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdDot1dToProfile_Object = MibTableColumn
wwpLeosTrafficProfileStdDot1dToProfile = _WwpLeosTrafficProfileStdDot1dToProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 5, 1, 2),
    _WwpLeosTrafficProfileStdDot1dToProfile_Type()
)
wwpLeosTrafficProfileStdDot1dToProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDot1dToProfile.setStatus("current")
_WwpLeosTrafficProfileStdDot1dStatus_Type = RowStatus
_WwpLeosTrafficProfileStdDot1dStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdDot1dStatus = _WwpLeosTrafficProfileStdDot1dStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 5, 1, 3),
    _WwpLeosTrafficProfileStdDot1dStatus_Type()
)
wwpLeosTrafficProfileStdDot1dStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDot1dStatus.setStatus("current")
_WwpLeosTrafficProfileStdIpPrecTable_Object = MibTable
wwpLeosTrafficProfileStdIpPrecTable = _WwpLeosTrafficProfileStdIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIpPrecTable.setStatus("current")
_WwpLeosTrafficProfileStdIpPrecEntry_Object = MibTableRow
wwpLeosTrafficProfileStdIpPrecEntry = _WwpLeosTrafficProfileStdIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 6, 1)
)
wwpLeosTrafficProfileStdIpPrecEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIpPrec"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIpPrecEntry.setStatus("current")


class _WwpLeosTrafficProfileStdIpPrec_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdIpPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTrafficProfileStdIpPrec_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdIpPrec_Object = MibTableColumn
wwpLeosTrafficProfileStdIpPrec = _WwpLeosTrafficProfileStdIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 6, 1, 1),
    _WwpLeosTrafficProfileStdIpPrec_Type()
)
wwpLeosTrafficProfileStdIpPrec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIpPrec.setStatus("current")


class _WwpLeosTrafficProfileStdIpPrecToProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdIpPrecToProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosTrafficProfileStdIpPrecToProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdIpPrecToProfile_Object = MibTableColumn
wwpLeosTrafficProfileStdIpPrecToProfile = _WwpLeosTrafficProfileStdIpPrecToProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 6, 1, 2),
    _WwpLeosTrafficProfileStdIpPrecToProfile_Type()
)
wwpLeosTrafficProfileStdIpPrecToProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIpPrecToProfile.setStatus("current")
_WwpLeosTrafficProfileStdIpPrecStatus_Type = RowStatus
_WwpLeosTrafficProfileStdIpPrecStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdIpPrecStatus = _WwpLeosTrafficProfileStdIpPrecStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 6, 1, 3),
    _WwpLeosTrafficProfileStdIpPrecStatus_Type()
)
wwpLeosTrafficProfileStdIpPrecStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdIpPrecStatus.setStatus("current")
_WwpLeosTrafficProfileStdPhbTable_Object = MibTable
wwpLeosTrafficProfileStdPhbTable = _WwpLeosTrafficProfileStdPhbTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPhbTable.setStatus("current")
_WwpLeosTrafficProfileStdPhbEntry_Object = MibTableRow
wwpLeosTrafficProfileStdPhbEntry = _WwpLeosTrafficProfileStdPhbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 7, 1)
)
wwpLeosTrafficProfileStdPhbEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdPhb"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPhbEntry.setStatus("current")


class _WwpLeosTrafficProfileStdPhb_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdPhb based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("af1", 9),
          ("af2", 10),
          ("af3", 11),
          ("af4", 12),
          ("cs0", 1),
          ("cs1", 2),
          ("cs2", 3),
          ("cs3", 4),
          ("cs4", 5),
          ("cs5", 6),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 13))
    )


_WwpLeosTrafficProfileStdPhb_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdPhb_Object = MibTableColumn
wwpLeosTrafficProfileStdPhb = _WwpLeosTrafficProfileStdPhb_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 7, 1, 1),
    _WwpLeosTrafficProfileStdPhb_Type()
)
wwpLeosTrafficProfileStdPhb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPhb.setStatus("current")


class _WwpLeosTrafficProfileStdPhbToProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdPhbToProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WwpLeosTrafficProfileStdPhbToProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdPhbToProfile_Object = MibTableColumn
wwpLeosTrafficProfileStdPhbToProfile = _WwpLeosTrafficProfileStdPhbToProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 7, 1, 2),
    _WwpLeosTrafficProfileStdPhbToProfile_Type()
)
wwpLeosTrafficProfileStdPhbToProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPhbToProfile.setStatus("current")
_WwpLeosTrafficProfileStdPhbStatus_Type = RowStatus
_WwpLeosTrafficProfileStdPhbStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdPhbStatus = _WwpLeosTrafficProfileStdPhbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 7, 1, 3),
    _WwpLeosTrafficProfileStdPhbStatus_Type()
)
wwpLeosTrafficProfileStdPhbStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdPhbStatus.setStatus("current")
_WwpLeosTrafficProfileCascadedStatsTable_Object = MibTable
wwpLeosTrafficProfileCascadedStatsTable = _WwpLeosTrafficProfileCascadedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedStatsTable.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedStatsEntry_Object = MibTableRow
wwpLeosTrafficProfileCascadedStatsEntry = _WwpLeosTrafficProfileCascadedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1)
)
wwpLeosTrafficProfileCascadedStatsEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileCascadedIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedStatsEntry.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedAcceptedBytesHi_Type = Counter32
_WwpLeosTrafficProfileCascadedAcceptedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileCascadedAcceptedBytesHi = _WwpLeosTrafficProfileCascadedAcceptedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1, 1),
    _WwpLeosTrafficProfileCascadedAcceptedBytesHi_Type()
)
wwpLeosTrafficProfileCascadedAcceptedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedAcceptedBytesHi.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedAcceptedBytesLo_Type = Counter32
_WwpLeosTrafficProfileCascadedAcceptedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileCascadedAcceptedBytesLo = _WwpLeosTrafficProfileCascadedAcceptedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1, 2),
    _WwpLeosTrafficProfileCascadedAcceptedBytesLo_Type()
)
wwpLeosTrafficProfileCascadedAcceptedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedAcceptedBytesLo.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedDroppedBytesHi_Type = Counter32
_WwpLeosTrafficProfileCascadedDroppedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileCascadedDroppedBytesHi = _WwpLeosTrafficProfileCascadedDroppedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1, 3),
    _WwpLeosTrafficProfileCascadedDroppedBytesHi_Type()
)
wwpLeosTrafficProfileCascadedDroppedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedDroppedBytesHi.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedDroppedBytesLo_Type = Counter32
_WwpLeosTrafficProfileCascadedDroppedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileCascadedDroppedBytesLo = _WwpLeosTrafficProfileCascadedDroppedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1, 4),
    _WwpLeosTrafficProfileCascadedDroppedBytesLo_Type()
)
wwpLeosTrafficProfileCascadedDroppedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedDroppedBytesLo.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedRemarkedBytesHi_Type = Counter32
_WwpLeosTrafficProfileCascadedRemarkedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileCascadedRemarkedBytesHi = _WwpLeosTrafficProfileCascadedRemarkedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1, 5),
    _WwpLeosTrafficProfileCascadedRemarkedBytesHi_Type()
)
wwpLeosTrafficProfileCascadedRemarkedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedRemarkedBytesHi.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedRemarkedBytesLo_Type = Counter32
_WwpLeosTrafficProfileCascadedRemarkedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileCascadedRemarkedBytesLo = _WwpLeosTrafficProfileCascadedRemarkedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 8, 1, 6),
    _WwpLeosTrafficProfileCascadedRemarkedBytesLo_Type()
)
wwpLeosTrafficProfileCascadedRemarkedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedRemarkedBytesLo.setStatus("deprecated")
_WwpLeosTrafficProfileStdStatsTable_Object = MibTable
wwpLeosTrafficProfileStdStatsTable = _WwpLeosTrafficProfileStdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdStatsTable.setStatus("current")
_WwpLeosTrafficProfileStdStatsEntry_Object = MibTableRow
wwpLeosTrafficProfileStdStatsEntry = _WwpLeosTrafficProfileStdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1)
)
wwpLeosTrafficProfileStdStatsEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdStatsEntry.setStatus("current")
_WwpLeosTrafficProfileStdAcceptedBytesHi_Type = Counter32
_WwpLeosTrafficProfileStdAcceptedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileStdAcceptedBytesHi = _WwpLeosTrafficProfileStdAcceptedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 1),
    _WwpLeosTrafficProfileStdAcceptedBytesHi_Type()
)
wwpLeosTrafficProfileStdAcceptedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdAcceptedBytesHi.setStatus("current")
_WwpLeosTrafficProfileStdAcceptedBytesLo_Type = Counter32
_WwpLeosTrafficProfileStdAcceptedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileStdAcceptedBytesLo = _WwpLeosTrafficProfileStdAcceptedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 2),
    _WwpLeosTrafficProfileStdAcceptedBytesLo_Type()
)
wwpLeosTrafficProfileStdAcceptedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdAcceptedBytesLo.setStatus("current")
_WwpLeosTrafficProfileStdDroppedBytesHi_Type = Counter32
_WwpLeosTrafficProfileStdDroppedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileStdDroppedBytesHi = _WwpLeosTrafficProfileStdDroppedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 3),
    _WwpLeosTrafficProfileStdDroppedBytesHi_Type()
)
wwpLeosTrafficProfileStdDroppedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDroppedBytesHi.setStatus("current")
_WwpLeosTrafficProfileStdDroppedBytesLo_Type = Counter32
_WwpLeosTrafficProfileStdDroppedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileStdDroppedBytesLo = _WwpLeosTrafficProfileStdDroppedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 4),
    _WwpLeosTrafficProfileStdDroppedBytesLo_Type()
)
wwpLeosTrafficProfileStdDroppedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDroppedBytesLo.setStatus("current")
_WwpLeosTrafficProfileStdHCAcceptedBytes_Type = Counter64
_WwpLeosTrafficProfileStdHCAcceptedBytes_Object = MibTableColumn
wwpLeosTrafficProfileStdHCAcceptedBytes = _WwpLeosTrafficProfileStdHCAcceptedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 5),
    _WwpLeosTrafficProfileStdHCAcceptedBytes_Type()
)
wwpLeosTrafficProfileStdHCAcceptedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdHCAcceptedBytes.setStatus("current")
_WwpLeosTrafficProfileStdHCDroppedBytes_Type = Counter64
_WwpLeosTrafficProfileStdHCDroppedBytes_Object = MibTableColumn
wwpLeosTrafficProfileStdHCDroppedBytes = _WwpLeosTrafficProfileStdHCDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 6),
    _WwpLeosTrafficProfileStdHCDroppedBytes_Type()
)
wwpLeosTrafficProfileStdHCDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdHCDroppedBytes.setStatus("current")
_WwpLeosTrafficProfileStdHCAcceptedPackets_Type = Counter64
_WwpLeosTrafficProfileStdHCAcceptedPackets_Object = MibTableColumn
wwpLeosTrafficProfileStdHCAcceptedPackets = _WwpLeosTrafficProfileStdHCAcceptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 7),
    _WwpLeosTrafficProfileStdHCAcceptedPackets_Type()
)
wwpLeosTrafficProfileStdHCAcceptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdHCAcceptedPackets.setStatus("current")
_WwpLeosTrafficProfileStdHCDroppedPackets_Type = Counter64
_WwpLeosTrafficProfileStdHCDroppedPackets_Object = MibTableColumn
wwpLeosTrafficProfileStdHCDroppedPackets = _WwpLeosTrafficProfileStdHCDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 9, 1, 8),
    _WwpLeosTrafficProfileStdHCDroppedPackets_Type()
)
wwpLeosTrafficProfileStdHCDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdHCDroppedPackets.setStatus("current")
_WwpLeosTrafficProfileCascadedGlobalTable_Object = MibTable
wwpLeosTrafficProfileCascadedGlobalTable = _WwpLeosTrafficProfileCascadedGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalTable.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedGlobalEntry_Object = MibTableRow
wwpLeosTrafficProfileCascadedGlobalEntry = _WwpLeosTrafficProfileCascadedGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10, 1)
)
wwpLeosTrafficProfileCascadedGlobalEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileCascadedIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalEntry.setStatus("deprecated")


class _WwpLeosTrafficProfileCascadedGlobalDot1d_Type(Integer32):
    """Custom type wwpLeosTrafficProfileCascadedGlobalDot1d based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_WwpLeosTrafficProfileCascadedGlobalDot1d_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileCascadedGlobalDot1d_Object = MibTableColumn
wwpLeosTrafficProfileCascadedGlobalDot1d = _WwpLeosTrafficProfileCascadedGlobalDot1d_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10, 1, 1),
    _WwpLeosTrafficProfileCascadedGlobalDot1d_Type()
)
wwpLeosTrafficProfileCascadedGlobalDot1d.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalDot1d.setStatus("deprecated")


class _WwpLeosTrafficProfileCascadedGlobalIpPrec_Type(Integer32):
    """Custom type wwpLeosTrafficProfileCascadedGlobalIpPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_WwpLeosTrafficProfileCascadedGlobalIpPrec_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileCascadedGlobalIpPrec_Object = MibTableColumn
wwpLeosTrafficProfileCascadedGlobalIpPrec = _WwpLeosTrafficProfileCascadedGlobalIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10, 1, 2),
    _WwpLeosTrafficProfileCascadedGlobalIpPrec_Type()
)
wwpLeosTrafficProfileCascadedGlobalIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalIpPrec.setStatus("deprecated")


class _WwpLeosTrafficProfileCascadedGlobalDscp_Type(Integer32):
    """Custom type wwpLeosTrafficProfileCascadedGlobalDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_WwpLeosTrafficProfileCascadedGlobalDscp_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileCascadedGlobalDscp_Object = MibTableColumn
wwpLeosTrafficProfileCascadedGlobalDscp = _WwpLeosTrafficProfileCascadedGlobalDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10, 1, 3),
    _WwpLeosTrafficProfileCascadedGlobalDscp_Type()
)
wwpLeosTrafficProfileCascadedGlobalDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalDscp.setStatus("deprecated")


class _WwpLeosTrafficProfileCascadedGlobalName_Type(DisplayString):
    """Custom type wwpLeosTrafficProfileCascadedGlobalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeosTrafficProfileCascadedGlobalName_Type.__name__ = "DisplayString"
_WwpLeosTrafficProfileCascadedGlobalName_Object = MibTableColumn
wwpLeosTrafficProfileCascadedGlobalName = _WwpLeosTrafficProfileCascadedGlobalName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10, 1, 4),
    _WwpLeosTrafficProfileCascadedGlobalName_Type()
)
wwpLeosTrafficProfileCascadedGlobalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalName.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedGlobalStatus_Type = RowStatus
_WwpLeosTrafficProfileCascadedGlobalStatus_Object = MibTableColumn
wwpLeosTrafficProfileCascadedGlobalStatus = _WwpLeosTrafficProfileCascadedGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 10, 1, 5),
    _WwpLeosTrafficProfileCascadedGlobalStatus_Type()
)
wwpLeosTrafficProfileCascadedGlobalStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedGlobalStatus.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalStatsTable_Object = MibTable
wwpLeosTrafficProfileCascadedTotalStatsTable = _WwpLeosTrafficProfileCascadedTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalStatsTable.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalStatsEntry_Object = MibTableRow
wwpLeosTrafficProfileCascadedTotalStatsEntry = _WwpLeosTrafficProfileCascadedTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1)
)
wwpLeosTrafficProfileCascadedTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileCascadedIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalStatsEntry.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Type = Counter32
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi = _WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1, 1),
    _WwpLeosTrafficProfileCascadedTotalAcceptedBytesHi_Type()
)
wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Type = Counter32
_WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo = _WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1, 2),
    _WwpLeosTrafficProfileCascadedTotalAcceptedBytesLo_Type()
)
wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Type = Counter32
_WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileCascadedTotalDroppedBytesHi = _WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1, 3),
    _WwpLeosTrafficProfileCascadedTotalDroppedBytesHi_Type()
)
wwpLeosTrafficProfileCascadedTotalDroppedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalDroppedBytesHi.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Type = Counter32
_WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileCascadedTotalDroppedBytesLo = _WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1, 4),
    _WwpLeosTrafficProfileCascadedTotalDroppedBytesLo_Type()
)
wwpLeosTrafficProfileCascadedTotalDroppedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalDroppedBytesLo.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Type = Counter32
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi = _WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1, 5),
    _WwpLeosTrafficProfileCascadedTotalRemarkedBytesHi_Type()
)
wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi.setStatus("deprecated")
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Type = Counter32
_WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo = _WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 11, 1, 6),
    _WwpLeosTrafficProfileCascadedTotalRemarkedBytesLo_Type()
)
wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo.setStatus("deprecated")
_WwpLeosTrafficProfileStdTotalStatsTable_Object = MibTable
wwpLeosTrafficProfileStdTotalStatsTable = _WwpLeosTrafficProfileStdTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 12)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTotalStatsTable.setStatus("current")
_WwpLeosTrafficProfileStdTotalStatsEntry_Object = MibTableRow
wwpLeosTrafficProfileStdTotalStatsEntry = _WwpLeosTrafficProfileStdTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 12, 1)
)
wwpLeosTrafficProfileStdTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTotalStatsEntry.setStatus("current")
_WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Type = Counter32
_WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileStdTotalAcceptedBytesHi = _WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 12, 1, 1),
    _WwpLeosTrafficProfileStdTotalAcceptedBytesHi_Type()
)
wwpLeosTrafficProfileStdTotalAcceptedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTotalAcceptedBytesHi.setStatus("current")
_WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Type = Counter32
_WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileStdTotalAcceptedBytesLo = _WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 12, 1, 2),
    _WwpLeosTrafficProfileStdTotalAcceptedBytesLo_Type()
)
wwpLeosTrafficProfileStdTotalAcceptedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTotalAcceptedBytesLo.setStatus("current")
_WwpLeosTrafficProfileStdTotalDroppedBytesHi_Type = Counter32
_WwpLeosTrafficProfileStdTotalDroppedBytesHi_Object = MibTableColumn
wwpLeosTrafficProfileStdTotalDroppedBytesHi = _WwpLeosTrafficProfileStdTotalDroppedBytesHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 12, 1, 3),
    _WwpLeosTrafficProfileStdTotalDroppedBytesHi_Type()
)
wwpLeosTrafficProfileStdTotalDroppedBytesHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTotalDroppedBytesHi.setStatus("current")
_WwpLeosTrafficProfileStdTotalDroppedBytesLo_Type = Counter32
_WwpLeosTrafficProfileStdTotalDroppedBytesLo_Object = MibTableColumn
wwpLeosTrafficProfileStdTotalDroppedBytesLo = _WwpLeosTrafficProfileStdTotalDroppedBytesLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 12, 1, 4),
    _WwpLeosTrafficProfileStdTotalDroppedBytesLo_Type()
)
wwpLeosTrafficProfileStdTotalDroppedBytesLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdTotalDroppedBytesLo.setStatus("current")
_WwpLeosTrafficProfileStdVlanTable_Object = MibTable
wwpLeosTrafficProfileStdVlanTable = _WwpLeosTrafficProfileStdVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 14)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanTable.setStatus("current")
_WwpLeosTrafficProfileStdVlanEntry_Object = MibTableRow
wwpLeosTrafficProfileStdVlanEntry = _WwpLeosTrafficProfileStdVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 14, 1)
)
wwpLeosTrafficProfileStdVlanEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdVlanIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanEntry.setStatus("current")


class _WwpLeosTrafficProfileStdVlanIndex_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosTrafficProfileStdVlanIndex_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdVlanIndex_Object = MibTableColumn
wwpLeosTrafficProfileStdVlanIndex = _WwpLeosTrafficProfileStdVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 14, 1, 1),
    _WwpLeosTrafficProfileStdVlanIndex_Type()
)
wwpLeosTrafficProfileStdVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanIndex.setStatus("current")


class _WwpLeosTrafficProfileStdVlanToProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdVlanToProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosTrafficProfileStdVlanToProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdVlanToProfile_Object = MibTableColumn
wwpLeosTrafficProfileStdVlanToProfile = _WwpLeosTrafficProfileStdVlanToProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 14, 1, 2),
    _WwpLeosTrafficProfileStdVlanToProfile_Type()
)
wwpLeosTrafficProfileStdVlanToProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanToProfile.setStatus("current")
_WwpLeosTrafficProfileStdVlanStatus_Type = RowStatus
_WwpLeosTrafficProfileStdVlanStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdVlanStatus = _WwpLeosTrafficProfileStdVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 14, 1, 3),
    _WwpLeosTrafficProfileStdVlanStatus_Type()
)
wwpLeosTrafficProfileStdVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanStatus.setStatus("current")
_WwpLeosTrafficProfileStdDscpTable_Object = MibTable
wwpLeosTrafficProfileStdDscpTable = _WwpLeosTrafficProfileStdDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 15)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDscpTable.setStatus("current")
_WwpLeosTrafficProfileStdDscpEntry_Object = MibTableRow
wwpLeosTrafficProfileStdDscpEntry = _WwpLeosTrafficProfileStdDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 15, 1)
)
wwpLeosTrafficProfileStdDscpEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdDscp"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDscpEntry.setStatus("current")


class _WwpLeosTrafficProfileStdDscp_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosTrafficProfileStdDscp_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdDscp_Object = MibTableColumn
wwpLeosTrafficProfileStdDscp = _WwpLeosTrafficProfileStdDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 15, 1, 1),
    _WwpLeosTrafficProfileStdDscp_Type()
)
wwpLeosTrafficProfileStdDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDscp.setStatus("current")


class _WwpLeosTrafficProfileStdDscpToProfile_Type(Integer32):
    """Custom type wwpLeosTrafficProfileStdDscpToProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosTrafficProfileStdDscpToProfile_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileStdDscpToProfile_Object = MibTableColumn
wwpLeosTrafficProfileStdDscpToProfile = _WwpLeosTrafficProfileStdDscpToProfile_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 15, 1, 2),
    _WwpLeosTrafficProfileStdDscpToProfile_Type()
)
wwpLeosTrafficProfileStdDscpToProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDscpToProfile.setStatus("current")
_WwpLeosTrafficProfileStdDscpStatus_Type = RowStatus
_WwpLeosTrafficProfileStdDscpStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdDscpStatus = _WwpLeosTrafficProfileStdDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 15, 1, 3),
    _WwpLeosTrafficProfileStdDscpStatus_Type()
)
wwpLeosTrafficProfileStdDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdDscpStatus.setStatus("current")
_WwpLeosTrafficProfileMeterPoolTable_Object = MibTable
wwpLeosTrafficProfileMeterPoolTable = _WwpLeosTrafficProfileMeterPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolTable.setStatus("current")
_WwpLeosTrafficProfileMeterPoolEntry_Object = MibTableRow
wwpLeosTrafficProfileMeterPoolEntry = _WwpLeosTrafficProfileMeterPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1)
)
wwpLeosTrafficProfileMeterPoolEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileMeterPoolIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolEntry.setStatus("current")


class _WwpLeosTrafficProfileMeterPoolIndex_Type(Integer32):
    """Custom type wwpLeosTrafficProfileMeterPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WwpLeosTrafficProfileMeterPoolIndex_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileMeterPoolIndex_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolIndex = _WwpLeosTrafficProfileMeterPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 1),
    _WwpLeosTrafficProfileMeterPoolIndex_Type()
)
wwpLeosTrafficProfileMeterPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolIndex.setStatus("current")


class _WwpLeosTrafficProfileMeterPoolName_Type(DisplayString):
    """Custom type wwpLeosTrafficProfileMeterPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeosTrafficProfileMeterPoolName_Type.__name__ = "DisplayString"
_WwpLeosTrafficProfileMeterPoolName_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolName = _WwpLeosTrafficProfileMeterPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 2),
    _WwpLeosTrafficProfileMeterPoolName_Type()
)
wwpLeosTrafficProfileMeterPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolName.setStatus("current")
_WwpLeosTrafficProfileMeterPoolNumOfMeters_Type = Integer32
_WwpLeosTrafficProfileMeterPoolNumOfMeters_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolNumOfMeters = _WwpLeosTrafficProfileMeterPoolNumOfMeters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 3),
    _WwpLeosTrafficProfileMeterPoolNumOfMeters_Type()
)
wwpLeosTrafficProfileMeterPoolNumOfMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolNumOfMeters.setStatus("current")
_WwpLeosTrafficProfileMeterPoolMetersUsed_Type = Integer32
_WwpLeosTrafficProfileMeterPoolMetersUsed_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolMetersUsed = _WwpLeosTrafficProfileMeterPoolMetersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 4),
    _WwpLeosTrafficProfileMeterPoolMetersUsed_Type()
)
wwpLeosTrafficProfileMeterPoolMetersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolMetersUsed.setStatus("current")
_WwpLeosTrafficProfileMeterPoolNumOfStats_Type = Integer32
_WwpLeosTrafficProfileMeterPoolNumOfStats_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolNumOfStats = _WwpLeosTrafficProfileMeterPoolNumOfStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 5),
    _WwpLeosTrafficProfileMeterPoolNumOfStats_Type()
)
wwpLeosTrafficProfileMeterPoolNumOfStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolNumOfStats.setStatus("current")
_WwpLeosTrafficProfileMeterPoolStatsUsed_Type = Integer32
_WwpLeosTrafficProfileMeterPoolStatsUsed_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolStatsUsed = _WwpLeosTrafficProfileMeterPoolStatsUsed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 6),
    _WwpLeosTrafficProfileMeterPoolStatsUsed_Type()
)
wwpLeosTrafficProfileMeterPoolStatsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolStatsUsed.setStatus("current")
_WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Type = Integer32
_WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolNumOfClassifiers = _WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 7),
    _WwpLeosTrafficProfileMeterPoolNumOfClassifiers_Type()
)
wwpLeosTrafficProfileMeterPoolNumOfClassifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolNumOfClassifiers.setStatus("current")
_WwpLeosTrafficProfileMeterPoolClassifiersUsed_Type = Integer32
_WwpLeosTrafficProfileMeterPoolClassifiersUsed_Object = MibTableColumn
wwpLeosTrafficProfileMeterPoolClassifiersUsed = _WwpLeosTrafficProfileMeterPoolClassifiersUsed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 16, 1, 8),
    _WwpLeosTrafficProfileMeterPoolClassifiersUsed_Type()
)
wwpLeosTrafficProfileMeterPoolClassifiersUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileMeterPoolClassifiersUsed.setStatus("current")
_WwpLeosTrafficProfileTosStampTable_Object = MibTable
wwpLeosTrafficProfileTosStampTable = _WwpLeosTrafficProfileTosStampTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 20)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileTosStampTable.setStatus("current")
_WwpLeosTrafficProfileTosStampEntry_Object = MibTableRow
wwpLeosTrafficProfileTosStampEntry = _WwpLeosTrafficProfileTosStampEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 20, 1)
)
wwpLeosTrafficProfileTosStampEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileTosStampEntry.setStatus("current")


class _WwpLeosTrafficProfileTosStampState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileTosStampState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileTosStampState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileTosStampState_Object = MibTableColumn
wwpLeosTrafficProfileTosStampState = _WwpLeosTrafficProfileTosStampState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 20, 1, 1),
    _WwpLeosTrafficProfileTosStampState_Type()
)
wwpLeosTrafficProfileTosStampState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileTosStampState.setStatus("current")


class _WwpLeosTrafficProfileTosStampValue_Type(Integer32):
    """Custom type wwpLeosTrafficProfileTosStampValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosTrafficProfileTosStampValue_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileTosStampValue_Object = MibTableColumn
wwpLeosTrafficProfileTosStampValue = _WwpLeosTrafficProfileTosStampValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 20, 1, 2),
    _WwpLeosTrafficProfileTosStampValue_Type()
)
wwpLeosTrafficProfileTosStampValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileTosStampValue.setStatus("current")
_WwpLeosTrafficProfileIpDscpTable_Object = MibTable
wwpLeosTrafficProfileIpDscpTable = _WwpLeosTrafficProfileIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpDscpTable.setStatus("current")
_WwpLeosTrafficProfileIpDscpEntry_Object = MibTableRow
wwpLeosTrafficProfileIpDscpEntry = _WwpLeosTrafficProfileIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1)
)
wwpLeosTrafficProfileIpDscpEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpDscpEntry.setStatus("current")


class _WwpLeosTrafficProfileIpp0Cs0State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp0Cs0State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp0Cs0State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp0Cs0State_Object = MibTableColumn
wwpLeosTrafficProfileIpp0Cs0State = _WwpLeosTrafficProfileIpp0Cs0State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 1),
    _WwpLeosTrafficProfileIpp0Cs0State_Type()
)
wwpLeosTrafficProfileIpp0Cs0State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp0Cs0State.setStatus("current")


class _WwpLeosTrafficProfileIpp1Cs1State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp1Cs1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp1Cs1State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp1Cs1State_Object = MibTableColumn
wwpLeosTrafficProfileIpp1Cs1State = _WwpLeosTrafficProfileIpp1Cs1State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 2),
    _WwpLeosTrafficProfileIpp1Cs1State_Type()
)
wwpLeosTrafficProfileIpp1Cs1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp1Cs1State.setStatus("current")


class _WwpLeosTrafficProfileIpp2Cs2State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp2Cs2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp2Cs2State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp2Cs2State_Object = MibTableColumn
wwpLeosTrafficProfileIpp2Cs2State = _WwpLeosTrafficProfileIpp2Cs2State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 3),
    _WwpLeosTrafficProfileIpp2Cs2State_Type()
)
wwpLeosTrafficProfileIpp2Cs2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp2Cs2State.setStatus("current")


class _WwpLeosTrafficProfileIpp3Cs3State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp3Cs3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp3Cs3State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp3Cs3State_Object = MibTableColumn
wwpLeosTrafficProfileIpp3Cs3State = _WwpLeosTrafficProfileIpp3Cs3State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 4),
    _WwpLeosTrafficProfileIpp3Cs3State_Type()
)
wwpLeosTrafficProfileIpp3Cs3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp3Cs3State.setStatus("current")


class _WwpLeosTrafficProfileIpp4Cs4State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp4Cs4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp4Cs4State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp4Cs4State_Object = MibTableColumn
wwpLeosTrafficProfileIpp4Cs4State = _WwpLeosTrafficProfileIpp4Cs4State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 5),
    _WwpLeosTrafficProfileIpp4Cs4State_Type()
)
wwpLeosTrafficProfileIpp4Cs4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp4Cs4State.setStatus("current")


class _WwpLeosTrafficProfileIpp5Cs5State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp5Cs5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp5Cs5State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp5Cs5State_Object = MibTableColumn
wwpLeosTrafficProfileIpp5Cs5State = _WwpLeosTrafficProfileIpp5Cs5State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 6),
    _WwpLeosTrafficProfileIpp5Cs5State_Type()
)
wwpLeosTrafficProfileIpp5Cs5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp5Cs5State.setStatus("current")


class _WwpLeosTrafficProfileIpp6Cs6State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp6Cs6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp6Cs6State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp6Cs6State_Object = MibTableColumn
wwpLeosTrafficProfileIpp6Cs6State = _WwpLeosTrafficProfileIpp6Cs6State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 7),
    _WwpLeosTrafficProfileIpp6Cs6State_Type()
)
wwpLeosTrafficProfileIpp6Cs6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp6Cs6State.setStatus("current")


class _WwpLeosTrafficProfileIpp7Cs7State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileIpp7Cs7State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileIpp7Cs7State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileIpp7Cs7State_Object = MibTableColumn
wwpLeosTrafficProfileIpp7Cs7State = _WwpLeosTrafficProfileIpp7Cs7State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 8),
    _WwpLeosTrafficProfileIpp7Cs7State_Type()
)
wwpLeosTrafficProfileIpp7Cs7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileIpp7Cs7State.setStatus("current")


class _WwpLeosTrafficProfileAf1State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileAf1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileAf1State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileAf1State_Object = MibTableColumn
wwpLeosTrafficProfileAf1State = _WwpLeosTrafficProfileAf1State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 9),
    _WwpLeosTrafficProfileAf1State_Type()
)
wwpLeosTrafficProfileAf1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileAf1State.setStatus("current")


class _WwpLeosTrafficProfileAf2State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileAf2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileAf2State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileAf2State_Object = MibTableColumn
wwpLeosTrafficProfileAf2State = _WwpLeosTrafficProfileAf2State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 10),
    _WwpLeosTrafficProfileAf2State_Type()
)
wwpLeosTrafficProfileAf2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileAf2State.setStatus("current")


class _WwpLeosTrafficProfileAf3State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileAf3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileAf3State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileAf3State_Object = MibTableColumn
wwpLeosTrafficProfileAf3State = _WwpLeosTrafficProfileAf3State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 11),
    _WwpLeosTrafficProfileAf3State_Type()
)
wwpLeosTrafficProfileAf3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileAf3State.setStatus("current")


class _WwpLeosTrafficProfileAf4State_Type(Integer32):
    """Custom type wwpLeosTrafficProfileAf4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileAf4State_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileAf4State_Object = MibTableColumn
wwpLeosTrafficProfileAf4State = _WwpLeosTrafficProfileAf4State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 12),
    _WwpLeosTrafficProfileAf4State_Type()
)
wwpLeosTrafficProfileAf4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileAf4State.setStatus("current")


class _WwpLeosTrafficProfileEfState_Type(Integer32):
    """Custom type wwpLeosTrafficProfileEfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosTrafficProfileEfState_Type.__name__ = "Integer32"
_WwpLeosTrafficProfileEfState_Object = MibTableColumn
wwpLeosTrafficProfileEfState = _WwpLeosTrafficProfileEfState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 21, 1, 13),
    _WwpLeosTrafficProfileEfState_Type()
)
wwpLeosTrafficProfileEfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileEfState.setStatus("current")
_WwpLeosTrafficProfileStdVlanDot1dTable_Object = MibTable
wwpLeosTrafficProfileStdVlanDot1dTable = _WwpLeosTrafficProfileStdVlanDot1dTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 40)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanDot1dTable.setStatus("current")
_WwpLeosTrafficProfileStdVlanDot1dEntry_Object = MibTableRow
wwpLeosTrafficProfileStdVlanDot1dEntry = _WwpLeosTrafficProfileStdVlanDot1dEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 40, 1)
)
wwpLeosTrafficProfileStdVlanDot1dEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdDot1d"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanDot1dEntry.setStatus("current")
_WwpLeosTrafficProfileStdVlanDot1dStatus_Type = RowStatus
_WwpLeosTrafficProfileStdVlanDot1dStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdVlanDot1dStatus = _WwpLeosTrafficProfileStdVlanDot1dStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 40, 1, 1),
    _WwpLeosTrafficProfileStdVlanDot1dStatus_Type()
)
wwpLeosTrafficProfileStdVlanDot1dStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanDot1dStatus.setStatus("current")
_WwpLeosTrafficProfileStdVlanIpPrecTable_Object = MibTable
wwpLeosTrafficProfileStdVlanIpPrecTable = _WwpLeosTrafficProfileStdVlanIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 41)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanIpPrecTable.setStatus("current")
_WwpLeosTrafficProfileStdVlanIpPrecEntry_Object = MibTableRow
wwpLeosTrafficProfileStdVlanIpPrecEntry = _WwpLeosTrafficProfileStdVlanIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 41, 1)
)
wwpLeosTrafficProfileStdVlanIpPrecEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIpPrec"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanIpPrecEntry.setStatus("current")
_WwpLeosTrafficProfileStdVlanIpPrecStatus_Type = RowStatus
_WwpLeosTrafficProfileStdVlanIpPrecStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdVlanIpPrecStatus = _WwpLeosTrafficProfileStdVlanIpPrecStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 41, 1, 1),
    _WwpLeosTrafficProfileStdVlanIpPrecStatus_Type()
)
wwpLeosTrafficProfileStdVlanIpPrecStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanIpPrecStatus.setStatus("current")
_WwpLeosTrafficProfileStdVlanDscpTable_Object = MibTable
wwpLeosTrafficProfileStdVlanDscpTable = _WwpLeosTrafficProfileStdVlanDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 42)
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanDscpTable.setStatus("current")
_WwpLeosTrafficProfileStdVlanDscpEntry_Object = MibTableRow
wwpLeosTrafficProfileStdVlanDscpEntry = _WwpLeosTrafficProfileStdVlanDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 42, 1)
)
wwpLeosTrafficProfileStdVlanDscpEntry.setIndexNames(
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfilePort"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdDscp"),
    (0, "WWP-LEOS-TRAFFIC-PROFILE-MIB", "wwpLeosTrafficProfileStdIndx"),
)
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanDscpEntry.setStatus("current")
_WwpLeosTrafficProfileStdVlanDscpStatus_Type = RowStatus
_WwpLeosTrafficProfileStdVlanDscpStatus_Object = MibTableColumn
wwpLeosTrafficProfileStdVlanDscpStatus = _WwpLeosTrafficProfileStdVlanDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 1, 1, 42, 1, 2),
    _WwpLeosTrafficProfileStdVlanDscpStatus_Type()
)
wwpLeosTrafficProfileStdVlanDscpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTrafficProfileStdVlanDscpStatus.setStatus("current")
_WwpLeosTrafficProfileNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileNotificationPrefix = _WwpLeosTrafficProfileNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 2)
)
_WwpLeosTrafficProfileNotifications_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileNotifications = _WwpLeosTrafficProfileNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 2, 0)
)
_WwpLeosTrafficProfileMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileMIBConformance = _WwpLeosTrafficProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 3)
)
_WwpLeosTrafficProfileMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileMIBCompliances = _WwpLeosTrafficProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 3, 1)
)
_WwpLeosTrafficProfileMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosTrafficProfileMIBGroups = _WwpLeosTrafficProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 27, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-TRAFFIC-PROFILE-MIB",
    **{"wwpLeosTrafficProfileMIB": wwpLeosTrafficProfileMIB,
       "wwpLeosTrafficProfileObjects": wwpLeosTrafficProfileObjects,
       "wwpLeosTrafficProfile": wwpLeosTrafficProfile,
       "wwpLeosTrafficProfileGlobalAttrs": wwpLeosTrafficProfileGlobalAttrs,
       "wwpLeosTrafficProfileGlobalState": wwpLeosTrafficProfileGlobalState,
       "wwpLeosTrafficProfileGlobalMeterProvisioningState": wwpLeosTrafficProfileGlobalMeterProvisioningState,
       "wwpLeosTrafficProfilePortTable": wwpLeosTrafficProfilePortTable,
       "wwpLeosTrafficProfilePortEntry": wwpLeosTrafficProfilePortEntry,
       "wwpLeosTrafficProfilePort": wwpLeosTrafficProfilePort,
       "wwpLeosTrafficProfileAdminState": wwpLeosTrafficProfileAdminState,
       "wwpLeosTrafficProfileOperState": wwpLeosTrafficProfileOperState,
       "wwpLeosTrafficProfileMode": wwpLeosTrafficProfileMode,
       "wwpLeosTrafficProfileNonConformCascadedProfile": wwpLeosTrafficProfileNonConformCascadedProfile,
       "wwpLeosTrafficProfileNonConformStdProfile": wwpLeosTrafficProfileNonConformStdProfile,
       "wwpLeosTrafficProfileArpCascadedProfile": wwpLeosTrafficProfileArpCascadedProfile,
       "wwpLeosTrafficProfileArpStdProfile": wwpLeosTrafficProfileArpStdProfile,
       "wwpLeosTrafficProfileMeterPool": wwpLeosTrafficProfileMeterPool,
       "wwpLeosTrafficProfileClassifierMode": wwpLeosTrafficProfileClassifierMode,
       "wwpLeosTrafficProfileCascadedTable": wwpLeosTrafficProfileCascadedTable,
       "wwpLeosTrafficProfileCascadedEntry": wwpLeosTrafficProfileCascadedEntry,
       "wwpLeosTrafficProfileCascadedIndx": wwpLeosTrafficProfileCascadedIndx,
       "wwpLeosTrafficProfileCascadedCir": wwpLeosTrafficProfileCascadedCir,
       "wwpLeosTrafficProfileCascadedPir": wwpLeosTrafficProfileCascadedPir,
       "wwpLeosTrafficProfileCascadedStatus": wwpLeosTrafficProfileCascadedStatus,
       "wwpLeosTrafficProfileStdTable": wwpLeosTrafficProfileStdTable,
       "wwpLeosTrafficProfileStdEntry": wwpLeosTrafficProfileStdEntry,
       "wwpLeosTrafficProfileStdIndx": wwpLeosTrafficProfileStdIndx,
       "wwpLeosTrafficProfileStdCir": wwpLeosTrafficProfileStdCir,
       "wwpLeosTrafficProfileStdPir": wwpLeosTrafficProfileStdPir,
       "wwpLeosTrafficProfileStdName": wwpLeosTrafficProfileStdName,
       "wwpLeosTrafficProfileStdStatus": wwpLeosTrafficProfileStdStatus,
       "wwpLeosTrafficProfileStdVlan": wwpLeosTrafficProfileStdVlan,
       "wwpLeosTrafficProfileStdCbs": wwpLeosTrafficProfileStdCbs,
       "wwpLeosTrafficProfileStdEbs": wwpLeosTrafficProfileStdEbs,
       "wwpLeosTrafficProfileStdDscpRemarkPolicy": wwpLeosTrafficProfileStdDscpRemarkPolicy,
       "wwpLeosTrafficProfileStdFixedDscp": wwpLeosTrafficProfileStdFixedDscp,
       "wwpLeosTrafficProfileStdUnsetVlan": wwpLeosTrafficProfileStdUnsetVlan,
       "wwpLeosTrafficProfileStdDefaultProfile": wwpLeosTrafficProfileStdDefaultProfile,
       "wwpLeosTrafficeProfileStdDrop": wwpLeosTrafficeProfileStdDrop,
       "wwpLeosTrafficProfileStdParentIndex": wwpLeosTrafficProfileStdParentIndex,
       "wwpLeosTrafficProfileStdChildMode": wwpLeosTrafficProfileStdChildMode,
       "wwpLeosTrafficProfileStdStatsMonitor": wwpLeosTrafficProfileStdStatsMonitor,
       "wwpLeosTrafficProfileStdUntaggedState": wwpLeosTrafficProfileStdUntaggedState,
       "wwpLeosTrafficProfileStdVs": wwpLeosTrafficProfileStdVs,
       "wwpLeosTrafficProfileStdRemarkColorPolicy": wwpLeosTrafficProfileStdRemarkColorPolicy,
       "wwpLeosTrafficProfileStdRemarkRcosPolicy": wwpLeosTrafficProfileStdRemarkRcosPolicy,
       "wwpLeosTrafficProfileStdYellowRemarkRcos": wwpLeosTrafficProfileStdYellowRemarkRcos,
       "wwpLeosTrafficProfileStdGreenRemarkRcos": wwpLeosTrafficProfileStdGreenRemarkRcos,
       "wwpLeosTrafficProfileStdIngressColorAware": wwpLeosTrafficProfileStdIngressColorAware,
       "wwpLeosTrafficProfileStdEir": wwpLeosTrafficProfileStdEir,
       "wwpLeosTrafficProfileStdDot1dTable": wwpLeosTrafficProfileStdDot1dTable,
       "wwpLeosTrafficProfileStdDot1dEntry": wwpLeosTrafficProfileStdDot1dEntry,
       "wwpLeosTrafficProfileStdDot1d": wwpLeosTrafficProfileStdDot1d,
       "wwpLeosTrafficProfileStdDot1dToProfile": wwpLeosTrafficProfileStdDot1dToProfile,
       "wwpLeosTrafficProfileStdDot1dStatus": wwpLeosTrafficProfileStdDot1dStatus,
       "wwpLeosTrafficProfileStdIpPrecTable": wwpLeosTrafficProfileStdIpPrecTable,
       "wwpLeosTrafficProfileStdIpPrecEntry": wwpLeosTrafficProfileStdIpPrecEntry,
       "wwpLeosTrafficProfileStdIpPrec": wwpLeosTrafficProfileStdIpPrec,
       "wwpLeosTrafficProfileStdIpPrecToProfile": wwpLeosTrafficProfileStdIpPrecToProfile,
       "wwpLeosTrafficProfileStdIpPrecStatus": wwpLeosTrafficProfileStdIpPrecStatus,
       "wwpLeosTrafficProfileStdPhbTable": wwpLeosTrafficProfileStdPhbTable,
       "wwpLeosTrafficProfileStdPhbEntry": wwpLeosTrafficProfileStdPhbEntry,
       "wwpLeosTrafficProfileStdPhb": wwpLeosTrafficProfileStdPhb,
       "wwpLeosTrafficProfileStdPhbToProfile": wwpLeosTrafficProfileStdPhbToProfile,
       "wwpLeosTrafficProfileStdPhbStatus": wwpLeosTrafficProfileStdPhbStatus,
       "wwpLeosTrafficProfileCascadedStatsTable": wwpLeosTrafficProfileCascadedStatsTable,
       "wwpLeosTrafficProfileCascadedStatsEntry": wwpLeosTrafficProfileCascadedStatsEntry,
       "wwpLeosTrafficProfileCascadedAcceptedBytesHi": wwpLeosTrafficProfileCascadedAcceptedBytesHi,
       "wwpLeosTrafficProfileCascadedAcceptedBytesLo": wwpLeosTrafficProfileCascadedAcceptedBytesLo,
       "wwpLeosTrafficProfileCascadedDroppedBytesHi": wwpLeosTrafficProfileCascadedDroppedBytesHi,
       "wwpLeosTrafficProfileCascadedDroppedBytesLo": wwpLeosTrafficProfileCascadedDroppedBytesLo,
       "wwpLeosTrafficProfileCascadedRemarkedBytesHi": wwpLeosTrafficProfileCascadedRemarkedBytesHi,
       "wwpLeosTrafficProfileCascadedRemarkedBytesLo": wwpLeosTrafficProfileCascadedRemarkedBytesLo,
       "wwpLeosTrafficProfileStdStatsTable": wwpLeosTrafficProfileStdStatsTable,
       "wwpLeosTrafficProfileStdStatsEntry": wwpLeosTrafficProfileStdStatsEntry,
       "wwpLeosTrafficProfileStdAcceptedBytesHi": wwpLeosTrafficProfileStdAcceptedBytesHi,
       "wwpLeosTrafficProfileStdAcceptedBytesLo": wwpLeosTrafficProfileStdAcceptedBytesLo,
       "wwpLeosTrafficProfileStdDroppedBytesHi": wwpLeosTrafficProfileStdDroppedBytesHi,
       "wwpLeosTrafficProfileStdDroppedBytesLo": wwpLeosTrafficProfileStdDroppedBytesLo,
       "wwpLeosTrafficProfileStdHCAcceptedBytes": wwpLeosTrafficProfileStdHCAcceptedBytes,
       "wwpLeosTrafficProfileStdHCDroppedBytes": wwpLeosTrafficProfileStdHCDroppedBytes,
       "wwpLeosTrafficProfileStdHCAcceptedPackets": wwpLeosTrafficProfileStdHCAcceptedPackets,
       "wwpLeosTrafficProfileStdHCDroppedPackets": wwpLeosTrafficProfileStdHCDroppedPackets,
       "wwpLeosTrafficProfileCascadedGlobalTable": wwpLeosTrafficProfileCascadedGlobalTable,
       "wwpLeosTrafficProfileCascadedGlobalEntry": wwpLeosTrafficProfileCascadedGlobalEntry,
       "wwpLeosTrafficProfileCascadedGlobalDot1d": wwpLeosTrafficProfileCascadedGlobalDot1d,
       "wwpLeosTrafficProfileCascadedGlobalIpPrec": wwpLeosTrafficProfileCascadedGlobalIpPrec,
       "wwpLeosTrafficProfileCascadedGlobalDscp": wwpLeosTrafficProfileCascadedGlobalDscp,
       "wwpLeosTrafficProfileCascadedGlobalName": wwpLeosTrafficProfileCascadedGlobalName,
       "wwpLeosTrafficProfileCascadedGlobalStatus": wwpLeosTrafficProfileCascadedGlobalStatus,
       "wwpLeosTrafficProfileCascadedTotalStatsTable": wwpLeosTrafficProfileCascadedTotalStatsTable,
       "wwpLeosTrafficProfileCascadedTotalStatsEntry": wwpLeosTrafficProfileCascadedTotalStatsEntry,
       "wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi": wwpLeosTrafficProfileCascadedTotalAcceptedBytesHi,
       "wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo": wwpLeosTrafficProfileCascadedTotalAcceptedBytesLo,
       "wwpLeosTrafficProfileCascadedTotalDroppedBytesHi": wwpLeosTrafficProfileCascadedTotalDroppedBytesHi,
       "wwpLeosTrafficProfileCascadedTotalDroppedBytesLo": wwpLeosTrafficProfileCascadedTotalDroppedBytesLo,
       "wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi": wwpLeosTrafficProfileCascadedTotalRemarkedBytesHi,
       "wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo": wwpLeosTrafficProfileCascadedTotalRemarkedBytesLo,
       "wwpLeosTrafficProfileStdTotalStatsTable": wwpLeosTrafficProfileStdTotalStatsTable,
       "wwpLeosTrafficProfileStdTotalStatsEntry": wwpLeosTrafficProfileStdTotalStatsEntry,
       "wwpLeosTrafficProfileStdTotalAcceptedBytesHi": wwpLeosTrafficProfileStdTotalAcceptedBytesHi,
       "wwpLeosTrafficProfileStdTotalAcceptedBytesLo": wwpLeosTrafficProfileStdTotalAcceptedBytesLo,
       "wwpLeosTrafficProfileStdTotalDroppedBytesHi": wwpLeosTrafficProfileStdTotalDroppedBytesHi,
       "wwpLeosTrafficProfileStdTotalDroppedBytesLo": wwpLeosTrafficProfileStdTotalDroppedBytesLo,
       "wwpLeosTrafficProfileStdVlanTable": wwpLeosTrafficProfileStdVlanTable,
       "wwpLeosTrafficProfileStdVlanEntry": wwpLeosTrafficProfileStdVlanEntry,
       "wwpLeosTrafficProfileStdVlanIndex": wwpLeosTrafficProfileStdVlanIndex,
       "wwpLeosTrafficProfileStdVlanToProfile": wwpLeosTrafficProfileStdVlanToProfile,
       "wwpLeosTrafficProfileStdVlanStatus": wwpLeosTrafficProfileStdVlanStatus,
       "wwpLeosTrafficProfileStdDscpTable": wwpLeosTrafficProfileStdDscpTable,
       "wwpLeosTrafficProfileStdDscpEntry": wwpLeosTrafficProfileStdDscpEntry,
       "wwpLeosTrafficProfileStdDscp": wwpLeosTrafficProfileStdDscp,
       "wwpLeosTrafficProfileStdDscpToProfile": wwpLeosTrafficProfileStdDscpToProfile,
       "wwpLeosTrafficProfileStdDscpStatus": wwpLeosTrafficProfileStdDscpStatus,
       "wwpLeosTrafficProfileMeterPoolTable": wwpLeosTrafficProfileMeterPoolTable,
       "wwpLeosTrafficProfileMeterPoolEntry": wwpLeosTrafficProfileMeterPoolEntry,
       "wwpLeosTrafficProfileMeterPoolIndex": wwpLeosTrafficProfileMeterPoolIndex,
       "wwpLeosTrafficProfileMeterPoolName": wwpLeosTrafficProfileMeterPoolName,
       "wwpLeosTrafficProfileMeterPoolNumOfMeters": wwpLeosTrafficProfileMeterPoolNumOfMeters,
       "wwpLeosTrafficProfileMeterPoolMetersUsed": wwpLeosTrafficProfileMeterPoolMetersUsed,
       "wwpLeosTrafficProfileMeterPoolNumOfStats": wwpLeosTrafficProfileMeterPoolNumOfStats,
       "wwpLeosTrafficProfileMeterPoolStatsUsed": wwpLeosTrafficProfileMeterPoolStatsUsed,
       "wwpLeosTrafficProfileMeterPoolNumOfClassifiers": wwpLeosTrafficProfileMeterPoolNumOfClassifiers,
       "wwpLeosTrafficProfileMeterPoolClassifiersUsed": wwpLeosTrafficProfileMeterPoolClassifiersUsed,
       "wwpLeosTrafficProfileTosStampTable": wwpLeosTrafficProfileTosStampTable,
       "wwpLeosTrafficProfileTosStampEntry": wwpLeosTrafficProfileTosStampEntry,
       "wwpLeosTrafficProfileTosStampState": wwpLeosTrafficProfileTosStampState,
       "wwpLeosTrafficProfileTosStampValue": wwpLeosTrafficProfileTosStampValue,
       "wwpLeosTrafficProfileIpDscpTable": wwpLeosTrafficProfileIpDscpTable,
       "wwpLeosTrafficProfileIpDscpEntry": wwpLeosTrafficProfileIpDscpEntry,
       "wwpLeosTrafficProfileIpp0Cs0State": wwpLeosTrafficProfileIpp0Cs0State,
       "wwpLeosTrafficProfileIpp1Cs1State": wwpLeosTrafficProfileIpp1Cs1State,
       "wwpLeosTrafficProfileIpp2Cs2State": wwpLeosTrafficProfileIpp2Cs2State,
       "wwpLeosTrafficProfileIpp3Cs3State": wwpLeosTrafficProfileIpp3Cs3State,
       "wwpLeosTrafficProfileIpp4Cs4State": wwpLeosTrafficProfileIpp4Cs4State,
       "wwpLeosTrafficProfileIpp5Cs5State": wwpLeosTrafficProfileIpp5Cs5State,
       "wwpLeosTrafficProfileIpp6Cs6State": wwpLeosTrafficProfileIpp6Cs6State,
       "wwpLeosTrafficProfileIpp7Cs7State": wwpLeosTrafficProfileIpp7Cs7State,
       "wwpLeosTrafficProfileAf1State": wwpLeosTrafficProfileAf1State,
       "wwpLeosTrafficProfileAf2State": wwpLeosTrafficProfileAf2State,
       "wwpLeosTrafficProfileAf3State": wwpLeosTrafficProfileAf3State,
       "wwpLeosTrafficProfileAf4State": wwpLeosTrafficProfileAf4State,
       "wwpLeosTrafficProfileEfState": wwpLeosTrafficProfileEfState,
       "wwpLeosTrafficProfileStdVlanDot1dTable": wwpLeosTrafficProfileStdVlanDot1dTable,
       "wwpLeosTrafficProfileStdVlanDot1dEntry": wwpLeosTrafficProfileStdVlanDot1dEntry,
       "wwpLeosTrafficProfileStdVlanDot1dStatus": wwpLeosTrafficProfileStdVlanDot1dStatus,
       "wwpLeosTrafficProfileStdVlanIpPrecTable": wwpLeosTrafficProfileStdVlanIpPrecTable,
       "wwpLeosTrafficProfileStdVlanIpPrecEntry": wwpLeosTrafficProfileStdVlanIpPrecEntry,
       "wwpLeosTrafficProfileStdVlanIpPrecStatus": wwpLeosTrafficProfileStdVlanIpPrecStatus,
       "wwpLeosTrafficProfileStdVlanDscpTable": wwpLeosTrafficProfileStdVlanDscpTable,
       "wwpLeosTrafficProfileStdVlanDscpEntry": wwpLeosTrafficProfileStdVlanDscpEntry,
       "wwpLeosTrafficProfileStdVlanDscpStatus": wwpLeosTrafficProfileStdVlanDscpStatus,
       "wwpLeosTrafficProfileNotificationPrefix": wwpLeosTrafficProfileNotificationPrefix,
       "wwpLeosTrafficProfileNotifications": wwpLeosTrafficProfileNotifications,
       "wwpLeosTrafficProfileMIBConformance": wwpLeosTrafficProfileMIBConformance,
       "wwpLeosTrafficProfileMIBCompliances": wwpLeosTrafficProfileMIBCompliances,
       "wwpLeosTrafficProfileMIBGroups": wwpLeosTrafficProfileMIBGroups}
)
