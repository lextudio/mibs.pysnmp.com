# SNMP MIB module (CTRON-ROUTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ROUTERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:14 2024
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

(nwRouter,
 nwRtrHighLevelView,
 nwRtrMibs,
 nwRtrProtoSuites) = mibBuilder.importSymbols(
    "ROUTER-OIDS",
    "nwRouter",
    "nwRtrHighLevelView",
    "nwRtrMibs",
    "nwRtrProtoSuites")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NwRtrMibRevision_ObjectIdentity = ObjectIdentity
nwRtrMibRevision = _NwRtrMibRevision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 1)
)
_NwRtrMibRevText_Type = DisplayString
_NwRtrMibRevText_Object = MibScalar
nwRtrMibRevText = _NwRtrMibRevText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 1, 1),
    _NwRtrMibRevText_Type()
)
nwRtrMibRevText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrMibRevText.setStatus("mandatory")
_NwRtrStandardMibs_ObjectIdentity = ObjectIdentity
nwRtrStandardMibs = _NwRtrStandardMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 2)
)
_NwRtrStdMibTable_Object = MibTable
nwRtrStdMibTable = _NwRtrStdMibTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nwRtrStdMibTable.setStatus("mandatory")
_NwRtrStdMibEntry_Object = MibTableRow
nwRtrStdMibEntry = _NwRtrStdMibEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 2, 1, 1)
)
nwRtrStdMibEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwRtrStdMibIndex"),
)
if mibBuilder.loadTexts:
    nwRtrStdMibEntry.setStatus("mandatory")
_NwRtrStdMibIndex_Type = Integer32
_NwRtrStdMibIndex_Object = MibTableColumn
nwRtrStdMibIndex = _NwRtrStdMibIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 2, 1, 1, 1),
    _NwRtrStdMibIndex_Type()
)
nwRtrStdMibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrStdMibIndex.setStatus("mandatory")
_NwRtrStdMibIdentifier_Type = ObjectIdentifier
_NwRtrStdMibIdentifier_Object = MibTableColumn
nwRtrStdMibIdentifier = _NwRtrStdMibIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1, 2, 1, 1, 2),
    _NwRtrStdMibIdentifier_Type()
)
nwRtrStdMibIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrStdMibIdentifier.setStatus("mandatory")
_NwRtrApplicationView_ObjectIdentity = ObjectIdentity
nwRtrApplicationView = _NwRtrApplicationView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1)
)
_NwRtrApplicationSystem_ObjectIdentity = ObjectIdentity
nwRtrApplicationSystem = _NwRtrApplicationSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1)
)
_NwRtrAdminChanges_Type = Counter32
_NwRtrAdminChanges_Object = MibScalar
nwRtrAdminChanges = _NwRtrAdminChanges_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 1),
    _NwRtrAdminChanges_Type()
)
nwRtrAdminChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrAdminChanges.setStatus("mandatory")
_NwRouterSystemTable_Object = MibTable
nwRouterSystemTable = _NwRouterSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    nwRouterSystemTable.setStatus("mandatory")
_NwRouterEntry_Object = MibTableRow
nwRouterEntry = _NwRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1)
)
nwRouterEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwRouterInstance"),
)
if mibBuilder.loadTexts:
    nwRouterEntry.setStatus("mandatory")
_NwRouterInstance_Type = Integer32
_NwRouterInstance_Object = MibTableColumn
nwRouterInstance = _NwRouterInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 1),
    _NwRouterInstance_Type()
)
nwRouterInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterInstance.setStatus("mandatory")


class _NwRouterAdminStatus_Type(Integer32):
    """Custom type nwRouterAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwRouterAdminStatus_Type.__name__ = "Integer32"
_NwRouterAdminStatus_Object = MibTableColumn
nwRouterAdminStatus = _NwRouterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 2),
    _NwRouterAdminStatus_Type()
)
nwRouterAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterAdminStatus.setStatus("mandatory")


class _NwRouterOperStatus_Type(Integer32):
    """Custom type nwRouterOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwRouterOperStatus_Type.__name__ = "Integer32"
