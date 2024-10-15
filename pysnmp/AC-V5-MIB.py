# SNMP MIB module (AC-V5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-V5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:39 2024
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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acV5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcV5Configuration_ObjectIdentity = ObjectIdentity
acV5Configuration = _AcV5Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1)
)
_Acv5Interfce_ObjectIdentity = ObjectIdentity
acv5Interfce = _Acv5Interfce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1)
)
_AcV5InterfceTable_Object = MibTable
acV5InterfceTable = _AcV5InterfceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acV5InterfceTable.setStatus("current")
_AcV5InterfceEntry_Object = MibTableRow
acV5InterfceEntry = _AcV5InterfceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1)
)
acV5InterfceEntry.setIndexNames(
    (0, "AC-V5-MIB", "acV5InterfceIndex"),
)
if mibBuilder.loadTexts:
    acV5InterfceEntry.setStatus("current")


class _AcV5InterfceIndex_Type(Unsigned32):
    """Custom type acV5InterfceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcV5InterfceIndex_Type.__name__ = "Unsigned32"
_AcV5InterfceIndex_Object = MibTableColumn
acV5InterfceIndex = _AcV5InterfceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 1),
    _AcV5InterfceIndex_Type()
)
acV5InterfceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceIndex.setStatus("current")
_AcV5InterfceRowStatus_Type = RowStatus
_AcV5InterfceRowStatus_Object = MibTableColumn
acV5InterfceRowStatus = _AcV5InterfceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 2),
    _AcV5InterfceRowStatus_Type()
)
acV5InterfceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceRowStatus.setStatus("current")


class _AcV5InterfceAction_Type(Integer32):
    """Custom type acV5InterfceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("offline", 0),
          ("protectionSwitchOver", 1))
    )


_AcV5InterfceAction_Type.__name__ = "Integer32"
_AcV5InterfceAction_Object = MibTableColumn
acV5InterfceAction = _AcV5InterfceAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 3),
    _AcV5InterfceAction_Type()
)
acV5InterfceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceAction.setStatus("current")


class _AcV5InterfceActionResult_Type(Integer32):
    """Custom type acV5InterfceActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("inProgress", 1),
          ("succeeded", 0))
    )


_AcV5InterfceActionResult_Type.__name__ = "Integer32"
_AcV5InterfceActionResult_Object = MibTableColumn
acV5InterfceActionResult = _AcV5InterfceActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 4),
    _AcV5InterfceActionResult_Type()
)
acV5InterfceActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceActionResult.setStatus("current")


class _AcV5InterfceOperationalState_Type(Integer32):
    """Custom type acV5InterfceOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("inService", 2),
          ("offline", 0))
    )


_AcV5InterfceOperationalState_Type.__name__ = "Integer32"
_AcV5InterfceOperationalState_Object = MibTableColumn
acV5InterfceOperationalState = _AcV5InterfceOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 5),
    _AcV5InterfceOperationalState_Type()
)
acV5InterfceOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceOperationalState.setStatus("current")


class _AcV5InterfceAdminState_Type(Integer32):
    """Custom type acV5InterfceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("offline", 0))
    )


_AcV5InterfceAdminState_Type.__name__ = "Integer32"
_AcV5InterfceAdminState_Object = MibTableColumn
acV5InterfceAdminState = _AcV5InterfceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 6),
    _AcV5InterfceAdminState_Type()
)
acV5InterfceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceAdminState.setStatus("current")


class _AcV5InterfceActiveSignalingLink_Type(Integer32):
    """Custom type acV5InterfceActiveSignalingLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", -1),
          ("primary", 0),
          ("secondary", 1))
    )


_AcV5InterfceActiveSignalingLink_Type.__name__ = "Integer32"
_AcV5InterfceActiveSignalingLink_Object = MibTableColumn
acV5InterfceActiveSignalingLink = _AcV5InterfceActiveSignalingLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 7),
    _AcV5InterfceActiveSignalingLink_Type()
)
acV5InterfceActiveSignalingLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceActiveSignalingLink.setStatus("current")


