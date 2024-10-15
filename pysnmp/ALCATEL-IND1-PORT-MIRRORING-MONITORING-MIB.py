# SNMP MIB module (ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:50 2024
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

(softentIND1PortMirroringMonitoring,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1PortMirroringMonitoring")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(sFlowCpEntry,
 sFlowFsEntry) = mibBuilder.importSymbols(
    "SFLOW-MIB",
    "sFlowCpEntry",
    "sFlowFsEntry")

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

alcatelIND1PortMirrorMonitoringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1)
)
alcatelIND1PortMirrorMonitoringMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MirMonErrorIds(Integer32, TextualConvention):
    status = "current"
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
        *(("hwQError", 3),
          ("other", 1),
          ("swQError", 4),
          ("wrongSession", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PortMirMonMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1PortMirMonMIBNotifications = _AlcatelIND1PortMirMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMirMonMIBNotifications.setStatus("current")
_AlcatelIND1PortMirMonMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PortMirMonMIBObjects = _AlcatelIND1PortMirMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMirMonMIBObjects.setStatus("current")
_MirmonMirroring_ObjectIdentity = ObjectIdentity
mirmonMirroring = _MirmonMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")


class _MirrorSessionNumber_Type(Integer32):
    """Custom type mirrorSessionNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MirrorSessionNumber_Type.__name__ = "Integer32"
_MirrorSessionNumber_Object = MibTableColumn
mirrorSessionNumber = _MirrorSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 1),
    _MirrorSessionNumber_Type()
)
mirrorSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorSessionNumber.setStatus("current")
_MirrorMirroredIfindex_Type = InterfaceIndex
_MirrorMirroredIfindex_Object = MibTableColumn
mirrorMirroredIfindex = _MirrorMirroredIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 2),
    _MirrorMirroredIfindex_Type()
)
mirrorMirroredIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorMirroredIfindex.setStatus("deprecated")
_MirrorMirroringIfindex_Type = InterfaceIndex
_MirrorMirroringIfindex_Object = MibTableColumn
mirrorMirroringIfindex = _MirrorMirroringIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 3),
    _MirrorMirroringIfindex_Type()
)
mirrorMirroringIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorMirroringIfindex.setStatus("current")


class _MirrorStatus_Type(Integer32):
    """Custom type mirrorStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MirrorStatus_Type.__name__ = "Integer32"
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")


class _MirrorUnblockedVLAN_Type(Integer32):
    """Custom type mirrorUnblockedVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MirrorUnblockedVLAN_Type.__name__ = "Integer32"
_MirrorUnblockedVLAN_Object = MibTableColumn
mirrorUnblockedVLAN = _MirrorUnblockedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 5),
    _MirrorUnblockedVLAN_Type()
)
mirrorUnblockedVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorUnblockedVLAN.setStatus("current")
_MirrorRowStatus_Type = RowStatus
_MirrorRowStatus_Object = MibTableColumn
mirrorRowStatus = _MirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 6),
    _MirrorRowStatus_Type()
)
mirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorRowStatus.setStatus("current")


class _MirrorDirection_Type(Integer32):
    """Custom type mirrorDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("inport", 1),
          ("outport", 2))
    )


_MirrorDirection_Type.__name__ = "Integer32"
_MirrorDirection_Object = MibTableColumn
mirrorDirection = _MirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 7),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("deprecated")


class _MirrorSessOperStatus_Type(Integer32):
    """Custom type mirrorSessOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MirrorSessOperStatus_Type.__name__ = "Integer32"
_MirrorSessOperStatus_Object = MibTableColumn
mirrorSessOperStatus = _MirrorSessOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 8),
    _MirrorSessOperStatus_Type()
)
mirrorSessOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorSessOperStatus.setStatus("current")


class _MirrorTaggedVLAN_Type(Integer32):
    """Custom type mirrorTaggedVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MirrorTaggedVLAN_Type.__name__ = "Integer32"
_MirrorTaggedVLAN_Object = MibTableColumn
mirrorTaggedVLAN = _MirrorTaggedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 9),
    _MirrorTaggedVLAN_Type()
)
mirrorTaggedVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorTaggedVLAN.setStatus("current")
_MirrorSrcTable_Object = MibTable
mirrorSrcTable = _MirrorSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mirrorSrcTable.setStatus("current")
_MirrorSrcEntry_Object = MibTableRow
mirrorSrcEntry = _MirrorSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1)
)
mirrorSrcEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"),
    (0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcMirroredIf"),
)
if mibBuilder.loadTexts:
    mirrorSrcEntry.setStatus("current")
