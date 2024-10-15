# SNMP MIB module (ZTE-UAS-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZTE-UAS-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:50 2024
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

zxMulticastMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxUas_ObjectIdentity = ObjectIdentity
zxUas = _ZxUas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006)
)
_ZxUasMulticastMibObjects_ObjectIdentity = ObjectIdentity
zxUasMulticastMibObjects = _ZxUasMulticastMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1)
)


class _ZxUasMulticastSwitch_Type(Integer32):
    """Custom type zxUasMulticastSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxUasMulticastSwitch_Type.__name__ = "Integer32"
_ZxUasMulticastSwitch_Object = MibScalar
zxUasMulticastSwitch = _ZxUasMulticastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 1),
    _ZxUasMulticastSwitch_Type()
)
zxUasMulticastSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasMulticastSwitch.setStatus("current")
_ZxIgmpGroup_ObjectIdentity = ObjectIdentity
zxIgmpGroup = _ZxIgmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2)
)
_ZxIgmpGroupTable_Object = MibTable
zxIgmpGroupTable = _ZxIgmpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxIgmpGroupTable.setStatus("current")
_ZxIgmpGroupEntry_Object = MibTableRow
zxIgmpGroupEntry = _ZxIgmpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1)
)
zxIgmpGroupEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpGroupAddr"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpGroupInterface"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpGroupLastReporterCircuit"),
)
if mibBuilder.loadTexts:
    zxIgmpGroupEntry.setStatus("current")
_ZxIgmpGroupAddr_Type = IpAddress
_ZxIgmpGroupAddr_Object = MibTableColumn
zxIgmpGroupAddr = _ZxIgmpGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1, 1),
    _ZxIgmpGroupAddr_Type()
)
zxIgmpGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpGroupAddr.setStatus("current")


class _ZxIgmpGroupInterface_Type(DisplayString):
    """Custom type zxIgmpGroupInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxIgmpGroupInterface_Type.__name__ = "DisplayString"
_ZxIgmpGroupInterface_Object = MibTableColumn
zxIgmpGroupInterface = _ZxIgmpGroupInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1, 2),
    _ZxIgmpGroupInterface_Type()
)
zxIgmpGroupInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpGroupInterface.setStatus("current")


class _ZxIgmpGroupFlag_Type(Integer32):
    """Custom type zxIgmpGroupFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ppp", 1))
    )


_ZxIgmpGroupFlag_Type.__name__ = "Integer32"
_ZxIgmpGroupFlag_Object = MibTableColumn
zxIgmpGroupFlag = _ZxIgmpGroupFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1, 3),
    _ZxIgmpGroupFlag_Type()
)
zxIgmpGroupFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpGroupFlag.setStatus("current")
_ZxIgmpGroupPresent_Type = DisplayString
_ZxIgmpGroupPresent_Object = MibTableColumn
zxIgmpGroupPresent = _ZxIgmpGroupPresent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1, 4),
    _ZxIgmpGroupPresent_Type()
)
zxIgmpGroupPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpGroupPresent.setStatus("current")
_ZxIgmpGroupExpire_Type = DisplayString
_ZxIgmpGroupExpire_Object = MibTableColumn
zxIgmpGroupExpire = _ZxIgmpGroupExpire_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1, 5),
    _ZxIgmpGroupExpire_Type()
)
zxIgmpGroupExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpGroupExpire.setStatus("current")
_ZxIgmpGroupLastReporterCircuit_Type = DisplayString
_ZxIgmpGroupLastReporterCircuit_Object = MibTableColumn
zxIgmpGroupLastReporterCircuit = _ZxIgmpGroupLastReporterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 1, 1, 6),
    _ZxIgmpGroupLastReporterCircuit_Type()
)
zxIgmpGroupLastReporterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpGroupLastReporterCircuit.setStatus("current")
_ZxIgmpInterfaceTable_Object = MibTable
zxIgmpInterfaceTable = _ZxIgmpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxIgmpInterfaceTable.setStatus("current")
_ZxIgmpInterfaceEntry_Object = MibTableRow
zxIgmpInterfaceEntry = _ZxIgmpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1)
)
zxIgmpInterfaceEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpInterface"),
)
if mibBuilder.loadTexts:
    zxIgmpInterfaceEntry.setStatus("current")


class _ZxIgmpInterface_Type(DisplayString):
    """Custom type zxIgmpInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxIgmpInterface_Type.__name__ = "DisplayString"
_ZxIgmpInterface_Object = MibTableColumn
zxIgmpInterface = _ZxIgmpInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 1),
    _ZxIgmpInterface_Type()
)
zxIgmpInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpInterface.setStatus("current")
_ZxIgmpInfIpAddr_Type = IpAddress
_ZxIgmpInfIpAddr_Object = MibTableColumn
zxIgmpInfIpAddr = _ZxIgmpInfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 2),
    _ZxIgmpInfIpAddr_Type()
)
zxIgmpInfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpInfIpAddr.setStatus("current")
_ZxIgmpInfMask_Type = IpAddress
_ZxIgmpInfMask_Object = MibTableColumn
zxIgmpInfMask = _ZxIgmpInfMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 3),
    _ZxIgmpInfMask_Type()
)
zxIgmpInfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpInfMask.setStatus("current")


