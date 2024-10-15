# SNMP MIB module (ALCATEL-IND1-E-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-E-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:57 2024
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

(softentIND1eService,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1eService")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

alcatelIND1EServiceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaEServiceUNIProfileProtocolTreatment(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("peer", 3),
          ("tunnel", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1eServiceMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1eServiceMIBObjects = _AlcatelIND1eServiceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1eServiceMIBObjects.setStatus("current")
_AlaEService_ObjectIdentity = ObjectIdentity
alaEService = _AlaEService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1)
)
_AlaEServiceInfo_ObjectIdentity = ObjectIdentity
alaEServiceInfo = _AlaEServiceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 1)
)


class _AlaEServiceMode_Type(Integer32):
    """Custom type alaEServiceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eServiceMode", 2),
          ("legacyMode", 1))
    )


_AlaEServiceMode_Type.__name__ = "Integer32"
_AlaEServiceMode_Object = MibScalar
alaEServiceMode = _AlaEServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 1, 1),
    _AlaEServiceMode_Type()
)
alaEServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEServiceMode.setStatus("current")
_AlaEServiceSapProfileTable_Object = MibTable
alaEServiceSapProfileTable = _AlaEServiceSapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileTable.setStatus("current")
_AlaEServiceSapProfileEntry_Object = MibTableRow
alaEServiceSapProfileEntry = _AlaEServiceSapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1)
)
alaEServiceSapProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileEntry.setStatus("current")


class _AlaEServiceSapProfileID_Type(SnmpAdminString):
    """Custom type alaEServiceSapProfileID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceSapProfileID_Type.__name__ = "SnmpAdminString"
_AlaEServiceSapProfileID_Object = MibTableColumn
alaEServiceSapProfileID = _AlaEServiceSapProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 1),
    _AlaEServiceSapProfileID_Type()
)
alaEServiceSapProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapProfileID.setStatus("current")


class _AlaEServiceSapProfileCVLANTreatment_Type(Integer32):
    """Custom type alaEServiceSapProfileCVLANTreatment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("changeCVLAN", 3),
          ("stackSVLAN", 1),
          ("translate", 2))
    )


_AlaEServiceSapProfileCVLANTreatment_Type.__name__ = "Integer32"
_AlaEServiceSapProfileCVLANTreatment_Object = MibTableColumn
alaEServiceSapProfileCVLANTreatment = _AlaEServiceSapProfileCVLANTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 2),
    _AlaEServiceSapProfileCVLANTreatment_Type()
)
alaEServiceSapProfileCVLANTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileCVLANTreatment.setStatus("current")


class _AlaEServiceSapProfileReplacementCVLAN_Type(Integer32):
    """Custom type alaEServiceSapProfileReplacementCVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaEServiceSapProfileReplacementCVLAN_Type.__name__ = "Integer32"
_AlaEServiceSapProfileReplacementCVLAN_Object = MibTableColumn
alaEServiceSapProfileReplacementCVLAN = _AlaEServiceSapProfileReplacementCVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 3),
    _AlaEServiceSapProfileReplacementCVLAN_Type()
)
alaEServiceSapProfileReplacementCVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileReplacementCVLAN.setStatus("current")


class _AlaEServiceSapProfilePriorityMapMode_Type(Integer32):
    """Custom type alaEServiceSapProfilePriorityMapMode based on Integer32"""
    defaultValue = 3

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
        *(("fixedP", 3),
          ("mapInnerDscpToOuterP", 2),
          ("mapInnerPtoOuterP", 1),
          ("notAssigned", 0))
    )


_AlaEServiceSapProfilePriorityMapMode_Type.__name__ = "Integer32"
_AlaEServiceSapProfilePriorityMapMode_Object = MibTableColumn
alaEServiceSapProfilePriorityMapMode = _AlaEServiceSapProfilePriorityMapMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 4),
    _AlaEServiceSapProfilePriorityMapMode_Type()
)
alaEServiceSapProfilePriorityMapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfilePriorityMapMode.setStatus("current")


