# SNMP MIB module (ALCATEL-IND1-TRAP-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TRAP-MGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:27 2024
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

(softentIND1TrapMgr,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1TrapMgr")

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

alcatelIND1TrapMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1)
)
alcatelIND1TrapMgrMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1TrapMgrMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1TrapMgrMIBNotifications = _AlcatelIND1TrapMgrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1TrapMgrMIBNotifications.setStatus("current")
_AlcatelIND1TrapMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1TrapMgrMIBObjects = _AlcatelIND1TrapMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TrapMgrMIBObjects.setStatus("current")
_TrapMgt_ObjectIdentity = ObjectIdentity
trapMgt = _TrapMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1)
)
_TrapConfigTable_Object = MibTable
trapConfigTable = _TrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trapConfigTable.setStatus("current")
_TrapConfigEntry_Object = MibTableRow
trapConfigEntry = _TrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 1, 1)
)
trapConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    trapConfigEntry.setStatus("current")


class _TrapIndex_Type(Integer32):
    """Custom type trapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TrapIndex_Type.__name__ = "Integer32"
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIndex.setStatus("current")


class _TrapName_Type(SnmpAdminString):
    """Custom type trapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrapName_Type.__name__ = "SnmpAdminString"
_TrapName_Object = MibTableColumn
trapName = _TrapName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2),
    _TrapName_Type()
)
trapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapName.setStatus("current")


class _TrapFamily_Type(SnmpAdminString):
    """Custom type trapFamily based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrapFamily_Type.__name__ = "SnmpAdminString"
_TrapFamily_Object = MibTableColumn
trapFamily = _TrapFamily_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3),
    _TrapFamily_Type()
)
trapFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFamily.setStatus("current")


class _TrapAbsorbPeriod_Type(Integer32):
    """Custom type trapAbsorbPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TrapAbsorbPeriod_Type.__name__ = "Integer32"
_TrapAbsorbPeriod_Object = MibTableColumn
trapAbsorbPeriod = _TrapAbsorbPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 1, 1, 4),
    _TrapAbsorbPeriod_Type()
)
trapAbsorbPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAbsorbPeriod.setStatus("current")
_TrapStationTable_Object = MibTable
trapStationTable = _TrapStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trapStationTable.setStatus("current")
_TrapStationEntry_Object = MibTableRow
trapStationEntry = _TrapStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1)
)
trapStationEntry.setIndexNames(
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "trapStationIP"),
)
if mibBuilder.loadTexts:
    trapStationEntry.setStatus("current")
_TrapStationIP_Type = IpAddress
_TrapStationIP_Object = MibTableColumn
trapStationIP = _TrapStationIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1),
    _TrapStationIP_Type()
)
trapStationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapStationIP.setStatus("current")


class _TrapStationPort_Type(Unsigned32):
    """Custom type trapStationPort based on Unsigned32"""
    defaultValue = 162


_TrapStationPort_Object = MibTableColumn
trapStationPort = _TrapStationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2),
    _TrapStationPort_Type()
)
trapStationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapStationPort.setStatus("current")
_TrapStationRowStatus_Type = RowStatus
_TrapStationRowStatus_Object = MibTableColumn
trapStationRowStatus = _TrapStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 3),
    _TrapStationRowStatus_Type()
)
trapStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapStationRowStatus.setStatus("current")


class _TrapStationProtocol_Type(Integer32):
    """Custom type trapStationProtocol based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_TrapStationProtocol_Type.__name__ = "Integer32"
_TrapStationProtocol_Object = MibTableColumn
trapStationProtocol = _TrapStationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 4),
    _TrapStationProtocol_Type()
)
trapStationProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapStationProtocol.setStatus("current")


class _TrapStationUser_Type(SnmpAdminString):
    """Custom type trapStationUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrapStationUser_Type.__name__ = "SnmpAdminString"
_TrapStationUser_Object = MibTableColumn
trapStationUser = _TrapStationUser_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 5),
    _TrapStationUser_Type()
)
trapStationUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapStationUser.setStatus("current")


class _TrapStationReplay_Type(Unsigned32):
    """Custom type trapStationReplay based on Unsigned32"""
    defaultValue = 0


_TrapStationReplay_Object = MibTableColumn
trapStationReplay = _TrapStationReplay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 6),
    _TrapStationReplay_Type()
)
trapStationReplay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapStationReplay.setStatus("current")


class _TrapStationNextSeq_Type(Unsigned32):
    """Custom type trapStationNextSeq based on Unsigned32"""
    defaultValue = 0