_NwRouterOperStatus_Object = MibTableColumn
nwRouterOperStatus = _NwRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 3),
    _NwRouterOperStatus_Type()
)
nwRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterOperStatus.setStatus("mandatory")
_NwRouterOperationalTime_Type = TimeTicks
_NwRouterOperationalTime_Object = MibTableColumn
nwRouterOperationalTime = _NwRouterOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 4),
    _NwRouterOperationalTime_Type()
)
nwRouterOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterOperationalTime.setStatus("mandatory")
_NwRouterEntMibGroup_Type = ObjectIdentifier
_NwRouterEntMibGroup_Object = MibTableColumn
nwRouterEntMibGroup = _NwRouterEntMibGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 5),
    _NwRouterEntMibGroup_Type()
)
nwRouterEntMibGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterEntMibGroup.setStatus("mandatory")
_NwRouterName_Type = DisplayString
_NwRouterName_Object = MibTableColumn
nwRouterName = _NwRouterName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 6),
    _NwRouterName_Type()
)
nwRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterName.setStatus("mandatory")
_NwRouterVersion_Type = DisplayString
_NwRouterVersion_Object = MibTableColumn
nwRouterVersion = _NwRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 7),
    _NwRouterVersion_Type()
)
nwRouterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterVersion.setStatus("mandatory")
_NwRouterIdentifier_Type = ObjectIdentifier
_NwRouterIdentifier_Object = MibTableColumn
nwRouterIdentifier = _NwRouterIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 2, 1, 8),
    _NwRouterIdentifier_Type()
)
nwRouterIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIdentifier.setStatus("mandatory")
_NwRtrVersion_Type = DisplayString
_NwRtrVersion_Object = MibScalar
nwRtrVersion = _NwRtrVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 1, 3),
    _NwRtrVersion_Type()
)
nwRtrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrVersion.setStatus("mandatory")
_NwRtrApplicationInterfaces_ObjectIdentity = ObjectIdentity
nwRtrApplicationInterfaces = _NwRtrApplicationInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2)
)
_NwRouterIfTable_Object = MibTable
nwRouterIfTable = _NwRouterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nwRouterIfTable.setStatus("mandatory")
_NwRouterIfEntry_Object = MibTableRow
nwRouterIfEntry = _NwRouterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1)
)
nwRouterIfEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwRouterIfIndex"),
    (0, "CTRON-ROUTERS-MIB", "nwRouterIfInstance"),
)
if mibBuilder.loadTexts:
    nwRouterIfEntry.setStatus("mandatory")
_NwRouterIfIndex_Type = Integer32
_NwRouterIfIndex_Object = MibTableColumn
nwRouterIfIndex = _NwRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1, 1),
    _NwRouterIfIndex_Type()
)
nwRouterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIfIndex.setStatus("mandatory")
_NwRouterIfInstance_Type = Integer32
_NwRouterIfInstance_Object = MibTableColumn
nwRouterIfInstance = _NwRouterIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1, 2),
    _NwRouterIfInstance_Type()
)
nwRouterIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIfInstance.setStatus("mandatory")


class _NwRouterIfAdminStatus_Type(Integer32):
    """Custom type nwRouterIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwRouterIfAdminStatus_Type.__name__ = "Integer32"
_NwRouterIfAdminStatus_Object = MibTableColumn
nwRouterIfAdminStatus = _NwRouterIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1, 3),
    _NwRouterIfAdminStatus_Type()
)
nwRouterIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIfAdminStatus.setStatus("mandatory")


class _NwRouterIfOperStatus_Type(Integer32):
    """Custom type nwRouterIfOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwRouterIfOperStatus_Type.__name__ = "Integer32"
_NwRouterIfOperStatus_Object = MibTableColumn
nwRouterIfOperStatus = _NwRouterIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1, 4),
    _NwRouterIfOperStatus_Type()
)
nwRouterIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIfOperStatus.setStatus("mandatory")
_NwRouterIfOperationalTime_Type = TimeTicks
_NwRouterIfOperationalTime_Object = MibTableColumn
nwRouterIfOperationalTime = _NwRouterIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1, 5),
    _NwRouterIfOperationalTime_Type()
)
nwRouterIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIfOperationalTime.setStatus("mandatory")
_NwRouterIfName_Type = DisplayString
_NwRouterIfName_Object = MibTableColumn
nwRouterIfName = _NwRouterIfName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 1, 2, 1, 1, 6),
    _NwRouterIfName_Type()
)
nwRouterIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRouterIfName.setStatus("mandatory")
_NwRtrRoutingView_ObjectIdentity = ObjectIdentity
nwRtrRoutingView = _NwRtrRoutingView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2)
)
_NwRtrRoutingSystem_ObjectIdentity = ObjectIdentity
nwRtrRoutingSystem = _NwRtrRoutingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1)
)
_NwRtgProtocolTable_Object = MibTable
nwRtgProtocolTable = _NwRtgProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nwRtgProtocolTable.setStatus("mandatory")
_NwRtgProtocolEntry_Object = MibTableRow
nwRtgProtocolEntry = _NwRtgProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1)
)
nwRtgProtocolEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwRtgProtocolRtrInstance"),
    (0, "CTRON-ROUTERS-MIB", "nwRtgProtocolInstance"),
)
if mibBuilder.loadTexts:
    nwRtgProtocolEntry.setStatus("mandatory")
_NwRtgProtocolRtrInstance_Type = Integer32
_NwRtgProtocolRtrInstance_Object = MibTableColumn
nwRtgProtocolRtrInstance = _NwRtgProtocolRtrInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 1),
    _NwRtgProtocolRtrInstance_Type()
)
nwRtgProtocolRtrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolRtrInstance.setStatus("mandatory")
_NwRtgProtocolInstance_Type = Integer32
_NwRtgProtocolInstance_Object = MibTableColumn
nwRtgProtocolInstance = _NwRtgProtocolInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 2),
    _NwRtgProtocolInstance_Type()
)
nwRtgProtocolInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolInstance.setStatus("mandatory")