class _AlaEServiceSapProfileFixedPriority_Type(Integer32):
    """Custom type alaEServiceSapProfileFixedPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaEServiceSapProfileFixedPriority_Type.__name__ = "Integer32"
_AlaEServiceSapProfileFixedPriority_Object = MibTableColumn
alaEServiceSapProfileFixedPriority = _AlaEServiceSapProfileFixedPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 5),
    _AlaEServiceSapProfileFixedPriority_Type()
)
alaEServiceSapProfileFixedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileFixedPriority.setStatus("current")
_AlaEServiceSapProfileIngressBW_Type = Integer32
_AlaEServiceSapProfileIngressBW_Object = MibTableColumn
alaEServiceSapProfileIngressBW = _AlaEServiceSapProfileIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 6),
    _AlaEServiceSapProfileIngressBW_Type()
)
alaEServiceSapProfileIngressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileIngressBW.setStatus("current")


class _AlaEServiceSapProfileBandwidthShare_Type(Integer32):
    """Custom type alaEServiceSapProfileBandwidthShare based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notShared", 2),
          ("shared", 1))
    )


_AlaEServiceSapProfileBandwidthShare_Type.__name__ = "Integer32"
_AlaEServiceSapProfileBandwidthShare_Object = MibTableColumn
alaEServiceSapProfileBandwidthShare = _AlaEServiceSapProfileBandwidthShare_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 7),
    _AlaEServiceSapProfileBandwidthShare_Type()
)
alaEServiceSapProfileBandwidthShare.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileBandwidthShare.setStatus("current")
_AlaEServiceSapProfileRowStatus_Type = RowStatus
_AlaEServiceSapProfileRowStatus_Object = MibTableColumn
alaEServiceSapProfileRowStatus = _AlaEServiceSapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 8),
    _AlaEServiceSapProfileRowStatus_Type()
)
alaEServiceSapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileRowStatus.setStatus("current")


class _AlaEServiceSapProfileEgressBW_Type(Integer32):
    """Custom type alaEServiceSapProfileEgressBW based on Integer32"""
    defaultValue = 0


_AlaEServiceSapProfileEgressBW_Object = MibTableColumn
alaEServiceSapProfileEgressBW = _AlaEServiceSapProfileEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 2, 1, 9),
    _AlaEServiceSapProfileEgressBW_Type()
)
alaEServiceSapProfileEgressBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfileEgressBW.setStatus("current")
_AlaEServiceUNIProfileTable_Object = MibTable
alaEServiceUNIProfileTable = _AlaEServiceUNIProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileTable.setStatus("current")
_AlaEServiceUNIProfileEntry_Object = MibTableRow
alaEServiceUNIProfileEntry = _AlaEServiceUNIProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1)
)
alaEServiceUNIProfileEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileID"),
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileEntry.setStatus("current")


