# SNMP MIB module (AVAYA-SURV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-SURV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:35 2024
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

(avGatewayMibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "avGatewayMibs")

(InetAddress,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

avSurvMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvSurvNotification_ObjectIdentity = ObjectIdentity
avSurvNotification = _AvSurvNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 0)
)
_AvSurvConfig_ObjectIdentity = ObjectIdentity
avSurvConfig = _AvSurvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1)
)


class _AvSurvAdminState_Type(Integer32):
    """Custom type avSurvAdminState based on Integer32"""
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


_AvSurvAdminState_Type.__name__ = "Integer32"
_AvSurvAdminState_Object = MibScalar
avSurvAdminState = _AvSurvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 1),
    _AvSurvAdminState_Type()
)
avSurvAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSurvAdminState.setStatus("current")


class _AvSurvStatus_Type(Integer32):
    """Custom type avSurvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AvSurvStatus_Type.__name__ = "Integer32"
_AvSurvStatus_Object = MibScalar
avSurvStatus = _AvSurvStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 2),
    _AvSurvStatus_Type()
)
avSurvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSurvStatus.setStatus("current")


class _AvSurvMaxIPReg_Type(Integer32):
    """Custom type avSurvMaxIPReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_AvSurvMaxIPReg_Type.__name__ = "Integer32"
_AvSurvMaxIPReg_Object = MibScalar
avSurvMaxIPReg = _AvSurvMaxIPReg_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 3),
    _AvSurvMaxIPReg_Type()
)
avSurvMaxIPReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSurvMaxIPReg.setStatus("current")


class _AvSurvDateFormat_Type(Integer32):
    """Custom type avSurvDateFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ddMmYy", 2),
          ("mmDdYy", 1),
          ("yyMmDd", 3))
    )


_AvSurvDateFormat_Type.__name__ = "Integer32"
_AvSurvDateFormat_Object = MibScalar
avSurvDateFormat = _AvSurvDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 4),
    _AvSurvDateFormat_Type()
)
avSurvDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSurvDateFormat.setStatus("current")
_AvSurvEndDLTimeStamp_Type = DateAndTime
_AvSurvEndDLTimeStamp_Object = MibScalar
avSurvEndDLTimeStamp = _AvSurvEndDLTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 5),
    _AvSurvEndDLTimeStamp_Type()
)
avSurvEndDLTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSurvEndDLTimeStamp.setStatus("current")


class _AvSurvNotificationSeverity_Type(Integer32):
    """Custom type avSurvNotificationSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_AvSurvNotificationSeverity_Type.__name__ = "Integer32"
_AvSurvNotificationSeverity_Object = MibScalar
avSurvNotificationSeverity = _AvSurvNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 6),
    _AvSurvNotificationSeverity_Type()
)
avSurvNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSurvNotificationSeverity.setStatus("current")


class _AvSurvConfigCommand_Type(Integer32):
    """Custom type avSurvConfigCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AvSurvConfigCommand_Type.__name__ = "Integer32"
_AvSurvConfigCommand_Object = MibScalar
avSurvConfigCommand = _AvSurvConfigCommand_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 7),
    _AvSurvConfigCommand_Type()
)
avSurvConfigCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSurvConfigCommand.setStatus("current")


class _AvSurvGatewayNumber_Type(Integer32):
    """Custom type avSurvGatewayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_AvSurvGatewayNumber_Type.__name__ = "Integer32"
_AvSurvGatewayNumber_Object = MibScalar
avSurvGatewayNumber = _AvSurvGatewayNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 8),
    _AvSurvGatewayNumber_Type()
)
avSurvGatewayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSurvGatewayNumber.setStatus("current")


class _AvSurvPimLockout_Type(Integer32):
    """Custom type avSurvPimLockout based on Integer32"""
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


_AvSurvPimLockout_Type.__name__ = "Integer32"
_AvSurvPimLockout_Object = MibScalar
avSurvPimLockout = _AvSurvPimLockout_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 9),
    _AvSurvPimLockout_Type()
)
avSurvPimLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avSurvPimLockout.setStatus("current")


class _AvSurvAttendantAccessCode_Type(DisplayString):
    """Custom type avSurvAttendantAccessCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_AvSurvAttendantAccessCode_Type.__name__ = "DisplayString"
_AvSurvAttendantAccessCode_Object = MibScalar
avSurvAttendantAccessCode = _AvSurvAttendantAccessCode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 10),
    _AvSurvAttendantAccessCode_Type()
)
avSurvAttendantAccessCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvAttendantAccessCode.setStatus("current")


class _AvSurvAttendantExtension_Type(DisplayString):
    """Custom type avSurvAttendantExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_AvSurvAttendantExtension_Type.__name__ = "DisplayString"
_AvSurvAttendantExtension_Object = MibScalar
avSurvAttendantExtension = _AvSurvAttendantExtension_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 1, 11),
    _AvSurvAttendantExtension_Type()
)
avSurvAttendantExtension.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvAttendantExtension.setStatus("current")
_AvSurvStationTable_Object = MibTable
avSurvStationTable = _AvSurvStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2)
)
if mibBuilder.loadTexts:
    avSurvStationTable.setStatus("current")
_AvSurvStationEntry_Object = MibTableRow
avSurvStationEntry = _AvSurvStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1)
)
avSurvStationEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvStationIndex"),
)
if mibBuilder.loadTexts:
    avSurvStationEntry.setStatus("current")


class _AvSurvStationIndex_Type(Integer32):
    """Custom type avSurvStationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 340),
    )


_AvSurvStationIndex_Type.__name__ = "Integer32"
_AvSurvStationIndex_Object = MibTableColumn
avSurvStationIndex = _AvSurvStationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 1),
    _AvSurvStationIndex_Type()
)
avSurvStationIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationIndex.setStatus("current")


class _AvSurvStationExt_Type(DisplayString):
    """Custom type avSurvStationExt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_AvSurvStationExt_Type.__name__ = "DisplayString"
_AvSurvStationExt_Object = MibTableColumn
avSurvStationExt = _AvSurvStationExt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 2),
    _AvSurvStationExt_Type()
)
avSurvStationExt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationExt.setStatus("current")


class _AvSurvStationType_Type(Integer32):
    """Custom type avSurvStationType based on Integer32"""
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
              20,
              21,
              22,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("analog2500", 10),
          ("dcp2402", 20),
          ("dcp2410", 21),
          ("dcp2420", 22),
          ("dcp6402", 30),
          ("dcp6402D", 31),
          ("dcp6408", 32),
          ("dcp6408D", 34),
          ("dcp6408Dplus", 35),
          ("dcp6408plus", 33),
          ("dcp6416Dplus", 36),
          ("dcp6424Dplus", 37),
          ("dcp8403B", 40),
          ("dcp8405B", 41),
          ("dcp8405Bplus", 42),
          ("dcp8405D", 43),
          ("dcp8405Dplus", 44),
          ("dcp8410B", 45),
          ("dcp8410D", 46),
          ("dcp8411B", 47),
          ("dcp8411D", 48),
          ("dcp8434D", 49),
          ("ip4601", 1),
          ("ip4602", 2),
          ("ip4602Sw", 3),
          ("ip4606", 4),
          ("ip4610Sw", 5),
          ("ip4612", 6),
          ("ip4620", 7),
          ("ip4620Sw", 8),
          ("ip4621", 11),
          ("ip4622", 12),
          ("ip4624", 9),
          ("ip4625", 13))
    )


_AvSurvStationType_Type.__name__ = "Integer32"
_AvSurvStationType_Object = MibTableColumn
avSurvStationType = _AvSurvStationType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 3),
    _AvSurvStationType_Type()
)
avSurvStationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationType.setStatus("current")


class _AvSurvStationInterfaceIndex_Type(Integer32):
    """Custom type avSurvStationInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AvSurvStationInterfaceIndex_Type.__name__ = "Integer32"
_AvSurvStationInterfaceIndex_Object = MibTableColumn
avSurvStationInterfaceIndex = _AvSurvStationInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 4),
    _AvSurvStationInterfaceIndex_Type()
)
avSurvStationInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationInterfaceIndex.setStatus("current")


class _AvSurvStationCOR_Type(Integer32):
    """Custom type avSurvStationCOR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("internal", 2),
          ("local", 3),
          ("toll", 4),
          ("unrestricted", 5))
    )


_AvSurvStationCOR_Type.__name__ = "Integer32"
_AvSurvStationCOR_Object = MibTableColumn
avSurvStationCOR = _AvSurvStationCOR_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 5),
    _AvSurvStationCOR_Type()
)
avSurvStationCOR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationCOR.setStatus("current")
_AvSurvStationTrunkDest_Type = TruthValue
_AvSurvStationTrunkDest_Object = MibTableColumn
avSurvStationTrunkDest = _AvSurvStationTrunkDest_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 6),
    _AvSurvStationTrunkDest_Type()
)
avSurvStationTrunkDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationTrunkDest.setStatus("current")
_AvSurvStationRowStatus_Type = RowStatus
_AvSurvStationRowStatus_Object = MibTableColumn
avSurvStationRowStatus = _AvSurvStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 7),
    _AvSurvStationRowStatus_Type()
)
avSurvStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationRowStatus.setStatus("current")
_AvSurvStationExpansionModule_Type = TruthValue
_AvSurvStationExpansionModule_Object = MibTableColumn
avSurvStationExpansionModule = _AvSurvStationExpansionModule_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 8),
    _AvSurvStationExpansionModule_Type()
)
avSurvStationExpansionModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationExpansionModule.setStatus("current")


class _AvSurvStationSlotPort_Type(DisplayString):
    """Custom type avSurvStationSlotPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AvSurvStationSlotPort_Type.__name__ = "DisplayString"
_AvSurvStationSlotPort_Object = MibTableColumn
avSurvStationSlotPort = _AvSurvStationSlotPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 9),
    _AvSurvStationSlotPort_Type()
)
avSurvStationSlotPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationSlotPort.setStatus("current")
_AvSurvStationSwitchHookFlash_Type = TruthValue
_AvSurvStationSwitchHookFlash_Object = MibTableColumn
avSurvStationSwitchHookFlash = _AvSurvStationSwitchHookFlash_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 10),
    _AvSurvStationSwitchHookFlash_Type()
)
avSurvStationSwitchHookFlash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationSwitchHookFlash.setStatus("current")


class _AvSurvStationIpAddressRegistered_Type(OctetString):
    """Custom type avSurvStationIpAddressRegistered based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_AvSurvStationIpAddressRegistered_Type.__name__ = "OctetString"
_AvSurvStationIpAddressRegistered_Object = MibTableColumn
avSurvStationIpAddressRegistered = _AvSurvStationIpAddressRegistered_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 11),
    _AvSurvStationIpAddressRegistered_Type()
)
avSurvStationIpAddressRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avSurvStationIpAddressRegistered.setStatus("current")


class _AvSurvStationName_Type(DisplayString):
    """Custom type avSurvStationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_AvSurvStationName_Type.__name__ = "DisplayString"
_AvSurvStationName_Object = MibTableColumn
avSurvStationName = _AvSurvStationName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 2, 1, 12),
    _AvSurvStationName_Type()
)
avSurvStationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvStationName.setStatus("current")
_AvSurvTrunkGroupTable_Object = MibTable
avSurvTrunkGroupTable = _AvSurvTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3)
)
if mibBuilder.loadTexts:
    avSurvTrunkGroupTable.setStatus("current")
_AvSurvTrunkGroupEntry_Object = MibTableRow
avSurvTrunkGroupEntry = _AvSurvTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1)
)
avSurvTrunkGroupEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvTrunkGroupNum"),
)
if mibBuilder.loadTexts:
    avSurvTrunkGroupEntry.setStatus("current")


class _AvSurvTrunkGroupNum_Type(Integer32):
    """Custom type avSurvTrunkGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_AvSurvTrunkGroupNum_Type.__name__ = "Integer32"