class _ZxIgmpVersion_Type(Integer32):
    """Custom type zxIgmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2))
    )


_ZxIgmpVersion_Type.__name__ = "Integer32"
_ZxIgmpVersion_Object = MibTableColumn
zxIgmpVersion = _ZxIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 4),
    _ZxIgmpVersion_Type()
)
zxIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpVersion.setStatus("current")
_ZxIgmpQueryInterval_Type = Integer32
_ZxIgmpQueryInterval_Object = MibTableColumn
zxIgmpQueryInterval = _ZxIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 5),
    _ZxIgmpQueryInterval_Type()
)
zxIgmpQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpQueryInterval.setStatus("current")
_ZxIgmpLastMemQueryIntvl_Type = Integer32
_ZxIgmpLastMemQueryIntvl_Object = MibTableColumn
zxIgmpLastMemQueryIntvl = _ZxIgmpLastMemQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 6),
    _ZxIgmpLastMemQueryIntvl_Type()
)
zxIgmpLastMemQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpLastMemQueryIntvl.setStatus("current")
_ZxIgmpMaxResponseTime_Type = Integer32
_ZxIgmpMaxResponseTime_Object = MibTableColumn
zxIgmpMaxResponseTime = _ZxIgmpMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 7),
    _ZxIgmpMaxResponseTime_Type()
)
zxIgmpMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpMaxResponseTime.setStatus("current")
_ZxIgmpQuerierTimeout_Type = Integer32
_ZxIgmpQuerierTimeout_Object = MibTableColumn
zxIgmpQuerierTimeout = _ZxIgmpQuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 8),
    _ZxIgmpQuerierTimeout_Type()
)
zxIgmpQuerierTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpQuerierTimeout.setStatus("current")
_ZxIgmpQuerier_Type = IpAddress
_ZxIgmpQuerier_Object = MibTableColumn
zxIgmpQuerier = _ZxIgmpQuerier_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 9),
    _ZxIgmpQuerier_Type()
)
zxIgmpQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpQuerier.setStatus("current")
_ZxIgmpQuerierExpire_Type = DisplayString
_ZxIgmpQuerierExpire_Object = MibTableColumn
zxIgmpQuerierExpire = _ZxIgmpQuerierExpire_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 10),
    _ZxIgmpQuerierExpire_Type()
)
zxIgmpQuerierExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpQuerierExpire.setStatus("current")
_ZxIgmpInboundAcl_Type = Integer32
_ZxIgmpInboundAcl_Object = MibTableColumn
zxIgmpInboundAcl = _ZxIgmpInboundAcl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 11),
    _ZxIgmpInboundAcl_Type()
)
zxIgmpInboundAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpInboundAcl.setStatus("current")
_ZxIgmpImmediateLeave_Type = Integer32
_ZxIgmpImmediateLeave_Object = MibTableColumn
zxIgmpImmediateLeave = _ZxIgmpImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 2, 1, 12),
    _ZxIgmpImmediateLeave_Type()
)
zxIgmpImmediateLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpImmediateLeave.setStatus("current")
_ZxIgmpInfRevPktTable_Object = MibTable
zxIgmpInfRevPktTable = _ZxIgmpInfRevPktTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zxIgmpInfRevPktTable.setStatus("current")
_ZxIgmpInfRevPktEntry_Object = MibTableRow
zxIgmpInfRevPktEntry = _ZxIgmpInfRevPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1)
)
zxIgmpInfRevPktEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpRevPktInterface"),
)
if mibBuilder.loadTexts:
    zxIgmpInfRevPktEntry.setStatus("current")


class _ZxIgmpRevPktInterface_Type(DisplayString):
    """Custom type zxIgmpRevPktInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxIgmpRevPktInterface_Type.__name__ = "DisplayString"
_ZxIgmpRevPktInterface_Object = MibTableColumn
zxIgmpRevPktInterface = _ZxIgmpRevPktInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 1),
    _ZxIgmpRevPktInterface_Type()
)
zxIgmpRevPktInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktInterface.setStatus("current")
_ZxIgmpRevPktQuery_Type = Integer32
_ZxIgmpRevPktQuery_Object = MibTableColumn
zxIgmpRevPktQuery = _ZxIgmpRevPktQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 2),
    _ZxIgmpRevPktQuery_Type()
)
zxIgmpRevPktQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktQuery.setStatus("current")
_ZxIgmpRevPktReportV2_Type = Integer32
_ZxIgmpRevPktReportV2_Object = MibTableColumn
zxIgmpRevPktReportV2 = _ZxIgmpRevPktReportV2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 3),
    _ZxIgmpRevPktReportV2_Type()
)
zxIgmpRevPktReportV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktReportV2.setStatus("current")
_ZxIgmpRevPktLeave_Type = Integer32
_ZxIgmpRevPktLeave_Object = MibTableColumn
zxIgmpRevPktLeave = _ZxIgmpRevPktLeave_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 4),
    _ZxIgmpRevPktLeave_Type()
)
zxIgmpRevPktLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktLeave.setStatus("current")
_ZxIgmpRevPktReportV1_Type = Integer32
_ZxIgmpRevPktReportV1_Object = MibTableColumn
zxIgmpRevPktReportV1 = _ZxIgmpRevPktReportV1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 5),
    _ZxIgmpRevPktReportV1_Type()
)
zxIgmpRevPktReportV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktReportV1.setStatus("current")
_ZxIgmpRevPktOther_Type = Integer32
_ZxIgmpRevPktOther_Object = MibTableColumn
zxIgmpRevPktOther = _ZxIgmpRevPktOther_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 6),
    _ZxIgmpRevPktOther_Type()
)
zxIgmpRevPktOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktOther.setStatus("current")
_ZxIgmpRevPktTotal_Type = Integer32
_ZxIgmpRevPktTotal_Object = MibTableColumn
zxIgmpRevPktTotal = _ZxIgmpRevPktTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 3, 1, 7),
    _ZxIgmpRevPktTotal_Type()
)
zxIgmpRevPktTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpRevPktTotal.setStatus("current")
_ZxIgmpInfSendPktTable_Object = MibTable
zxIgmpInfSendPktTable = _ZxIgmpInfSendPktTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zxIgmpInfSendPktTable.setStatus("current")
_ZxIgmpInfSendPktEntry_Object = MibTableRow
zxIgmpInfSendPktEntry = _ZxIgmpInfSendPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 4, 1)
)
zxIgmpInfSendPktEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpSendPktInterface"),
)
if mibBuilder.loadTexts:
    zxIgmpInfSendPktEntry.setStatus("current")