class _NwRtgProtocolAdminStatus_Type(Integer32):
    """Custom type nwRtgProtocolAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwRtgProtocolAdminStatus_Type.__name__ = "Integer32"
_NwRtgProtocolAdminStatus_Object = MibTableColumn
nwRtgProtocolAdminStatus = _NwRtgProtocolAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 3),
    _NwRtgProtocolAdminStatus_Type()
)
nwRtgProtocolAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolAdminStatus.setStatus("mandatory")


class _NwRtgProtocolOperStatus_Type(Integer32):
    """Custom type nwRtgProtocolOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwRtgProtocolOperStatus_Type.__name__ = "Integer32"
_NwRtgProtocolOperStatus_Object = MibTableColumn
nwRtgProtocolOperStatus = _NwRtgProtocolOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 4),
    _NwRtgProtocolOperStatus_Type()
)
nwRtgProtocolOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolOperStatus.setStatus("mandatory")
_NwRtgProtocolOperationalTime_Type = TimeTicks
_NwRtgProtocolOperationalTime_Object = MibTableColumn
nwRtgProtocolOperationalTime = _NwRtgProtocolOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 5),
    _NwRtgProtocolOperationalTime_Type()
)
nwRtgProtocolOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolOperationalTime.setStatus("mandatory")
_NwRtgProtocolEntMibGroup_Type = ObjectIdentifier
_NwRtgProtocolEntMibGroup_Object = MibTableColumn
nwRtgProtocolEntMibGroup = _NwRtgProtocolEntMibGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 6),
    _NwRtgProtocolEntMibGroup_Type()
)
nwRtgProtocolEntMibGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolEntMibGroup.setStatus("mandatory")
_NwRtgProtocolName_Type = DisplayString
_NwRtgProtocolName_Object = MibTableColumn
nwRtgProtocolName = _NwRtgProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 7),
    _NwRtgProtocolName_Type()
)
nwRtgProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolName.setStatus("mandatory")
_NwRtgProtocolVersion_Type = DisplayString
_NwRtgProtocolVersion_Object = MibTableColumn
nwRtgProtocolVersion = _NwRtgProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 8),
    _NwRtgProtocolVersion_Type()
)
nwRtgProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolVersion.setStatus("mandatory")
_NwRtgProtocolIdentifier_Type = ObjectIdentifier
_NwRtgProtocolIdentifier_Object = MibTableColumn
nwRtgProtocolIdentifier = _NwRtgProtocolIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 1, 1, 1, 9),
    _NwRtgProtocolIdentifier_Type()
)
nwRtgProtocolIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIdentifier.setStatus("mandatory")
_NwRtrRoutingInterfaces_ObjectIdentity = ObjectIdentity
nwRtrRoutingInterfaces = _NwRtrRoutingInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2)
)
_NwRtgProtocolIfTable_Object = MibTable
nwRtgProtocolIfTable = _NwRtgProtocolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nwRtgProtocolIfTable.setStatus("mandatory")
_NwRtgProtocolIfEntry_Object = MibTableRow
nwRtgProtocolIfEntry = _NwRtgProtocolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1)
)
nwRtgProtocolIfEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwRtgProtocolIfIndex"),
    (0, "CTRON-ROUTERS-MIB", "nwRtgProtocolIfRtrInstance"),
    (0, "CTRON-ROUTERS-MIB", "nwRtgProtocolIfInstance"),
)
if mibBuilder.loadTexts:
    nwRtgProtocolIfEntry.setStatus("mandatory")
_NwRtgProtocolIfIndex_Type = Integer32
_NwRtgProtocolIfIndex_Object = MibTableColumn
nwRtgProtocolIfIndex = _NwRtgProtocolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 1),
    _NwRtgProtocolIfIndex_Type()
)
nwRtgProtocolIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfIndex.setStatus("mandatory")
_NwRtgProtocolIfRtrInstance_Type = Integer32
_NwRtgProtocolIfRtrInstance_Object = MibTableColumn
nwRtgProtocolIfRtrInstance = _NwRtgProtocolIfRtrInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 2),
    _NwRtgProtocolIfRtrInstance_Type()
)
nwRtgProtocolIfRtrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfRtrInstance.setStatus("mandatory")
_NwRtgProtocolIfInstance_Type = Integer32
_NwRtgProtocolIfInstance_Object = MibTableColumn
nwRtgProtocolIfInstance = _NwRtgProtocolIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 3),
    _NwRtgProtocolIfInstance_Type()
)
nwRtgProtocolIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfInstance.setStatus("mandatory")


class _NwRtgProtocolIfAdminStatus_Type(Integer32):
    """Custom type nwRtgProtocolIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwRtgProtocolIfAdminStatus_Type.__name__ = "Integer32"
_NwRtgProtocolIfAdminStatus_Object = MibTableColumn
nwRtgProtocolIfAdminStatus = _NwRtgProtocolIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 4),
    _NwRtgProtocolIfAdminStatus_Type()
)
nwRtgProtocolIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfAdminStatus.setStatus("mandatory")


class _NwRtgProtocolIfOperStatus_Type(Integer32):
    """Custom type nwRtgProtocolIfOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwRtgProtocolIfOperStatus_Type.__name__ = "Integer32"