class _AcV5InterfceIdNotEqual_Type(Integer32):
    """Custom type acV5InterfceIdNotEqual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceIdNotEqual_Type.__name__ = "Integer32"
_AcV5InterfceIdNotEqual_Object = MibTableColumn
acV5InterfceIdNotEqual = _AcV5InterfceIdNotEqual_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 8),
    _AcV5InterfceIdNotEqual_Type()
)
acV5InterfceIdNotEqual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceIdNotEqual.setStatus("current")


class _AcV5InterfceVariantNotEqual_Type(Integer32):
    """Custom type acV5InterfceVariantNotEqual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceVariantNotEqual_Type.__name__ = "Integer32"
_AcV5InterfceVariantNotEqual_Object = MibTableColumn
acV5InterfceVariantNotEqual = _AcV5InterfceVariantNotEqual_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 9),
    _AcV5InterfceVariantNotEqual_Type()
)
acV5InterfceVariantNotEqual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceVariantNotEqual.setStatus("current")


class _AcV5InterfceIDCheckTimeOutError_Type(Integer32):
    """Custom type acV5InterfceIDCheckTimeOutError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceIDCheckTimeOutError_Type.__name__ = "Integer32"
_AcV5InterfceIDCheckTimeOutError_Object = MibTableColumn
acV5InterfceIDCheckTimeOutError = _AcV5InterfceIDCheckTimeOutError_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 10),
    _AcV5InterfceIDCheckTimeOutError_Type()
)
acV5InterfceIDCheckTimeOutError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceIDCheckTimeOutError.setStatus("current")


class _AcV5InterfceL2StartupFailed_Type(Integer32):
    """Custom type acV5InterfceL2StartupFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceL2StartupFailed_Type.__name__ = "Integer32"
_AcV5InterfceL2StartupFailed_Object = MibTableColumn
acV5InterfceL2StartupFailed = _AcV5InterfceL2StartupFailed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 11),
    _AcV5InterfceL2StartupFailed_Type()
)
acV5InterfceL2StartupFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceL2StartupFailed.setStatus("current")


class _AcV5InterfceRestartFailed_Type(Integer32):
    """Custom type acV5InterfceRestartFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceRestartFailed_Type.__name__ = "Integer32"
_AcV5InterfceRestartFailed_Object = MibTableColumn
acV5InterfceRestartFailed = _AcV5InterfceRestartFailed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 12),
    _AcV5InterfceRestartFailed_Type()
)
acV5InterfceRestartFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceRestartFailed.setStatus("current")


class _AcV5InterfceControlProtocolDataLinkError_Type(Integer32):
    """Custom type acV5InterfceControlProtocolDataLinkError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceControlProtocolDataLinkError_Type.__name__ = "Integer32"
_AcV5InterfceControlProtocolDataLinkError_Object = MibTableColumn
acV5InterfceControlProtocolDataLinkError = _AcV5InterfceControlProtocolDataLinkError_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 13),
    _AcV5InterfceControlProtocolDataLinkError_Type()
)
acV5InterfceControlProtocolDataLinkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceControlProtocolDataLinkError.setStatus("current")


class _AcV5InterfceLinkControlProtocolDataLinkError_Type(Integer32):
    """Custom type acV5InterfceLinkControlProtocolDataLinkError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceLinkControlProtocolDataLinkError_Type.__name__ = "Integer32"
_AcV5InterfceLinkControlProtocolDataLinkError_Object = MibTableColumn
acV5InterfceLinkControlProtocolDataLinkError = _AcV5InterfceLinkControlProtocolDataLinkError_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 14),
    _AcV5InterfceLinkControlProtocolDataLinkError_Type()
)
acV5InterfceLinkControlProtocolDataLinkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceLinkControlProtocolDataLinkError.setStatus("current")


class _AcV5InterfceBCCProtocolDataLinkError_Type(Integer32):
    """Custom type acV5InterfceBCCProtocolDataLinkError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceBCCProtocolDataLinkError_Type.__name__ = "Integer32"
_AcV5InterfceBCCProtocolDataLinkError_Object = MibTableColumn
acV5InterfceBCCProtocolDataLinkError = _AcV5InterfceBCCProtocolDataLinkError_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 15),
    _AcV5InterfceBCCProtocolDataLinkError_Type()
)
acV5InterfceBCCProtocolDataLinkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceBCCProtocolDataLinkError.setStatus("current")