class _AlaEServiceUNIProfileID_Type(SnmpAdminString):
    """Custom type alaEServiceUNIProfileID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServiceUNIProfileID_Type.__name__ = "SnmpAdminString"
_AlaEServiceUNIProfileID_Object = MibTableColumn
alaEServiceUNIProfileID = _AlaEServiceUNIProfileID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 1),
    _AlaEServiceUNIProfileID_Type()
)
alaEServiceUNIProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileID.setStatus("current")


class _AlaEServiceUNIProfileStpBpduTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileStpBpduTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfileStpBpduTreatment_Object = MibTableColumn
alaEServiceUNIProfileStpBpduTreatment = _AlaEServiceUNIProfileStpBpduTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 2),
    _AlaEServiceUNIProfileStpBpduTreatment_Type()
)
alaEServiceUNIProfileStpBpduTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileStpBpduTreatment.setStatus("current")


class _AlaEServiceUNIProfile8021xTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8021xTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfile8021xTreatment_Object = MibTableColumn
alaEServiceUNIProfile8021xTreatment = _AlaEServiceUNIProfile8021xTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 3),
    _AlaEServiceUNIProfile8021xTreatment_Type()
)
alaEServiceUNIProfile8021xTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8021xTreatment.setStatus("current")


class _AlaEServiceUNIProfile8021ABTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8021ABTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfile8021ABTreatment_Object = MibTableColumn
alaEServiceUNIProfile8021ABTreatment = _AlaEServiceUNIProfile8021ABTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 4),
    _AlaEServiceUNIProfile8021ABTreatment_Type()
)
alaEServiceUNIProfile8021ABTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8021ABTreatment.setStatus("current")


class _AlaEServiceUNIProfile8023adTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfile8023adTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfile8023adTreatment_Object = MibTableColumn
alaEServiceUNIProfile8023adTreatment = _AlaEServiceUNIProfile8023adTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 5),
    _AlaEServiceUNIProfile8023adTreatment_Type()
)
alaEServiceUNIProfile8023adTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfile8023adTreatment.setStatus("current")


class _AlaEServiceUNIProfileGvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileGvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfileGvrpTreatment_Object = MibTableColumn
alaEServiceUNIProfileGvrpTreatment = _AlaEServiceUNIProfileGvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 6),
    _AlaEServiceUNIProfileGvrpTreatment_Type()
)
alaEServiceUNIProfileGvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileGvrpTreatment.setStatus("deprecated")


class _AlaEServiceUNIProfileAmapTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileAmapTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfileAmapTreatment_Object = MibTableColumn
alaEServiceUNIProfileAmapTreatment = _AlaEServiceUNIProfileAmapTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 7),
    _AlaEServiceUNIProfileAmapTreatment_Type()
)
alaEServiceUNIProfileAmapTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileAmapTreatment.setStatus("current")


class _AlaEServiceUNIProfileMvrpTreatment_Type(AlaEServiceUNIProfileProtocolTreatment):
    """Custom type alaEServiceUNIProfileMvrpTreatment based on AlaEServiceUNIProfileProtocolTreatment"""


_AlaEServiceUNIProfileMvrpTreatment_Object = MibTableColumn
alaEServiceUNIProfileMvrpTreatment = _AlaEServiceUNIProfileMvrpTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 8),
    _AlaEServiceUNIProfileMvrpTreatment_Type()
)
alaEServiceUNIProfileMvrpTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileMvrpTreatment.setStatus("current")
_AlaEServiceUNIProfileRowStatus_Type = RowStatus
_AlaEServiceUNIProfileRowStatus_Object = MibTableColumn
alaEServiceUNIProfileRowStatus = _AlaEServiceUNIProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 3, 1, 9),
    _AlaEServiceUNIProfileRowStatus_Type()
)
alaEServiceUNIProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceUNIProfileRowStatus.setStatus("current")
_AlaEServiceTable_Object = MibTable
alaEServiceTable = _AlaEServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaEServiceTable.setStatus("current")
_AlaEServiceEntry_Object = MibTableRow
alaEServiceEntry = _AlaEServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 4, 1)
)
alaEServiceEntry.setIndexNames(
    (1, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceID"),
)
if mibBuilder.loadTexts:
    alaEServiceEntry.setStatus("current")


class _AlaEServiceID_Type(SnmpAdminString):
    """Custom type alaEServiceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceID_Type.__name__ = "SnmpAdminString"
_AlaEServiceID_Object = MibTableColumn
alaEServiceID = _AlaEServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 4, 1, 1),
    _AlaEServiceID_Type()
)
alaEServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceID.setStatus("current")


class _AlaEServiceSVLAN_Type(Integer32):
    """Custom type alaEServiceSVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaEServiceSVLAN_Type.__name__ = "Integer32"
_AlaEServiceSVLAN_Object = MibTableColumn
alaEServiceSVLAN = _AlaEServiceSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 4, 1, 2),
    _AlaEServiceSVLAN_Type()
)
alaEServiceSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSVLAN.setStatus("current")


class _AlaEServiceVlanType_Type(Integer32):
    """Custom type alaEServiceVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipmvlan", 2),
          ("svlan", 1),
          ("unknown", 0))
    )


_AlaEServiceVlanType_Type.__name__ = "Integer32"
_AlaEServiceVlanType_Object = MibTableColumn
alaEServiceVlanType = _AlaEServiceVlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 4, 1, 3),
    _AlaEServiceVlanType_Type()
)
alaEServiceVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceVlanType.setStatus("current")
_AlaEServiceRowStatus_Type = RowStatus
_AlaEServiceRowStatus_Object = MibTableColumn
alaEServiceRowStatus = _AlaEServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 4, 1, 4),
    _AlaEServiceRowStatus_Type()
)
alaEServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceRowStatus.setStatus("current")
_AlaEServiceSapTable_Object = MibTable
alaEServiceSapTable = _AlaEServiceSapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaEServiceSapTable.setStatus("current")
_AlaEServiceSapEntry_Object = MibTableRow
alaEServiceSapEntry = _AlaEServiceSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 5, 1)
)
alaEServiceSapEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapID"),
)
if mibBuilder.loadTexts:
    alaEServiceSapEntry.setStatus("current")