_TrapStationNextSeq_Object = MibTableColumn
trapStationNextSeq = _TrapStationNextSeq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 2, 1, 7),
    _TrapStationNextSeq_Type()
)
trapStationNextSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapStationNextSeq.setStatus("current")
_TrapFilterTable_Object = MibTable
trapFilterTable = _TrapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    trapFilterTable.setStatus("current")
_TrapFilterEntry_Object = MibTableRow
trapFilterEntry = _TrapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 3, 1)
)
trapFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "trapStationIP"),
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    trapFilterEntry.setStatus("current")


class _TrapFilterStatus_Type(Integer32):
    """Custom type trapFilterStatus based on Integer32"""
    defaultValue = 2

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


_TrapFilterStatus_Type.__name__ = "Integer32"
_TrapFilterStatus_Object = MibTableColumn
trapFilterStatus = _TrapFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 3, 1, 1),
    _TrapFilterStatus_Type()
)
trapFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapFilterStatus.setStatus("current")


class _TrapAbsorption_Type(Integer32):
    """Custom type trapAbsorption based on Integer32"""
    defaultValue = 1

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


_TrapAbsorption_Type.__name__ = "Integer32"
_TrapAbsorption_Object = MibScalar
trapAbsorption = _TrapAbsorption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 4),
    _TrapAbsorption_Type()
)
trapAbsorption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAbsorption.setStatus("current")


class _TrapToWebView_Type(Integer32):
    """Custom type trapToWebView based on Integer32"""
    defaultValue = 1

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


_TrapToWebView_Type.__name__ = "Integer32"
_TrapToWebView_Object = MibScalar
trapToWebView = _TrapToWebView_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 5),
    _TrapToWebView_Type()
)
trapToWebView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapToWebView.setStatus("current")
_AlaTrapInetStationTable_Object = MibTable
alaTrapInetStationTable = _AlaTrapInetStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaTrapInetStationTable.setStatus("current")
_AlaTrapInetStationEntry_Object = MibTableRow
alaTrapInetStationEntry = _AlaTrapInetStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1)
)
alaTrapInetStationEntry.setIndexNames(
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationIPType"),
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationIP"),
)
if mibBuilder.loadTexts:
    alaTrapInetStationEntry.setStatus("current")
_AlaTrapInetStationIPType_Type = InetAddressType
_AlaTrapInetStationIPType_Object = MibTableColumn
alaTrapInetStationIPType = _AlaTrapInetStationIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 1),
    _AlaTrapInetStationIPType_Type()
)
alaTrapInetStationIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaTrapInetStationIPType.setStatus("current")


class _AlaTrapInetStationIP_Type(InetAddress):
    """Custom type alaTrapInetStationIP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaTrapInetStationIP_Type.__name__ = "InetAddress"
_AlaTrapInetStationIP_Object = MibTableColumn
alaTrapInetStationIP = _AlaTrapInetStationIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 2),
    _AlaTrapInetStationIP_Type()
)
alaTrapInetStationIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaTrapInetStationIP.setStatus("current")


class _AlaTrapInetStationPort_Type(Unsigned32):
    """Custom type alaTrapInetStationPort based on Unsigned32"""
    defaultValue = 162


_AlaTrapInetStationPort_Object = MibTableColumn
alaTrapInetStationPort = _AlaTrapInetStationPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 3),
    _AlaTrapInetStationPort_Type()
)
alaTrapInetStationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTrapInetStationPort.setStatus("current")
_AlaTrapInetStationRowStatus_Type = RowStatus
_AlaTrapInetStationRowStatus_Object = MibTableColumn
alaTrapInetStationRowStatus = _AlaTrapInetStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 4),
    _AlaTrapInetStationRowStatus_Type()
)
alaTrapInetStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTrapInetStationRowStatus.setStatus("current")


class _AlaTrapInetStationProtocol_Type(Integer32):
    """Custom type alaTrapInetStationProtocol based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_AlaTrapInetStationProtocol_Type.__name__ = "Integer32"
_AlaTrapInetStationProtocol_Object = MibTableColumn
alaTrapInetStationProtocol = _AlaTrapInetStationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 5),
    _AlaTrapInetStationProtocol_Type()
)
alaTrapInetStationProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTrapInetStationProtocol.setStatus("current")


