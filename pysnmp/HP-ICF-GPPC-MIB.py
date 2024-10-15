# SNMP MIB module (HP-ICF-GPPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-GPPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:29 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfGppcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41)
)
hpicfGppcMIB.setRevisions(
        ("2009-12-15 01:05",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfGppcPolicyName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_HpicfGppcConformance_ObjectIdentity = ObjectIdentity
hpicfGppcConformance = _HpicfGppcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1)
)
_HpicfGppcMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfGppcMIBCompliances = _HpicfGppcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 1)
)
_HpicfGppcMIBGroups_ObjectIdentity = ObjectIdentity
hpicfGppcMIBGroups = _HpicfGppcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 2)
)
_HpicfGppcAppControlTable_Object = MibTable
hpicfGppcAppControlTable = _HpicfGppcAppControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2)
)
if mibBuilder.loadTexts:
    hpicfGppcAppControlTable.setStatus("current")
_HpicfGppcAppControlEntry_Object = MibTableRow
hpicfGppcAppControlEntry = _HpicfGppcAppControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1)
)
hpicfGppcAppControlEntry.setIndexNames(
    (0, "HP-ICF-GPPC-MIB", "hpicfGppcAcAppName"),
    (0, "HP-ICF-GPPC-MIB", "hpicfGppcAcAppInstance"),
    (0, "HP-ICF-GPPC-MIB", "hpicfGppcAcPolicyName"),
)
if mibBuilder.loadTexts:
    hpicfGppcAppControlEntry.setStatus("current")


class _HpicfGppcAcAppName_Type(SnmpAdminString):
    """Custom type hpicfGppcAcAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpicfGppcAcAppName_Type.__name__ = "SnmpAdminString"
_HpicfGppcAcAppName_Object = MibTableColumn
hpicfGppcAcAppName = _HpicfGppcAcAppName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 1),
    _HpicfGppcAcAppName_Type()
)
hpicfGppcAcAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcAcAppName.setStatus("current")


class _HpicfGppcAcAppInstance_Type(SnmpAdminString):
    """Custom type hpicfGppcAcAppInstance based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpicfGppcAcAppInstance_Type.__name__ = "SnmpAdminString"
_HpicfGppcAcAppInstance_Object = MibTableColumn
hpicfGppcAcAppInstance = _HpicfGppcAcAppInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 2),
    _HpicfGppcAcAppInstance_Type()
)
hpicfGppcAcAppInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcAcAppInstance.setStatus("current")
_HpicfGppcAcPolicyName_Type = HpicfGppcPolicyName
_HpicfGppcAcPolicyName_Object = MibTableColumn
hpicfGppcAcPolicyName = _HpicfGppcAcPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 3),
    _HpicfGppcAcPolicyName_Type()
)
hpicfGppcAcPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcAcPolicyName.setStatus("current")
_HpicfGppcAcIngressIfList_Type = PortList
_HpicfGppcAcIngressIfList_Object = MibTableColumn
hpicfGppcAcIngressIfList = _HpicfGppcAcIngressIfList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 4),
    _HpicfGppcAcIngressIfList_Type()
)
hpicfGppcAcIngressIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcIngressIfList.setStatus("current")


class _HpicfGppcAcIngressVlanMap1k_Type(OctetString):
    """Custom type hpicfGppcAcIngressVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcIngressVlanMap1k_Type.__name__ = "OctetString"
_HpicfGppcAcIngressVlanMap1k_Object = MibTableColumn
hpicfGppcAcIngressVlanMap1k = _HpicfGppcAcIngressVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 5),
    _HpicfGppcAcIngressVlanMap1k_Type()
)
hpicfGppcAcIngressVlanMap1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcIngressVlanMap1k.setStatus("current")


class _HpicfGppcAcIngressVlanMap2k_Type(OctetString):
    """Custom type hpicfGppcAcIngressVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcIngressVlanMap2k_Type.__name__ = "OctetString"
_HpicfGppcAcIngressVlanMap2k_Object = MibTableColumn
hpicfGppcAcIngressVlanMap2k = _HpicfGppcAcIngressVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 6),
    _HpicfGppcAcIngressVlanMap2k_Type()
)
hpicfGppcAcIngressVlanMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcIngressVlanMap2k.setStatus("current")