class _AlaEServiceSapID_Type(Integer32):
    """Custom type alaEServiceSapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapID_Type.__name__ = "Integer32"
_AlaEServiceSapID_Object = MibTableColumn
alaEServiceSapID = _AlaEServiceSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 5, 1, 1),
    _AlaEServiceSapID_Type()
)
alaEServiceSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapID.setStatus("current")


class _AlaEServiceSapServiceID_Type(SnmpAdminString):
    """Custom type alaEServiceSapServiceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceSapServiceID_Type.__name__ = "SnmpAdminString"
_AlaEServiceSapServiceID_Object = MibTableColumn
alaEServiceSapServiceID = _AlaEServiceSapServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 5, 1, 2),
    _AlaEServiceSapServiceID_Type()
)
alaEServiceSapServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapServiceID.setStatus("current")


class _AlaEServiceSapProfile_Type(SnmpAdminString):
    """Custom type alaEServiceSapProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaEServiceSapProfile_Type.__name__ = "SnmpAdminString"
_AlaEServiceSapProfile_Object = MibTableColumn
alaEServiceSapProfile = _AlaEServiceSapProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 5, 1, 3),
    _AlaEServiceSapProfile_Type()
)
alaEServiceSapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapProfile.setStatus("current")
_AlaEServiceSapRowStatus_Type = RowStatus
_AlaEServiceSapRowStatus_Object = MibTableColumn
alaEServiceSapRowStatus = _AlaEServiceSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 5, 1, 4),
    _AlaEServiceSapRowStatus_Type()
)
alaEServiceSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapRowStatus.setStatus("current")
_AlaEServiceSapCvlanTable_Object = MibTable
alaEServiceSapCvlanTable = _AlaEServiceSapCvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanTable.setStatus("current")
_AlaEServiceSapCvlanEntry_Object = MibTableRow
alaEServiceSapCvlanEntry = _AlaEServiceSapCvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 6, 1)
)
alaEServiceSapCvlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanSapID"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanCvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanEntry.setStatus("current")


class _AlaEServiceSapCvlanSapID_Type(Integer32):
    """Custom type alaEServiceSapCvlanSapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapCvlanSapID_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanSapID_Object = MibTableColumn
alaEServiceSapCvlanSapID = _AlaEServiceSapCvlanSapID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 6, 1, 1),
    _AlaEServiceSapCvlanSapID_Type()
)
alaEServiceSapCvlanSapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanSapID.setStatus("current")


class _AlaEServiceSapCvlanCvlan_Type(Integer32):
    """Custom type alaEServiceSapCvlanCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaEServiceSapCvlanCvlan_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanCvlan_Object = MibTableColumn
alaEServiceSapCvlanCvlan = _AlaEServiceSapCvlanCvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 6, 1, 2),
    _AlaEServiceSapCvlanCvlan_Type()
)
alaEServiceSapCvlanCvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanCvlan.setStatus("current")


class _AlaEServiceSapCvlanMapType_Type(Integer32):
    """Custom type alaEServiceSapCvlanMapType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("single", 1),
          ("untaggedOnly", 3))
    )


_AlaEServiceSapCvlanMapType_Type.__name__ = "Integer32"
_AlaEServiceSapCvlanMapType_Object = MibTableColumn
alaEServiceSapCvlanMapType = _AlaEServiceSapCvlanMapType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 6, 1, 3),
    _AlaEServiceSapCvlanMapType_Type()
)
alaEServiceSapCvlanMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanMapType.setStatus("current")
_AlaEServiceSapCvlanRowStatus_Type = RowStatus
_AlaEServiceSapCvlanRowStatus_Object = MibTableColumn
alaEServiceSapCvlanRowStatus = _AlaEServiceSapCvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 6, 1, 4),
    _AlaEServiceSapCvlanRowStatus_Type()
)
alaEServiceSapCvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapCvlanRowStatus.setStatus("current")
_AlaEServicePortTable_Object = MibTable
alaEServicePortTable = _AlaEServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaEServicePortTable.setStatus("current")
_AlaEServicePortEntry_Object = MibTableRow
alaEServicePortEntry = _AlaEServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1)
)
alaEServicePortEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortID"),
)
if mibBuilder.loadTexts:
    alaEServicePortEntry.setStatus("current")