_NwRtgProtocolIfOperStatus_Object = MibTableColumn
nwRtgProtocolIfOperStatus = _NwRtgProtocolIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 5),
    _NwRtgProtocolIfOperStatus_Type()
)
nwRtgProtocolIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfOperStatus.setStatus("mandatory")
_NwRtgProtocolIfOperationalTime_Type = TimeTicks
_NwRtgProtocolIfOperationalTime_Object = MibTableColumn
nwRtgProtocolIfOperationalTime = _NwRtgProtocolIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 6),
    _NwRtgProtocolIfOperationalTime_Type()
)
nwRtgProtocolIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfOperationalTime.setStatus("mandatory")
_NwRtgProtocolIfName_Type = DisplayString
_NwRtgProtocolIfName_Object = MibTableColumn
nwRtgProtocolIfName = _NwRtgProtocolIfName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 2, 2, 1, 1, 7),
    _NwRtgProtocolIfName_Type()
)
nwRtgProtocolIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtgProtocolIfName.setStatus("mandatory")
_NwRtrComponentView_ObjectIdentity = ObjectIdentity
nwRtrComponentView = _NwRtrComponentView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3)
)
_NwRtrComponentSystem_ObjectIdentity = ObjectIdentity
nwRtrComponentSystem = _NwRtrComponentSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1)
)
_NwComponentTable_Object = MibTable
nwComponentTable = _NwComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nwComponentTable.setStatus("mandatory")
_NwComponentEntry_Object = MibTableRow
nwComponentEntry = _NwComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1)
)
nwComponentEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwComponentRtrInstance"),
    (0, "CTRON-ROUTERS-MIB", "nwComponentInstance"),
)
if mibBuilder.loadTexts:
    nwComponentEntry.setStatus("mandatory")
_NwComponentRtrInstance_Type = Integer32
_NwComponentRtrInstance_Object = MibTableColumn
nwComponentRtrInstance = _NwComponentRtrInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 1),
    _NwComponentRtrInstance_Type()
)
nwComponentRtrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentRtrInstance.setStatus("mandatory")
_NwComponentInstance_Type = Integer32
_NwComponentInstance_Object = MibTableColumn
nwComponentInstance = _NwComponentInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 2),
    _NwComponentInstance_Type()
)
nwComponentInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentInstance.setStatus("mandatory")


class _NwComponentAdminStatus_Type(Integer32):
    """Custom type nwComponentAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwComponentAdminStatus_Type.__name__ = "Integer32"
_NwComponentAdminStatus_Object = MibTableColumn
nwComponentAdminStatus = _NwComponentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 3),
    _NwComponentAdminStatus_Type()
)
nwComponentAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentAdminStatus.setStatus("mandatory")


class _NwComponentOperStatus_Type(Integer32):
    """Custom type nwComponentOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwComponentOperStatus_Type.__name__ = "Integer32"
_NwComponentOperStatus_Object = MibTableColumn
nwComponentOperStatus = _NwComponentOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 4),
    _NwComponentOperStatus_Type()
)
nwComponentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentOperStatus.setStatus("mandatory")
_NwComponentOperationalTime_Type = TimeTicks
_NwComponentOperationalTime_Object = MibTableColumn
nwComponentOperationalTime = _NwComponentOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 5),
    _NwComponentOperationalTime_Type()
)
nwComponentOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentOperationalTime.setStatus("mandatory")
_NwComponentEntMibGroup_Type = ObjectIdentifier
_NwComponentEntMibGroup_Object = MibTableColumn
nwComponentEntMibGroup = _NwComponentEntMibGroup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 6),
    _NwComponentEntMibGroup_Type()
)
nwComponentEntMibGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentEntMibGroup.setStatus("mandatory")
_NwComponentName_Type = DisplayString
_NwComponentName_Object = MibTableColumn
nwComponentName = _NwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 7),
    _NwComponentName_Type()
)
nwComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentName.setStatus("mandatory")
_NwComponentVersion_Type = DisplayString
_NwComponentVersion_Object = MibTableColumn
nwComponentVersion = _NwComponentVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 8),
    _NwComponentVersion_Type()
)
nwComponentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentVersion.setStatus("mandatory")
_NwComponentIdentifier_Type = ObjectIdentifier
_NwComponentIdentifier_Object = MibTableColumn
nwComponentIdentifier = _NwComponentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 1, 1, 1, 9),
    _NwComponentIdentifier_Type()
)
nwComponentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIdentifier.setStatus("mandatory")
_NwRtrComponentInterfaces_ObjectIdentity = ObjectIdentity
nwRtrComponentInterfaces = _NwRtrComponentInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2)
)
_NwComponentIfTable_Object = MibTable
nwComponentIfTable = _NwComponentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    nwComponentIfTable.setStatus("mandatory")
_NwComponentIfEntry_Object = MibTableRow
nwComponentIfEntry = _NwComponentIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1)
)
nwComponentIfEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwComponentIfIndex"),
    (0, "CTRON-ROUTERS-MIB", "nwComponentIfRtrInstance"),
    (0, "CTRON-ROUTERS-MIB", "nwComponentIfInstance"),
)
if mibBuilder.loadTexts:
    nwComponentIfEntry.setStatus("mandatory")