_AvSurvTrunkGroupNum_Object = MibTableColumn
avSurvTrunkGroupNum = _AvSurvTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 1),
    _AvSurvTrunkGroupNum_Type()
)
avSurvTrunkGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupNum.setStatus("current")


class _AvSurvTrunkGroupType_Type(Integer32):
    """Custom type avSurvTrunkGroupType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("analogDid", 2),
          ("analogGroundStart", 3),
          ("analogLoopStart", 1),
          ("bri", 4),
          ("e1InBandSignaling", 7),
          ("e1IsdnSignaling", 8),
          ("t1InBandSignaling", 5),
          ("t1IsdnSignaling", 6))
    )


_AvSurvTrunkGroupType_Type.__name__ = "Integer32"
_AvSurvTrunkGroupType_Object = MibTableColumn
avSurvTrunkGroupType = _AvSurvTrunkGroupType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 2),
    _AvSurvTrunkGroupType_Type()
)
avSurvTrunkGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupType.setStatus("current")


class _AvSurvTrunkGroupTAC_Type(DisplayString):
    """Custom type avSurvTrunkGroupTAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_AvSurvTrunkGroupTAC_Type.__name__ = "DisplayString"
_AvSurvTrunkGroupTAC_Object = MibTableColumn
avSurvTrunkGroupTAC = _AvSurvTrunkGroupTAC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 3),
    _AvSurvTrunkGroupTAC_Type()
)
avSurvTrunkGroupTAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupTAC.setStatus("current")


class _AvSurvTrunkGroupDial_Type(Integer32):
    """Custom type avSurvTrunkGroupDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 2),
          ("mf", 3),
          ("rotary", 1))
    )


_AvSurvTrunkGroupDial_Type.__name__ = "Integer32"
_AvSurvTrunkGroupDial_Object = MibTableColumn
avSurvTrunkGroupDial = _AvSurvTrunkGroupDial_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 4),
    _AvSurvTrunkGroupDial_Type()
)
avSurvTrunkGroupDial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupDial.setStatus("current")
_AvSurvTrunkGroupRowStatus_Type = RowStatus
_AvSurvTrunkGroupRowStatus_Object = MibTableColumn
avSurvTrunkGroupRowStatus = _AvSurvTrunkGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 5),
    _AvSurvTrunkGroupRowStatus_Type()
)
avSurvTrunkGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupRowStatus.setStatus("current")


class _AvSurvTrunkGroupDidDigitTreatment_Type(Integer32):
    """Custom type avSurvTrunkGroupDidDigitTreatment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11,
              12,
              13,
              14,
              99)
        )
    )
    namedValues = NamedValues(
        *(("absorb1", 1),
          ("absorb2", 2),
          ("absorb3", 3),
          ("absorb4", 4),
          ("absorb5", 5),
          ("blank", 99),
          ("insert1", 11),
          ("insert2", 12),
          ("insert3", 13),
          ("insert4", 14))
    )


_AvSurvTrunkGroupDidDigitTreatment_Type.__name__ = "Integer32"
_AvSurvTrunkGroupDidDigitTreatment_Object = MibTableColumn
avSurvTrunkGroupDidDigitTreatment = _AvSurvTrunkGroupDidDigitTreatment_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 6),
    _AvSurvTrunkGroupDidDigitTreatment_Type()
)
avSurvTrunkGroupDidDigitTreatment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupDidDigitTreatment.setStatus("current")


class _AvSurvTrunkGroupDidDigitsInsert_Type(DisplayString):
    """Custom type avSurvTrunkGroupDidDigitsInsert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_AvSurvTrunkGroupDidDigitsInsert_Type.__name__ = "DisplayString"
_AvSurvTrunkGroupDidDigitsInsert_Object = MibTableColumn
avSurvTrunkGroupDidDigitsInsert = _AvSurvTrunkGroupDidDigitsInsert_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 7),
    _AvSurvTrunkGroupDidDigitsInsert_Type()
)
avSurvTrunkGroupDidDigitsInsert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupDidDigitsInsert.setStatus("current")


class _AvSurvTrunkGroupDidSupervision_Type(Integer32):
    """Custom type avSurvTrunkGroupDidSupervision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("wink", 2))
    )


_AvSurvTrunkGroupDidSupervision_Type.__name__ = "Integer32"
_AvSurvTrunkGroupDidSupervision_Object = MibTableColumn
avSurvTrunkGroupDidSupervision = _AvSurvTrunkGroupDidSupervision_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 8),
    _AvSurvTrunkGroupDidSupervision_Type()
)
avSurvTrunkGroupDidSupervision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupDidSupervision.setStatus("current")


class _AvSurvTrunkGroupName_Type(DisplayString):
    """Custom type avSurvTrunkGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_AvSurvTrunkGroupName_Type.__name__ = "DisplayString"
_AvSurvTrunkGroupName_Object = MibTableColumn
avSurvTrunkGroupName = _AvSurvTrunkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 9),
    _AvSurvTrunkGroupName_Type()
)
avSurvTrunkGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupName.setStatus("current")


class _AvSurvTrunkGroupCodesetDisplay_Type(Integer32):
    """Custom type avSurvTrunkGroupCodesetDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("codeset0", 0),
          ("codeset6", 6),
          ("codeset7", 7))
    )


_AvSurvTrunkGroupCodesetDisplay_Type.__name__ = "Integer32"
_AvSurvTrunkGroupCodesetDisplay_Object = MibTableColumn
avSurvTrunkGroupCodesetDisplay = _AvSurvTrunkGroupCodesetDisplay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 10),
    _AvSurvTrunkGroupCodesetDisplay_Type()
)
avSurvTrunkGroupCodesetDisplay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupCodesetDisplay.setStatus("current")


class _AvSurvTrunkGroupCodesetNational_Type(Integer32):
    """Custom type avSurvTrunkGroupCodesetNational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("codeset6", 6),
          ("codeset7", 7))
    )


_AvSurvTrunkGroupCodesetNational_Type.__name__ = "Integer32"
_AvSurvTrunkGroupCodesetNational_Object = MibTableColumn
avSurvTrunkGroupCodesetNational = _AvSurvTrunkGroupCodesetNational_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 11),
    _AvSurvTrunkGroupCodesetNational_Type()
)
avSurvTrunkGroupCodesetNational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupCodesetNational.setStatus("current")


class _AvSurvTrunkGroupChannelPreference_Type(Integer32):
    """Custom type avSurvTrunkGroupChannelPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("preferred", 2))
    )


_AvSurvTrunkGroupChannelPreference_Type.__name__ = "Integer32"
_AvSurvTrunkGroupChannelPreference_Object = MibTableColumn
avSurvTrunkGroupChannelPreference = _AvSurvTrunkGroupChannelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 12),
    _AvSurvTrunkGroupChannelPreference_Type()
)
avSurvTrunkGroupChannelPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupChannelPreference.setStatus("current")


class _AvSurvTrunkGroupDigitHandling_Type(Integer32):
    """Custom type avSurvTrunkGroupDigitHandling based on Integer32"""
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
        *(("enblocEnbloc", 0),
          ("enblocOverlap", 1),
          ("overlapEnbloc", 2),
          ("overlapOverlap", 3))
    )


_AvSurvTrunkGroupDigitHandling_Type.__name__ = "Integer32"
_AvSurvTrunkGroupDigitHandling_Object = MibTableColumn
avSurvTrunkGroupDigitHandling = _AvSurvTrunkGroupDigitHandling_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 13),
    _AvSurvTrunkGroupDigitHandling_Type()
)
avSurvTrunkGroupDigitHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupDigitHandling.setStatus("current")


class _AvSurvTrunkGroupJapanDisconnect_Type(Integer32):
    """Custom type avSurvTrunkGroupJapanDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvTrunkGroupJapanDisconnect_Type.__name__ = "Integer32"
_AvSurvTrunkGroupJapanDisconnect_Object = MibTableColumn
avSurvTrunkGroupJapanDisconnect = _AvSurvTrunkGroupJapanDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 14),
    _AvSurvTrunkGroupJapanDisconnect_Type()
)
avSurvTrunkGroupJapanDisconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupJapanDisconnect.setStatus("current")


class _AvSurvTrunkGroupSendName_Type(Integer32):
    """Custom type avSurvTrunkGroupSendName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("restricted", 3),
          ("yes", 1))
    )


_AvSurvTrunkGroupSendName_Type.__name__ = "Integer32"
_AvSurvTrunkGroupSendName_Object = MibTableColumn
avSurvTrunkGroupSendName = _AvSurvTrunkGroupSendName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 15),
    _AvSurvTrunkGroupSendName_Type()
)
avSurvTrunkGroupSendName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupSendName.setStatus("current")


class _AvSurvTrunkGroupSendCallingNumber_Type(Integer32):
    """Custom type avSurvTrunkGroupSendCallingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("restricted", 3),
          ("yes", 1))
    )


_AvSurvTrunkGroupSendCallingNumber_Type.__name__ = "Integer32"
_AvSurvTrunkGroupSendCallingNumber_Object = MibTableColumn
avSurvTrunkGroupSendCallingNumber = _AvSurvTrunkGroupSendCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 16),
    _AvSurvTrunkGroupSendCallingNumber_Type()
)
avSurvTrunkGroupSendCallingNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupSendCallingNumber.setStatus("current")


class _AvSurvTrunkGroupNumberingFormat_Type(Integer32):
    """Custom type avSurvTrunkGroupNumberingFormat based on Integer32"""
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
        *(("private", 3),
          ("public", 2),
          ("unknown", 1),
          ("unknownPrivate", 4))
    )


_AvSurvTrunkGroupNumberingFormat_Type.__name__ = "Integer32"
_AvSurvTrunkGroupNumberingFormat_Object = MibTableColumn
avSurvTrunkGroupNumberingFormat = _AvSurvTrunkGroupNumberingFormat_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 17),
    _AvSurvTrunkGroupNumberingFormat_Type()
)
avSurvTrunkGroupNumberingFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupNumberingFormat.setStatus("current")


class _AvSurvTrunkGroupIncomingDestination_Type(DisplayString):
    """Custom type avSurvTrunkGroupIncomingDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_AvSurvTrunkGroupIncomingDestination_Type.__name__ = "DisplayString"
_AvSurvTrunkGroupIncomingDestination_Object = MibTableColumn
avSurvTrunkGroupIncomingDestination = _AvSurvTrunkGroupIncomingDestination_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 18),
    _AvSurvTrunkGroupIncomingDestination_Type()
)
avSurvTrunkGroupIncomingDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupIncomingDestination.setStatus("current")


class _AvSurvTrunkGroupIncomingDialTone_Type(Integer32):
    """Custom type avSurvTrunkGroupIncomingDialTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvTrunkGroupIncomingDialTone_Type.__name__ = "Integer32"
_AvSurvTrunkGroupIncomingDialTone_Object = MibTableColumn
avSurvTrunkGroupIncomingDialTone = _AvSurvTrunkGroupIncomingDialTone_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 19),
    _AvSurvTrunkGroupIncomingDialTone_Type()
)
avSurvTrunkGroupIncomingDialTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupIncomingDialTone.setStatus("current")


class _AvSurvTrunkGroupR2MFCSignaling_Type(Integer32):
    """Custom type avSurvTrunkGroupR2MFCSignaling based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("set1", 1),
          ("set2", 2),
          ("set3", 3),
          ("set4", 4),
          ("set5", 5),
          ("set6", 6),
          ("set7", 7),
          ("set8", 8))
    )