class _AcV5InterfcePSTNProtocolDataLinkError_Type(Integer32):
    """Custom type acV5InterfcePSTNProtocolDataLinkError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfcePSTNProtocolDataLinkError_Type.__name__ = "Integer32"
_AcV5InterfcePSTNProtocolDataLinkError_Object = MibTableColumn
acV5InterfcePSTNProtocolDataLinkError = _AcV5InterfcePSTNProtocolDataLinkError_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 16),
    _AcV5InterfcePSTNProtocolDataLinkError_Type()
)
acV5InterfcePSTNProtocolDataLinkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfcePSTNProtocolDataLinkError.setStatus("current")


class _AcV5InterfceProtectionDL1Error_Type(Integer32):
    """Custom type acV5InterfceProtectionDL1Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceProtectionDL1Error_Type.__name__ = "Integer32"
_AcV5InterfceProtectionDL1Error_Object = MibTableColumn
acV5InterfceProtectionDL1Error = _AcV5InterfceProtectionDL1Error_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 17),
    _AcV5InterfceProtectionDL1Error_Type()
)
acV5InterfceProtectionDL1Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceProtectionDL1Error.setStatus("current")


class _AcV5InterfceProtectionDL2Error_Type(Integer32):
    """Custom type acV5InterfceProtectionDL2Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("raised", 1),
          ("unknown", 2))
    )


_AcV5InterfceProtectionDL2Error_Type.__name__ = "Integer32"
_AcV5InterfceProtectionDL2Error_Object = MibTableColumn
acV5InterfceProtectionDL2Error = _AcV5InterfceProtectionDL2Error_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 18),
    _AcV5InterfceProtectionDL2Error_Type()
)
acV5InterfceProtectionDL2Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceProtectionDL2Error.setStatus("current")


class _AcV5InterfceType_Type(Integer32):
    """Custom type acV5InterfceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("v52", 1)
    )


_AcV5InterfceType_Type.__name__ = "Integer32"
_AcV5InterfceType_Object = MibTableColumn
acV5InterfceType = _AcV5InterfceType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 19),
    _AcV5InterfceType_Type()
)
acV5InterfceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceType.setStatus("current")


class _AcV5InterfceProtocolSide_Type(Integer32):
    """Custom type acV5InterfceProtocolSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("an-Side", 0),
          ("le-Side", 1))
    )


_AcV5InterfceProtocolSide_Type.__name__ = "Integer32"
_AcV5InterfceProtocolSide_Object = MibTableColumn
acV5InterfceProtocolSide = _AcV5InterfceProtocolSide_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 20),
    _AcV5InterfceProtocolSide_Type()
)
acV5InterfceProtocolSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfceProtocolSide.setStatus("current")


class _AcV5InterfceId_Type(Integer32):
    """Custom type acV5InterfceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16777215),
    )


_AcV5InterfceId_Type.__name__ = "Integer32"
_AcV5InterfceId_Object = MibTableColumn
acV5InterfceId = _AcV5InterfceId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 21),
    _AcV5InterfceId_Type()
)
acV5InterfceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceId.setStatus("current")


class _AcV5InterfceVariantId_Type(Unsigned32):
    """Custom type acV5InterfceVariantId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AcV5InterfceVariantId_Type.__name__ = "Unsigned32"
_AcV5InterfceVariantId_Object = MibTableColumn
acV5InterfceVariantId = _AcV5InterfceVariantId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 22),
    _AcV5InterfceVariantId_Type()
)
acV5InterfceVariantId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceVariantId.setStatus("current")


class _AcV5InterfceLogicalCchannelId_Type(Unsigned32):
    """Custom type acV5InterfceLogicalCchannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcV5InterfceLogicalCchannelId_Type.__name__ = "Unsigned32"
_AcV5InterfceLogicalCchannelId_Object = MibTableColumn
acV5InterfceLogicalCchannelId = _AcV5InterfceLogicalCchannelId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 23),
    _AcV5InterfceLogicalCchannelId_Type()
)
acV5InterfceLogicalCchannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceLogicalCchannelId.setStatus("current")