_MirrorSrcMirroredIf_Type = InterfaceIndex
_MirrorSrcMirroredIf_Object = MibTableColumn
mirrorSrcMirroredIf = _MirrorSrcMirroredIf_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 1),
    _MirrorSrcMirroredIf_Type()
)
mirrorSrcMirroredIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorSrcMirroredIf.setStatus("current")


class _MirrorSrcStatus_Type(Integer32):
    """Custom type mirrorSrcStatus based on Integer32"""
    defaultValue = 2

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


_MirrorSrcStatus_Type.__name__ = "Integer32"
_MirrorSrcStatus_Object = MibTableColumn
mirrorSrcStatus = _MirrorSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 2),
    _MirrorSrcStatus_Type()
)
mirrorSrcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorSrcStatus.setStatus("current")


class _MirrorSrcDirection_Type(Integer32):
    """Custom type mirrorSrcDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("inport", 1),
          ("outport", 2))
    )


_MirrorSrcDirection_Type.__name__ = "Integer32"
_MirrorSrcDirection_Object = MibTableColumn
mirrorSrcDirection = _MirrorSrcDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 3),
    _MirrorSrcDirection_Type()
)
mirrorSrcDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorSrcDirection.setStatus("current")
_MirrorSrcRowStatus_Type = RowStatus
_MirrorSrcRowStatus_Object = MibTableColumn
mirrorSrcRowStatus = _MirrorSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 4),
    _MirrorSrcRowStatus_Type()
)
mirrorSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorSrcRowStatus.setStatus("current")


class _MirrorSrcOperStatus_Type(Integer32):
    """Custom type mirrorSrcOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MirrorSrcOperStatus_Type.__name__ = "Integer32"
_MirrorSrcOperStatus_Object = MibTableColumn
mirrorSrcOperStatus = _MirrorSrcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 5),
    _MirrorSrcOperStatus_Type()
)
mirrorSrcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorSrcOperStatus.setStatus("current")
_MirmonMonitoring_ObjectIdentity = ObjectIdentity
mirmonMonitoring = _MirmonMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2)
)
_MonitorTable_Object = MibTable
monitorTable = _MonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    monitorTable.setStatus("current")
_MonitorEntry_Object = MibTableRow
monitorEntry = _MonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1)
)
monitorEntry.setIndexNames(
    (0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorSessionNumber"),
)
if mibBuilder.loadTexts:
    monitorEntry.setStatus("current")


class _MonitorSessionNumber_Type(Integer32):
    """Custom type monitorSessionNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MonitorSessionNumber_Type.__name__ = "Integer32"
_MonitorSessionNumber_Object = MibTableColumn
monitorSessionNumber = _MonitorSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 1),
    _MonitorSessionNumber_Type()
)
monitorSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorSessionNumber.setStatus("current")


class _MonitorIfindex_Type(InterfaceIndex):
    """Custom type monitorIfindex based on InterfaceIndex"""
    defaultValue = 1


_MonitorIfindex_Object = MibTableColumn
monitorIfindex = _MonitorIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 2),
    _MonitorIfindex_Type()
)
monitorIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorIfindex.setStatus("current")


class _MonitorFileStatus_Type(Integer32):
    """Custom type monitorFileStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MonitorFileStatus_Type.__name__ = "Integer32"
_MonitorFileStatus_Object = MibTableColumn
monitorFileStatus = _MonitorFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 3),
    _MonitorFileStatus_Type()
)
monitorFileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorFileStatus.setStatus("current")


class _MonitorFileName_Type(SnmpAdminString):
    """Custom type monitorFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MonitorFileName_Type.__name__ = "SnmpAdminString"
_MonitorFileName_Object = MibTableColumn
monitorFileName = _MonitorFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 4),
    _MonitorFileName_Type()
)
monitorFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorFileName.setStatus("current")


class _MonitorFileSize_Type(Integer32):
    """Custom type monitorFileSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MonitorFileSize_Type.__name__ = "Integer32"