_AvSurvTrunkGroupR2MFCSignaling_Type.__name__ = "Integer32"
_AvSurvTrunkGroupR2MFCSignaling_Object = MibTableColumn
avSurvTrunkGroupR2MFCSignaling = _AvSurvTrunkGroupR2MFCSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 20),
    _AvSurvTrunkGroupR2MFCSignaling_Type()
)
avSurvTrunkGroupR2MFCSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupR2MFCSignaling.setStatus("current")


class _AvSurvTrunkGroupTrunkHunt_Type(Integer32):
    """Custom type avSurvTrunkGroupTrunkHunt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascend", 1),
          ("cyclical", 2),
          ("descend", 3))
    )


_AvSurvTrunkGroupTrunkHunt_Type.__name__ = "Integer32"
_AvSurvTrunkGroupTrunkHunt_Object = MibTableColumn
avSurvTrunkGroupTrunkHunt = _AvSurvTrunkGroupTrunkHunt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 21),
    _AvSurvTrunkGroupTrunkHunt_Type()
)
avSurvTrunkGroupTrunkHunt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupTrunkHunt.setStatus("current")


class _AvSurvTrunkGroupDs1Supervision_Type(Integer32):
    """Custom type avSurvTrunkGroupDs1Supervision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("autoAuto", 9),
          ("autoWink", 10),
          ("groundStart", 4),
          ("immediateImmediate", 8),
          ("loopStart", 3),
          ("winkAuto", 7),
          ("winkImmediate", 6),
          ("winkWink", 5))
    )


_AvSurvTrunkGroupDs1Supervision_Type.__name__ = "Integer32"
_AvSurvTrunkGroupDs1Supervision_Object = MibTableColumn
avSurvTrunkGroupDs1Supervision = _AvSurvTrunkGroupDs1Supervision_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 22),
    _AvSurvTrunkGroupDs1Supervision_Type()
)
avSurvTrunkGroupDs1Supervision.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupDs1Supervision.setStatus("current")


class _AvSurvTrunkGroupCbc_Type(Integer32):
    """Custom type avSurvTrunkGroupCbc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvTrunkGroupCbc_Type.__name__ = "Integer32"
_AvSurvTrunkGroupCbc_Object = MibTableColumn
avSurvTrunkGroupCbc = _AvSurvTrunkGroupCbc_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 23),
    _AvSurvTrunkGroupCbc_Type()
)
avSurvTrunkGroupCbc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupCbc.setStatus("current")


class _AvSurvTrunkGroupCbcServiceFeature_Type(Integer32):
    """Custom type avSurvTrunkGroupCbcServiceFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(197,
              198,
              225,
              227,
              231,
              246)
        )
    )
    namedValues = NamedValues(
        *(("lds", 231),
          ("megacom", 227),
          ("operator", 197),
          ("scocs", 246),
          ("sdn", 225),
          ("suboperator", 198))
    )


_AvSurvTrunkGroupCbcServiceFeature_Type.__name__ = "Integer32"
_AvSurvTrunkGroupCbcServiceFeature_Object = MibTableColumn
avSurvTrunkGroupCbcServiceFeature = _AvSurvTrunkGroupCbcServiceFeature_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 24),
    _AvSurvTrunkGroupCbcServiceFeature_Type()
)
avSurvTrunkGroupCbcServiceFeature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupCbcServiceFeature.setStatus("current")


class _AvSurvTrunkGroupCbcParameter_Type(Integer32):
    """Custom type avSurvTrunkGroupCbcParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AvSurvTrunkGroupCbcParameter_Type.__name__ = "Integer32"
_AvSurvTrunkGroupCbcParameter_Object = MibTableColumn
avSurvTrunkGroupCbcParameter = _AvSurvTrunkGroupCbcParameter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 25),
    _AvSurvTrunkGroupCbcParameter_Type()
)
avSurvTrunkGroupCbcParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupCbcParameter.setStatus("current")


class _AvSurvTrunkGroupBusyDisconnect_Type(Integer32):
    """Custom type avSurvTrunkGroupBusyDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvTrunkGroupBusyDisconnect_Type.__name__ = "Integer32"
_AvSurvTrunkGroupBusyDisconnect_Object = MibTableColumn
avSurvTrunkGroupBusyDisconnect = _AvSurvTrunkGroupBusyDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 3, 1, 26),
    _AvSurvTrunkGroupBusyDisconnect_Type()
)
avSurvTrunkGroupBusyDisconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupBusyDisconnect.setStatus("current")
_AvSurvTrunkTable_Object = MibTable
avSurvTrunkTable = _AvSurvTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4)
)
if mibBuilder.loadTexts:
    avSurvTrunkTable.setStatus("current")
_AvSurvTrunkEntry_Object = MibTableRow
avSurvTrunkEntry = _AvSurvTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1)
)
avSurvTrunkEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvTrunkGroupRefNumber"),
    (0, "AVAYA-SURV-MIB", "avSurvTrunkIndex"),
)
if mibBuilder.loadTexts:
    avSurvTrunkEntry.setStatus("current")


class _AvSurvTrunkGroupRefNumber_Type(Integer32):
    """Custom type avSurvTrunkGroupRefNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_AvSurvTrunkGroupRefNumber_Type.__name__ = "Integer32"
_AvSurvTrunkGroupRefNumber_Object = MibTableColumn
avSurvTrunkGroupRefNumber = _AvSurvTrunkGroupRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1, 1),
    _AvSurvTrunkGroupRefNumber_Type()
)
avSurvTrunkGroupRefNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkGroupRefNumber.setStatus("current")


class _AvSurvTrunkIndex_Type(Integer32):
    """Custom type avSurvTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AvSurvTrunkIndex_Type.__name__ = "Integer32"
_AvSurvTrunkIndex_Object = MibTableColumn
avSurvTrunkIndex = _AvSurvTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1, 2),
    _AvSurvTrunkIndex_Type()
)
avSurvTrunkIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkIndex.setStatus("current")


class _AvSurvTrunkInterfaceIndex_Type(Integer32):
    """Custom type avSurvTrunkInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AvSurvTrunkInterfaceIndex_Type.__name__ = "Integer32"
_AvSurvTrunkInterfaceIndex_Object = MibTableColumn
avSurvTrunkInterfaceIndex = _AvSurvTrunkInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1, 3),
    _AvSurvTrunkInterfaceIndex_Type()
)
avSurvTrunkInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkInterfaceIndex.setStatus("current")
_AvSurvTrunkRowStatus_Type = RowStatus
_AvSurvTrunkRowStatus_Object = MibTableColumn
avSurvTrunkRowStatus = _AvSurvTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1, 4),
    _AvSurvTrunkRowStatus_Type()
)
avSurvTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkRowStatus.setStatus("current")


class _AvSurvTrunkSlotPort_Type(DisplayString):
    """Custom type avSurvTrunkSlotPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AvSurvTrunkSlotPort_Type.__name__ = "DisplayString"
_AvSurvTrunkSlotPort_Object = MibTableColumn
avSurvTrunkSlotPort = _AvSurvTrunkSlotPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1, 5),
    _AvSurvTrunkSlotPort_Type()
)
avSurvTrunkSlotPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkSlotPort.setStatus("current")


class _AvSurvTrunkSigGroupRefNumber_Type(Integer32):
    """Custom type avSurvTrunkSigGroupRefNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_AvSurvTrunkSigGroupRefNumber_Type.__name__ = "Integer32"
_AvSurvTrunkSigGroupRefNumber_Object = MibTableColumn
avSurvTrunkSigGroupRefNumber = _AvSurvTrunkSigGroupRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 4, 1, 6),
    _AvSurvTrunkSigGroupRefNumber_Type()
)
avSurvTrunkSigGroupRefNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvTrunkSigGroupRefNumber.setStatus("current")
_AvSurvArsTable_Object = MibTable
avSurvArsTable = _AvSurvArsTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5)
)
if mibBuilder.loadTexts:
    avSurvArsTable.setStatus("current")
_AvSurvArsEntry_Object = MibTableRow
avSurvArsEntry = _AvSurvArsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1)
)
avSurvArsEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvDialIndex"),
)
if mibBuilder.loadTexts:
    avSurvArsEntry.setStatus("current")


class _AvSurvDialIndex_Type(Integer32):
    """Custom type avSurvDialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AvSurvDialIndex_Type.__name__ = "Integer32"
_AvSurvDialIndex_Object = MibTableColumn
avSurvDialIndex = _AvSurvDialIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 1),
    _AvSurvDialIndex_Type()
)
avSurvDialIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialIndex.setStatus("current")


class _AvSurvDialString_Type(DisplayString):
    """Custom type avSurvDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_AvSurvDialString_Type.__name__ = "DisplayString"
_AvSurvDialString_Object = MibTableColumn
avSurvDialString = _AvSurvDialString_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 2),
    _AvSurvDialString_Type()
)
avSurvDialString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialString.setStatus("current")


class _AvSurvDialType_Type(Integer32):
    """Custom type avSurvDialType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("foreignNumberingPlanArea", 2),
          ("homeNumberingPlanArea", 3),
          ("international", 4),
          ("internationalOperator", 5),
          ("local", 6),
          ("national", 7),
          ("operator", 8),
          ("service", 9))
    )


_AvSurvDialType_Type.__name__ = "Integer32"
_AvSurvDialType_Object = MibTableColumn
avSurvDialType = _AvSurvDialType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 3),
    _AvSurvDialType_Type()
)
avSurvDialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialType.setStatus("current")


class _AvSurvDialMaximumLength_Type(Integer32):
    """Custom type avSurvDialMaximumLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_AvSurvDialMaximumLength_Type.__name__ = "Integer32"
_AvSurvDialMaximumLength_Object = MibTableColumn
avSurvDialMaximumLength = _AvSurvDialMaximumLength_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 4),
    _AvSurvDialMaximumLength_Type()
)
avSurvDialMaximumLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialMaximumLength.setStatus("current")


class _AvSurvDialGroupRefNumber_Type(Integer32):
    """Custom type avSurvDialGroupRefNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_AvSurvDialGroupRefNumber_Type.__name__ = "Integer32"
_AvSurvDialGroupRefNumber_Object = MibTableColumn
avSurvDialGroupRefNumber = _AvSurvDialGroupRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 5),
    _AvSurvDialGroupRefNumber_Type()
)
avSurvDialGroupRefNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialGroupRefNumber.setStatus("current")


class _AvSurvDialAction_Type(Integer32):
    """Custom type avSurvDialAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowCall", 2),
          ("denyCall", 1))
    )


_AvSurvDialAction_Type.__name__ = "Integer32"
_AvSurvDialAction_Object = MibTableColumn
avSurvDialAction = _AvSurvDialAction_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 6),
    _AvSurvDialAction_Type()
)
avSurvDialAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialAction.setStatus("current")
_AvSurvDialRowStatus_Type = RowStatus
_AvSurvDialRowStatus_Object = MibTableColumn
avSurvDialRowStatus = _AvSurvDialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 7),
    _AvSurvDialRowStatus_Type()
)
avSurvDialRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialRowStatus.setStatus("current")


class _AvSurvDialDeleteDigits_Type(Integer32):
    """Custom type avSurvDialDeleteDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_AvSurvDialDeleteDigits_Type.__name__ = "Integer32"
_AvSurvDialDeleteDigits_Object = MibTableColumn
avSurvDialDeleteDigits = _AvSurvDialDeleteDigits_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 8),
    _AvSurvDialDeleteDigits_Type()
)
avSurvDialDeleteDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialDeleteDigits.setStatus("current")


class _AvSurvDialInsertDigits_Type(DisplayString):
    """Custom type avSurvDialInsertDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_AvSurvDialInsertDigits_Type.__name__ = "DisplayString"
_AvSurvDialInsertDigits_Object = MibTableColumn
avSurvDialInsertDigits = _AvSurvDialInsertDigits_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 9),
    _AvSurvDialInsertDigits_Type()
)
avSurvDialInsertDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialInsertDigits.setStatus("current")


class _AvSurvDialMinimumLength_Type(Integer32):
    """Custom type avSurvDialMinimumLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_AvSurvDialMinimumLength_Type.__name__ = "Integer32"