_AlaEServicePortID_Type = InterfaceIndex
_AlaEServicePortID_Object = MibTableColumn
alaEServicePortID = _AlaEServicePortID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 1),
    _AlaEServicePortID_Type()
)
alaEServicePortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServicePortID.setStatus("current")


class _AlaEServicePortType_Type(Integer32):
    """Custom type alaEServicePortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nni", 3),
          ("uni", 1))
    )


_AlaEServicePortType_Type.__name__ = "Integer32"
_AlaEServicePortType_Object = MibTableColumn
alaEServicePortType = _AlaEServicePortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 2),
    _AlaEServicePortType_Type()
)
alaEServicePortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortType.setStatus("current")


class _AlaEServicePortVendorTpid_Type(Integer32):
    """Custom type alaEServicePortVendorTpid based on Integer32"""
    defaultValue = 33024


_AlaEServicePortVendorTpid_Object = MibTableColumn
alaEServicePortVendorTpid = _AlaEServicePortVendorTpid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 3),
    _AlaEServicePortVendorTpid_Type()
)
alaEServicePortVendorTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortVendorTpid.setStatus("current")


class _AlaEServicePortLegacyStpBpdu_Type(Integer32):
    """Custom type alaEServicePortLegacyStpBpdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 0))
    )


_AlaEServicePortLegacyStpBpdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyStpBpdu_Object = MibTableColumn
alaEServicePortLegacyStpBpdu = _AlaEServicePortLegacyStpBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 4),
    _AlaEServicePortLegacyStpBpdu_Type()
)
alaEServicePortLegacyStpBpdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortLegacyStpBpdu.setStatus("current")


class _AlaEServicePortLegacyGvrpPdu_Type(Integer32):
    """Custom type alaEServicePortLegacyGvrpPdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 0))
    )


_AlaEServicePortLegacyGvrpPdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyGvrpPdu_Object = MibTableColumn
alaEServicePortLegacyGvrpPdu = _AlaEServicePortLegacyGvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 5),
    _AlaEServicePortLegacyGvrpPdu_Type()
)
alaEServicePortLegacyGvrpPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortLegacyGvrpPdu.setStatus("deprecated")


class _AlaEServicePortUniProfile_Type(SnmpAdminString):
    """Custom type alaEServicePortUniProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaEServicePortUniProfile_Type.__name__ = "SnmpAdminString"
_AlaEServicePortUniProfile_Object = MibTableColumn
alaEServicePortUniProfile = _AlaEServicePortUniProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 6),
    _AlaEServicePortUniProfile_Type()
)
alaEServicePortUniProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortUniProfile.setStatus("current")


class _AlaEServicePortTransBridging_Type(Integer32):
    """Custom type alaEServicePortTransBridging based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaEServicePortTransBridging_Type.__name__ = "Integer32"
_AlaEServicePortTransBridging_Object = MibTableColumn
alaEServicePortTransBridging = _AlaEServicePortTransBridging_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 7),
    _AlaEServicePortTransBridging_Type()
)
alaEServicePortTransBridging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortTransBridging.setStatus("current")


class _AlaEServicePortLegacyMvrpPdu_Type(Integer32):
    """Custom type alaEServicePortLegacyMvrpPdu based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 0))
    )


_AlaEServicePortLegacyMvrpPdu_Type.__name__ = "Integer32"
_AlaEServicePortLegacyMvrpPdu_Object = MibTableColumn
alaEServicePortLegacyMvrpPdu = _AlaEServicePortLegacyMvrpPdu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 8),
    _AlaEServicePortLegacyMvrpPdu_Type()
)
alaEServicePortLegacyMvrpPdu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortLegacyMvrpPdu.setStatus("current")
_AlaEServicePortRowStatus_Type = RowStatus
_AlaEServicePortRowStatus_Object = MibTableColumn
alaEServicePortRowStatus = _AlaEServicePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 7, 1, 9),
    _AlaEServicePortRowStatus_Type()
)
alaEServicePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServicePortRowStatus.setStatus("current")
_AlaEServiceSapUniTable_Object = MibTable
alaEServiceSapUniTable = _AlaEServiceSapUniTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaEServiceSapUniTable.setStatus("current")
_AlaEServiceSapUniEntry_Object = MibTableRow
alaEServiceSapUniEntry = _AlaEServiceSapUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 8, 1)
)
alaEServiceSapUniEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniSap"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniUni"),
)
if mibBuilder.loadTexts:
    alaEServiceSapUniEntry.setStatus("current")