class _AcV5InterfceTraceLevel_Type(Integer32):
    """Custom type acV5InterfceTraceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("full-Trace-No-Duplication", 20),
          ("full-Trace-With-Duplication", 21),
          ("layer3-Up-Trace-No-Duplication", 22),
          ("layer3-Up-Trace-With-Duplication", 23),
          ("noTrace", 0))
    )


_AcV5InterfceTraceLevel_Type.__name__ = "Integer32"
_AcV5InterfceTraceLevel_Object = MibTableColumn
acV5InterfceTraceLevel = _AcV5InterfceTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 24),
    _AcV5InterfceTraceLevel_Type()
)
acV5InterfceTraceLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceTraceLevel.setStatus("current")


class _AcV5InterfceNumberOfPortsInCard_Type(Unsigned32):
    """Custom type acV5InterfceNumberOfPortsInCard based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65533),
    )


_AcV5InterfceNumberOfPortsInCard_Type.__name__ = "Unsigned32"
_AcV5InterfceNumberOfPortsInCard_Object = MibTableColumn
acV5InterfceNumberOfPortsInCard = _AcV5InterfceNumberOfPortsInCard_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 25),
    _AcV5InterfceNumberOfPortsInCard_Type()
)
acV5InterfceNumberOfPortsInCard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceNumberOfPortsInCard.setStatus("current")


class _AcV5InterfceEnableRegisterRecallConfiguration_Type(Integer32):
    """Custom type acV5InterfceEnableRegisterRecallConfiguration based on Integer32"""
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


_AcV5InterfceEnableRegisterRecallConfiguration_Type.__name__ = "Integer32"
_AcV5InterfceEnableRegisterRecallConfiguration_Object = MibTableColumn
acV5InterfceEnableRegisterRecallConfiguration = _AcV5InterfceEnableRegisterRecallConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 26),
    _AcV5InterfceEnableRegisterRecallConfiguration_Type()
)
acV5InterfceEnableRegisterRecallConfiguration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceEnableRegisterRecallConfiguration.setStatus("current")


class _AcV5InterfceRegisterRecallDurationType_Type(Unsigned32):
    """Custom type acV5InterfceRegisterRecallDurationType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcV5InterfceRegisterRecallDurationType_Type.__name__ = "Unsigned32"
_AcV5InterfceRegisterRecallDurationType_Object = MibTableColumn
acV5InterfceRegisterRecallDurationType = _AcV5InterfceRegisterRecallDurationType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 1, 1, 1, 27),
    _AcV5InterfceRegisterRecallDurationType_Type()
)
acV5InterfceRegisterRecallDurationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5InterfceRegisterRecallDurationType.setStatus("current")
_AcV5Link_ObjectIdentity = ObjectIdentity
acV5Link = _AcV5Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2)
)
_AcV5LinkTable_Object = MibTable
acV5LinkTable = _AcV5LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acV5LinkTable.setStatus("current")
_AcV5LinkEntry_Object = MibTableRow
acV5LinkEntry = _AcV5LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1)
)
acV5LinkEntry.setIndexNames(
    (0, "AC-V5-MIB", "acV5LinkIndex"),
)
if mibBuilder.loadTexts:
    acV5LinkEntry.setStatus("current")


class _AcV5LinkIndex_Type(Unsigned32):
    """Custom type acV5LinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_AcV5LinkIndex_Type.__name__ = "Unsigned32"
_AcV5LinkIndex_Object = MibTableColumn
acV5LinkIndex = _AcV5LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 1),
    _AcV5LinkIndex_Type()
)
acV5LinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5LinkIndex.setStatus("current")
_AcV5LinkRowStatus_Type = RowStatus
_AcV5LinkRowStatus_Object = MibTableColumn
acV5LinkRowStatus = _AcV5LinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 2),
    _AcV5LinkRowStatus_Type()
)
acV5LinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5LinkRowStatus.setStatus("current")


class _AcV5LinkAction_Type(Integer32):
    """Custom type acV5LinkAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("linkIdCheck", 2),
          ("unBlock", 0))
    )


_AcV5LinkAction_Type.__name__ = "Integer32"
_AcV5LinkAction_Object = MibTableColumn
acV5LinkAction = _AcV5LinkAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 3),
    _AcV5LinkAction_Type()
)
acV5LinkAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5LinkAction.setStatus("current")


class _AcV5LinkActionResult_Type(Integer32):
    """Custom type acV5LinkActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("inProgress", 1),
          ("succeeded", 0))
    )