class _AlaTrapInetStationUser_Type(SnmpAdminString):
    """Custom type alaTrapInetStationUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTrapInetStationUser_Type.__name__ = "SnmpAdminString"
_AlaTrapInetStationUser_Object = MibTableColumn
alaTrapInetStationUser = _AlaTrapInetStationUser_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 6),
    _AlaTrapInetStationUser_Type()
)
alaTrapInetStationUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTrapInetStationUser.setStatus("current")


class _AlaTrapInetStationReplay_Type(Unsigned32):
    """Custom type alaTrapInetStationReplay based on Unsigned32"""
    defaultValue = 0


_AlaTrapInetStationReplay_Object = MibTableColumn
alaTrapInetStationReplay = _AlaTrapInetStationReplay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 7),
    _AlaTrapInetStationReplay_Type()
)
alaTrapInetStationReplay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTrapInetStationReplay.setStatus("current")


class _AlaTrapInetStationNextSeq_Type(Unsigned32):
    """Custom type alaTrapInetStationNextSeq based on Unsigned32"""
    defaultValue = 0


_AlaTrapInetStationNextSeq_Object = MibTableColumn
alaTrapInetStationNextSeq = _AlaTrapInetStationNextSeq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 6, 1, 8),
    _AlaTrapInetStationNextSeq_Type()
)
alaTrapInetStationNextSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTrapInetStationNextSeq.setStatus("current")
_AlaTrapInetFilterTable_Object = MibTable
alaTrapInetFilterTable = _AlaTrapInetFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaTrapInetFilterTable.setStatus("current")
_AlaTrapInetFilterEntry_Object = MibTableRow
alaTrapInetFilterEntry = _AlaTrapInetFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 7, 1)
)
alaTrapInetFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationIPType"),
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationIP"),
    (0, "ALCATEL-IND1-TRAP-MGR-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    alaTrapInetFilterEntry.setStatus("current")


class _AlaTrapInetFilterStatus_Type(Integer32):
    """Custom type alaTrapInetFilterStatus based on Integer32"""
    defaultValue = 2

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


_AlaTrapInetFilterStatus_Type.__name__ = "Integer32"
_AlaTrapInetFilterStatus_Object = MibTableColumn
alaTrapInetFilterStatus = _AlaTrapInetFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 1, 7, 1, 1),
    _AlaTrapInetFilterStatus_Type()
)
alaTrapInetFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaTrapInetFilterStatus.setStatus("current")
_TrapNotif_ObjectIdentity = ObjectIdentity
trapNotif = _TrapNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 3)
)
_TrapAbsorStamp_Type = Unsigned32
_TrapAbsorStamp_Object = MibScalar
trapAbsorStamp = _TrapAbsorStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 3, 1),
    _TrapAbsorStamp_Type()
)
trapAbsorStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAbsorStamp.setStatus("current")


class _TrapAbsorTrapId_Type(Integer32):
    """Custom type trapAbsorTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TrapAbsorTrapId_Type.__name__ = "Integer32"
_TrapAbsorTrapId_Object = MibScalar
trapAbsorTrapId = _TrapAbsorTrapId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 3, 2),
    _TrapAbsorTrapId_Type()
)
trapAbsorTrapId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAbsorTrapId.setStatus("current")
_TrapAbsorCounter_Type = Unsigned32
_TrapAbsorCounter_Object = MibScalar
trapAbsorCounter = _TrapAbsorCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 3, 3),
    _TrapAbsorCounter_Type()
)
trapAbsorCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAbsorCounter.setStatus("current")
_TrapAbsorTime_Type = Unsigned32
_TrapAbsorTime_Object = MibScalar
trapAbsorTime = _TrapAbsorTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 1, 3, 4),
    _TrapAbsorTime_Type()
)
trapAbsorTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAbsorTime.setStatus("current")
_AlcatelIND1TrapMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1TrapMgrMIBConformance = _AlcatelIND1TrapMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1TrapMgrMIBConformance.setStatus("current")
_AlcatelIND1TrapMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1TrapMgrMIBGroups = _AlcatelIND1TrapMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TrapMgrMIBGroups.setStatus("current")
_AlcatelIND1TrapMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1TrapMgrMIBCompliances = _AlcatelIND1TrapMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1TrapMgrMIBCompliances.setStatus("current")

# Managed Objects groups

trapMgtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2, 1, 1)
)
trapMgtGroup.setObjects(
      *(("ALCATEL-IND1-TRAP-MGR-MIB", "trapIndex"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapName"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapFamily"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorbPeriod"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationIP"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationPort"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationRowStatus"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationProtocol"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationUser"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationReplay"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapStationNextSeq"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapFilterStatus"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorption"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapToWebView"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationPort"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationRowStatus"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationProtocol"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationUser"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationReplay"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetStationNextSeq"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "alaTrapInetFilterStatus"))
)
if mibBuilder.loadTexts:
    trapMgtGroup.setStatus("current")

trapNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2, 1, 3)
)
trapNotifGroup.setObjects(
      *(("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorStamp"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorTrapId"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorCounter"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorTime"))
)
if mibBuilder.loadTexts:
    trapNotifGroup.setStatus("current")


# Notification objects

trapAbsorptionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 0, 1)
)
trapAbsorptionTrap.setObjects(
      *(("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorStamp"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorTrapId"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorCounter"),
        ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorTime"))
)
if mibBuilder.loadTexts:
    trapAbsorptionTrap.setStatus(
        "current"
    )


# Notifications groups

trapTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2, 1, 2)
)
trapTrapsGroup.setObjects(
    ("ALCATEL-IND1-TRAP-MGR-MIB", "trapAbsorptionTrap")
)
if mibBuilder.loadTexts:
    trapTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1TrapMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TrapMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TRAP-MGR-MIB",
    **{"alcatelIND1TrapMgrMIB": alcatelIND1TrapMgrMIB,
       "alcatelIND1TrapMgrMIBNotifications": alcatelIND1TrapMgrMIBNotifications,
       "trapAbsorptionTrap": trapAbsorptionTrap,
       "alcatelIND1TrapMgrMIBObjects": alcatelIND1TrapMgrMIBObjects,
       "trapMgt": trapMgt,
       "trapConfigTable": trapConfigTable,
       "trapConfigEntry": trapConfigEntry,
       "trapIndex": trapIndex,
       "trapName": trapName,
       "trapFamily": trapFamily,
       "trapAbsorbPeriod": trapAbsorbPeriod,
       "trapStationTable": trapStationTable,
       "trapStationEntry": trapStationEntry,
       "trapStationIP": trapStationIP,
       "trapStationPort": trapStationPort,
       "trapStationRowStatus": trapStationRowStatus,
       "trapStationProtocol": trapStationProtocol,
       "trapStationUser": trapStationUser,
       "trapStationReplay": trapStationReplay,
       "trapStationNextSeq": trapStationNextSeq,
       "trapFilterTable": trapFilterTable,
       "trapFilterEntry": trapFilterEntry,
       "trapFilterStatus": trapFilterStatus,
       "trapAbsorption": trapAbsorption,
       "trapToWebView": trapToWebView,
       "alaTrapInetStationTable": alaTrapInetStationTable,
       "alaTrapInetStationEntry": alaTrapInetStationEntry,
       "alaTrapInetStationIPType": alaTrapInetStationIPType,
       "alaTrapInetStationIP": alaTrapInetStationIP,
       "alaTrapInetStationPort": alaTrapInetStationPort,
       "alaTrapInetStationRowStatus": alaTrapInetStationRowStatus,
       "alaTrapInetStationProtocol": alaTrapInetStationProtocol,
       "alaTrapInetStationUser": alaTrapInetStationUser,
       "alaTrapInetStationReplay": alaTrapInetStationReplay,
       "alaTrapInetStationNextSeq": alaTrapInetStationNextSeq,
       "alaTrapInetFilterTable": alaTrapInetFilterTable,
       "alaTrapInetFilterEntry": alaTrapInetFilterEntry,
       "alaTrapInetFilterStatus": alaTrapInetFilterStatus,
       "trapNotif": trapNotif,
       "trapAbsorStamp": trapAbsorStamp,
       "trapAbsorTrapId": trapAbsorTrapId,
       "trapAbsorCounter": trapAbsorCounter,
       "trapAbsorTime": trapAbsorTime,
       "alcatelIND1TrapMgrMIBConformance": alcatelIND1TrapMgrMIBConformance,
       "alcatelIND1TrapMgrMIBGroups": alcatelIND1TrapMgrMIBGroups,
       "trapMgtGroup": trapMgtGroup,
       "trapTrapsGroup": trapTrapsGroup,
       "trapNotifGroup": trapNotifGroup,
       "alcatelIND1TrapMgrMIBCompliances": alcatelIND1TrapMgrMIBCompliances,
       "alcatelIND1TrapMgrMIBCompliance": alcatelIND1TrapMgrMIBCompliance}
)