_NwComponentIfIndex_Type = Integer32
_NwComponentIfIndex_Object = MibTableColumn
nwComponentIfIndex = _NwComponentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 1),
    _NwComponentIfIndex_Type()
)
nwComponentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfIndex.setStatus("mandatory")
_NwComponentIfRtrInstance_Type = Integer32
_NwComponentIfRtrInstance_Object = MibTableColumn
nwComponentIfRtrInstance = _NwComponentIfRtrInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 2),
    _NwComponentIfRtrInstance_Type()
)
nwComponentIfRtrInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfRtrInstance.setStatus("mandatory")
_NwComponentIfInstance_Type = Integer32
_NwComponentIfInstance_Object = MibTableColumn
nwComponentIfInstance = _NwComponentIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 3),
    _NwComponentIfInstance_Type()
)
nwComponentIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfInstance.setStatus("mandatory")


class _NwComponentIfAdminStatus_Type(Integer32):
    """Custom type nwComponentIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwComponentIfAdminStatus_Type.__name__ = "Integer32"
_NwComponentIfAdminStatus_Object = MibTableColumn
nwComponentIfAdminStatus = _NwComponentIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 4),
    _NwComponentIfAdminStatus_Type()
)
nwComponentIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfAdminStatus.setStatus("mandatory")


class _NwComponentIfOperStatus_Type(Integer32):
    """Custom type nwComponentIfOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_NwComponentIfOperStatus_Type.__name__ = "Integer32"
_NwComponentIfOperStatus_Object = MibTableColumn
nwComponentIfOperStatus = _NwComponentIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 5),
    _NwComponentIfOperStatus_Type()
)
nwComponentIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfOperStatus.setStatus("mandatory")
_NwComponentIfOperationalTime_Type = TimeTicks
_NwComponentIfOperationalTime_Object = MibTableColumn
nwComponentIfOperationalTime = _NwComponentIfOperationalTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 6),
    _NwComponentIfOperationalTime_Type()
)
nwComponentIfOperationalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfOperationalTime.setStatus("mandatory")
_NwComponentIfName_Type = DisplayString
_NwComponentIfName_Object = MibTableColumn
nwComponentIfName = _NwComponentIfName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 3, 2, 1, 1, 7),
    _NwComponentIfName_Type()
)
nwComponentIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwComponentIfName.setStatus("mandatory")
_NwRtrCountersView_ObjectIdentity = ObjectIdentity
nwRtrCountersView = _NwRtrCountersView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4)
)
_NwRtrCountersControl_ObjectIdentity = ObjectIdentity
nwRtrCountersControl = _NwRtrCountersControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 1)
)
_NwRtrInterfaceCounters_ObjectIdentity = ObjectIdentity
nwRtrInterfaceCounters = _NwRtrInterfaceCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2)
)
_NwRtrIfFwdCtrTable_Object = MibTable
nwRtrIfFwdCtrTable = _NwRtrIfFwdCtrTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrTable.setStatus("mandatory")
_NwRtrIfFwdCtrEntry_Object = MibTableRow
nwRtrIfFwdCtrEntry = _NwRtrIfFwdCtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1)
)
nwRtrIfFwdCtrEntry.setIndexNames(
    (0, "CTRON-ROUTERS-MIB", "nwRtrIfFwdCtrIfIndex"),
)
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrEntry.setStatus("mandatory")
_NwRtrIfFwdCtrIfIndex_Type = Integer32
_NwRtrIfFwdCtrIfIndex_Object = MibTableColumn
nwRtrIfFwdCtrIfIndex = _NwRtrIfFwdCtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 1),
    _NwRtrIfFwdCtrIfIndex_Type()
)
nwRtrIfFwdCtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrIfIndex.setStatus("mandatory")