class _ZxIgmpSendPktInterface_Type(DisplayString):
    """Custom type zxIgmpSendPktInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxIgmpSendPktInterface_Type.__name__ = "DisplayString"
_ZxIgmpSendPktInterface_Object = MibTableColumn
zxIgmpSendPktInterface = _ZxIgmpSendPktInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 4, 1, 1),
    _ZxIgmpSendPktInterface_Type()
)
zxIgmpSendPktInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpSendPktInterface.setStatus("current")
_ZxIgmpSendPktQuery_Type = Integer32
_ZxIgmpSendPktQuery_Object = MibTableColumn
zxIgmpSendPktQuery = _ZxIgmpSendPktQuery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 4, 1, 2),
    _ZxIgmpSendPktQuery_Type()
)
zxIgmpSendPktQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpSendPktQuery.setStatus("current")
_ZxIgmpSendPktSpec_Type = Integer32
_ZxIgmpSendPktSpec_Object = MibTableColumn
zxIgmpSendPktSpec = _ZxIgmpSendPktSpec_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 4, 1, 3),
    _ZxIgmpSendPktSpec_Type()
)
zxIgmpSendPktSpec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpSendPktSpec.setStatus("current")
_ZxIgmpSendPktTotal_Type = Integer32
_ZxIgmpSendPktTotal_Object = MibTableColumn
zxIgmpSendPktTotal = _ZxIgmpSendPktTotal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 4, 1, 4),
    _ZxIgmpSendPktTotal_Type()
)
zxIgmpSendPktTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpSendPktTotal.setStatus("current")
_ZxIgmpServerLogTable_Object = MibTable
zxIgmpServerLogTable = _ZxIgmpServerLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    zxIgmpServerLogTable.setStatus("current")
_ZxIgmpServerLogEntry_Object = MibTableRow
zxIgmpServerLogEntry = _ZxIgmpServerLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1)
)
zxIgmpServerLogEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpServerLogInterface"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpServerLogGroupAddr"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpServerLogSourceAddr"),
)
if mibBuilder.loadTexts:
    zxIgmpServerLogEntry.setStatus("current")


class _ZxIgmpServerLogInterface_Type(DisplayString):
    """Custom type zxIgmpServerLogInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxIgmpServerLogInterface_Type.__name__ = "DisplayString"
_ZxIgmpServerLogInterface_Object = MibTableColumn
zxIgmpServerLogInterface = _ZxIgmpServerLogInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 1),
    _ZxIgmpServerLogInterface_Type()
)
zxIgmpServerLogInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogInterface.setStatus("current")