class _HpicfGppcAcIngressVlanMap3k_Type(OctetString):
    """Custom type hpicfGppcAcIngressVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcIngressVlanMap3k_Type.__name__ = "OctetString"
_HpicfGppcAcIngressVlanMap3k_Object = MibTableColumn
hpicfGppcAcIngressVlanMap3k = _HpicfGppcAcIngressVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 7),
    _HpicfGppcAcIngressVlanMap3k_Type()
)
hpicfGppcAcIngressVlanMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcIngressVlanMap3k.setStatus("current")


class _HpicfGppcAcIngressVlanMap4k_Type(OctetString):
    """Custom type hpicfGppcAcIngressVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcIngressVlanMap4k_Type.__name__ = "OctetString"
_HpicfGppcAcIngressVlanMap4k_Object = MibTableColumn
hpicfGppcAcIngressVlanMap4k = _HpicfGppcAcIngressVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 8),
    _HpicfGppcAcIngressVlanMap4k_Type()
)
hpicfGppcAcIngressVlanMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcIngressVlanMap4k.setStatus("current")
_HpicfGppcAcEgressIfList_Type = PortList
_HpicfGppcAcEgressIfList_Object = MibTableColumn
hpicfGppcAcEgressIfList = _HpicfGppcAcEgressIfList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 9),
    _HpicfGppcAcEgressIfList_Type()
)
hpicfGppcAcEgressIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcEgressIfList.setStatus("current")


class _HpicfGppcAcEgressVlanMap1k_Type(OctetString):
    """Custom type hpicfGppcAcEgressVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcEgressVlanMap1k_Type.__name__ = "OctetString"
_HpicfGppcAcEgressVlanMap1k_Object = MibTableColumn
hpicfGppcAcEgressVlanMap1k = _HpicfGppcAcEgressVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 10),
    _HpicfGppcAcEgressVlanMap1k_Type()
)
hpicfGppcAcEgressVlanMap1k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcEgressVlanMap1k.setStatus("current")


class _HpicfGppcAcEgressVlanMap2k_Type(OctetString):
    """Custom type hpicfGppcAcEgressVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcEgressVlanMap2k_Type.__name__ = "OctetString"
_HpicfGppcAcEgressVlanMap2k_Object = MibTableColumn
hpicfGppcAcEgressVlanMap2k = _HpicfGppcAcEgressVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 11),
    _HpicfGppcAcEgressVlanMap2k_Type()
)
hpicfGppcAcEgressVlanMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcEgressVlanMap2k.setStatus("current")


class _HpicfGppcAcEgressVlanMap3k_Type(OctetString):
    """Custom type hpicfGppcAcEgressVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcEgressVlanMap3k_Type.__name__ = "OctetString"
_HpicfGppcAcEgressVlanMap3k_Object = MibTableColumn
hpicfGppcAcEgressVlanMap3k = _HpicfGppcAcEgressVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 12),
    _HpicfGppcAcEgressVlanMap3k_Type()
)
hpicfGppcAcEgressVlanMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcEgressVlanMap3k.setStatus("current")


class _HpicfGppcAcEgressVlanMap4k_Type(OctetString):
    """Custom type hpicfGppcAcEgressVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcAcEgressVlanMap4k_Type.__name__ = "OctetString"
_HpicfGppcAcEgressVlanMap4k_Object = MibTableColumn
hpicfGppcAcEgressVlanMap4k = _HpicfGppcAcEgressVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 13),
    _HpicfGppcAcEgressVlanMap4k_Type()
)
hpicfGppcAcEgressVlanMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcEgressVlanMap4k.setStatus("current")


class _HpicfGppcAcExpPolicy_Type(Integer32):
    """Custom type hpicfGppcAcExpPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("app-down", 3),
          ("permanent", 1),
          ("slot-down", 2))
    )


_HpicfGppcAcExpPolicy_Type.__name__ = "Integer32"
_HpicfGppcAcExpPolicy_Object = MibTableColumn
hpicfGppcAcExpPolicy = _HpicfGppcAcExpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 14),
    _HpicfGppcAcExpPolicy_Type()
)
hpicfGppcAcExpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcExpPolicy.setStatus("current")


class _HpicfGppcAcExpString_Type(OctetString):
    """Custom type hpicfGppcAcExpString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HpicfGppcAcExpString_Type.__name__ = "OctetString"