_MonitorFileSize_Object = MibTableColumn
monitorFileSize = _MonitorFileSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 5),
    _MonitorFileSize_Type()
)
monitorFileSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorFileSize.setStatus("current")


class _MonitorScreenStatus_Type(Integer32):
    """Custom type monitorScreenStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MonitorScreenStatus_Type.__name__ = "Integer32"
_MonitorScreenStatus_Object = MibTableColumn
monitorScreenStatus = _MonitorScreenStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 6),
    _MonitorScreenStatus_Type()
)
monitorScreenStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorScreenStatus.setStatus("current")


class _MonitorScreenLine_Type(Integer32):
    """Custom type monitorScreenLine based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MonitorScreenLine_Type.__name__ = "Integer32"
_MonitorScreenLine_Object = MibTableColumn
monitorScreenLine = _MonitorScreenLine_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 7),
    _MonitorScreenLine_Type()
)
monitorScreenLine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorScreenLine.setStatus("current")


class _MonitorTrafficType_Type(Integer32):
    """Custom type monitorTrafficType based on Integer32"""
    defaultValue = 1

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
        *(("all", 1),
          ("broadcast", 4),
          ("multibroad", 7),
          ("multicast", 3),
          ("unibroad", 6),
          ("unicast", 2),
          ("unimulti", 5))
    )


_MonitorTrafficType_Type.__name__ = "Integer32"
_MonitorTrafficType_Object = MibTableColumn
monitorTrafficType = _MonitorTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 8),
    _MonitorTrafficType_Type()
)
monitorTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorTrafficType.setStatus("current")


class _MonitorStatus_Type(Integer32):
    """Custom type monitorStatus based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("suspended", 3))
    )


_MonitorStatus_Type.__name__ = "Integer32"
_MonitorStatus_Object = MibTableColumn
monitorStatus = _MonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 9),
    _MonitorStatus_Type()
)
monitorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorStatus.setStatus("current")


class _MonitorFileOverWrite_Type(Integer32):
    """Custom type monitorFileOverWrite based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MonitorFileOverWrite_Type.__name__ = "Integer32"
_MonitorFileOverWrite_Object = MibTableColumn
monitorFileOverWrite = _MonitorFileOverWrite_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 10),
    _MonitorFileOverWrite_Type()
)
monitorFileOverWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorFileOverWrite.setStatus("current")


class _MonitorDirection_Type(Integer32):
    """Custom type monitorDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("inport", 1),
          ("outport", 2))
    )


_MonitorDirection_Type.__name__ = "Integer32"
_MonitorDirection_Object = MibTableColumn
monitorDirection = _MonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 11),
    _MonitorDirection_Type()
)
monitorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorDirection.setStatus("current")


class _MonitorTimeout_Type(Integer32):
    """Custom type monitorTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MonitorTimeout_Type.__name__ = "Integer32"
_MonitorTimeout_Object = MibTableColumn
monitorTimeout = _MonitorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 12),
    _MonitorTimeout_Type()
)
monitorTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorTimeout.setStatus("current")
_MonitorRowStatus_Type = RowStatus
_MonitorRowStatus_Object = MibTableColumn
monitorRowStatus = _MonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 13),
    _MonitorRowStatus_Type()
)
monitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorRowStatus.setStatus("current")


class _MonitorCaptureType_Type(Integer32):
    """Custom type monitorCaptureType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("brief", 1),
          ("full", 2))
    )


_MonitorCaptureType_Type.__name__ = "Integer32"
_MonitorCaptureType_Object = MibTableColumn
monitorCaptureType = _MonitorCaptureType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 14),
    _MonitorCaptureType_Type()
)
monitorCaptureType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    monitorCaptureType.setStatus("current")
_MirmonNotificationVars_ObjectIdentity = ObjectIdentity
mirmonNotificationVars = _MirmonNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3)
)


class _MirmonPrimarySlot_Type(Integer32):
    """Custom type mirmonPrimarySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MirmonPrimarySlot_Type.__name__ = "Integer32"
_MirmonPrimarySlot_Object = MibScalar
mirmonPrimarySlot = _MirmonPrimarySlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 1),
    _MirmonPrimarySlot_Type()
)
mirmonPrimarySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirmonPrimarySlot.setStatus("current")