_AvSurvDialMinimumLength_Object = MibTableColumn
avSurvDialMinimumLength = _AvSurvDialMinimumLength_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 5, 1, 10),
    _AvSurvDialMinimumLength_Type()
)
avSurvDialMinimumLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDialMinimumLength.setStatus("current")
_AvSurvFacTable_Object = MibTable
avSurvFacTable = _AvSurvFacTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 6)
)
if mibBuilder.loadTexts:
    avSurvFacTable.setStatus("current")
_AvSurvFacEntry_Object = MibTableRow
avSurvFacEntry = _AvSurvFacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 6, 1)
)
avSurvFacEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvFacIndex"),
)
if mibBuilder.loadTexts:
    avSurvFacEntry.setStatus("current")


class _AvSurvFacIndex_Type(Integer32):
    """Custom type avSurvFacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AvSurvFacIndex_Type.__name__ = "Integer32"
_AvSurvFacIndex_Object = MibTableColumn
avSurvFacIndex = _AvSurvFacIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 6, 1, 1),
    _AvSurvFacIndex_Type()
)
avSurvFacIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvFacIndex.setStatus("current")


class _AvSurvFacId_Type(DisplayString):
    """Custom type avSurvFacId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_AvSurvFacId_Type.__name__ = "DisplayString"
_AvSurvFacId_Object = MibTableColumn
avSurvFacId = _AvSurvFacId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 6, 1, 2),
    _AvSurvFacId_Type()
)
avSurvFacId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvFacId.setStatus("current")
_AvSurvFacRowStatus_Type = RowStatus
_AvSurvFacRowStatus_Object = MibTableColumn
avSurvFacRowStatus = _AvSurvFacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 6, 1, 3),
    _AvSurvFacRowStatus_Type()
)
avSurvFacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvFacRowStatus.setStatus("current")


class _AvSurvFacType_Type(Integer32):
    """Custom type avSurvFacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ars1", 1),
          ("ars2", 2),
          ("contactClose", 5),
          ("contactOpen", 4),
          ("contactPulse", 6),
          ("hold", 3))
    )


_AvSurvFacType_Type.__name__ = "Integer32"
_AvSurvFacType_Object = MibTableColumn
avSurvFacType = _AvSurvFacType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 6, 1, 4),
    _AvSurvFacType_Type()
)
avSurvFacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvFacType.setStatus("current")
_AvSurvIpVoiceCodecSetTable_Object = MibTable
avSurvIpVoiceCodecSetTable = _AvSurvIpVoiceCodecSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7)
)
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetTable.setStatus("current")
_AvSurvIpVoiceCodecSetEntry_Object = MibTableRow
avSurvIpVoiceCodecSetEntry = _AvSurvIpVoiceCodecSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1)
)
avSurvIpVoiceCodecSetEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvIpVoiceCodecSetNum"),
    (0, "AVAYA-SURV-MIB", "avSurvIpVoiceCodecSetIndex"),
)
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetEntry.setStatus("current")


class _AvSurvIpVoiceCodecSetNum_Type(Integer32):
    """Custom type avSurvIpVoiceCodecSetNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AvSurvIpVoiceCodecSetNum_Type.__name__ = "Integer32"
_AvSurvIpVoiceCodecSetNum_Object = MibTableColumn
avSurvIpVoiceCodecSetNum = _AvSurvIpVoiceCodecSetNum_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 1),
    _AvSurvIpVoiceCodecSetNum_Type()
)
avSurvIpVoiceCodecSetNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetNum.setStatus("current")


class _AvSurvIpVoiceCodecSetIndex_Type(Integer32):
    """Custom type avSurvIpVoiceCodecSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AvSurvIpVoiceCodecSetIndex_Type.__name__ = "Integer32"
_AvSurvIpVoiceCodecSetIndex_Object = MibTableColumn
avSurvIpVoiceCodecSetIndex = _AvSurvIpVoiceCodecSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 2),
    _AvSurvIpVoiceCodecSetIndex_Type()
)
avSurvIpVoiceCodecSetIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetIndex.setStatus("current")


class _AvSurvIpVoiceCodecSetPriority_Type(Integer32):
    """Custom type avSurvIpVoiceCodecSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AvSurvIpVoiceCodecSetPriority_Type.__name__ = "Integer32"
_AvSurvIpVoiceCodecSetPriority_Object = MibTableColumn
avSurvIpVoiceCodecSetPriority = _AvSurvIpVoiceCodecSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 3),
    _AvSurvIpVoiceCodecSetPriority_Type()
)
avSurvIpVoiceCodecSetPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetPriority.setStatus("current")


class _AvSurvIpVoiceCodecSetType_Type(Integer32):
    """Custom type avSurvIpVoiceCodecSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 2),
          ("g711u", 1),
          ("g723", 3),
          ("g729", 4),
          ("g729a", 5),
          ("g729ab", 7),
          ("g729b", 6))
    )


_AvSurvIpVoiceCodecSetType_Type.__name__ = "Integer32"
_AvSurvIpVoiceCodecSetType_Object = MibTableColumn
avSurvIpVoiceCodecSetType = _AvSurvIpVoiceCodecSetType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 4),
    _AvSurvIpVoiceCodecSetType_Type()
)
avSurvIpVoiceCodecSetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetType.setStatus("current")
_AvSurvIpVoiceCodecSetSilence_Type = TruthValue
_AvSurvIpVoiceCodecSetSilence_Object = MibTableColumn
avSurvIpVoiceCodecSetSilence = _AvSurvIpVoiceCodecSetSilence_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 5),
    _AvSurvIpVoiceCodecSetSilence_Type()
)
avSurvIpVoiceCodecSetSilence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetSilence.setStatus("current")


class _AvSurvIpVoiceCodecSetFrames_Type(Integer32):
    """Custom type avSurvIpVoiceCodecSetFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AvSurvIpVoiceCodecSetFrames_Type.__name__ = "Integer32"
_AvSurvIpVoiceCodecSetFrames_Object = MibTableColumn
avSurvIpVoiceCodecSetFrames = _AvSurvIpVoiceCodecSetFrames_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 6),
    _AvSurvIpVoiceCodecSetFrames_Type()
)
avSurvIpVoiceCodecSetFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetFrames.setStatus("current")
_AvSurvIpVoiceCodecSetRowStatus_Type = RowStatus
_AvSurvIpVoiceCodecSetRowStatus_Object = MibTableColumn
avSurvIpVoiceCodecSetRowStatus = _AvSurvIpVoiceCodecSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 7, 1, 7),
    _AvSurvIpVoiceCodecSetRowStatus_Type()
)
avSurvIpVoiceCodecSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpVoiceCodecSetRowStatus.setStatus("current")
_AvSurvIpCodecSetConfig_ObjectIdentity = ObjectIdentity
avSurvIpCodecSetConfig = _AvSurvIpCodecSetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8)
)


class _AvSurvIpCodecSetFaxMode_Type(Integer32):
    """Custom type avSurvIpCodecSetFaxMode based on Integer32"""
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
        *(("off", 1),
          ("passthru", 3),
          ("relay", 2),
          ("t38", 4))
    )


_AvSurvIpCodecSetFaxMode_Type.__name__ = "Integer32"
_AvSurvIpCodecSetFaxMode_Object = MibScalar
avSurvIpCodecSetFaxMode = _AvSurvIpCodecSetFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 1),
    _AvSurvIpCodecSetFaxMode_Type()
)
avSurvIpCodecSetFaxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetFaxMode.setStatus("current")


class _AvSurvIpCodecSetFaxRedundancy_Type(Integer32):
    """Custom type avSurvIpCodecSetFaxRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AvSurvIpCodecSetFaxRedundancy_Type.__name__ = "Integer32"
_AvSurvIpCodecSetFaxRedundancy_Object = MibScalar
avSurvIpCodecSetFaxRedundancy = _AvSurvIpCodecSetFaxRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 2),
    _AvSurvIpCodecSetFaxRedundancy_Type()
)
avSurvIpCodecSetFaxRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetFaxRedundancy.setStatus("current")


class _AvSurvIpCodecSetModemMode_Type(Integer32):
    """Custom type avSurvIpCodecSetModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("passthru", 3),
          ("relay", 2))
    )


_AvSurvIpCodecSetModemMode_Type.__name__ = "Integer32"
_AvSurvIpCodecSetModemMode_Object = MibScalar
avSurvIpCodecSetModemMode = _AvSurvIpCodecSetModemMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 3),
    _AvSurvIpCodecSetModemMode_Type()
)
avSurvIpCodecSetModemMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetModemMode.setStatus("current")


class _AvSurvIpCodecSetModemRedundancy_Type(Integer32):
    """Custom type avSurvIpCodecSetModemRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AvSurvIpCodecSetModemRedundancy_Type.__name__ = "Integer32"
_AvSurvIpCodecSetModemRedundancy_Object = MibScalar
avSurvIpCodecSetModemRedundancy = _AvSurvIpCodecSetModemRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 4),
    _AvSurvIpCodecSetModemRedundancy_Type()
)
avSurvIpCodecSetModemRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetModemRedundancy.setStatus("current")


class _AvSurvIpCodecSetTtyMode_Type(Integer32):
    """Custom type avSurvIpCodecSetTtyMode based on Integer32"""
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
        *(("off", 1),
          ("passthru", 4),
          ("uk", 3),
          ("us", 2))
    )


_AvSurvIpCodecSetTtyMode_Type.__name__ = "Integer32"
_AvSurvIpCodecSetTtyMode_Object = MibScalar
avSurvIpCodecSetTtyMode = _AvSurvIpCodecSetTtyMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 5),
    _AvSurvIpCodecSetTtyMode_Type()
)
avSurvIpCodecSetTtyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetTtyMode.setStatus("current")


class _AvSurvIpCodecSetTtyRedundancy_Type(Integer32):
    """Custom type avSurvIpCodecSetTtyRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AvSurvIpCodecSetTtyRedundancy_Type.__name__ = "Integer32"
_AvSurvIpCodecSetTtyRedundancy_Object = MibScalar
avSurvIpCodecSetTtyRedundancy = _AvSurvIpCodecSetTtyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 6),
    _AvSurvIpCodecSetTtyRedundancy_Type()
)
avSurvIpCodecSetTtyRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetTtyRedundancy.setStatus("current")


class _AvSurvIpCodecSetClearChanMode_Type(Integer32):
    """Custom type avSurvIpCodecSetClearChanMode based on Integer32"""
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


_AvSurvIpCodecSetClearChanMode_Type.__name__ = "Integer32"
_AvSurvIpCodecSetClearChanMode_Object = MibScalar
avSurvIpCodecSetClearChanMode = _AvSurvIpCodecSetClearChanMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 7),
    _AvSurvIpCodecSetClearChanMode_Type()
)
avSurvIpCodecSetClearChanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetClearChanMode.setStatus("current")


class _AvSurvIpCodecSetClearChanRedundancy_Type(Integer32):
    """Custom type avSurvIpCodecSetClearChanRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AvSurvIpCodecSetClearChanRedundancy_Type.__name__ = "Integer32"
_AvSurvIpCodecSetClearChanRedundancy_Object = MibScalar
avSurvIpCodecSetClearChanRedundancy = _AvSurvIpCodecSetClearChanRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 8),
    _AvSurvIpCodecSetClearChanRedundancy_Type()
)
avSurvIpCodecSetClearChanRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetClearChanRedundancy.setStatus("current")


class _AvSurvIpCodecSetEncryptPriority1_Type(Integer32):
    """Custom type avSurvIpCodecSetEncryptPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aea", 2),
          ("aes", 1),
          ("none", 3))
    )