_HpicfGppcAcExpString_Object = MibTableColumn
hpicfGppcAcExpString = _HpicfGppcAcExpString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 15),
    _HpicfGppcAcExpString_Type()
)
hpicfGppcAcExpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcExpString.setStatus("current")


class _HpicfGppcAcLastErrorCode_Type(Integer32):
    """Custom type hpicfGppcAcLastErrorCode based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85)
        )
    )
    namedValues = NamedValues(
        *(("gppc-already-reserved", 9),
          ("gppc-app-using-policy", 13),
          ("gppc-cfg-add-record-error", 55),
          ("gppc-cfg-entry-not-found", 51),
          ("gppc-cfg-generic-error", 50),
          ("gppc-cfg-get-error", 53),
          ("gppc-cfg-invalid", 56),
          ("gppc-cfg-malloc-error", 57),
          ("gppc-cfg-no-record", 54),
          ("gppc-cfg-set-error", 52),
          ("gppc-entry-exists", 11),
          ("gppc-entry-not-found", 10),
          ("gppc-generic-error", 1),
          ("gppc-invalid-policy-type", 14),
          ("gppc-length-error", 2),
          ("gppc-mac-mirror-convert-error", 37),
          ("gppc-mac-mirror-dir-both-conflict", 31),
          ("gppc-mac-mirror-dir-dst-conflict", 33),
          ("gppc-mac-mirror-dir-src-conflict", 32),
          ("gppc-mac-mirror-invalid-direction", 35),
          ("gppc-mac-mirror-invalid-session", 34),
          ("gppc-mac-mirror-mac-exists", 30),
          ("gppc-mac-mirror-no-entry", 36),
          ("gppc-mac-mirror-table-full", 38),
          ("gppc-malloc-error", 6),
          ("gppc-name-error", 3),
          ("gppc-no-policy", 16),
          ("gppc-not-implemented", 5),
          ("gppc-not-reserved", 15),
          ("gppc-parameter-error", 4),
          ("gppc-platform-error", 12),
          ("gppc-policy-has-rules", 18),
          ("gppc-policy-not-active", 17),
          ("gppc-rule-exists", 19),
          ("gppc-too-many-apps", 7),
          ("gppc-too-many-policies", 8),
          ("gppcTrmodeCannotAllocateClassifierResources", 85),
          ("gppcTrmodeCannotAllocateMirrorSession", 84),
          ("gppcTrmodeCannotDeleteDefaultZone", 78),
          ("gppcTrmodeCannotDeleteZoneWithRules", 79),
          ("gppcTrmodeCannotFilterTrafficWithinZone", 81),
          ("gppcTrmodeErr", 70),
          ("gppcTrmodeInvalidAction", 82),
          ("gppcTrmodeInvalidFilterNumber", 80),
          ("gppcTrmodeInvalidZoneNumber", 71),
          ("gppcTrmodeOperationNotSupported", 72),
          ("gppcTrmodeTooManyZoneNames", 76),
          ("gppcTrmodeUnicastInterceptMacaddrRequired", 83),
          ("gppcTrmodeUnknownPort", 77),
          ("gppcTrmodeZoneNameAlreadyExists", 75),
          ("gppcTrmodeZoneNameNotFound", 74),
          ("gppcTrmodeZoneNameTooLong", 73),
          ("no-error", 0))
    )


_HpicfGppcAcLastErrorCode_Type.__name__ = "Integer32"
_HpicfGppcAcLastErrorCode_Object = MibTableColumn
hpicfGppcAcLastErrorCode = _HpicfGppcAcLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 16),
    _HpicfGppcAcLastErrorCode_Type()
)
hpicfGppcAcLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcAcLastErrorCode.setStatus("current")


class _HpicfGppcAcLastErrorString_Type(OctetString):
    """Custom type hpicfGppcAcLastErrorString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfGppcAcLastErrorString_Type.__name__ = "OctetString"
_HpicfGppcAcLastErrorString_Object = MibTableColumn
hpicfGppcAcLastErrorString = _HpicfGppcAcLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 17),
    _HpicfGppcAcLastErrorString_Type()
)
hpicfGppcAcLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcAcLastErrorString.setStatus("current")


