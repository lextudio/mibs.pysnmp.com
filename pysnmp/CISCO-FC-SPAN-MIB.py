# SNMP MIB module (CISCO-FC-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-SPAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:20 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcList,) = mibBuilder.importSymbols(
    "CISCO-ZS-MIB",
    "FcList")

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

ciscoFcSpanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 363)
)
ciscoFcSpanMIB.setRevisions(
        ("2003-04-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SessionIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSpanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSpanMIBObjects = _CiscoSpanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1)
)
_CspanConfiguration_ObjectIdentity = ObjectIdentity
cspanConfiguration = _CspanConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1)
)


class _CspanMaxSessions_Type(Integer32):
    """Custom type cspanMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CspanMaxSessions_Type.__name__ = "Integer32"
_CspanMaxSessions_Object = MibScalar
cspanMaxSessions = _CspanMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 1),
    _CspanMaxSessions_Type()
)
cspanMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanMaxSessions.setStatus("current")
_CspanSessionTable_Object = MibTable
cspanSessionTable = _CspanSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cspanSessionTable.setStatus("current")
_CspanSessionEntry_Object = MibTableRow
cspanSessionEntry = _CspanSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1)
)
cspanSessionEntry.setIndexNames(
    (0, "CISCO-FC-SPAN-MIB", "cspanSessionIndex"),
)
if mibBuilder.loadTexts:
    cspanSessionEntry.setStatus("current")
_CspanSessionIndex_Type = SessionIndex
_CspanSessionIndex_Object = MibTableColumn
cspanSessionIndex = _CspanSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 1),
    _CspanSessionIndex_Type()
)
cspanSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspanSessionIndex.setStatus("current")
_CspanSessionDestIfIndex_Type = InterfaceIndex
_CspanSessionDestIfIndex_Object = MibTableColumn
cspanSessionDestIfIndex = _CspanSessionDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 2),
    _CspanSessionDestIfIndex_Type()
)
cspanSessionDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspanSessionDestIfIndex.setStatus("current")


class _CspanSessionAdminStatus_Type(Integer32):
    """Custom type cspanSessionAdminStatus based on Integer32"""
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


_CspanSessionAdminStatus_Type.__name__ = "Integer32"
_CspanSessionAdminStatus_Object = MibTableColumn
cspanSessionAdminStatus = _CspanSessionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 3),
    _CspanSessionAdminStatus_Type()
)
cspanSessionAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspanSessionAdminStatus.setStatus("current")


class _CspanSessionOperStatus_Type(Integer32):
    """Custom type cspanSessionOperStatus based on Integer32"""
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


_CspanSessionOperStatus_Type.__name__ = "Integer32"
_CspanSessionOperStatus_Object = MibTableColumn
cspanSessionOperStatus = _CspanSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 4),
    _CspanSessionOperStatus_Type()
)
cspanSessionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanSessionOperStatus.setStatus("current")
_CspanSessionInactiveReason_Type = SnmpAdminString
_CspanSessionInactiveReason_Object = MibTableColumn
cspanSessionInactiveReason = _CspanSessionInactiveReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 5),
    _CspanSessionInactiveReason_Type()
)
cspanSessionInactiveReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanSessionInactiveReason.setStatus("current")
_CspanSessionRowStatus_Type = RowStatus
_CspanSessionRowStatus_Object = MibTableColumn
cspanSessionRowStatus = _CspanSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 2, 1, 6),
    _CspanSessionRowStatus_Type()
)
cspanSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspanSessionRowStatus.setStatus("current")
_CspanSourcesIfTable_Object = MibTable
cspanSourcesIfTable = _CspanSourcesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cspanSourcesIfTable.setStatus("current")
_CspanSourcesIfEntry_Object = MibTableRow
cspanSourcesIfEntry = _CspanSourcesIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1)
)
cspanSourcesIfEntry.setIndexNames(
    (0, "CISCO-FC-SPAN-MIB", "cspanSessionIndex"),
    (0, "CISCO-FC-SPAN-MIB", "cspanSourcesIfIndex"),
    (0, "CISCO-FC-SPAN-MIB", "cspanSourcesDirection"),
)
if mibBuilder.loadTexts:
    cspanSourcesIfEntry.setStatus("current")
_CspanSourcesIfIndex_Type = InterfaceIndex
_CspanSourcesIfIndex_Object = MibTableColumn
cspanSourcesIfIndex = _CspanSourcesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1, 1),
    _CspanSourcesIfIndex_Type()
)
cspanSourcesIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspanSourcesIfIndex.setStatus("current")


class _CspanSourcesDirection_Type(Integer32):
    """Custom type cspanSourcesDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("receive", 1),
          ("transmit", 2))
    )