_AvSurvIpCodecSetEncryptPriority1_Type.__name__ = "Integer32"
_AvSurvIpCodecSetEncryptPriority1_Object = MibScalar
avSurvIpCodecSetEncryptPriority1 = _AvSurvIpCodecSetEncryptPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 9),
    _AvSurvIpCodecSetEncryptPriority1_Type()
)
avSurvIpCodecSetEncryptPriority1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetEncryptPriority1.setStatus("current")


class _AvSurvIpCodecSetEncryptPriority2_Type(Integer32):
    """Custom type avSurvIpCodecSetEncryptPriority2 based on Integer32"""
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
        *(("aea", 2),
          ("aes", 1),
          ("none", 3),
          ("unused", 4))
    )


_AvSurvIpCodecSetEncryptPriority2_Type.__name__ = "Integer32"
_AvSurvIpCodecSetEncryptPriority2_Object = MibScalar
avSurvIpCodecSetEncryptPriority2 = _AvSurvIpCodecSetEncryptPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 10),
    _AvSurvIpCodecSetEncryptPriority2_Type()
)
avSurvIpCodecSetEncryptPriority2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetEncryptPriority2.setStatus("current")


class _AvSurvIpCodecSetEncryptPriority3_Type(Integer32):
    """Custom type avSurvIpCodecSetEncryptPriority3 based on Integer32"""
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
        *(("aea", 2),
          ("aes", 1),
          ("none", 3),
          ("unused", 4))
    )


_AvSurvIpCodecSetEncryptPriority3_Type.__name__ = "Integer32"
_AvSurvIpCodecSetEncryptPriority3_Object = MibScalar
avSurvIpCodecSetEncryptPriority3 = _AvSurvIpCodecSetEncryptPriority3_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 8, 11),
    _AvSurvIpCodecSetEncryptPriority3_Type()
)
avSurvIpCodecSetEncryptPriority3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIpCodecSetEncryptPriority3.setStatus("current")
_AvSurvSlotConfigTable_Object = MibTable
avSurvSlotConfigTable = _AvSurvSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 9)
)
if mibBuilder.loadTexts:
    avSurvSlotConfigTable.setStatus("current")
_AvSurvSlotConfigEntry_Object = MibTableRow
avSurvSlotConfigEntry = _AvSurvSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 9, 1)
)
avSurvSlotConfigEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvSlotConfigIndex"),
)
if mibBuilder.loadTexts:
    avSurvSlotConfigEntry.setStatus("current")


class _AvSurvSlotConfigIndex_Type(Integer32):
    """Custom type avSurvSlotConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AvSurvSlotConfigIndex_Type.__name__ = "Integer32"
_AvSurvSlotConfigIndex_Object = MibTableColumn
avSurvSlotConfigIndex = _AvSurvSlotConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 9, 1, 1),
    _AvSurvSlotConfigIndex_Type()
)
avSurvSlotConfigIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSlotConfigIndex.setStatus("current")


class _AvSurvSlotConfigNumberId_Type(DisplayString):
    """Custom type avSurvSlotConfigNumberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AvSurvSlotConfigNumberId_Type.__name__ = "DisplayString"
_AvSurvSlotConfigNumberId_Object = MibTableColumn
avSurvSlotConfigNumberId = _AvSurvSlotConfigNumberId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 9, 1, 2),
    _AvSurvSlotConfigNumberId_Type()
)
avSurvSlotConfigNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSlotConfigNumberId.setStatus("current")


class _AvSurvSlotConfigBoardType_Type(Integer32):
    """Custom type avSurvSlotConfigBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              7,
              8,
              9,
              14,
              16,
              17,
              18,
              19,
              22,
              23,
              24,
              25,
              26,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("anaImm1t2l", 9),
          ("anaImm4t2l", 16),
          ("briImm", 17),
          ("dcpImm", 18),
          ("ds1Imm", 19),
          ("mm312", 32),
          ("mm710", 5),
          ("mm711", 4),
          ("mm712", 3),
          ("mm714", 7),
          ("mm716", 22),
          ("mm717", 14),
          ("mm720", 2),
          ("mm722", 8),
          ("tgm550", 23),
          ("tim508", 29),
          ("tim510", 25),
          ("tim514", 24),
          ("tim516", 30),
          ("tim518", 31),
          ("tim521", 26))
    )


_AvSurvSlotConfigBoardType_Type.__name__ = "Integer32"
_AvSurvSlotConfigBoardType_Object = MibTableColumn
avSurvSlotConfigBoardType = _AvSurvSlotConfigBoardType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 9, 1, 3),
    _AvSurvSlotConfigBoardType_Type()
)
avSurvSlotConfigBoardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSlotConfigBoardType.setStatus("current")
_AvSurvSlotConfigRowStatus_Type = RowStatus
_AvSurvSlotConfigRowStatus_Object = MibTableColumn
avSurvSlotConfigRowStatus = _AvSurvSlotConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 9, 1, 4),
    _AvSurvSlotConfigRowStatus_Type()
)
avSurvSlotConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSlotConfigRowStatus.setStatus("current")
_AvSurvDs1Table_Object = MibTable
avSurvDs1Table = _AvSurvDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10)
)
if mibBuilder.loadTexts:
    avSurvDs1Table.setStatus("current")
_AvSurvDs1Entry_Object = MibTableRow
avSurvDs1Entry = _AvSurvDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1)
)
avSurvDs1Entry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvDs1Index"),
)
if mibBuilder.loadTexts:
    avSurvDs1Entry.setStatus("current")


class _AvSurvDs1Index_Type(Integer32):
    """Custom type avSurvDs1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AvSurvDs1Index_Type.__name__ = "Integer32"
_AvSurvDs1Index_Object = MibTableColumn
avSurvDs1Index = _AvSurvDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 1),
    _AvSurvDs1Index_Type()
)
avSurvDs1Index.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1Index.setStatus("current")


class _AvSurvDs1Name_Type(DisplayString):
    """Custom type avSurvDs1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AvSurvDs1Name_Type.__name__ = "DisplayString"
_AvSurvDs1Name_Object = MibTableColumn
avSurvDs1Name = _AvSurvDs1Name_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 2),
    _AvSurvDs1Name_Type()
)
avSurvDs1Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1Name.setStatus("current")


class _AvSurvDs1BitRate_Type(Integer32):
    """Custom type avSurvDs1BitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate1544", 1),
          ("rate2048", 2))
    )


_AvSurvDs1BitRate_Type.__name__ = "Integer32"
_AvSurvDs1BitRate_Object = MibTableColumn
avSurvDs1BitRate = _AvSurvDs1BitRate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 3),
    _AvSurvDs1BitRate_Type()
)
avSurvDs1BitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1BitRate.setStatus("current")


class _AvSurvDs1SignalingMode_Type(Integer32):
    """Custom type avSurvDs1SignalingMode based on Integer32"""
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
        *(("cas", 1),
          ("isdnExt", 4),
          ("isdnPri", 3),
          ("robbedBit", 2))
    )


_AvSurvDs1SignalingMode_Type.__name__ = "Integer32"
_AvSurvDs1SignalingMode_Object = MibTableColumn
avSurvDs1SignalingMode = _AvSurvDs1SignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 4),
    _AvSurvDs1SignalingMode_Type()
)
avSurvDs1SignalingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1SignalingMode.setStatus("current")


class _AvSurvDs1ChannelNumbering_Type(Integer32):
    """Custom type avSurvDs1ChannelNumbering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sequential", 1),
          ("timeSlot", 2))
    )


_AvSurvDs1ChannelNumbering_Type.__name__ = "Integer32"
_AvSurvDs1ChannelNumbering_Object = MibTableColumn
avSurvDs1ChannelNumbering = _AvSurvDs1ChannelNumbering_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 5),
    _AvSurvDs1ChannelNumbering_Type()
)
avSurvDs1ChannelNumbering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1ChannelNumbering.setStatus("current")


class _AvSurvDs1Connect_Type(Integer32):
    """Custom type avSurvDs1Connect based on Integer32"""
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
        *(("host", 1),
          ("lineSide", 4),
          ("network", 2),
          ("pbx", 3))
    )


_AvSurvDs1Connect_Type.__name__ = "Integer32"
_AvSurvDs1Connect_Object = MibTableColumn
avSurvDs1Connect = _AvSurvDs1Connect_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 6),
    _AvSurvDs1Connect_Type()
)
avSurvDs1Connect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1Connect.setStatus("current")


class _AvSurvDs1Interface_Type(Integer32):
    """Custom type avSurvDs1Interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("peerMaster", 3),
          ("peerSlave", 4),
          ("user", 0))
    )


_AvSurvDs1Interface_Type.__name__ = "Integer32"
_AvSurvDs1Interface_Object = MibTableColumn
avSurvDs1Interface = _AvSurvDs1Interface_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 7),
    _AvSurvDs1Interface_Type()
)
avSurvDs1Interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1Interface.setStatus("current")


class _AvSurvDs1Side_Type(Integer32):
    """Custom type avSurvDs1Side based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1))
    )


_AvSurvDs1Side_Type.__name__ = "Integer32"
_AvSurvDs1Side_Object = MibTableColumn
avSurvDs1Side = _AvSurvDs1Side_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 8),
    _AvSurvDs1Side_Type()
)
avSurvDs1Side.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1Side.setStatus("current")


class _AvSurvDs1CountryProtocol_Type(Integer32):
    """Custom type avSurvDs1CountryProtocol based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("country1", 1),
          ("country10", 10),
          ("country11", 11),
          ("country12", 12),
          ("country13", 13),
          ("country14", 14),
          ("country15", 15),
          ("country16", 16),
          ("country17", 17),
          ("country18", 18),
          ("country19", 19),
          ("country2", 2),
          ("country20", 20),
          ("country21", 21),
          ("country22", 22),
          ("country23", 23),
          ("country24", 24),
          ("country25", 25),
          ("country3", 3),
          ("country4", 4),
          ("country5", 5),
          ("country6", 6),
          ("country7", 7),
          ("country8", 8),
          ("country9", 9),
          ("etsi", 62),
          ("qsig", 63))
    )


_AvSurvDs1CountryProtocol_Type.__name__ = "Integer32"
_AvSurvDs1CountryProtocol_Object = MibTableColumn
avSurvDs1CountryProtocol = _AvSurvDs1CountryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 9),
    _AvSurvDs1CountryProtocol_Type()
)
avSurvDs1CountryProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1CountryProtocol.setStatus("current")


class _AvSurvDs1ProtocolVersion_Type(Integer32):
    """Custom type avSurvDs1ProtocolVersion based on Integer32"""
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
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3))
    )


_AvSurvDs1ProtocolVersion_Type.__name__ = "Integer32"
_AvSurvDs1ProtocolVersion_Object = MibTableColumn
avSurvDs1ProtocolVersion = _AvSurvDs1ProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 10),
    _AvSurvDs1ProtocolVersion_Type()
)
avSurvDs1ProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1ProtocolVersion.setStatus("current")


class _AvSurvDs1BearerCapability_Type(Integer32):
    """Custom type avSurvDs1BearerCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("speech", 1),
          ("threeKhz", 0))
    )


_AvSurvDs1BearerCapability_Type.__name__ = "Integer32"
_AvSurvDs1BearerCapability_Object = MibTableColumn
avSurvDs1BearerCapability = _AvSurvDs1BearerCapability_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 11),
    _AvSurvDs1BearerCapability_Type()
)
avSurvDs1BearerCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1BearerCapability.setStatus("current")


class _AvSurvDs1InterfaceCompanding_Type(Integer32):
    """Custom type avSurvDs1InterfaceCompanding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2))
    )