class _AlaEServiceSapUniSap_Type(Integer32):
    """Custom type alaEServiceSapUniSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaEServiceSapUniSap_Type.__name__ = "Integer32"
_AlaEServiceSapUniSap_Object = MibTableColumn
alaEServiceSapUniSap = _AlaEServiceSapUniSap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 8, 1, 1),
    _AlaEServiceSapUniSap_Type()
)
alaEServiceSapUniSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniSap.setStatus("current")
_AlaEServiceSapUniUni_Type = InterfaceIndex
_AlaEServiceSapUniUni_Object = MibTableColumn
alaEServiceSapUniUni = _AlaEServiceSapUniUni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 8, 1, 2),
    _AlaEServiceSapUniUni_Type()
)
alaEServiceSapUniUni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceSapUniUni.setStatus("current")
_AlaEServiceSapUniRowStatus_Type = RowStatus
_AlaEServiceSapUniRowStatus_Object = MibTableColumn
alaEServiceSapUniRowStatus = _AlaEServiceSapUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 8, 1, 3),
    _AlaEServiceSapUniRowStatus_Type()
)
alaEServiceSapUniRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceSapUniRowStatus.setStatus("current")
_AlaEServiceNniSvlanTable_Object = MibTable
alaEServiceNniSvlanTable = _AlaEServiceNniSvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanTable.setStatus("current")
_AlaEServiceNniSvlanEntry_Object = MibTableRow
alaEServiceNniSvlanEntry = _AlaEServiceNniSvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 9, 1)
)
alaEServiceNniSvlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanNni"),
    (0, "ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanSvlan"),
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanEntry.setStatus("current")
_AlaEServiceNniSvlanNni_Type = InterfaceIndex
_AlaEServiceNniSvlanNni_Object = MibTableColumn
alaEServiceNniSvlanNni = _AlaEServiceNniSvlanNni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 9, 1, 1),
    _AlaEServiceNniSvlanNni_Type()
)
alaEServiceNniSvlanNni.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanNni.setStatus("current")


class _AlaEServiceNniSvlanSvlan_Type(Integer32):
    """Custom type alaEServiceNniSvlanSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AlaEServiceNniSvlanSvlan_Type.__name__ = "Integer32"
_AlaEServiceNniSvlanSvlan_Object = MibTableColumn
alaEServiceNniSvlanSvlan = _AlaEServiceNniSvlanSvlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 9, 1, 2),
    _AlaEServiceNniSvlanSvlan_Type()
)
alaEServiceNniSvlanSvlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanSvlan.setStatus("current")
_AlaEServiceNniSvlanRowStatus_Type = RowStatus
_AlaEServiceNniSvlanRowStatus_Object = MibTableColumn
alaEServiceNniSvlanRowStatus = _AlaEServiceNniSvlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 9, 1, 3),
    _AlaEServiceNniSvlanRowStatus_Type()
)
alaEServiceNniSvlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanRowStatus.setStatus("current")