_AcV5LinkActionResult_Type.__name__ = "Integer32"
_AcV5LinkActionResult_Object = MibTableColumn
acV5LinkActionResult = _AcV5LinkActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 4),
    _AcV5LinkActionResult_Type()
)
acV5LinkActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5LinkActionResult.setStatus("current")


class _AcV5LinkIdCheckStatus_Type(Integer32):
    """Custom type acV5LinkIdCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("succes", 0),
          ("testRejected", 2))
    )


_AcV5LinkIdCheckStatus_Type.__name__ = "Integer32"
_AcV5LinkIdCheckStatus_Object = MibTableColumn
acV5LinkIdCheckStatus = _AcV5LinkIdCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 5),
    _AcV5LinkIdCheckStatus_Type()
)
acV5LinkIdCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5LinkIdCheckStatus.setStatus("current")


class _AcV5LinkOperationalState_Type(Integer32):
    """Custom type acV5LinkOperationalState based on Integer32"""
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
        *(("blocked", 1),
          ("blockedAndFailed", 3),
          ("failed", 2),
          ("operational", 0))
    )


_AcV5LinkOperationalState_Type.__name__ = "Integer32"
_AcV5LinkOperationalState_Object = MibTableColumn
acV5LinkOperationalState = _AcV5LinkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 6),
    _AcV5LinkOperationalState_Type()
)
acV5LinkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5LinkOperationalState.setStatus("current")


class _AcV5LinkInterfaceIndx_Type(Unsigned32):
    """Custom type acV5LinkInterfaceIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AcV5LinkInterfaceIndx_Type.__name__ = "Unsigned32"
_AcV5LinkInterfaceIndx_Object = MibTableColumn
acV5LinkInterfaceIndx = _AcV5LinkInterfaceIndx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 7),
    _AcV5LinkInterfaceIndx_Type()
)
acV5LinkInterfaceIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5LinkInterfaceIndx.setStatus("current")


class _AcV5LinkId_Type(Integer32):
    """Custom type acV5LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 16777215),
    )


_AcV5LinkId_Type.__name__ = "Integer32"
_AcV5LinkId_Object = MibTableColumn
acV5LinkId = _AcV5LinkId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 8),
    _AcV5LinkId_Type()
)
acV5LinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5LinkId.setStatus("current")


class _AcV5LinkType_Type(Integer32):
    """Custom type acV5LinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_AcV5LinkType_Type.__name__ = "Integer32"
_AcV5LinkType_Object = MibTableColumn
acV5LinkType = _AcV5LinkType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 1, 2, 1, 1, 9),
    _AcV5LinkType_Type()
)
acV5LinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acV5LinkType.setStatus("current")
_AcV5Action_ObjectIdentity = ObjectIdentity
acV5Action = _AcV5Action_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 3)
)
_AcV5PortAction_ObjectIdentity = ObjectIdentity
acV5PortAction = _AcV5PortAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 3, 1)
)


class _AcV5PortActionType_Type(Integer32):
    """Custom type acV5PortActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("actionDone", 10),
          ("none", 0),
          ("removeAllPorts", 1),
          ("removeIFPorts", 2))
    )


_AcV5PortActionType_Type.__name__ = "Integer32"
_AcV5PortActionType_Object = MibScalar
acV5PortActionType = _AcV5PortActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 3, 1, 1),
    _AcV5PortActionType_Type()
)
acV5PortActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acV5PortActionType.setStatus("current")


class _AcV5PortActionID_Type(Unsigned32):
    """Custom type acV5PortActionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcV5PortActionID_Type.__name__ = "Unsigned32"
_AcV5PortActionID_Object = MibScalar
acV5PortActionID = _AcV5PortActionID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 3, 1, 2),
    _AcV5PortActionID_Type()
)
acV5PortActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acV5PortActionID.setStatus("current")