_AvSurvDs1InterfaceCompanding_Type.__name__ = "Integer32"
_AvSurvDs1InterfaceCompanding_Object = MibTableColumn
avSurvDs1InterfaceCompanding = _AvSurvDs1InterfaceCompanding_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 12),
    _AvSurvDs1InterfaceCompanding_Type()
)
avSurvDs1InterfaceCompanding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1InterfaceCompanding.setStatus("current")


class _AvSurvDs1LongTimer_Type(Integer32):
    """Custom type avSurvDs1LongTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AvSurvDs1LongTimer_Type.__name__ = "Integer32"
_AvSurvDs1LongTimer_Object = MibTableColumn
avSurvDs1LongTimer = _AvSurvDs1LongTimer_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 13),
    _AvSurvDs1LongTimer_Type()
)
avSurvDs1LongTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1LongTimer.setStatus("current")
_AvSurvDs1RowStatus_Type = RowStatus
_AvSurvDs1RowStatus_Object = MibTableColumn
avSurvDs1RowStatus = _AvSurvDs1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 14),
    _AvSurvDs1RowStatus_Type()
)
avSurvDs1RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1RowStatus.setStatus("current")


class _AvSurvDs1SlotNumberId_Type(DisplayString):
    """Custom type avSurvDs1SlotNumberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AvSurvDs1SlotNumberId_Type.__name__ = "DisplayString"
_AvSurvDs1SlotNumberId_Object = MibTableColumn
avSurvDs1SlotNumberId = _AvSurvDs1SlotNumberId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 10, 1, 15),
    _AvSurvDs1SlotNumberId_Type()
)
avSurvDs1SlotNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvDs1SlotNumberId.setStatus("current")
_AvSurvSigGroupTable_Object = MibTable
avSurvSigGroupTable = _AvSurvSigGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11)
)
if mibBuilder.loadTexts:
    avSurvSigGroupTable.setStatus("current")
_AvSurvSigGroupEntry_Object = MibTableRow
avSurvSigGroupEntry = _AvSurvSigGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11, 1)
)
avSurvSigGroupEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvSigGroupIndex"),
)
if mibBuilder.loadTexts:
    avSurvSigGroupEntry.setStatus("current")


class _AvSurvSigGroupIndex_Type(Integer32):
    """Custom type avSurvSigGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_AvSurvSigGroupIndex_Type.__name__ = "Integer32"
_AvSurvSigGroupIndex_Object = MibTableColumn
avSurvSigGroupIndex = _AvSurvSigGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11, 1, 1),
    _AvSurvSigGroupIndex_Type()
)
avSurvSigGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSigGroupIndex.setStatus("current")


class _AvSurvSigGroupChannelSelection_Type(Integer32):
    """Custom type avSurvSigGroupChannelSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_AvSurvSigGroupChannelSelection_Type.__name__ = "Integer32"
_AvSurvSigGroupChannelSelection_Object = MibTableColumn
avSurvSigGroupChannelSelection = _AvSurvSigGroupChannelSelection_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11, 1, 2),
    _AvSurvSigGroupChannelSelection_Type()
)
avSurvSigGroupChannelSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSigGroupChannelSelection.setStatus("current")


class _AvSurvSigGroupAssociatedSignaling_Type(Integer32):
    """Custom type avSurvSigGroupAssociatedSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvSigGroupAssociatedSignaling_Type.__name__ = "Integer32"
_AvSurvSigGroupAssociatedSignaling_Object = MibTableColumn
avSurvSigGroupAssociatedSignaling = _AvSurvSigGroupAssociatedSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11, 1, 3),
    _AvSurvSigGroupAssociatedSignaling_Type()
)
avSurvSigGroupAssociatedSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSigGroupAssociatedSignaling.setStatus("current")


class _AvSurvSigGroupPrimaryDChannel_Type(DisplayString):
    """Custom type avSurvSigGroupPrimaryDChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_AvSurvSigGroupPrimaryDChannel_Type.__name__ = "DisplayString"
_AvSurvSigGroupPrimaryDChannel_Object = MibTableColumn
avSurvSigGroupPrimaryDChannel = _AvSurvSigGroupPrimaryDChannel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11, 1, 4),
    _AvSurvSigGroupPrimaryDChannel_Type()
)
avSurvSigGroupPrimaryDChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSigGroupPrimaryDChannel.setStatus("current")
_AvSurvSigGroupRowStatus_Type = RowStatus
_AvSurvSigGroupRowStatus_Object = MibTableColumn
avSurvSigGroupRowStatus = _AvSurvSigGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 11, 1, 5),
    _AvSurvSigGroupRowStatus_Type()
)
avSurvSigGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvSigGroupRowStatus.setStatus("current")
_AvSurvBriTable_Object = MibTable
avSurvBriTable = _AvSurvBriTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12)
)
if mibBuilder.loadTexts:
    avSurvBriTable.setStatus("current")
_AvSurvBriEntry_Object = MibTableRow
avSurvBriEntry = _AvSurvBriEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1)
)
avSurvBriEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvBriIndex"),
)
if mibBuilder.loadTexts:
    avSurvBriEntry.setStatus("current")


class _AvSurvBriIndex_Type(Integer32):
    """Custom type avSurvBriIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AvSurvBriIndex_Type.__name__ = "Integer32"
_AvSurvBriIndex_Object = MibTableColumn
avSurvBriIndex = _AvSurvBriIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 1),
    _AvSurvBriIndex_Type()
)
avSurvBriIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriIndex.setStatus("current")


class _AvSurvBriName_Type(DisplayString):
    """Custom type avSurvBriName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AvSurvBriName_Type.__name__ = "DisplayString"
_AvSurvBriName_Object = MibTableColumn
avSurvBriName = _AvSurvBriName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 2),
    _AvSurvBriName_Type()
)
avSurvBriName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriName.setStatus("current")


class _AvSurvBriInterface_Type(Integer32):
    """Custom type avSurvBriInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("peerMaster", 3),
          ("peerSlave", 4),
          ("user", 0))
    )


_AvSurvBriInterface_Type.__name__ = "Integer32"
_AvSurvBriInterface_Object = MibTableColumn
avSurvBriInterface = _AvSurvBriInterface_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 3),
    _AvSurvBriInterface_Type()
)
avSurvBriInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriInterface.setStatus("current")


class _AvSurvBriSide_Type(Integer32):
    """Custom type avSurvBriSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1))
    )


_AvSurvBriSide_Type.__name__ = "Integer32"
_AvSurvBriSide_Object = MibTableColumn
avSurvBriSide = _AvSurvBriSide_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 4),
    _AvSurvBriSide_Type()
)
avSurvBriSide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriSide.setStatus("current")


class _AvSurvBriCountryProtocol_Type(Integer32):
    """Custom type avSurvBriCountryProtocol based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("country1", 1),
          ("country10", 10),
          ("country11", 11),
          ("country12", 12),
          ("country13", 13),
          ("country14", 14),
          ("country15", 15),
          ("country16", 16),
          ("country17", 17),
          ("country18", 18),
          ("country19", 19),
          ("country2", 2),
          ("country20", 20),
          ("country21", 21),
          ("country22", 22),
          ("country23", 23),
          ("country24", 24),
          ("country25", 25),
          ("country3", 3),
          ("country4", 4),
          ("country5", 5),
          ("country6", 6),
          ("country7", 7),
          ("country8", 8),
          ("country9", 9),
          ("etsi", 62),
          ("qsig", 63))
    )


_AvSurvBriCountryProtocol_Type.__name__ = "Integer32"
_AvSurvBriCountryProtocol_Object = MibTableColumn
avSurvBriCountryProtocol = _AvSurvBriCountryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 5),
    _AvSurvBriCountryProtocol_Type()
)
avSurvBriCountryProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriCountryProtocol.setStatus("current")


class _AvSurvBriBearerCapability_Type(Integer32):
    """Custom type avSurvBriBearerCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("speech", 1),
          ("threeKhz", 0))
    )


_AvSurvBriBearerCapability_Type.__name__ = "Integer32"
_AvSurvBriBearerCapability_Object = MibTableColumn
avSurvBriBearerCapability = _AvSurvBriBearerCapability_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 6),
    _AvSurvBriBearerCapability_Type()
)
avSurvBriBearerCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriBearerCapability.setStatus("current")


class _AvSurvBriInterfaceCompanding_Type(Integer32):
    """Custom type avSurvBriInterfaceCompanding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2))
    )


_AvSurvBriInterfaceCompanding_Type.__name__ = "Integer32"
_AvSurvBriInterfaceCompanding_Object = MibTableColumn
avSurvBriInterfaceCompanding = _AvSurvBriInterfaceCompanding_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 7),
    _AvSurvBriInterfaceCompanding_Type()
)
avSurvBriInterfaceCompanding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriInterfaceCompanding.setStatus("current")


class _AvSurvBriTeiAssignment_Type(Integer32):
    """Custom type avSurvBriTeiAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("zero", 2))
    )


_AvSurvBriTeiAssignment_Type.__name__ = "Integer32"
_AvSurvBriTeiAssignment_Object = MibTableColumn
avSurvBriTeiAssignment = _AvSurvBriTeiAssignment_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 8),
    _AvSurvBriTeiAssignment_Type()
)
avSurvBriTeiAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriTeiAssignment.setStatus("current")


class _AvSurvBriDirectoryNumberA_Type(DisplayString):
    """Custom type avSurvBriDirectoryNumberA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AvSurvBriDirectoryNumberA_Type.__name__ = "DisplayString"
_AvSurvBriDirectoryNumberA_Object = MibTableColumn
avSurvBriDirectoryNumberA = _AvSurvBriDirectoryNumberA_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 9),
    _AvSurvBriDirectoryNumberA_Type()
)
avSurvBriDirectoryNumberA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriDirectoryNumberA.setStatus("current")


class _AvSurvBriDirectoryNumberB_Type(DisplayString):
    """Custom type avSurvBriDirectoryNumberB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AvSurvBriDirectoryNumberB_Type.__name__ = "DisplayString"
_AvSurvBriDirectoryNumberB_Object = MibTableColumn
avSurvBriDirectoryNumberB = _AvSurvBriDirectoryNumberB_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 10),
    _AvSurvBriDirectoryNumberB_Type()
)
avSurvBriDirectoryNumberB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriDirectoryNumberB.setStatus("current")


class _AvSurvBriSpidA_Type(DisplayString):
    """Custom type avSurvBriSpidA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AvSurvBriSpidA_Type.__name__ = "DisplayString"
_AvSurvBriSpidA_Object = MibTableColumn
avSurvBriSpidA = _AvSurvBriSpidA_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 11),
    _AvSurvBriSpidA_Type()
)
avSurvBriSpidA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriSpidA.setStatus("current")


class _AvSurvBriSpidB_Type(DisplayString):
    """Custom type avSurvBriSpidB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AvSurvBriSpidB_Type.__name__ = "DisplayString"
_AvSurvBriSpidB_Object = MibTableColumn
avSurvBriSpidB = _AvSurvBriSpidB_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 12),
    _AvSurvBriSpidB_Type()
)
avSurvBriSpidB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriSpidB.setStatus("current")


class _AvSurvBriEndpointInit_Type(Integer32):
    """Custom type avSurvBriEndpointInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvBriEndpointInit_Type.__name__ = "Integer32"
_AvSurvBriEndpointInit_Object = MibTableColumn
avSurvBriEndpointInit = _AvSurvBriEndpointInit_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 13),
    _AvSurvBriEndpointInit_Type()
)
avSurvBriEndpointInit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriEndpointInit.setStatus("current")


class _AvSurvBriLayer1Stable_Type(Integer32):
    """Custom type avSurvBriLayer1Stable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AvSurvBriLayer1Stable_Type.__name__ = "Integer32"