class _ZxIgmpServerLogProtocol_Type(Integer32):
    """Custom type zxIgmpServerLogProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("pimDm", 2),
          ("pimSm", 1))
    )


_ZxIgmpServerLogProtocol_Type.__name__ = "Integer32"
_ZxIgmpServerLogProtocol_Object = MibTableColumn
zxIgmpServerLogProtocol = _ZxIgmpServerLogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 2),
    _ZxIgmpServerLogProtocol_Type()
)
zxIgmpServerLogProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogProtocol.setStatus("current")
_ZxIgmpServerLogVpi_Type = Integer32
_ZxIgmpServerLogVpi_Object = MibTableColumn
zxIgmpServerLogVpi = _ZxIgmpServerLogVpi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 3),
    _ZxIgmpServerLogVpi_Type()
)
zxIgmpServerLogVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogVpi.setStatus("current")
_ZxIgmpServerLogVci_Type = Integer32
_ZxIgmpServerLogVci_Object = MibTableColumn
zxIgmpServerLogVci = _ZxIgmpServerLogVci_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 4),
    _ZxIgmpServerLogVci_Type()
)
zxIgmpServerLogVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogVci.setStatus("current")
_ZxIgmpServerLogGroupAddr_Type = IpAddress
_ZxIgmpServerLogGroupAddr_Object = MibTableColumn
zxIgmpServerLogGroupAddr = _ZxIgmpServerLogGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 5),
    _ZxIgmpServerLogGroupAddr_Type()
)
zxIgmpServerLogGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogGroupAddr.setStatus("current")
_ZxIgmpServerLogSourceAddr_Type = IpAddress
_ZxIgmpServerLogSourceAddr_Object = MibTableColumn
zxIgmpServerLogSourceAddr = _ZxIgmpServerLogSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 6),
    _ZxIgmpServerLogSourceAddr_Type()
)
zxIgmpServerLogSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogSourceAddr.setStatus("current")
_ZxIgmpServerLogRecTime_Type = DisplayString
_ZxIgmpServerLogRecTime_Object = MibTableColumn
zxIgmpServerLogRecTime = _ZxIgmpServerLogRecTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 7),
    _ZxIgmpServerLogRecTime_Type()
)
zxIgmpServerLogRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogRecTime.setStatus("current")
_ZxIgmpServerLogPPPoESID_Type = Integer32
_ZxIgmpServerLogPPPoESID_Object = MibTableColumn
zxIgmpServerLogPPPoESID = _ZxIgmpServerLogPPPoESID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 2, 5, 1, 8),
    _ZxIgmpServerLogPPPoESID_Type()
)
zxIgmpServerLogPPPoESID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpServerLogPPPoESID.setStatus("current")
_ZxPimGroup_ObjectIdentity = ObjectIdentity
zxPimGroup = _ZxPimGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3)
)
_ZxPimBSR_Type = DisplayString
_ZxPimBSR_Object = MibScalar
zxPimBSR = _ZxPimBSR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 1),
    _ZxPimBSR_Type()
)
zxPimBSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimBSR.setStatus("current")
_ZxPimCBsr_Type = DisplayString
_ZxPimCBsr_Object = MibScalar
zxPimCBsr = _ZxPimCBsr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 2),
    _ZxPimCBsr_Type()
)
zxPimCBsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimCBsr.setStatus("current")
_ZxPimCRP_Type = DisplayString
_ZxPimCRP_Object = MibScalar
zxPimCRP = _ZxPimCRP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 3),
    _ZxPimCRP_Type()
)
zxPimCRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimCRP.setStatus("current")
_ZxPimRpMapTable_Object = MibTable
zxPimRpMapTable = _ZxPimRpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    zxPimRpMapTable.setStatus("current")
_ZxPimRpMapEntry_Object = MibTableRow
zxPimRpMapEntry = _ZxPimRpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 4, 1)
)
zxPimRpMapEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimRpMapGroupAddr"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimRpMapGroupMask"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimRpMapRpAddr"),
)
if mibBuilder.loadTexts:
    zxPimRpMapEntry.setStatus("current")
_ZxPimRpMapGroupAddr_Type = IpAddress
_ZxPimRpMapGroupAddr_Object = MibTableColumn
zxPimRpMapGroupAddr = _ZxPimRpMapGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 4, 1, 1),
    _ZxPimRpMapGroupAddr_Type()
)
zxPimRpMapGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimRpMapGroupAddr.setStatus("current")
_ZxPimRpMapGroupMask_Type = IpAddress
_ZxPimRpMapGroupMask_Object = MibTableColumn
zxPimRpMapGroupMask = _ZxPimRpMapGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 4, 1, 2),
    _ZxPimRpMapGroupMask_Type()
)
zxPimRpMapGroupMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimRpMapGroupMask.setStatus("current")
_ZxPimRpMapRpAddr_Type = IpAddress
_ZxPimRpMapRpAddr_Object = MibTableColumn
zxPimRpMapRpAddr = _ZxPimRpMapRpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 4, 1, 3),
    _ZxPimRpMapRpAddr_Type()
)
zxPimRpMapRpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimRpMapRpAddr.setStatus("current")
_ZxPimRpMapRpDescr_Type = DisplayString
_ZxPimRpMapRpDescr_Object = MibTableColumn
zxPimRpMapRpDescr = _ZxPimRpMapRpDescr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 4, 1, 4),
    _ZxPimRpMapRpDescr_Type()
)
zxPimRpMapRpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimRpMapRpDescr.setStatus("current")
_ZxPimSmInterfaceTable_Object = MibTable
zxPimSmInterfaceTable = _ZxPimSmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    zxPimSmInterfaceTable.setStatus("current")
_ZxPimSmIntfEntry_Object = MibTableRow
zxPimSmIntfEntry = _ZxPimSmIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1)
)
zxPimSmIntfEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimSmInterface"),
)
if mibBuilder.loadTexts:
    zxPimSmIntfEntry.setStatus("current")
_ZxPimSmAddr_Type = IpAddress
_ZxPimSmAddr_Object = MibTableColumn
zxPimSmAddr = _ZxPimSmAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 1),
    _ZxPimSmAddr_Type()
)
zxPimSmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmAddr.setStatus("current")


class _ZxPimSmInterface_Type(DisplayString):
    """Custom type zxPimSmInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxPimSmInterface_Type.__name__ = "DisplayString"
_ZxPimSmInterface_Object = MibTableColumn
zxPimSmInterface = _ZxPimSmInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 2),
    _ZxPimSmInterface_Type()
)
zxPimSmInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmInterface.setStatus("current")