_CspanSourcesDirection_Type.__name__ = "Integer32"
_CspanSourcesDirection_Object = MibTableColumn
cspanSourcesDirection = _CspanSourcesDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1, 2),
    _CspanSourcesDirection_Type()
)
cspanSourcesDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspanSourcesDirection.setStatus("current")
_CspanSourcesRowStatus_Type = RowStatus
_CspanSourcesRowStatus_Object = MibTableColumn
cspanSourcesRowStatus = _CspanSourcesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 3, 1, 3),
    _CspanSourcesRowStatus_Type()
)
cspanSourcesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cspanSourcesRowStatus.setStatus("current")
_CspanSourcesVsanTable_Object = MibTable
cspanSourcesVsanTable = _CspanSourcesVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cspanSourcesVsanTable.setStatus("current")
_CspanSourcesVsanEntry_Object = MibTableRow
cspanSourcesVsanEntry = _CspanSourcesVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4, 1)
)
cspanSourcesVsanEntry.setIndexNames(
    (0, "CISCO-FC-SPAN-MIB", "cspanSessionIndex"),
)
if mibBuilder.loadTexts:
    cspanSourcesVsanEntry.setStatus("current")
_CspanSourcesVsans2k_Type = FcList
_CspanSourcesVsans2k_Object = MibTableColumn
cspanSourcesVsans2k = _CspanSourcesVsans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4, 1, 1),
    _CspanSourcesVsans2k_Type()
)
cspanSourcesVsans2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanSourcesVsans2k.setStatus("current")
_CspanSourcesVsans4k_Type = FcList
_CspanSourcesVsans4k_Object = MibTableColumn
cspanSourcesVsans4k = _CspanSourcesVsans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 4, 1, 2),
    _CspanSourcesVsans4k_Type()
)
cspanSourcesVsans4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanSourcesVsans4k.setStatus("current")
_CspanSourcesVsanCfgTable_Object = MibTable
cspanSourcesVsanCfgTable = _CspanSourcesVsanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cspanSourcesVsanCfgTable.setStatus("current")
_CspanSourcesVsanCfgEntry_Object = MibTableRow
cspanSourcesVsanCfgEntry = _CspanSourcesVsanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1)
)
cspanSourcesVsanCfgEntry.setIndexNames(
    (0, "CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgSessIndex"),
)
if mibBuilder.loadTexts:
    cspanSourcesVsanCfgEntry.setStatus("current")
_CspanSourcesVsanCfgSessIndex_Type = SessionIndex
_CspanSourcesVsanCfgSessIndex_Object = MibTableColumn
cspanSourcesVsanCfgSessIndex = _CspanSourcesVsanCfgSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 1),
    _CspanSourcesVsanCfgSessIndex_Type()
)
cspanSourcesVsanCfgSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspanSourcesVsanCfgSessIndex.setStatus("current")