_AvSurvBriLayer1Stable_Object = MibTableColumn
avSurvBriLayer1Stable = _AvSurvBriLayer1Stable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 14),
    _AvSurvBriLayer1Stable_Type()
)
avSurvBriLayer1Stable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriLayer1Stable.setStatus("current")
_AvSurvBriRowStatus_Type = RowStatus
_AvSurvBriRowStatus_Object = MibTableColumn
avSurvBriRowStatus = _AvSurvBriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 15),
    _AvSurvBriRowStatus_Type()
)
avSurvBriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriRowStatus.setStatus("current")


class _AvSurvBriSlotPortNumberId_Type(DisplayString):
    """Custom type avSurvBriSlotPortNumberId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AvSurvBriSlotPortNumberId_Type.__name__ = "DisplayString"
_AvSurvBriSlotPortNumberId_Object = MibTableColumn
avSurvBriSlotPortNumberId = _AvSurvBriSlotPortNumberId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 12, 1, 16),
    _AvSurvBriSlotPortNumberId_Type()
)
avSurvBriSlotPortNumberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvBriSlotPortNumberId.setStatus("current")
_AvSurvIncomingRoutingTable_Object = MibTable
avSurvIncomingRoutingTable = _AvSurvIncomingRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13)
)
if mibBuilder.loadTexts:
    avSurvIncomingRoutingTable.setStatus("current")
_AvSurvIncomingRoutingEntry_Object = MibTableRow
avSurvIncomingRoutingEntry = _AvSurvIncomingRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1)
)
avSurvIncomingRoutingEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvIncomingRoutingGroupRefNumber"),
    (0, "AVAYA-SURV-MIB", "avSurvIncomingRoutingIndex"),
)
if mibBuilder.loadTexts:
    avSurvIncomingRoutingEntry.setStatus("current")


class _AvSurvIncomingRoutingGroupRefNumber_Type(Integer32):
    """Custom type avSurvIncomingRoutingGroupRefNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_AvSurvIncomingRoutingGroupRefNumber_Type.__name__ = "Integer32"
_AvSurvIncomingRoutingGroupRefNumber_Object = MibTableColumn
avSurvIncomingRoutingGroupRefNumber = _AvSurvIncomingRoutingGroupRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 1),
    _AvSurvIncomingRoutingGroupRefNumber_Type()
)
avSurvIncomingRoutingGroupRefNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingGroupRefNumber.setStatus("current")


class _AvSurvIncomingRoutingIndex_Type(Integer32):
    """Custom type avSurvIncomingRoutingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AvSurvIncomingRoutingIndex_Type.__name__ = "Integer32"
_AvSurvIncomingRoutingIndex_Object = MibTableColumn
avSurvIncomingRoutingIndex = _AvSurvIncomingRoutingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 2),
    _AvSurvIncomingRoutingIndex_Type()
)
avSurvIncomingRoutingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingIndex.setStatus("current")


class _AvSurvIncomingRoutingMatchPattern_Type(DisplayString):
    """Custom type avSurvIncomingRoutingMatchPattern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AvSurvIncomingRoutingMatchPattern_Type.__name__ = "DisplayString"
_AvSurvIncomingRoutingMatchPattern_Object = MibTableColumn
avSurvIncomingRoutingMatchPattern = _AvSurvIncomingRoutingMatchPattern_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 3),
    _AvSurvIncomingRoutingMatchPattern_Type()
)
avSurvIncomingRoutingMatchPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingMatchPattern.setStatus("current")


class _AvSurvIncomingRoutingLength_Type(Integer32):
    """Custom type avSurvIncomingRoutingLength based on Integer32"""
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
              20,
              21,
              99)
        )
    )
    namedValues = NamedValues(
        *(("blank", 99),
          ("len0", 0),
          ("len1", 1),
          ("len10", 10),
          ("len11", 11),
          ("len12", 12),
          ("len13", 13),
          ("len14", 14),
          ("len15", 15),
          ("len16", 16),
          ("len17", 17),
          ("len18", 18),
          ("len19", 19),
          ("len2", 2),
          ("len20", 20),
          ("len21", 21),
          ("len3", 3),
          ("len4", 4),
          ("len5", 5),
          ("len6", 6),
          ("len7", 7),
          ("len8", 8),
          ("len9", 9))
    )


_AvSurvIncomingRoutingLength_Type.__name__ = "Integer32"
_AvSurvIncomingRoutingLength_Object = MibTableColumn
avSurvIncomingRoutingLength = _AvSurvIncomingRoutingLength_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 4),
    _AvSurvIncomingRoutingLength_Type()
)
avSurvIncomingRoutingLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingLength.setStatus("current")


class _AvSurvIncomingRoutingDeleteDigits_Type(Integer32):
    """Custom type avSurvIncomingRoutingDeleteDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_AvSurvIncomingRoutingDeleteDigits_Type.__name__ = "Integer32"
_AvSurvIncomingRoutingDeleteDigits_Object = MibTableColumn
avSurvIncomingRoutingDeleteDigits = _AvSurvIncomingRoutingDeleteDigits_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 5),
    _AvSurvIncomingRoutingDeleteDigits_Type()
)
avSurvIncomingRoutingDeleteDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingDeleteDigits.setStatus("current")


class _AvSurvIncomingRoutingInsertDigits_Type(DisplayString):
    """Custom type avSurvIncomingRoutingInsertDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AvSurvIncomingRoutingInsertDigits_Type.__name__ = "DisplayString"
_AvSurvIncomingRoutingInsertDigits_Object = MibTableColumn
avSurvIncomingRoutingInsertDigits = _AvSurvIncomingRoutingInsertDigits_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 6),
    _AvSurvIncomingRoutingInsertDigits_Type()
)
avSurvIncomingRoutingInsertDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingInsertDigits.setStatus("current")


class _AvSurvIncomingRoutingMode_Type(Integer32):
    """Custom type avSurvIncomingRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enbloc", 0),
          ("overlap", 1))
    )


_AvSurvIncomingRoutingMode_Type.__name__ = "Integer32"
_AvSurvIncomingRoutingMode_Object = MibTableColumn
avSurvIncomingRoutingMode = _AvSurvIncomingRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 7),
    _AvSurvIncomingRoutingMode_Type()
)
avSurvIncomingRoutingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingMode.setStatus("current")
_AvSurvIncomingRoutingRowStatus_Type = RowStatus
_AvSurvIncomingRoutingRowStatus_Object = MibTableColumn
avSurvIncomingRoutingRowStatus = _AvSurvIncomingRoutingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 13, 1, 8),
    _AvSurvIncomingRoutingRowStatus_Type()
)
avSurvIncomingRoutingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvIncomingRoutingRowStatus.setStatus("current")
_AvSurvNfasTable_Object = MibTable
avSurvNfasTable = _AvSurvNfasTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14)
)
if mibBuilder.loadTexts:
    avSurvNfasTable.setStatus("current")
_AvSurvNfasEntry_Object = MibTableRow
avSurvNfasEntry = _AvSurvNfasEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14, 1)
)
avSurvNfasEntry.setIndexNames(
    (0, "AVAYA-SURV-MIB", "avSurvNfasSigGroupRefNumber"),
    (0, "AVAYA-SURV-MIB", "avSurvNfasIndex"),
)
if mibBuilder.loadTexts:
    avSurvNfasEntry.setStatus("current")


class _AvSurvNfasSigGroupRefNumber_Type(Integer32):
    """Custom type avSurvNfasSigGroupRefNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_AvSurvNfasSigGroupRefNumber_Type.__name__ = "Integer32"
_AvSurvNfasSigGroupRefNumber_Object = MibTableColumn
avSurvNfasSigGroupRefNumber = _AvSurvNfasSigGroupRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14, 1, 1),
    _AvSurvNfasSigGroupRefNumber_Type()
)
avSurvNfasSigGroupRefNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvNfasSigGroupRefNumber.setStatus("current")


class _AvSurvNfasIndex_Type(Integer32):
    """Custom type avSurvNfasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AvSurvNfasIndex_Type.__name__ = "Integer32"
_AvSurvNfasIndex_Object = MibTableColumn
avSurvNfasIndex = _AvSurvNfasIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14, 1, 2),
    _AvSurvNfasIndex_Type()
)
avSurvNfasIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvNfasIndex.setStatus("current")


class _AvSurvNfasInterface_Type(DisplayString):
    """Custom type avSurvNfasInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_AvSurvNfasInterface_Type.__name__ = "DisplayString"
_AvSurvNfasInterface_Object = MibTableColumn
avSurvNfasInterface = _AvSurvNfasInterface_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14, 1, 3),
    _AvSurvNfasInterface_Type()
)
avSurvNfasInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvNfasInterface.setStatus("current")