class _AlaEServiceNniSvlanVpaType_Type(Integer32):
    """Custom type alaEServiceNniSvlanVpaType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erp", 2),
          ("stp", 1))
    )


_AlaEServiceNniSvlanVpaType_Type.__name__ = "Integer32"
_AlaEServiceNniSvlanVpaType_Object = MibTableColumn
alaEServiceNniSvlanVpaType = _AlaEServiceNniSvlanVpaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 1, 1, 9, 1, 4),
    _AlaEServiceNniSvlanVpaType_Type()
)
alaEServiceNniSvlanVpaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEServiceNniSvlanVpaType.setStatus("current")
_AlcatelIND1EServiceMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBConformance = _AlcatelIND1EServiceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBConformance.setStatus("current")
_AlcatelIND1EServiceMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBGroups = _AlcatelIND1EServiceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBGroups.setStatus("current")
_AlcatelIND1EServiceMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1EServiceMIBCompliances = _AlcatelIND1EServiceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBCompliances.setStatus("current")

# Managed Objects groups

alaEServiceSapProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 1)
)
alaEServiceSapProfileGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileCVLANTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileReplacementCVLAN"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfilePriorityMapMode"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileFixedPriority"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileIngressBW"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileBandwidthShare"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfileEgressBW"))
)
if mibBuilder.loadTexts:
    alaEServiceSapProfileGroup.setStatus("current")

alaEServiceUNIProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 2)
)
alaEServiceUNIProfileGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileStpBpduTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8021xTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8021ABTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfile8023adTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileGvrpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileAmapTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileMvrpTreatment"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceUNIProfileRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceUNIProfileGroup.setStatus("current")

alaEServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 3)
)
alaEServiceGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSVLAN"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceVlanType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceGroup.setStatus("current")

alaEServiceSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 4)
)
alaEServiceSapGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapServiceID"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapProfile"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceSapGroup.setStatus("current")

alaEServiceSapCvlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 5)
)
alaEServiceSapCvlanGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanMapType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapCvlanRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServiceSapCvlanGroup.setStatus("current")

alaEServicePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 6)
)
alaEServicePortGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortType"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortVendorTpid"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyStpBpdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyGvrpPdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortUniProfile"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortTransBridging"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortLegacyMvrpPdu"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServicePortRowStatus"))
)
if mibBuilder.loadTexts:
    alaEServicePortGroup.setStatus("current")

alaEServiceSapUniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 7)
)
alaEServiceSapUniGroup.setObjects(
    ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceSapUniRowStatus")
)
if mibBuilder.loadTexts:
    alaEServiceSapUniGroup.setStatus("current")

alaEServiceNniSvlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 8)
)
alaEServiceNniSvlanGroup.setObjects(
      *(("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanRowStatus"),
        ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceNniSvlanVpaType"))
)
if mibBuilder.loadTexts:
    alaEServiceNniSvlanGroup.setStatus("current")

alaEServiceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 1, 9)
)
alaEServiceInfoGroup.setObjects(
    ("ALCATEL-IND1-E-SERVICE-MIB", "alaEServiceMode")
)
if mibBuilder.loadTexts:
    alaEServiceInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1EServiceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 50, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EServiceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-E-SERVICE-MIB",
    **{"AlaEServiceUNIProfileProtocolTreatment": AlaEServiceUNIProfileProtocolTreatment,
       "alcatelIND1EServiceMIB": alcatelIND1EServiceMIB,
       "alcatelIND1eServiceMIBObjects": alcatelIND1eServiceMIBObjects,
       "alaEService": alaEService,
       "alaEServiceInfo": alaEServiceInfo,
       "alaEServiceMode": alaEServiceMode,
       "alaEServiceSapProfileTable": alaEServiceSapProfileTable,
       "alaEServiceSapProfileEntry": alaEServiceSapProfileEntry,
       "alaEServiceSapProfileID": alaEServiceSapProfileID,
       "alaEServiceSapProfileCVLANTreatment": alaEServiceSapProfileCVLANTreatment,
       "alaEServiceSapProfileReplacementCVLAN": alaEServiceSapProfileReplacementCVLAN,
       "alaEServiceSapProfilePriorityMapMode": alaEServiceSapProfilePriorityMapMode,
       "alaEServiceSapProfileFixedPriority": alaEServiceSapProfileFixedPriority,
       "alaEServiceSapProfileIngressBW": alaEServiceSapProfileIngressBW,
       "alaEServiceSapProfileBandwidthShare": alaEServiceSapProfileBandwidthShare,
       "alaEServiceSapProfileRowStatus": alaEServiceSapProfileRowStatus,
       "alaEServiceSapProfileEgressBW": alaEServiceSapProfileEgressBW,
       "alaEServiceUNIProfileTable": alaEServiceUNIProfileTable,
       "alaEServiceUNIProfileEntry": alaEServiceUNIProfileEntry,
       "alaEServiceUNIProfileID": alaEServiceUNIProfileID,
       "alaEServiceUNIProfileStpBpduTreatment": alaEServiceUNIProfileStpBpduTreatment,
       "alaEServiceUNIProfile8021xTreatment": alaEServiceUNIProfile8021xTreatment,
       "alaEServiceUNIProfile8021ABTreatment": alaEServiceUNIProfile8021ABTreatment,
       "alaEServiceUNIProfile8023adTreatment": alaEServiceUNIProfile8023adTreatment,
       "alaEServiceUNIProfileGvrpTreatment": alaEServiceUNIProfileGvrpTreatment,
       "alaEServiceUNIProfileAmapTreatment": alaEServiceUNIProfileAmapTreatment,
       "alaEServiceUNIProfileMvrpTreatment": alaEServiceUNIProfileMvrpTreatment,
       "alaEServiceUNIProfileRowStatus": alaEServiceUNIProfileRowStatus,
       "alaEServiceTable": alaEServiceTable,
       "alaEServiceEntry": alaEServiceEntry,
       "alaEServiceID": alaEServiceID,
       "alaEServiceSVLAN": alaEServiceSVLAN,
       "alaEServiceVlanType": alaEServiceVlanType,
       "alaEServiceRowStatus": alaEServiceRowStatus,
       "alaEServiceSapTable": alaEServiceSapTable,
       "alaEServiceSapEntry": alaEServiceSapEntry,
       "alaEServiceSapID": alaEServiceSapID,
       "alaEServiceSapServiceID": alaEServiceSapServiceID,
       "alaEServiceSapProfile": alaEServiceSapProfile,
       "alaEServiceSapRowStatus": alaEServiceSapRowStatus,
       "alaEServiceSapCvlanTable": alaEServiceSapCvlanTable,
       "alaEServiceSapCvlanEntry": alaEServiceSapCvlanEntry,
       "alaEServiceSapCvlanSapID": alaEServiceSapCvlanSapID,
       "alaEServiceSapCvlanCvlan": alaEServiceSapCvlanCvlan,
       "alaEServiceSapCvlanMapType": alaEServiceSapCvlanMapType,
       "alaEServiceSapCvlanRowStatus": alaEServiceSapCvlanRowStatus,
       "alaEServicePortTable": alaEServicePortTable,
       "alaEServicePortEntry": alaEServicePortEntry,
       "alaEServicePortID": alaEServicePortID,
       "alaEServicePortType": alaEServicePortType,
       "alaEServicePortVendorTpid": alaEServicePortVendorTpid,
       "alaEServicePortLegacyStpBpdu": alaEServicePortLegacyStpBpdu,
       "alaEServicePortLegacyGvrpPdu": alaEServicePortLegacyGvrpPdu,
       "alaEServicePortUniProfile": alaEServicePortUniProfile,
       "alaEServicePortTransBridging": alaEServicePortTransBridging,
       "alaEServicePortLegacyMvrpPdu": alaEServicePortLegacyMvrpPdu,
       "alaEServicePortRowStatus": alaEServicePortRowStatus,
       "alaEServiceSapUniTable": alaEServiceSapUniTable,
       "alaEServiceSapUniEntry": alaEServiceSapUniEntry,
       "alaEServiceSapUniSap": alaEServiceSapUniSap,
       "alaEServiceSapUniUni": alaEServiceSapUniUni,
       "alaEServiceSapUniRowStatus": alaEServiceSapUniRowStatus,
       "alaEServiceNniSvlanTable": alaEServiceNniSvlanTable,
       "alaEServiceNniSvlanEntry": alaEServiceNniSvlanEntry,
       "alaEServiceNniSvlanNni": alaEServiceNniSvlanNni,
       "alaEServiceNniSvlanSvlan": alaEServiceNniSvlanSvlan,
       "alaEServiceNniSvlanRowStatus": alaEServiceNniSvlanRowStatus,
       "alaEServiceNniSvlanVpaType": alaEServiceNniSvlanVpaType,
       "alcatelIND1EServiceMIBConformance": alcatelIND1EServiceMIBConformance,
       "alcatelIND1EServiceMIBGroups": alcatelIND1EServiceMIBGroups,
       "alaEServiceSapProfileGroup": alaEServiceSapProfileGroup,
       "alaEServiceUNIProfileGroup": alaEServiceUNIProfileGroup,
       "alaEServiceGroup": alaEServiceGroup,
       "alaEServiceSapGroup": alaEServiceSapGroup,
       "alaEServiceSapCvlanGroup": alaEServiceSapCvlanGroup,
       "alaEServicePortGroup": alaEServicePortGroup,
       "alaEServiceSapUniGroup": alaEServiceSapUniGroup,
       "alaEServiceNniSvlanGroup": alaEServiceNniSvlanGroup,
       "alaEServiceInfoGroup": alaEServiceInfoGroup,
       "alcatelIND1EServiceMIBCompliances": alcatelIND1EServiceMIBCompliances,
       "alcatelIND1EServiceMIBCompliance": alcatelIND1EServiceMIBCompliance}
)