class _HpicfGppcAcRowAdminStatus_Type(Integer32):
    """Custom type hpicfGppcAcRowAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HpicfGppcAcRowAdminStatus_Type.__name__ = "Integer32"
_HpicfGppcAcRowAdminStatus_Object = MibTableColumn
hpicfGppcAcRowAdminStatus = _HpicfGppcAcRowAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 18),
    _HpicfGppcAcRowAdminStatus_Type()
)
hpicfGppcAcRowAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcRowAdminStatus.setStatus("current")
_HpicfGppcAcRowStatus_Type = RowStatus
_HpicfGppcAcRowStatus_Object = MibTableColumn
hpicfGppcAcRowStatus = _HpicfGppcAcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 2, 1, 19),
    _HpicfGppcAcRowStatus_Type()
)
hpicfGppcAcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcAcRowStatus.setStatus("current")
_HpicfGppcNamedPolicyTable_Object = MibTable
hpicfGppcNamedPolicyTable = _HpicfGppcNamedPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3)
)
if mibBuilder.loadTexts:
    hpicfGppcNamedPolicyTable.setStatus("current")
_HpicfGppcNamedPolicyEntry_Object = MibTableRow
hpicfGppcNamedPolicyEntry = _HpicfGppcNamedPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1)
)
hpicfGppcNamedPolicyEntry.setIndexNames(
    (0, "HP-ICF-GPPC-MIB", "hpicfGppcNpPolicyName"),
)
if mibBuilder.loadTexts:
    hpicfGppcNamedPolicyEntry.setStatus("current")
_HpicfGppcNpPolicyName_Type = HpicfGppcPolicyName
_HpicfGppcNpPolicyName_Object = MibTableColumn
hpicfGppcNpPolicyName = _HpicfGppcNpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1, 1),
    _HpicfGppcNpPolicyName_Type()
)
hpicfGppcNpPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcNpPolicyName.setStatus("current")


class _HpicfGppcNpPolicyType_Type(Integer32):
    """Custom type hpicfGppcNpPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-based-mirroring", 1),
          ("zone-intercept", 2))
    )


_HpicfGppcNpPolicyType_Type.__name__ = "Integer32"
_HpicfGppcNpPolicyType_Object = MibTableColumn
hpicfGppcNpPolicyType = _HpicfGppcNpPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1, 2),
    _HpicfGppcNpPolicyType_Type()
)
hpicfGppcNpPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcNpPolicyType.setStatus("current")
_HpicfGppcNpRowStatus_Type = RowStatus
_HpicfGppcNpRowStatus_Object = MibTableColumn
hpicfGppcNpRowStatus = _HpicfGppcNpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 3, 1, 3),
    _HpicfGppcNpRowStatus_Type()
)
hpicfGppcNpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcNpRowStatus.setStatus("current")
_HpicfGppcPolicyRulesTable_Object = MibTable
hpicfGppcPolicyRulesTable = _HpicfGppcPolicyRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4)
)
if mibBuilder.loadTexts:
    hpicfGppcPolicyRulesTable.setStatus("current")
_HpicfGppcPolicyRulesEntry_Object = MibTableRow
hpicfGppcPolicyRulesEntry = _HpicfGppcPolicyRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1)
)
hpicfGppcPolicyRulesEntry.setIndexNames(
    (0, "HP-ICF-GPPC-MIB", "hpicfGppcNpPolicyName"),
    (0, "HP-ICF-GPPC-MIB", "hpicfGppcPrRuleId"),
)
if mibBuilder.loadTexts:
    hpicfGppcPolicyRulesEntry.setStatus("current")
_HpicfGppcPrRuleId_Type = Integer32
_HpicfGppcPrRuleId_Object = MibTableColumn
hpicfGppcPrRuleId = _HpicfGppcPrRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1, 1),
    _HpicfGppcPrRuleId_Type()
)
hpicfGppcPrRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcPrRuleId.setStatus("current")