class _AvSurvNfasInterfaceId_Type(Integer32):
    """Custom type avSurvNfasInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AvSurvNfasInterfaceId_Type.__name__ = "Integer32"
_AvSurvNfasInterfaceId_Object = MibTableColumn
avSurvNfasInterfaceId = _AvSurvNfasInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14, 1, 4),
    _AvSurvNfasInterfaceId_Type()
)
avSurvNfasInterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvNfasInterfaceId.setStatus("current")
_AvSurvNfasRowStatus_Type = RowStatus
_AvSurvNfasRowStatus_Object = MibTableColumn
avSurvNfasRowStatus = _AvSurvNfasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 14, 1, 5),
    _AvSurvNfasRowStatus_Type()
)
avSurvNfasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avSurvNfasRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

avSurvEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 0, 1)
)
avSurvEnabled.setObjects(
    ("AVAYA-SURV-MIB", "avSurvNotificationSeverity")
)
if mibBuilder.loadTexts:
    avSurvEnabled.setStatus(
        "current"
    )

avSurvDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 0, 2)
)
avSurvDisabled.setObjects(
    ("AVAYA-SURV-MIB", "avSurvNotificationSeverity")
)
if mibBuilder.loadTexts:
    avSurvDisabled.setStatus(
        "current"
    )

avSurvActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 0, 3)
)
avSurvActive.setObjects(
    ("AVAYA-SURV-MIB", "avSurvNotificationSeverity")
)
if mibBuilder.loadTexts:
    avSurvActive.setStatus(
        "current"
    )

avSurvInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 4, 0, 4)
)
avSurvInactive.setObjects(
    ("AVAYA-SURV-MIB", "avSurvNotificationSeverity")
)
if mibBuilder.loadTexts:
    avSurvInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-SURV-MIB",
    **{"avSurvMib": avSurvMib,
       "avSurvNotification": avSurvNotification,
       "avSurvEnabled": avSurvEnabled,
       "avSurvDisabled": avSurvDisabled,
       "avSurvActive": avSurvActive,
       "avSurvInactive": avSurvInactive,
       "avSurvConfig": avSurvConfig,
       "avSurvAdminState": avSurvAdminState,
       "avSurvStatus": avSurvStatus,
       "avSurvMaxIPReg": avSurvMaxIPReg,
       "avSurvDateFormat": avSurvDateFormat,
       "avSurvEndDLTimeStamp": avSurvEndDLTimeStamp,
       "avSurvNotificationSeverity": avSurvNotificationSeverity,
       "avSurvConfigCommand": avSurvConfigCommand,
       "avSurvGatewayNumber": avSurvGatewayNumber,
       "avSurvPimLockout": avSurvPimLockout,
       "avSurvAttendantAccessCode": avSurvAttendantAccessCode,
       "avSurvAttendantExtension": avSurvAttendantExtension,
       "avSurvStationTable": avSurvStationTable,
       "avSurvStationEntry": avSurvStationEntry,
       "avSurvStationIndex": avSurvStationIndex,
       "avSurvStationExt": avSurvStationExt,
       "avSurvStationType": avSurvStationType,
       "avSurvStationInterfaceIndex": avSurvStationInterfaceIndex,
       "avSurvStationCOR": avSurvStationCOR,
       "avSurvStationTrunkDest": avSurvStationTrunkDest,
       "avSurvStationRowStatus": avSurvStationRowStatus,
       "avSurvStationExpansionModule": avSurvStationExpansionModule,
       "avSurvStationSlotPort": avSurvStationSlotPort,
       "avSurvStationSwitchHookFlash": avSurvStationSwitchHookFlash,
       "avSurvStationIpAddressRegistered": avSurvStationIpAddressRegistered,
       "avSurvStationName": avSurvStationName,
       "avSurvTrunkGroupTable": avSurvTrunkGroupTable,
       "avSurvTrunkGroupEntry": avSurvTrunkGroupEntry,
       "avSurvTrunkGroupNum": avSurvTrunkGroupNum,
       "avSurvTrunkGroupType": avSurvTrunkGroupType,
       "avSurvTrunkGroupTAC": avSurvTrunkGroupTAC,
       "avSurvTrunkGroupDial": avSurvTrunkGroupDial,
       "avSurvTrunkGroupRowStatus": avSurvTrunkGroupRowStatus,
       "avSurvTrunkGroupDidDigitTreatment": avSurvTrunkGroupDidDigitTreatment,
       "avSurvTrunkGroupDidDigitsInsert": avSurvTrunkGroupDidDigitsInsert,
       "avSurvTrunkGroupDidSupervision": avSurvTrunkGroupDidSupervision,
       "avSurvTrunkGroupName": avSurvTrunkGroupName,
       "avSurvTrunkGroupCodesetDisplay": avSurvTrunkGroupCodesetDisplay,
       "avSurvTrunkGroupCodesetNational": avSurvTrunkGroupCodesetNational,
       "avSurvTrunkGroupChannelPreference": avSurvTrunkGroupChannelPreference,
       "avSurvTrunkGroupDigitHandling": avSurvTrunkGroupDigitHandling,
       "avSurvTrunkGroupJapanDisconnect": avSurvTrunkGroupJapanDisconnect,
       "avSurvTrunkGroupSendName": avSurvTrunkGroupSendName,
       "avSurvTrunkGroupSendCallingNumber": avSurvTrunkGroupSendCallingNumber,
       "avSurvTrunkGroupNumberingFormat": avSurvTrunkGroupNumberingFormat,
       "avSurvTrunkGroupIncomingDestination": avSurvTrunkGroupIncomingDestination,
       "avSurvTrunkGroupIncomingDialTone": avSurvTrunkGroupIncomingDialTone,
       "avSurvTrunkGroupR2MFCSignaling": avSurvTrunkGroupR2MFCSignaling,
       "avSurvTrunkGroupTrunkHunt": avSurvTrunkGroupTrunkHunt,
       "avSurvTrunkGroupDs1Supervision": avSurvTrunkGroupDs1Supervision,
       "avSurvTrunkGroupCbc": avSurvTrunkGroupCbc,
       "avSurvTrunkGroupCbcServiceFeature": avSurvTrunkGroupCbcServiceFeature,
       "avSurvTrunkGroupCbcParameter": avSurvTrunkGroupCbcParameter,
       "avSurvTrunkGroupBusyDisconnect": avSurvTrunkGroupBusyDisconnect,
       "avSurvTrunkTable": avSurvTrunkTable,
       "avSurvTrunkEntry": avSurvTrunkEntry,
       "avSurvTrunkGroupRefNumber": avSurvTrunkGroupRefNumber,
       "avSurvTrunkIndex": avSurvTrunkIndex,
       "avSurvTrunkInterfaceIndex": avSurvTrunkInterfaceIndex,
       "avSurvTrunkRowStatus": avSurvTrunkRowStatus,
       "avSurvTrunkSlotPort": avSurvTrunkSlotPort,
       "avSurvTrunkSigGroupRefNumber": avSurvTrunkSigGroupRefNumber,
       "avSurvArsTable": avSurvArsTable,
       "avSurvArsEntry": avSurvArsEntry,
       "avSurvDialIndex": avSurvDialIndex,
       "avSurvDialString": avSurvDialString,
       "avSurvDialType": avSurvDialType,
       "avSurvDialMaximumLength": avSurvDialMaximumLength,
       "avSurvDialGroupRefNumber": avSurvDialGroupRefNumber,
       "avSurvDialAction": avSurvDialAction,
       "avSurvDialRowStatus": avSurvDialRowStatus,
       "avSurvDialDeleteDigits": avSurvDialDeleteDigits,
       "avSurvDialInsertDigits": avSurvDialInsertDigits,
       "avSurvDialMinimumLength": avSurvDialMinimumLength,
       "avSurvFacTable": avSurvFacTable,
       "avSurvFacEntry": avSurvFacEntry,
       "avSurvFacIndex": avSurvFacIndex,
       "avSurvFacId": avSurvFacId,
       "avSurvFacRowStatus": avSurvFacRowStatus,
       "avSurvFacType": avSurvFacType,
       "avSurvIpVoiceCodecSetTable": avSurvIpVoiceCodecSetTable,
       "avSurvIpVoiceCodecSetEntry": avSurvIpVoiceCodecSetEntry,
       "avSurvIpVoiceCodecSetNum": avSurvIpVoiceCodecSetNum,
       "avSurvIpVoiceCodecSetIndex": avSurvIpVoiceCodecSetIndex,
       "avSurvIpVoiceCodecSetPriority": avSurvIpVoiceCodecSetPriority,
       "avSurvIpVoiceCodecSetType": avSurvIpVoiceCodecSetType,
       "avSurvIpVoiceCodecSetSilence": avSurvIpVoiceCodecSetSilence,
       "avSurvIpVoiceCodecSetFrames": avSurvIpVoiceCodecSetFrames,
       "avSurvIpVoiceCodecSetRowStatus": avSurvIpVoiceCodecSetRowStatus,
       "avSurvIpCodecSetConfig": avSurvIpCodecSetConfig,
       "avSurvIpCodecSetFaxMode": avSurvIpCodecSetFaxMode,
       "avSurvIpCodecSetFaxRedundancy": avSurvIpCodecSetFaxRedundancy,
       "avSurvIpCodecSetModemMode": avSurvIpCodecSetModemMode,
       "avSurvIpCodecSetModemRedundancy": avSurvIpCodecSetModemRedundancy,
       "avSurvIpCodecSetTtyMode": avSurvIpCodecSetTtyMode,
       "avSurvIpCodecSetTtyRedundancy": avSurvIpCodecSetTtyRedundancy,
       "avSurvIpCodecSetClearChanMode": avSurvIpCodecSetClearChanMode,
       "avSurvIpCodecSetClearChanRedundancy": avSurvIpCodecSetClearChanRedundancy,
       "avSurvIpCodecSetEncryptPriority1": avSurvIpCodecSetEncryptPriority1,
       "avSurvIpCodecSetEncryptPriority2": avSurvIpCodecSetEncryptPriority2,
       "avSurvIpCodecSetEncryptPriority3": avSurvIpCodecSetEncryptPriority3,
       "avSurvSlotConfigTable": avSurvSlotConfigTable,
       "avSurvSlotConfigEntry": avSurvSlotConfigEntry,
       "avSurvSlotConfigIndex": avSurvSlotConfigIndex,
       "avSurvSlotConfigNumberId": avSurvSlotConfigNumberId,
       "avSurvSlotConfigBoardType": avSurvSlotConfigBoardType,
       "avSurvSlotConfigRowStatus": avSurvSlotConfigRowStatus,
       "avSurvDs1Table": avSurvDs1Table,
       "avSurvDs1Entry": avSurvDs1Entry,
       "avSurvDs1Index": avSurvDs1Index,
       "avSurvDs1Name": avSurvDs1Name,
       "avSurvDs1BitRate": avSurvDs1BitRate,
       "avSurvDs1SignalingMode": avSurvDs1SignalingMode,
       "avSurvDs1ChannelNumbering": avSurvDs1ChannelNumbering,
       "avSurvDs1Connect": avSurvDs1Connect,
       "avSurvDs1Interface": avSurvDs1Interface,
       "avSurvDs1Side": avSurvDs1Side,
       "avSurvDs1CountryProtocol": avSurvDs1CountryProtocol,
       "avSurvDs1ProtocolVersion": avSurvDs1ProtocolVersion,
       "avSurvDs1BearerCapability": avSurvDs1BearerCapability,
       "avSurvDs1InterfaceCompanding": avSurvDs1InterfaceCompanding,
       "avSurvDs1LongTimer": avSurvDs1LongTimer,
       "avSurvDs1RowStatus": avSurvDs1RowStatus,
       "avSurvDs1SlotNumberId": avSurvDs1SlotNumberId,
       "avSurvSigGroupTable": avSurvSigGroupTable,
       "avSurvSigGroupEntry": avSurvSigGroupEntry,
       "avSurvSigGroupIndex": avSurvSigGroupIndex,
       "avSurvSigGroupChannelSelection": avSurvSigGroupChannelSelection,
       "avSurvSigGroupAssociatedSignaling": avSurvSigGroupAssociatedSignaling,
       "avSurvSigGroupPrimaryDChannel": avSurvSigGroupPrimaryDChannel,
       "avSurvSigGroupRowStatus": avSurvSigGroupRowStatus,
       "avSurvBriTable": avSurvBriTable,
       "avSurvBriEntry": avSurvBriEntry,
       "avSurvBriIndex": avSurvBriIndex,
       "avSurvBriName": avSurvBriName,
       "avSurvBriInterface": avSurvBriInterface,
       "avSurvBriSide": avSurvBriSide,
       "avSurvBriCountryProtocol": avSurvBriCountryProtocol,
       "avSurvBriBearerCapability": avSurvBriBearerCapability,
       "avSurvBriInterfaceCompanding": avSurvBriInterfaceCompanding,
       "avSurvBriTeiAssignment": avSurvBriTeiAssignment,
       "avSurvBriDirectoryNumberA": avSurvBriDirectoryNumberA,
       "avSurvBriDirectoryNumberB": avSurvBriDirectoryNumberB,
       "avSurvBriSpidA": avSurvBriSpidA,
       "avSurvBriSpidB": avSurvBriSpidB,
       "avSurvBriEndpointInit": avSurvBriEndpointInit,
       "avSurvBriLayer1Stable": avSurvBriLayer1Stable,
       "avSurvBriRowStatus": avSurvBriRowStatus,
       "avSurvBriSlotPortNumberId": avSurvBriSlotPortNumberId,
       "avSurvIncomingRoutingTable": avSurvIncomingRoutingTable,
       "avSurvIncomingRoutingEntry": avSurvIncomingRoutingEntry,
       "avSurvIncomingRoutingGroupRefNumber": avSurvIncomingRoutingGroupRefNumber,
       "avSurvIncomingRoutingIndex": avSurvIncomingRoutingIndex,
       "avSurvIncomingRoutingMatchPattern": avSurvIncomingRoutingMatchPattern,
       "avSurvIncomingRoutingLength": avSurvIncomingRoutingLength,
       "avSurvIncomingRoutingDeleteDigits": avSurvIncomingRoutingDeleteDigits,
       "avSurvIncomingRoutingInsertDigits": avSurvIncomingRoutingInsertDigits,
       "avSurvIncomingRoutingMode": avSurvIncomingRoutingMode,
       "avSurvIncomingRoutingRowStatus": avSurvIncomingRoutingRowStatus,
       "avSurvNfasTable": avSurvNfasTable,
       "avSurvNfasEntry": avSurvNfasEntry,
       "avSurvNfasSigGroupRefNumber": avSurvNfasSigGroupRefNumber,
       "avSurvNfasIndex": avSurvNfasIndex,
       "avSurvNfasInterface": avSurvNfasInterface,
       "avSurvNfasInterfaceId": avSurvNfasInterfaceId,
       "avSurvNfasRowStatus": avSurvNfasRowStatus}
)