class _ZxPimSmIntfState_Type(Integer32):
    """Custom type zxPimSmIntfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_ZxPimSmIntfState_Type.__name__ = "Integer32"
_ZxPimSmIntfState_Object = MibTableColumn
zxPimSmIntfState = _ZxPimSmIntfState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 3),
    _ZxPimSmIntfState_Type()
)
zxPimSmIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmIntfState.setStatus("current")
_ZxPimSmNbrCount_Type = Integer32
_ZxPimSmNbrCount_Object = MibTableColumn
zxPimSmNbrCount = _ZxPimSmNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 4),
    _ZxPimSmNbrCount_Type()
)
zxPimSmNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrCount.setStatus("current")
_ZxPimSmQueryIntvl_Type = Integer32
_ZxPimSmQueryIntvl_Object = MibTableColumn
zxPimSmQueryIntvl = _ZxPimSmQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 5),
    _ZxPimSmQueryIntvl_Type()
)
zxPimSmQueryIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmQueryIntvl.setStatus("current")
_ZxPimSmDR_Type = IpAddress
_ZxPimSmDR_Object = MibTableColumn
zxPimSmDR = _ZxPimSmDR_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 6),
    _ZxPimSmDR_Type()
)
zxPimSmDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmDR.setStatus("current")
_ZxPimSmDrPriority_Type = Integer32
_ZxPimSmDrPriority_Object = MibTableColumn
zxPimSmDrPriority = _ZxPimSmDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 5, 1, 7),
    _ZxPimSmDrPriority_Type()
)
zxPimSmDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmDrPriority.setStatus("current")
_ZxPimSmNbrTable_Object = MibTable
zxPimSmNbrTable = _ZxPimSmNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    zxPimSmNbrTable.setStatus("current")
_ZxPimSmNbrEntry_Object = MibTableRow
zxPimSmNbrEntry = _ZxPimSmNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1)
)
zxPimSmNbrEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimSmNbrAddr"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimSmNbrIntf"),
)
if mibBuilder.loadTexts:
    zxPimSmNbrEntry.setStatus("current")
_ZxPimSmNbrAddr_Type = IpAddress
_ZxPimSmNbrAddr_Object = MibTableColumn
zxPimSmNbrAddr = _ZxPimSmNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1, 1),
    _ZxPimSmNbrAddr_Type()
)
zxPimSmNbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrAddr.setStatus("current")


class _ZxPimSmNbrIntf_Type(DisplayString):
    """Custom type zxPimSmNbrIntf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxPimSmNbrIntf_Type.__name__ = "DisplayString"
_ZxPimSmNbrIntf_Object = MibTableColumn
zxPimSmNbrIntf = _ZxPimSmNbrIntf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1, 2),
    _ZxPimSmNbrIntf_Type()
)
zxPimSmNbrIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrIntf.setStatus("current")
_ZxPimSmNbrDrPriority_Type = Integer32
_ZxPimSmNbrDrPriority_Object = MibTableColumn
zxPimSmNbrDrPriority = _ZxPimSmNbrDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1, 3),
    _ZxPimSmNbrDrPriority_Type()
)
zxPimSmNbrDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrDrPriority.setStatus("current")
_ZxPimSmNbrUptime_Type = DisplayString
_ZxPimSmNbrUptime_Object = MibTableColumn
zxPimSmNbrUptime = _ZxPimSmNbrUptime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1, 4),
    _ZxPimSmNbrUptime_Type()
)
zxPimSmNbrUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrUptime.setStatus("current")
_ZxPimSmNbrExpire_Type = DisplayString
_ZxPimSmNbrExpire_Object = MibTableColumn
zxPimSmNbrExpire = _ZxPimSmNbrExpire_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1, 5),
    _ZxPimSmNbrExpire_Type()
)
zxPimSmNbrExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrExpire.setStatus("current")


class _ZxPimSmNbrVer_Type(Integer32):
    """Custom type zxPimSmNbrVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpv1", 1),
          ("igmpv2", 2))
    )


_ZxPimSmNbrVer_Type.__name__ = "Integer32"
_ZxPimSmNbrVer_Object = MibTableColumn
zxPimSmNbrVer = _ZxPimSmNbrVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 6, 1, 6),
    _ZxPimSmNbrVer_Type()
)
zxPimSmNbrVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmNbrVer.setStatus("current")
_ZxPimSmPktTable_Object = MibTable
zxPimSmPktTable = _ZxPimSmPktTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    zxPimSmPktTable.setStatus("current")
_ZxPimSmPktEntry_Object = MibTableRow
zxPimSmPktEntry = _ZxPimSmPktEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1)
)
zxPimSmPktEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimSmPktIntf"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxPimSmPktType"),
)
if mibBuilder.loadTexts:
    zxPimSmPktEntry.setStatus("current")


class _ZxPimSmPktIntf_Type(DisplayString):
    """Custom type zxPimSmPktIntf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxPimSmPktIntf_Type.__name__ = "DisplayString"
_ZxPimSmPktIntf_Object = MibTableColumn
zxPimSmPktIntf = _ZxPimSmPktIntf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1, 1),
    _ZxPimSmPktIntf_Type()
)
zxPimSmPktIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmPktIntf.setStatus("current")


class _ZxPimSmPktType_Type(Integer32):
    """Custom type zxPimSmPktType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("assert", 6),
          ("bsr", 5),
          ("crp-adv", 9),
          ("err-type", 11),
          ("graft", 7),
          ("graft-ack", 8),
          ("hello", 1),
          ("joinOrPrune", 4),
          ("probe", 10),
          ("register", 2),
          ("register-Stop", 3))
    )


_ZxPimSmPktType_Type.__name__ = "Integer32"
_ZxPimSmPktType_Object = MibTableColumn
zxPimSmPktType = _ZxPimSmPktType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1, 2),
    _ZxPimSmPktType_Type()
)
zxPimSmPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmPktType.setStatus("current")
_ZxPimSmPktRxOk_Type = Integer32
_ZxPimSmPktRxOk_Object = MibTableColumn
zxPimSmPktRxOk = _ZxPimSmPktRxOk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1, 3),
    _ZxPimSmPktRxOk_Type()
)
zxPimSmPktRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmPktRxOk.setStatus("current")
_ZxPimSmPktTxOk_Type = Integer32
_ZxPimSmPktTxOk_Object = MibTableColumn
zxPimSmPktTxOk = _ZxPimSmPktTxOk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1, 4),
    _ZxPimSmPktTxOk_Type()
)
zxPimSmPktTxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmPktTxOk.setStatus("current")
_ZxPimSmPktRxError_Type = Integer32
_ZxPimSmPktRxError_Object = MibTableColumn
zxPimSmPktRxError = _ZxPimSmPktRxError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1, 5),
    _ZxPimSmPktRxError_Type()
)
zxPimSmPktRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmPktRxError.setStatus("current")
_ZxPimSmPktTxError_Type = Integer32
_ZxPimSmPktTxError_Object = MibTableColumn
zxPimSmPktTxError = _ZxPimSmPktTxError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 3, 7, 1, 6),
    _ZxPimSmPktTxError_Type()
)
zxPimSmPktTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxPimSmPktTxError.setStatus("current")
_ZxIgmpUasGroup_ObjectIdentity = ObjectIdentity
zxIgmpUasGroup = _ZxIgmpUasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4)
)


class _ZxIgmpUasAclSwitch_Type(Integer32):
    """Custom type zxIgmpUasAclSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxIgmpUasAclSwitch_Type.__name__ = "Integer32"