class _AcV5PortActionParams_Type(SnmpAdminString):
    """Custom type acV5PortActionParams based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcV5PortActionParams_Type.__name__ = "SnmpAdminString"
_AcV5PortActionParams_Object = MibScalar
acV5PortActionParams = _AcV5PortActionParams_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 3, 1, 3),
    _AcV5PortActionParams_Type()
)
acV5PortActionParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acV5PortActionParams.setStatus("current")


class _AcV5PortActionResult_Type(SnmpAdminString):
    """Custom type acV5PortActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcV5PortActionResult_Type.__name__ = "SnmpAdminString"
_AcV5PortActionResult_Object = MibScalar
acV5PortActionResult = _AcV5PortActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 13, 3, 1, 4),
    _AcV5PortActionResult_Type()
)
acV5PortActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5PortActionResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-V5-MIB",
    **{"acV5": acV5,
       "acV5Configuration": acV5Configuration,
       "acv5Interfce": acv5Interfce,
       "acV5InterfceTable": acV5InterfceTable,
       "acV5InterfceEntry": acV5InterfceEntry,
       "acV5InterfceIndex": acV5InterfceIndex,
       "acV5InterfceRowStatus": acV5InterfceRowStatus,
       "acV5InterfceAction": acV5InterfceAction,
       "acV5InterfceActionResult": acV5InterfceActionResult,
       "acV5InterfceOperationalState": acV5InterfceOperationalState,
       "acV5InterfceAdminState": acV5InterfceAdminState,
       "acV5InterfceActiveSignalingLink": acV5InterfceActiveSignalingLink,
       "acV5InterfceIdNotEqual": acV5InterfceIdNotEqual,
       "acV5InterfceVariantNotEqual": acV5InterfceVariantNotEqual,
       "acV5InterfceIDCheckTimeOutError": acV5InterfceIDCheckTimeOutError,
       "acV5InterfceL2StartupFailed": acV5InterfceL2StartupFailed,
       "acV5InterfceRestartFailed": acV5InterfceRestartFailed,
       "acV5InterfceControlProtocolDataLinkError": acV5InterfceControlProtocolDataLinkError,
       "acV5InterfceLinkControlProtocolDataLinkError": acV5InterfceLinkControlProtocolDataLinkError,
       "acV5InterfceBCCProtocolDataLinkError": acV5InterfceBCCProtocolDataLinkError,
       "acV5InterfcePSTNProtocolDataLinkError": acV5InterfcePSTNProtocolDataLinkError,
       "acV5InterfceProtectionDL1Error": acV5InterfceProtectionDL1Error,
       "acV5InterfceProtectionDL2Error": acV5InterfceProtectionDL2Error,
       "acV5InterfceType": acV5InterfceType,
       "acV5InterfceProtocolSide": acV5InterfceProtocolSide,
       "acV5InterfceId": acV5InterfceId,
       "acV5InterfceVariantId": acV5InterfceVariantId,
       "acV5InterfceLogicalCchannelId": acV5InterfceLogicalCchannelId,
       "acV5InterfceTraceLevel": acV5InterfceTraceLevel,
       "acV5InterfceNumberOfPortsInCard": acV5InterfceNumberOfPortsInCard,
       "acV5InterfceEnableRegisterRecallConfiguration": acV5InterfceEnableRegisterRecallConfiguration,
       "acV5InterfceRegisterRecallDurationType": acV5InterfceRegisterRecallDurationType,
       "acV5Link": acV5Link,
       "acV5LinkTable": acV5LinkTable,
       "acV5LinkEntry": acV5LinkEntry,
       "acV5LinkIndex": acV5LinkIndex,
       "acV5LinkRowStatus": acV5LinkRowStatus,
       "acV5LinkAction": acV5LinkAction,
       "acV5LinkActionResult": acV5LinkActionResult,
       "acV5LinkIdCheckStatus": acV5LinkIdCheckStatus,
       "acV5LinkOperationalState": acV5LinkOperationalState,
       "acV5LinkInterfaceIndx": acV5LinkInterfaceIndx,
       "acV5LinkId": acV5LinkId,
       "acV5LinkType": acV5LinkType,
       "acV5Action": acV5Action,
       "acV5PortAction": acV5PortAction,
       "acV5PortActionType": acV5PortActionType,
       "acV5PortActionID": acV5PortActionID,
       "acV5PortActionParams": acV5PortActionParams,
       "acV5PortActionResult": acV5PortActionResult}
)