class _NwRtrIfFwdCtrOperStatus_Type(Integer32):
    """Custom type nwRtrIfFwdCtrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_NwRtrIfFwdCtrOperStatus_Type.__name__ = "Integer32"
_NwRtrIfFwdCtrOperStatus_Object = MibTableColumn
nwRtrIfFwdCtrOperStatus = _NwRtrIfFwdCtrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 2),
    _NwRtrIfFwdCtrOperStatus_Type()
)
nwRtrIfFwdCtrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrOperStatus.setStatus("mandatory")
_NwRtrIfFwdCtrInPkts_Type = Counter32
_NwRtrIfFwdCtrInPkts_Object = MibTableColumn
nwRtrIfFwdCtrInPkts = _NwRtrIfFwdCtrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 3),
    _NwRtrIfFwdCtrInPkts_Type()
)
nwRtrIfFwdCtrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrInPkts.setStatus("mandatory")
_NwRtrIfFwdCtrOutPkts_Type = Counter32
_NwRtrIfFwdCtrOutPkts_Object = MibTableColumn
nwRtrIfFwdCtrOutPkts = _NwRtrIfFwdCtrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 4),
    _NwRtrIfFwdCtrOutPkts_Type()
)
nwRtrIfFwdCtrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrOutPkts.setStatus("mandatory")
_NwRtrIfFwdCtrFwdPkts_Type = Counter32
_NwRtrIfFwdCtrFwdPkts_Object = MibTableColumn
nwRtrIfFwdCtrFwdPkts = _NwRtrIfFwdCtrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 5),
    _NwRtrIfFwdCtrFwdPkts_Type()
)
nwRtrIfFwdCtrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrFwdPkts.setStatus("mandatory")
_NwRtrIfFwdCtrFilteredPkts_Type = Counter32
_NwRtrIfFwdCtrFilteredPkts_Object = MibTableColumn
nwRtrIfFwdCtrFilteredPkts = _NwRtrIfFwdCtrFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 6),
    _NwRtrIfFwdCtrFilteredPkts_Type()
)
nwRtrIfFwdCtrFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrFilteredPkts.setStatus("mandatory")
_NwRtrIfFwdCtrDiscardPkts_Type = Counter32
_NwRtrIfFwdCtrDiscardPkts_Object = MibTableColumn
nwRtrIfFwdCtrDiscardPkts = _NwRtrIfFwdCtrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 7),
    _NwRtrIfFwdCtrDiscardPkts_Type()
)
nwRtrIfFwdCtrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrDiscardPkts.setStatus("mandatory")
_NwRtrIfFwdCtrAddrErrPkts_Type = Counter32
_NwRtrIfFwdCtrAddrErrPkts_Object = MibTableColumn
nwRtrIfFwdCtrAddrErrPkts = _NwRtrIfFwdCtrAddrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 8),
    _NwRtrIfFwdCtrAddrErrPkts_Type()
)
nwRtrIfFwdCtrAddrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrAddrErrPkts.setStatus("mandatory")
_NwRtrIfFwdCtrLenErrPkts_Type = Counter32
_NwRtrIfFwdCtrLenErrPkts_Object = MibTableColumn
nwRtrIfFwdCtrLenErrPkts = _NwRtrIfFwdCtrLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 9),
    _NwRtrIfFwdCtrLenErrPkts_Type()
)
nwRtrIfFwdCtrLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrLenErrPkts.setStatus("mandatory")
_NwRtrIfFwdCtrHdrErrPkts_Type = Counter32
_NwRtrIfFwdCtrHdrErrPkts_Object = MibTableColumn
nwRtrIfFwdCtrHdrErrPkts = _NwRtrIfFwdCtrHdrErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 10),
    _NwRtrIfFwdCtrHdrErrPkts_Type()
)
nwRtrIfFwdCtrHdrErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHdrErrPkts.setStatus("mandatory")
_NwRtrIfFwdCtrInBytes_Type = Counter32
_NwRtrIfFwdCtrInBytes_Object = MibTableColumn
nwRtrIfFwdCtrInBytes = _NwRtrIfFwdCtrInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 11),
    _NwRtrIfFwdCtrInBytes_Type()
)
nwRtrIfFwdCtrInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrInBytes.setStatus("mandatory")
_NwRtrIfFwdCtrOutBytes_Type = Counter32
_NwRtrIfFwdCtrOutBytes_Object = MibTableColumn
nwRtrIfFwdCtrOutBytes = _NwRtrIfFwdCtrOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 12),
    _NwRtrIfFwdCtrOutBytes_Type()
)
nwRtrIfFwdCtrOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrOutBytes.setStatus("mandatory")
_NwRtrIfFwdCtrFwdBytes_Type = Counter32
_NwRtrIfFwdCtrFwdBytes_Object = MibTableColumn
nwRtrIfFwdCtrFwdBytes = _NwRtrIfFwdCtrFwdBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 13),
    _NwRtrIfFwdCtrFwdBytes_Type()
)
nwRtrIfFwdCtrFwdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrFwdBytes.setStatus("mandatory")
_NwRtrIfFwdCtrFilteredBytes_Type = Counter32
_NwRtrIfFwdCtrFilteredBytes_Object = MibTableColumn
nwRtrIfFwdCtrFilteredBytes = _NwRtrIfFwdCtrFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 14),
    _NwRtrIfFwdCtrFilteredBytes_Type()
)
nwRtrIfFwdCtrFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrFilteredBytes.setStatus("mandatory")
_NwRtrIfFwdCtrDiscardBytes_Type = Counter32
_NwRtrIfFwdCtrDiscardBytes_Object = MibTableColumn
nwRtrIfFwdCtrDiscardBytes = _NwRtrIfFwdCtrDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 15),
    _NwRtrIfFwdCtrDiscardBytes_Type()
)
nwRtrIfFwdCtrDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrDiscardBytes.setStatus("mandatory")
_NwRtrIfFwdCtrHostInPkts_Type = Counter32
_NwRtrIfFwdCtrHostInPkts_Object = MibTableColumn
nwRtrIfFwdCtrHostInPkts = _NwRtrIfFwdCtrHostInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 16),
    _NwRtrIfFwdCtrHostInPkts_Type()
)
nwRtrIfFwdCtrHostInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHostInPkts.setStatus("mandatory")
_NwRtrIfFwdCtrHostOutPkts_Type = Counter32
_NwRtrIfFwdCtrHostOutPkts_Object = MibTableColumn
nwRtrIfFwdCtrHostOutPkts = _NwRtrIfFwdCtrHostOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 17),
    _NwRtrIfFwdCtrHostOutPkts_Type()
)
nwRtrIfFwdCtrHostOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHostOutPkts.setStatus("mandatory")
_NwRtrIfFwdCtrHostDiscardPkts_Type = Counter32
_NwRtrIfFwdCtrHostDiscardPkts_Object = MibTableColumn
nwRtrIfFwdCtrHostDiscardPkts = _NwRtrIfFwdCtrHostDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 18),
    _NwRtrIfFwdCtrHostDiscardPkts_Type()
)
nwRtrIfFwdCtrHostDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHostDiscardPkts.setStatus("mandatory")
_NwRtrIfFwdCtrHostInBytes_Type = Counter32
_NwRtrIfFwdCtrHostInBytes_Object = MibTableColumn
nwRtrIfFwdCtrHostInBytes = _NwRtrIfFwdCtrHostInBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 19),
    _NwRtrIfFwdCtrHostInBytes_Type()
)
nwRtrIfFwdCtrHostInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHostInBytes.setStatus("mandatory")
_NwRtrIfFwdCtrHostOutBytes_Type = Counter32
_NwRtrIfFwdCtrHostOutBytes_Object = MibTableColumn
nwRtrIfFwdCtrHostOutBytes = _NwRtrIfFwdCtrHostOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 20),
    _NwRtrIfFwdCtrHostOutBytes_Type()
)
nwRtrIfFwdCtrHostOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHostOutBytes.setStatus("mandatory")
_NwRtrIfFwdCtrHostDiscardBytes_Type = Counter32
_NwRtrIfFwdCtrHostDiscardBytes_Object = MibTableColumn
nwRtrIfFwdCtrHostDiscardBytes = _NwRtrIfFwdCtrHostDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2, 4, 2, 1, 1, 21),
    _NwRtrIfFwdCtrHostDiscardBytes_Type()
)
nwRtrIfFwdCtrHostDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwRtrIfFwdCtrHostDiscardBytes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ROUTERS-MIB",
    **{"nwRtrMibRevision": nwRtrMibRevision,
       "nwRtrMibRevText": nwRtrMibRevText,
       "nwRtrStandardMibs": nwRtrStandardMibs,
       "nwRtrStdMibTable": nwRtrStdMibTable,
       "nwRtrStdMibEntry": nwRtrStdMibEntry,
       "nwRtrStdMibIndex": nwRtrStdMibIndex,
       "nwRtrStdMibIdentifier": nwRtrStdMibIdentifier,
       "nwRtrApplicationView": nwRtrApplicationView,
       "nwRtrApplicationSystem": nwRtrApplicationSystem,
       "nwRtrAdminChanges": nwRtrAdminChanges,
       "nwRouterSystemTable": nwRouterSystemTable,
       "nwRouterEntry": nwRouterEntry,
       "nwRouterInstance": nwRouterInstance,
       "nwRouterAdminStatus": nwRouterAdminStatus,
       "nwRouterOperStatus": nwRouterOperStatus,
       "nwRouterOperationalTime": nwRouterOperationalTime,
       "nwRouterEntMibGroup": nwRouterEntMibGroup,
       "nwRouterName": nwRouterName,
       "nwRouterVersion": nwRouterVersion,
       "nwRouterIdentifier": nwRouterIdentifier,
       "nwRtrVersion": nwRtrVersion,
       "nwRtrApplicationInterfaces": nwRtrApplicationInterfaces,
       "nwRouterIfTable": nwRouterIfTable,
       "nwRouterIfEntry": nwRouterIfEntry,
       "nwRouterIfIndex": nwRouterIfIndex,
       "nwRouterIfInstance": nwRouterIfInstance,
       "nwRouterIfAdminStatus": nwRouterIfAdminStatus,
       "nwRouterIfOperStatus": nwRouterIfOperStatus,
       "nwRouterIfOperationalTime": nwRouterIfOperationalTime,
       "nwRouterIfName": nwRouterIfName,
       "nwRtrRoutingView": nwRtrRoutingView,
       "nwRtrRoutingSystem": nwRtrRoutingSystem,
       "nwRtgProtocolTable": nwRtgProtocolTable,
       "nwRtgProtocolEntry": nwRtgProtocolEntry,
       "nwRtgProtocolRtrInstance": nwRtgProtocolRtrInstance,
       "nwRtgProtocolInstance": nwRtgProtocolInstance,
       "nwRtgProtocolAdminStatus": nwRtgProtocolAdminStatus,
       "nwRtgProtocolOperStatus": nwRtgProtocolOperStatus,
       "nwRtgProtocolOperationalTime": nwRtgProtocolOperationalTime,
       "nwRtgProtocolEntMibGroup": nwRtgProtocolEntMibGroup,
       "nwRtgProtocolName": nwRtgProtocolName,
       "nwRtgProtocolVersion": nwRtgProtocolVersion,
       "nwRtgProtocolIdentifier": nwRtgProtocolIdentifier,
       "nwRtrRoutingInterfaces": nwRtrRoutingInterfaces,
       "nwRtgProtocolIfTable": nwRtgProtocolIfTable,
       "nwRtgProtocolIfEntry": nwRtgProtocolIfEntry,
       "nwRtgProtocolIfIndex": nwRtgProtocolIfIndex,
       "nwRtgProtocolIfRtrInstance": nwRtgProtocolIfRtrInstance,
       "nwRtgProtocolIfInstance": nwRtgProtocolIfInstance,
       "nwRtgProtocolIfAdminStatus": nwRtgProtocolIfAdminStatus,
       "nwRtgProtocolIfOperStatus": nwRtgProtocolIfOperStatus,
       "nwRtgProtocolIfOperationalTime": nwRtgProtocolIfOperationalTime,
       "nwRtgProtocolIfName": nwRtgProtocolIfName,
       "nwRtrComponentView": nwRtrComponentView,
       "nwRtrComponentSystem": nwRtrComponentSystem,
       "nwComponentTable": nwComponentTable,
       "nwComponentEntry": nwComponentEntry,
       "nwComponentRtrInstance": nwComponentRtrInstance,
       "nwComponentInstance": nwComponentInstance,
       "nwComponentAdminStatus": nwComponentAdminStatus,
       "nwComponentOperStatus": nwComponentOperStatus,
       "nwComponentOperationalTime": nwComponentOperationalTime,
       "nwComponentEntMibGroup": nwComponentEntMibGroup,
       "nwComponentName": nwComponentName,
       "nwComponentVersion": nwComponentVersion,
       "nwComponentIdentifier": nwComponentIdentifier,
       "nwRtrComponentInterfaces": nwRtrComponentInterfaces,
       "nwComponentIfTable": nwComponentIfTable,
       "nwComponentIfEntry": nwComponentIfEntry,
       "nwComponentIfIndex": nwComponentIfIndex,
       "nwComponentIfRtrInstance": nwComponentIfRtrInstance,
       "nwComponentIfInstance": nwComponentIfInstance,
       "nwComponentIfAdminStatus": nwComponentIfAdminStatus,
       "nwComponentIfOperStatus": nwComponentIfOperStatus,
       "nwComponentIfOperationalTime": nwComponentIfOperationalTime,
       "nwComponentIfName": nwComponentIfName,
       "nwRtrCountersView": nwRtrCountersView,
       "nwRtrCountersControl": nwRtrCountersControl,
       "nwRtrInterfaceCounters": nwRtrInterfaceCounters,
       "nwRtrIfFwdCtrTable": nwRtrIfFwdCtrTable,
       "nwRtrIfFwdCtrEntry": nwRtrIfFwdCtrEntry,
       "nwRtrIfFwdCtrIfIndex": nwRtrIfFwdCtrIfIndex,
       "nwRtrIfFwdCtrOperStatus": nwRtrIfFwdCtrOperStatus,
       "nwRtrIfFwdCtrInPkts": nwRtrIfFwdCtrInPkts,
       "nwRtrIfFwdCtrOutPkts": nwRtrIfFwdCtrOutPkts,
       "nwRtrIfFwdCtrFwdPkts": nwRtrIfFwdCtrFwdPkts,
       "nwRtrIfFwdCtrFilteredPkts": nwRtrIfFwdCtrFilteredPkts,
       "nwRtrIfFwdCtrDiscardPkts": nwRtrIfFwdCtrDiscardPkts,
       "nwRtrIfFwdCtrAddrErrPkts": nwRtrIfFwdCtrAddrErrPkts,
       "nwRtrIfFwdCtrLenErrPkts": nwRtrIfFwdCtrLenErrPkts,
       "nwRtrIfFwdCtrHdrErrPkts": nwRtrIfFwdCtrHdrErrPkts,
       "nwRtrIfFwdCtrInBytes": nwRtrIfFwdCtrInBytes,
       "nwRtrIfFwdCtrOutBytes": nwRtrIfFwdCtrOutBytes,
       "nwRtrIfFwdCtrFwdBytes": nwRtrIfFwdCtrFwdBytes,
       "nwRtrIfFwdCtrFilteredBytes": nwRtrIfFwdCtrFilteredBytes,
       "nwRtrIfFwdCtrDiscardBytes": nwRtrIfFwdCtrDiscardBytes,
       "nwRtrIfFwdCtrHostInPkts": nwRtrIfFwdCtrHostInPkts,
       "nwRtrIfFwdCtrHostOutPkts": nwRtrIfFwdCtrHostOutPkts,
       "nwRtrIfFwdCtrHostDiscardPkts": nwRtrIfFwdCtrHostDiscardPkts,
       "nwRtrIfFwdCtrHostInBytes": nwRtrIfFwdCtrHostInBytes,
       "nwRtrIfFwdCtrHostOutBytes": nwRtrIfFwdCtrHostOutBytes,
       "nwRtrIfFwdCtrHostDiscardBytes": nwRtrIfFwdCtrHostDiscardBytes}
)