class _MirmonPrimaryPort_Type(Integer32):
    """Custom type mirmonPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MirmonPrimaryPort_Type.__name__ = "Integer32"
_MirmonPrimaryPort_Object = MibScalar
mirmonPrimaryPort = _MirmonPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 2),
    _MirmonPrimaryPort_Type()
)
mirmonPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirmonPrimaryPort.setStatus("current")


class _MirroringSlot_Type(Integer32):
    """Custom type mirroringSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MirroringSlot_Type.__name__ = "Integer32"
_MirroringSlot_Object = MibScalar
mirroringSlot = _MirroringSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 3),
    _MirroringSlot_Type()
)
mirroringSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirroringSlot.setStatus("current")


class _MirroringPort_Type(Integer32):
    """Custom type mirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_MirroringPort_Type.__name__ = "Integer32"
_MirroringPort_Object = MibScalar
mirroringPort = _MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 4),
    _MirroringPort_Type()
)
mirroringPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirroringPort.setStatus("current")


class _MirMonSession_Type(Integer32):
    """Custom type mirMonSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MirMonSession_Type.__name__ = "Integer32"
_MirMonSession_Object = MibScalar
mirMonSession = _MirMonSession_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 5),
    _MirMonSession_Type()
)
mirMonSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirMonSession.setStatus("current")
_MirMonError_Type = MirMonErrorIds
_MirMonError_Object = MibScalar
mirMonError = _MirMonError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 6),
    _MirMonError_Type()
)
mirMonError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirMonError.setStatus("current")


class _MirMonErrorNi_Type(Integer32):
    """Custom type mirMonErrorNi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MirMonErrorNi_Type.__name__ = "Integer32"
_MirMonErrorNi_Object = MibScalar
mirMonErrorNi = _MirMonErrorNi_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 7),
    _MirMonErrorNi_Type()
)
mirMonErrorNi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirMonErrorNi.setStatus("current")
_MirmonSFlowObjects_ObjectIdentity = ObjectIdentity
mirmonSFlowObjects = _MirmonSFlowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4)
)
_AlasFlowFsTable_Object = MibTable
alasFlowFsTable = _AlasFlowFsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alasFlowFsTable.setStatus("current")
_AlasFlowFsEntry_Object = MibTableRow
alasFlowFsEntry = _AlasFlowFsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    alasFlowFsEntry.setStatus("current")


class _AlasFlowFsDeleteEntry_Type(Integer32):
    """Custom type alasFlowFsDeleteEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 6),
          ("notInService", 2))
    )


_AlasFlowFsDeleteEntry_Type.__name__ = "Integer32"
_AlasFlowFsDeleteEntry_Object = MibTableColumn
alasFlowFsDeleteEntry = _AlasFlowFsDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 1, 1, 1),
    _AlasFlowFsDeleteEntry_Type()
)
alasFlowFsDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alasFlowFsDeleteEntry.setStatus("current")
_AlasFlowCpTable_Object = MibTable
alasFlowCpTable = _AlasFlowCpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    alasFlowCpTable.setStatus("current")
_AlasFlowCpEntry_Object = MibTableRow
alasFlowCpEntry = _AlasFlowCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    alasFlowCpEntry.setStatus("current")


class _AlasFlowCpDeleteEntry_Type(Integer32):
    """Custom type alasFlowCpDeleteEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 6),
          ("notInService", 2))
    )


_AlasFlowCpDeleteEntry_Type.__name__ = "Integer32"
_AlasFlowCpDeleteEntry_Object = MibTableColumn
alasFlowCpDeleteEntry = _AlasFlowCpDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 2, 1, 1),
    _AlasFlowCpDeleteEntry_Type()
)
alasFlowCpDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alasFlowCpDeleteEntry.setStatus("current")


class _AlasFlowAgentConfigType_Type(Integer32):
    """Custom type alasFlowAgentConfigType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("user", 2))
    )