_ZxIgmpUasAclSwitch_Object = MibScalar
zxIgmpUasAclSwitch = _ZxIgmpUasAclSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 1),
    _ZxIgmpUasAclSwitch_Type()
)
zxIgmpUasAclSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasAclSwitch.setStatus("current")


class _ZxIgmpUasPrivateServerLogSwitch_Type(Integer32):
    """Custom type zxIgmpUasPrivateServerLogSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxIgmpUasPrivateServerLogSwitch_Type.__name__ = "Integer32"
_ZxIgmpUasPrivateServerLogSwitch_Object = MibScalar
zxIgmpUasPrivateServerLogSwitch = _ZxIgmpUasPrivateServerLogSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 2),
    _ZxIgmpUasPrivateServerLogSwitch_Type()
)
zxIgmpUasPrivateServerLogSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasPrivateServerLogSwitch.setStatus("current")
_ZxIgmpUasAclTable_Object = MibTable
zxIgmpUasAclTable = _ZxIgmpUasAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    zxIgmpUasAclTable.setStatus("current")
_ZxIgmpUasAclEntry_Object = MibTableRow
zxIgmpUasAclEntry = _ZxIgmpUasAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 3, 1)
)
zxIgmpUasAclEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpUasAclSourceAddr"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpUasAclDestAddr"),
)
if mibBuilder.loadTexts:
    zxIgmpUasAclEntry.setStatus("current")
_ZxIgmpUasAclSourceAddr_Type = IpAddress
_ZxIgmpUasAclSourceAddr_Object = MibTableColumn
zxIgmpUasAclSourceAddr = _ZxIgmpUasAclSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 3, 1, 1),
    _ZxIgmpUasAclSourceAddr_Type()
)
zxIgmpUasAclSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasAclSourceAddr.setStatus("current")


class _ZxIgmpUasAclDestAddr_Type(DisplayString):
    """Custom type zxIgmpUasAclDestAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ZxIgmpUasAclDestAddr_Type.__name__ = "DisplayString"