class _HpicfGppcPrPolicyRule_Type(OctetString):
    """Custom type hpicfGppcPrPolicyRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfGppcPrPolicyRule_Type.__name__ = "OctetString"
_HpicfGppcPrPolicyRule_Object = MibTableColumn
hpicfGppcPrPolicyRule = _HpicfGppcPrPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1, 2),
    _HpicfGppcPrPolicyRule_Type()
)
hpicfGppcPrPolicyRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcPrPolicyRule.setStatus("current")
_HpicfGppcPrRowStatus_Type = RowStatus
_HpicfGppcPrRowStatus_Object = MibTableColumn
hpicfGppcPrRowStatus = _HpicfGppcPrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 4, 1, 3),
    _HpicfGppcPrRowStatus_Type()
)
hpicfGppcPrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcPrRowStatus.setStatus("current")

# Managed Objects groups

hpicfGppcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 2, 1)
)
hpicfGppcGroup.setObjects(
      *(("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressIfList"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap1k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap2k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap3k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcIngressVlanMap4k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressIfList"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap1k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap2k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap3k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcEgressVlanMap4k"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcExpPolicy"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcExpString"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcLastErrorCode"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcLastErrorString"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcRowAdminStatus"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcAcRowStatus"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcNpPolicyType"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcNpRowStatus"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcPrPolicyRule"),
        ("HP-ICF-GPPC-MIB", "hpicfGppcPrRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfGppcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfGppcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfGppcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-GPPC-MIB",
    **{"HpicfGppcPolicyName": HpicfGppcPolicyName,
       "hpicfGppcMIB": hpicfGppcMIB,
       "hpicfGppcConformance": hpicfGppcConformance,
       "hpicfGppcMIBCompliances": hpicfGppcMIBCompliances,
       "hpicfGppcMIBCompliance": hpicfGppcMIBCompliance,
       "hpicfGppcMIBGroups": hpicfGppcMIBGroups,
       "hpicfGppcGroup": hpicfGppcGroup,
       "hpicfGppcAppControlTable": hpicfGppcAppControlTable,
       "hpicfGppcAppControlEntry": hpicfGppcAppControlEntry,
       "hpicfGppcAcAppName": hpicfGppcAcAppName,
       "hpicfGppcAcAppInstance": hpicfGppcAcAppInstance,
       "hpicfGppcAcPolicyName": hpicfGppcAcPolicyName,
       "hpicfGppcAcIngressIfList": hpicfGppcAcIngressIfList,
       "hpicfGppcAcIngressVlanMap1k": hpicfGppcAcIngressVlanMap1k,
       "hpicfGppcAcIngressVlanMap2k": hpicfGppcAcIngressVlanMap2k,
       "hpicfGppcAcIngressVlanMap3k": hpicfGppcAcIngressVlanMap3k,
       "hpicfGppcAcIngressVlanMap4k": hpicfGppcAcIngressVlanMap4k,
       "hpicfGppcAcEgressIfList": hpicfGppcAcEgressIfList,
       "hpicfGppcAcEgressVlanMap1k": hpicfGppcAcEgressVlanMap1k,
       "hpicfGppcAcEgressVlanMap2k": hpicfGppcAcEgressVlanMap2k,
       "hpicfGppcAcEgressVlanMap3k": hpicfGppcAcEgressVlanMap3k,
       "hpicfGppcAcEgressVlanMap4k": hpicfGppcAcEgressVlanMap4k,
       "hpicfGppcAcExpPolicy": hpicfGppcAcExpPolicy,
       "hpicfGppcAcExpString": hpicfGppcAcExpString,
       "hpicfGppcAcLastErrorCode": hpicfGppcAcLastErrorCode,
       "hpicfGppcAcLastErrorString": hpicfGppcAcLastErrorString,
       "hpicfGppcAcRowAdminStatus": hpicfGppcAcRowAdminStatus,
       "hpicfGppcAcRowStatus": hpicfGppcAcRowStatus,
       "hpicfGppcNamedPolicyTable": hpicfGppcNamedPolicyTable,
       "hpicfGppcNamedPolicyEntry": hpicfGppcNamedPolicyEntry,
       "hpicfGppcNpPolicyName": hpicfGppcNpPolicyName,
       "hpicfGppcNpPolicyType": hpicfGppcNpPolicyType,
       "hpicfGppcNpRowStatus": hpicfGppcNpRowStatus,
       "hpicfGppcPolicyRulesTable": hpicfGppcPolicyRulesTable,
       "hpicfGppcPolicyRulesEntry": hpicfGppcPolicyRulesEntry,
       "hpicfGppcPrRuleId": hpicfGppcPrRuleId,
       "hpicfGppcPrPolicyRule": hpicfGppcPrPolicyRule,
       "hpicfGppcPrRowStatus": hpicfGppcPrRowStatus}
)