class _CspanSourcesVsanCfgCommand_Type(Integer32):
    """Custom type cspanSourcesVsanCfgCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("none", 3),
          ("remove", 2))
    )


_CspanSourcesVsanCfgCommand_Type.__name__ = "Integer32"
_CspanSourcesVsanCfgCommand_Object = MibTableColumn
cspanSourcesVsanCfgCommand = _CspanSourcesVsanCfgCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 2),
    _CspanSourcesVsanCfgCommand_Type()
)
cspanSourcesVsanCfgCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspanSourcesVsanCfgCommand.setStatus("current")
_CspanSourcesVsanCfgVsans2k_Type = FcList
_CspanSourcesVsanCfgVsans2k_Object = MibTableColumn
cspanSourcesVsanCfgVsans2k = _CspanSourcesVsanCfgVsans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 3),
    _CspanSourcesVsanCfgVsans2k_Type()
)
cspanSourcesVsanCfgVsans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspanSourcesVsanCfgVsans2k.setStatus("current")
_CspanSourcesVsanCfgVsans4k_Type = FcList
_CspanSourcesVsanCfgVsans4k_Object = MibTableColumn
cspanSourcesVsanCfgVsans4k = _CspanSourcesVsanCfgVsans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 5, 1, 4),
    _CspanSourcesVsanCfgVsans4k_Type()
)
cspanSourcesVsanCfgVsans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspanSourcesVsanCfgVsans4k.setStatus("current")
_CspanVsanFilterTable_Object = MibTable
cspanVsanFilterTable = _CspanVsanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cspanVsanFilterTable.setStatus("current")
_CspanVsanFilterEntry_Object = MibTableRow
cspanVsanFilterEntry = _CspanVsanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1)
)
cspanVsanFilterEntry.setIndexNames(
    (0, "CISCO-FC-SPAN-MIB", "cspanVsanFilterSessIndex"),
)
if mibBuilder.loadTexts:
    cspanVsanFilterEntry.setStatus("current")
_CspanVsanFilterSessIndex_Type = SessionIndex
_CspanVsanFilterSessIndex_Object = MibTableColumn
cspanVsanFilterSessIndex = _CspanVsanFilterSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1, 1),
    _CspanVsanFilterSessIndex_Type()
)
cspanVsanFilterSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspanVsanFilterSessIndex.setStatus("current")
_CspanVsanFilterVsans2k_Type = FcList
_CspanVsanFilterVsans2k_Object = MibTableColumn
cspanVsanFilterVsans2k = _CspanVsanFilterVsans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1, 2),
    _CspanVsanFilterVsans2k_Type()
)
cspanVsanFilterVsans2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanVsanFilterVsans2k.setStatus("current")
_CspanVsanFilterVsans4k_Type = FcList
_CspanVsanFilterVsans4k_Object = MibTableColumn
cspanVsanFilterVsans4k = _CspanVsanFilterVsans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 6, 1, 3),
    _CspanVsanFilterVsans4k_Type()
)
cspanVsanFilterVsans4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspanVsanFilterVsans4k.setStatus("current")
_CspanVsanFilterOpTable_Object = MibTable
cspanVsanFilterOpTable = _CspanVsanFilterOpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cspanVsanFilterOpTable.setStatus("current")
_CspanVsanFilterOpEntry_Object = MibTableRow
cspanVsanFilterOpEntry = _CspanVsanFilterOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1)
)
cspanVsanFilterOpEntry.setIndexNames(
    (0, "CISCO-FC-SPAN-MIB", "cspanVsanFilterOpSessIndex"),
)
if mibBuilder.loadTexts:
    cspanVsanFilterOpEntry.setStatus("current")
_CspanVsanFilterOpSessIndex_Type = SessionIndex
_CspanVsanFilterOpSessIndex_Object = MibTableColumn
cspanVsanFilterOpSessIndex = _CspanVsanFilterOpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 1),
    _CspanVsanFilterOpSessIndex_Type()
)
cspanVsanFilterOpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cspanVsanFilterOpSessIndex.setStatus("current")


class _CspanVsanFilterOpCommand_Type(Integer32):
    """Custom type cspanVsanFilterOpCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("none", 3),
          ("remove", 2))
    )