_AlasFlowAgentConfigType_Type.__name__ = "Integer32"
_AlasFlowAgentConfigType_Object = MibScalar
alasFlowAgentConfigType = _AlasFlowAgentConfigType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 3),
    _AlasFlowAgentConfigType_Type()
)
alasFlowAgentConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alasFlowAgentConfigType.setStatus("current")
_AlasFlowAgentAddressType_Type = InetAddressType
_AlasFlowAgentAddressType_Object = MibScalar
alasFlowAgentAddressType = _AlasFlowAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 4),
    _AlasFlowAgentAddressType_Type()
)
alasFlowAgentAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alasFlowAgentAddressType.setStatus("current")
_AlasFlowAgentAddress_Type = InetAddress
_AlasFlowAgentAddress_Object = MibScalar
alasFlowAgentAddress = _AlasFlowAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 5),
    _AlasFlowAgentAddress_Type()
)
alasFlowAgentAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alasFlowAgentAddress.setStatus("current")
_AlcatelIND1PortMirMonMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PortMirMonMIBConformance = _AlcatelIND1PortMirMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMirMonMIBConformance.setStatus("current")
_AlcatelIND1PortMirMonMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PortMirMonMIBGroups = _AlcatelIND1PortMirMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMirMonMIBGroups.setStatus("current")
_AlcatelIND1PortMirMonMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PortMirMonMIBCompliances = _AlcatelIND1PortMirMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMirMonMIBCompliances.setStatus("current")
sFlowFsEntry.registerAugmentions(
    ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB",
     "alasFlowFsEntry")
)
alasFlowFsEntry.setIndexNames(*sFlowFsEntry.getIndexNames())
sFlowCpEntry.registerAugmentions(
    ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB",
     "alasFlowCpEntry")
)
alasFlowCpEntry.setIndexNames(*sFlowCpEntry.getIndexNames())

# Managed Objects groups

portMirroringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 1)
)
portMirroringGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroredIfindex"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroringIfindex"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorUnblockedVLAN"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorRowStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorDirection"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessOperStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcMirroredIf"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcDirection"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcRowStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcOperStatus"))
)
if mibBuilder.loadTexts:
    portMirroringGroup.setStatus("current")

portMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 2)
)
portMonitoringGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorSessionNumber"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorIfindex"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileName"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileSize"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorScreenStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorScreenLine"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorTrafficType"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileOverWrite"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorDirection"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorTimeout"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorRowStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorCaptureType"))
)
if mibBuilder.loadTexts:
    portMonitoringGroup.setStatus("current")

portNotificationVarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 3)
)
portNotificationVarsGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringSlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonSession"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonError"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonErrorNi"))
)
if mibBuilder.loadTexts:
    portNotificationVarsGroup.setStatus("current")

sFlowAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 5)
)
sFlowAgentGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowAgentAddress"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowAgentAddressType"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowAgentConfigType"))
)
if mibBuilder.loadTexts:
    sFlowAgentGroup.setStatus("current")

portMirrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 6)
)
portMirrorGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroredIfindex"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroringIfindex"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorUnblockedVLAN"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorRowStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorDirection"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessOperStatus"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorTaggedVLAN"))
)
if mibBuilder.loadTexts:
    portMirrorGroup.setStatus("current")

portSFlowCpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 7)
)
portSFlowCpGroup.setObjects(
    ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowCpDeleteEntry")
)
if mibBuilder.loadTexts:
    portSFlowCpGroup.setStatus("current")

portSFlowFsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 8)
)
portSFlowFsGroup.setObjects(
    ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowFsDeleteEntry")
)
if mibBuilder.loadTexts:
    portSFlowFsGroup.setStatus("current")


# Notification objects

mirrorConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0, 1)
)
mirrorConfigError.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringSlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonErrorNi"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonError"))
)
if mibBuilder.loadTexts:
    mirrorConfigError.setStatus(
        "current"
    )

monitorFileWritten = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0, 2)
)
monitorFileWritten.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileName"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileSize"))
)
if mibBuilder.loadTexts:
    monitorFileWritten.setStatus(
        "current"
    )

mirrorUnlikeNi = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0, 3)
)
mirrorUnlikeNi.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringSlot"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringPort"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonErrorNi"))
)
if mibBuilder.loadTexts:
    mirrorUnlikeNi.setStatus(
        "current"
    )


# Notifications groups

mirmonTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 4)
)
mirmonTrapsGroup.setObjects(
      *(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorConfigError"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorUnlikeNi"),
        ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileWritten"))
)
if mibBuilder.loadTexts:
    mirmonTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1PortMirMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PortMirMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB",
    **{"MirMonErrorIds": MirMonErrorIds,
       "alcatelIND1PortMirrorMonitoringMIB": alcatelIND1PortMirrorMonitoringMIB,
       "alcatelIND1PortMirMonMIBNotifications": alcatelIND1PortMirMonMIBNotifications,
       "mirrorConfigError": mirrorConfigError,
       "monitorFileWritten": monitorFileWritten,
       "mirrorUnlikeNi": mirrorUnlikeNi,
       "alcatelIND1PortMirMonMIBObjects": alcatelIND1PortMirMonMIBObjects,
       "mirmonMirroring": mirmonMirroring,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorSessionNumber": mirrorSessionNumber,
       "mirrorMirroredIfindex": mirrorMirroredIfindex,
       "mirrorMirroringIfindex": mirrorMirroringIfindex,
       "mirrorStatus": mirrorStatus,
       "mirrorUnblockedVLAN": mirrorUnblockedVLAN,
       "mirrorRowStatus": mirrorRowStatus,
       "mirrorDirection": mirrorDirection,
       "mirrorSessOperStatus": mirrorSessOperStatus,
       "mirrorTaggedVLAN": mirrorTaggedVLAN,
       "mirrorSrcTable": mirrorSrcTable,
       "mirrorSrcEntry": mirrorSrcEntry,
       "mirrorSrcMirroredIf": mirrorSrcMirroredIf,
       "mirrorSrcStatus": mirrorSrcStatus,
       "mirrorSrcDirection": mirrorSrcDirection,
       "mirrorSrcRowStatus": mirrorSrcRowStatus,
       "mirrorSrcOperStatus": mirrorSrcOperStatus,
       "mirmonMonitoring": mirmonMonitoring,
       "monitorTable": monitorTable,
       "monitorEntry": monitorEntry,
       "monitorSessionNumber": monitorSessionNumber,
       "monitorIfindex": monitorIfindex,
       "monitorFileStatus": monitorFileStatus,
       "monitorFileName": monitorFileName,
       "monitorFileSize": monitorFileSize,
       "monitorScreenStatus": monitorScreenStatus,
       "monitorScreenLine": monitorScreenLine,
       "monitorTrafficType": monitorTrafficType,
       "monitorStatus": monitorStatus,
       "monitorFileOverWrite": monitorFileOverWrite,
       "monitorDirection": monitorDirection,
       "monitorTimeout": monitorTimeout,
       "monitorRowStatus": monitorRowStatus,
       "monitorCaptureType": monitorCaptureType,
       "mirmonNotificationVars": mirmonNotificationVars,
       "mirmonPrimarySlot": mirmonPrimarySlot,
       "mirmonPrimaryPort": mirmonPrimaryPort,
       "mirroringSlot": mirroringSlot,
       "mirroringPort": mirroringPort,
       "mirMonSession": mirMonSession,
       "mirMonError": mirMonError,
       "mirMonErrorNi": mirMonErrorNi,
       "mirmonSFlowObjects": mirmonSFlowObjects,
       "alasFlowFsTable": alasFlowFsTable,
       "alasFlowFsEntry": alasFlowFsEntry,
       "alasFlowFsDeleteEntry": alasFlowFsDeleteEntry,
       "alasFlowCpTable": alasFlowCpTable,
       "alasFlowCpEntry": alasFlowCpEntry,
       "alasFlowCpDeleteEntry": alasFlowCpDeleteEntry,
       "alasFlowAgentConfigType": alasFlowAgentConfigType,
       "alasFlowAgentAddressType": alasFlowAgentAddressType,
       "alasFlowAgentAddress": alasFlowAgentAddress,
       "alcatelIND1PortMirMonMIBConformance": alcatelIND1PortMirMonMIBConformance,
       "alcatelIND1PortMirMonMIBGroups": alcatelIND1PortMirMonMIBGroups,
       "portMirroringGroup": portMirroringGroup,
       "portMonitoringGroup": portMonitoringGroup,
       "portNotificationVarsGroup": portNotificationVarsGroup,
       "mirmonTrapsGroup": mirmonTrapsGroup,
       "sFlowAgentGroup": sFlowAgentGroup,
       "portMirrorGroup": portMirrorGroup,
       "portSFlowCpGroup": portSFlowCpGroup,
       "portSFlowFsGroup": portSFlowFsGroup,
       "alcatelIND1PortMirMonMIBCompliances": alcatelIND1PortMirMonMIBCompliances,
       "alcatelIND1PortMirMonMIBCompliance": alcatelIND1PortMirMonMIBCompliance}
)