_ZxIgmpUasAclDestAddr_Object = MibTableColumn
zxIgmpUasAclDestAddr = _ZxIgmpUasAclDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 3, 1, 2),
    _ZxIgmpUasAclDestAddr_Type()
)
zxIgmpUasAclDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasAclDestAddr.setStatus("current")
_ZxIgmpUasServiceProfileTable_Object = MibTable
zxIgmpUasServiceProfileTable = _ZxIgmpUasServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileTable.setStatus("current")
_ZxIgmpUasServiceProfileEntry_Object = MibTableRow
zxIgmpUasServiceProfileEntry = _ZxIgmpUasServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1)
)
zxIgmpUasServiceProfileEntry.setIndexNames(
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpUasServiceProfileNumber"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpUasServiceProfilePrwGroup"),
    (0, "ZTE-UAS-MULTICAST-MIB", "zxIgmpUasServiceProfilePrwGroupMask"),
)
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileEntry.setStatus("current")
_ZxIgmpUasServiceProfileNumber_Type = Integer32
_ZxIgmpUasServiceProfileNumber_Object = MibTableColumn
zxIgmpUasServiceProfileNumber = _ZxIgmpUasServiceProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 1),
    _ZxIgmpUasServiceProfileNumber_Type()
)
zxIgmpUasServiceProfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileNumber.setStatus("current")
_ZxIgmpUasServiceProfileAccGroup_Type = Integer32
_ZxIgmpUasServiceProfileAccGroup_Object = MibTableColumn
zxIgmpUasServiceProfileAccGroup = _ZxIgmpUasServiceProfileAccGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 2),
    _ZxIgmpUasServiceProfileAccGroup_Type()
)
zxIgmpUasServiceProfileAccGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileAccGroup.setStatus("current")
_ZxIgmpUasServiceProfileDescr_Type = DisplayString
_ZxIgmpUasServiceProfileDescr_Object = MibTableColumn
zxIgmpUasServiceProfileDescr = _ZxIgmpUasServiceProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 3),
    _ZxIgmpUasServiceProfileDescr_Type()
)
zxIgmpUasServiceProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileDescr.setStatus("current")
_ZxIgmpUasServiceProfileMaxGroup_Type = Integer32
_ZxIgmpUasServiceProfileMaxGroup_Object = MibTableColumn
zxIgmpUasServiceProfileMaxGroup = _ZxIgmpUasServiceProfileMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 4),
    _ZxIgmpUasServiceProfileMaxGroup_Type()
)
zxIgmpUasServiceProfileMaxGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileMaxGroup.setStatus("current")
_ZxIgmpUasServiceProfileMaxPrwGroup_Type = Integer32
_ZxIgmpUasServiceProfileMaxPrwGroup_Object = MibTableColumn
zxIgmpUasServiceProfileMaxPrwGroup = _ZxIgmpUasServiceProfileMaxPrwGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 5),
    _ZxIgmpUasServiceProfileMaxPrwGroup_Type()
)
zxIgmpUasServiceProfileMaxPrwGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileMaxPrwGroup.setStatus("current")
_ZxIgmpUasServiceProfilePrwGroup_Type = IpAddress
_ZxIgmpUasServiceProfilePrwGroup_Object = MibTableColumn
zxIgmpUasServiceProfilePrwGroup = _ZxIgmpUasServiceProfilePrwGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 6),
    _ZxIgmpUasServiceProfilePrwGroup_Type()
)
zxIgmpUasServiceProfilePrwGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfilePrwGroup.setStatus("current")
_ZxIgmpUasServiceProfilePrwGroupMask_Type = IpAddress
_ZxIgmpUasServiceProfilePrwGroupMask_Object = MibTableColumn
zxIgmpUasServiceProfilePrwGroupMask = _ZxIgmpUasServiceProfilePrwGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 7),
    _ZxIgmpUasServiceProfilePrwGroupMask_Type()
)
zxIgmpUasServiceProfilePrwGroupMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfilePrwGroupMask.setStatus("current")
_ZxIgmpUasServiceProfileMaxPrwCount_Type = Integer32
_ZxIgmpUasServiceProfileMaxPrwCount_Object = MibTableColumn
zxIgmpUasServiceProfileMaxPrwCount = _ZxIgmpUasServiceProfileMaxPrwCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 8),
    _ZxIgmpUasServiceProfileMaxPrwCount_Type()
)
zxIgmpUasServiceProfileMaxPrwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfileMaxPrwCount.setStatus("current")
_ZxIgmpUasServiceProfilePrwResumeIntvl_Type = Integer32
_ZxIgmpUasServiceProfilePrwResumeIntvl_Object = MibTableColumn
zxIgmpUasServiceProfilePrwResumeIntvl = _ZxIgmpUasServiceProfilePrwResumeIntvl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 1, 4, 4, 1, 9),
    _ZxIgmpUasServiceProfilePrwResumeIntvl_Type()
)
zxIgmpUasServiceProfilePrwResumeIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxIgmpUasServiceProfilePrwResumeIntvl.setStatus("current")
_ZxUasTraps_ObjectIdentity = ObjectIdentity
zxUasTraps = _ZxUasTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-UAS-MULTICAST-MIB",
    **{"zte": zte,
       "zxUas": zxUas,
       "zxMulticastMib": zxMulticastMib,
       "zxUasMulticastMibObjects": zxUasMulticastMibObjects,
       "zxUasMulticastSwitch": zxUasMulticastSwitch,
       "zxIgmpGroup": zxIgmpGroup,
       "zxIgmpGroupTable": zxIgmpGroupTable,
       "zxIgmpGroupEntry": zxIgmpGroupEntry,
       "zxIgmpGroupAddr": zxIgmpGroupAddr,
       "zxIgmpGroupInterface": zxIgmpGroupInterface,
       "zxIgmpGroupFlag": zxIgmpGroupFlag,
       "zxIgmpGroupPresent": zxIgmpGroupPresent,
       "zxIgmpGroupExpire": zxIgmpGroupExpire,
       "zxIgmpGroupLastReporterCircuit": zxIgmpGroupLastReporterCircuit,
       "zxIgmpInterfaceTable": zxIgmpInterfaceTable,
       "zxIgmpInterfaceEntry": zxIgmpInterfaceEntry,
       "zxIgmpInterface": zxIgmpInterface,
       "zxIgmpInfIpAddr": zxIgmpInfIpAddr,
       "zxIgmpInfMask": zxIgmpInfMask,
       "zxIgmpVersion": zxIgmpVersion,
       "zxIgmpQueryInterval": zxIgmpQueryInterval,
       "zxIgmpLastMemQueryIntvl": zxIgmpLastMemQueryIntvl,
       "zxIgmpMaxResponseTime": zxIgmpMaxResponseTime,
       "zxIgmpQuerierTimeout": zxIgmpQuerierTimeout,
       "zxIgmpQuerier": zxIgmpQuerier,
       "zxIgmpQuerierExpire": zxIgmpQuerierExpire,
       "zxIgmpInboundAcl": zxIgmpInboundAcl,
       "zxIgmpImmediateLeave": zxIgmpImmediateLeave,
       "zxIgmpInfRevPktTable": zxIgmpInfRevPktTable,
       "zxIgmpInfRevPktEntry": zxIgmpInfRevPktEntry,
       "zxIgmpRevPktInterface": zxIgmpRevPktInterface,
       "zxIgmpRevPktQuery": zxIgmpRevPktQuery,
       "zxIgmpRevPktReportV2": zxIgmpRevPktReportV2,
       "zxIgmpRevPktLeave": zxIgmpRevPktLeave,
       "zxIgmpRevPktReportV1": zxIgmpRevPktReportV1,
       "zxIgmpRevPktOther": zxIgmpRevPktOther,
       "zxIgmpRevPktTotal": zxIgmpRevPktTotal,
       "zxIgmpInfSendPktTable": zxIgmpInfSendPktTable,
       "zxIgmpInfSendPktEntry": zxIgmpInfSendPktEntry,
       "zxIgmpSendPktInterface": zxIgmpSendPktInterface,
       "zxIgmpSendPktQuery": zxIgmpSendPktQuery,
       "zxIgmpSendPktSpec": zxIgmpSendPktSpec,
       "zxIgmpSendPktTotal": zxIgmpSendPktTotal,
       "zxIgmpServerLogTable": zxIgmpServerLogTable,
       "zxIgmpServerLogEntry": zxIgmpServerLogEntry,
       "zxIgmpServerLogInterface": zxIgmpServerLogInterface,
       "zxIgmpServerLogProtocol": zxIgmpServerLogProtocol,
       "zxIgmpServerLogVpi": zxIgmpServerLogVpi,
       "zxIgmpServerLogVci": zxIgmpServerLogVci,
       "zxIgmpServerLogGroupAddr": zxIgmpServerLogGroupAddr,
       "zxIgmpServerLogSourceAddr": zxIgmpServerLogSourceAddr,
       "zxIgmpServerLogRecTime": zxIgmpServerLogRecTime,
       "zxIgmpServerLogPPPoESID": zxIgmpServerLogPPPoESID,
       "zxPimGroup": zxPimGroup,
       "zxPimBSR": zxPimBSR,
       "zxPimCBsr": zxPimCBsr,
       "zxPimCRP": zxPimCRP,
       "zxPimRpMapTable": zxPimRpMapTable,
       "zxPimRpMapEntry": zxPimRpMapEntry,
       "zxPimRpMapGroupAddr": zxPimRpMapGroupAddr,
       "zxPimRpMapGroupMask": zxPimRpMapGroupMask,
       "zxPimRpMapRpAddr": zxPimRpMapRpAddr,
       "zxPimRpMapRpDescr": zxPimRpMapRpDescr,
       "zxPimSmInterfaceTable": zxPimSmInterfaceTable,
       "zxPimSmIntfEntry": zxPimSmIntfEntry,
       "zxPimSmAddr": zxPimSmAddr,
       "zxPimSmInterface": zxPimSmInterface,
       "zxPimSmIntfState": zxPimSmIntfState,
       "zxPimSmNbrCount": zxPimSmNbrCount,
       "zxPimSmQueryIntvl": zxPimSmQueryIntvl,
       "zxPimSmDR": zxPimSmDR,
       "zxPimSmDrPriority": zxPimSmDrPriority,
       "zxPimSmNbrTable": zxPimSmNbrTable,
       "zxPimSmNbrEntry": zxPimSmNbrEntry,
       "zxPimSmNbrAddr": zxPimSmNbrAddr,
       "zxPimSmNbrIntf": zxPimSmNbrIntf,
       "zxPimSmNbrDrPriority": zxPimSmNbrDrPriority,
       "zxPimSmNbrUptime": zxPimSmNbrUptime,
       "zxPimSmNbrExpire": zxPimSmNbrExpire,
       "zxPimSmNbrVer": zxPimSmNbrVer,
       "zxPimSmPktTable": zxPimSmPktTable,
       "zxPimSmPktEntry": zxPimSmPktEntry,
       "zxPimSmPktIntf": zxPimSmPktIntf,
       "zxPimSmPktType": zxPimSmPktType,
       "zxPimSmPktRxOk": zxPimSmPktRxOk,
       "zxPimSmPktTxOk": zxPimSmPktTxOk,
       "zxPimSmPktRxError": zxPimSmPktRxError,
       "zxPimSmPktTxError": zxPimSmPktTxError,
       "zxIgmpUasGroup": zxIgmpUasGroup,
       "zxIgmpUasAclSwitch": zxIgmpUasAclSwitch,
       "zxIgmpUasPrivateServerLogSwitch": zxIgmpUasPrivateServerLogSwitch,
       "zxIgmpUasAclTable": zxIgmpUasAclTable,
       "zxIgmpUasAclEntry": zxIgmpUasAclEntry,
       "zxIgmpUasAclSourceAddr": zxIgmpUasAclSourceAddr,
       "zxIgmpUasAclDestAddr": zxIgmpUasAclDestAddr,
       "zxIgmpUasServiceProfileTable": zxIgmpUasServiceProfileTable,
       "zxIgmpUasServiceProfileEntry": zxIgmpUasServiceProfileEntry,
       "zxIgmpUasServiceProfileNumber": zxIgmpUasServiceProfileNumber,
       "zxIgmpUasServiceProfileAccGroup": zxIgmpUasServiceProfileAccGroup,
       "zxIgmpUasServiceProfileDescr": zxIgmpUasServiceProfileDescr,
       "zxIgmpUasServiceProfileMaxGroup": zxIgmpUasServiceProfileMaxGroup,
       "zxIgmpUasServiceProfileMaxPrwGroup": zxIgmpUasServiceProfileMaxPrwGroup,
       "zxIgmpUasServiceProfilePrwGroup": zxIgmpUasServiceProfilePrwGroup,
       "zxIgmpUasServiceProfilePrwGroupMask": zxIgmpUasServiceProfilePrwGroupMask,
       "zxIgmpUasServiceProfileMaxPrwCount": zxIgmpUasServiceProfileMaxPrwCount,
       "zxIgmpUasServiceProfilePrwResumeIntvl": zxIgmpUasServiceProfilePrwResumeIntvl,
       "zxUasTraps": zxUasTraps}
)