_CspanVsanFilterOpCommand_Type.__name__ = "Integer32"
_CspanVsanFilterOpCommand_Object = MibTableColumn
cspanVsanFilterOpCommand = _CspanVsanFilterOpCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 2),
    _CspanVsanFilterOpCommand_Type()
)
cspanVsanFilterOpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspanVsanFilterOpCommand.setStatus("current")
_CspanVsanFilterOpVsans2k_Type = FcList
_CspanVsanFilterOpVsans2k_Object = MibTableColumn
cspanVsanFilterOpVsans2k = _CspanVsanFilterOpVsans2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 3),
    _CspanVsanFilterOpVsans2k_Type()
)
cspanVsanFilterOpVsans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspanVsanFilterOpVsans2k.setStatus("current")
_CspanVsanFilterOpVsans4k_Type = FcList
_CspanVsanFilterOpVsans4k_Object = MibTableColumn
cspanVsanFilterOpVsans4k = _CspanVsanFilterOpVsans4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 1, 1, 7, 1, 4),
    _CspanVsanFilterOpVsans4k_Type()
)
cspanVsanFilterOpVsans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspanVsanFilterOpVsans4k.setStatus("current")
_CiscoFcSpanMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFcSpanMIBConformance = _CiscoFcSpanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2)
)
_CiscoFcSpanMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFcSpanMIBCompliances = _CiscoFcSpanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 1)
)
_CiscoFcSpanMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFcSpanMIBGroups = _CiscoFcSpanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2)
)

# Managed Objects groups

cspanScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 1)
)
cspanScalarsGroup.setObjects(
    ("CISCO-FC-SPAN-MIB", "cspanMaxSessions")
)
if mibBuilder.loadTexts:
    cspanScalarsGroup.setStatus("current")

cspanSessionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 2)
)
cspanSessionsGroup.setObjects(
      *(("CISCO-FC-SPAN-MIB", "cspanSessionDestIfIndex"),
        ("CISCO-FC-SPAN-MIB", "cspanSessionAdminStatus"),
        ("CISCO-FC-SPAN-MIB", "cspanSessionOperStatus"),
        ("CISCO-FC-SPAN-MIB", "cspanSessionInactiveReason"),
        ("CISCO-FC-SPAN-MIB", "cspanSessionRowStatus"))
)
if mibBuilder.loadTexts:
    cspanSessionsGroup.setStatus("current")

cspanSourceIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 3)
)
cspanSourceIfGroup.setObjects(
    ("CISCO-FC-SPAN-MIB", "cspanSourcesRowStatus")
)
if mibBuilder.loadTexts:
    cspanSourceIfGroup.setStatus("current")

cspanSourceVsanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 4)
)
cspanSourceVsanGroup.setObjects(
      *(("CISCO-FC-SPAN-MIB", "cspanSourcesVsans2k"),
        ("CISCO-FC-SPAN-MIB", "cspanSourcesVsans4k"))
)
if mibBuilder.loadTexts:
    cspanSourceVsanGroup.setStatus("current")

cspanSourceVsanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 5)
)
cspanSourceVsanCfgGroup.setObjects(
      *(("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgCommand"),
        ("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgVsans2k"),
        ("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgVsans4k"))
)
if mibBuilder.loadTexts:
    cspanSourceVsanCfgGroup.setStatus("current")

cspanVsanFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 6)
)
cspanVsanFilterGroup.setObjects(
      *(("CISCO-FC-SPAN-MIB", "cspanSourcesVsanCfgVsans2k"),
        ("CISCO-FC-SPAN-MIB", "cspanVsanFilterVsans2k"),
        ("CISCO-FC-SPAN-MIB", "cspanVsanFilterVsans4k"))
)
if mibBuilder.loadTexts:
    cspanVsanFilterGroup.setStatus("current")

cspanVsanFilterOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 2, 7)
)
cspanVsanFilterOpGroup.setObjects(
      *(("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpCommand"),
        ("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpVsans2k"),
        ("CISCO-FC-SPAN-MIB", "cspanVsanFilterOpVsans4k"))
)
if mibBuilder.loadTexts:
    cspanVsanFilterOpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFcSpanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 363, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFcSpanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-SPAN-MIB",
    **{"SessionIndex": SessionIndex,
       "ciscoFcSpanMIB": ciscoFcSpanMIB,
       "ciscoSpanMIBObjects": ciscoSpanMIBObjects,
       "cspanConfiguration": cspanConfiguration,
       "cspanMaxSessions": cspanMaxSessions,
       "cspanSessionTable": cspanSessionTable,
       "cspanSessionEntry": cspanSessionEntry,
       "cspanSessionIndex": cspanSessionIndex,
       "cspanSessionDestIfIndex": cspanSessionDestIfIndex,
       "cspanSessionAdminStatus": cspanSessionAdminStatus,
       "cspanSessionOperStatus": cspanSessionOperStatus,
       "cspanSessionInactiveReason": cspanSessionInactiveReason,
       "cspanSessionRowStatus": cspanSessionRowStatus,
       "cspanSourcesIfTable": cspanSourcesIfTable,
       "cspanSourcesIfEntry": cspanSourcesIfEntry,
       "cspanSourcesIfIndex": cspanSourcesIfIndex,
       "cspanSourcesDirection": cspanSourcesDirection,
       "cspanSourcesRowStatus": cspanSourcesRowStatus,
       "cspanSourcesVsanTable": cspanSourcesVsanTable,
       "cspanSourcesVsanEntry": cspanSourcesVsanEntry,
       "cspanSourcesVsans2k": cspanSourcesVsans2k,
       "cspanSourcesVsans4k": cspanSourcesVsans4k,
       "cspanSourcesVsanCfgTable": cspanSourcesVsanCfgTable,
       "cspanSourcesVsanCfgEntry": cspanSourcesVsanCfgEntry,
       "cspanSourcesVsanCfgSessIndex": cspanSourcesVsanCfgSessIndex,
       "cspanSourcesVsanCfgCommand": cspanSourcesVsanCfgCommand,
       "cspanSourcesVsanCfgVsans2k": cspanSourcesVsanCfgVsans2k,
       "cspanSourcesVsanCfgVsans4k": cspanSourcesVsanCfgVsans4k,
       "cspanVsanFilterTable": cspanVsanFilterTable,
       "cspanVsanFilterEntry": cspanVsanFilterEntry,
       "cspanVsanFilterSessIndex": cspanVsanFilterSessIndex,
       "cspanVsanFilterVsans2k": cspanVsanFilterVsans2k,
       "cspanVsanFilterVsans4k": cspanVsanFilterVsans4k,
       "cspanVsanFilterOpTable": cspanVsanFilterOpTable,
       "cspanVsanFilterOpEntry": cspanVsanFilterOpEntry,
       "cspanVsanFilterOpSessIndex": cspanVsanFilterOpSessIndex,
       "cspanVsanFilterOpCommand": cspanVsanFilterOpCommand,
       "cspanVsanFilterOpVsans2k": cspanVsanFilterOpVsans2k,
       "cspanVsanFilterOpVsans4k": cspanVsanFilterOpVsans4k,
       "ciscoFcSpanMIBConformance": ciscoFcSpanMIBConformance,
       "ciscoFcSpanMIBCompliances": ciscoFcSpanMIBCompliances,
       "ciscoFcSpanMIBCompliance": ciscoFcSpanMIBCompliance,
       "ciscoFcSpanMIBGroups": ciscoFcSpanMIBGroups,
       "cspanScalarsGroup": cspanScalarsGroup,
       "cspanSessionsGroup": cspanSessionsGroup,
       "cspanSourceIfGroup": cspanSourceIfGroup,
       "cspanSourceVsanGroup": cspanSourceVsanGroup,
       "cspanSourceVsanCfgGroup": cspanSourceVsanCfgGroup,
       "cspanVsanFilterGroup": cspanVsanFilterGroup,
       "cspanVsanFilterOpGroup": cspanVsanFilterOpGroup}
)
