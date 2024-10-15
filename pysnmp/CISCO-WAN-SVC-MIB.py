# SNMP MIB module (CISCO-WAN-SVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-SVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:20 2024
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

(AtmAddress,
 NetPrefix) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "AtmAddress",
    "NetPrefix")

(CiscoWanNsapAtmAddress,) = mibBuilder.importSymbols(
    "CISCO-WAN-ATM-CONN-MIB",
    "CiscoWanNsapAtmAddress")

(stratacom,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "stratacom")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PnniNodeId,
 PnniPortId) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "PnniNodeId",
    "PnniPortId")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoWANSvcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140)
)
ciscoWANSvcMIB.setRevisions(
        ("2003-03-10 00:00",
         "2002-09-16 00:00",
         "2002-03-01 00:00",
         "2001-07-19 00:00",
         "2001-07-06 00:00",
         "2001-06-06 00:00",
         "2001-05-10 00:00",
         "2000-10-20 00:00",
         "2000-09-01 00:00",
         "2000-08-03 00:00",
         "2000-06-15 00:00",
         "2000-04-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CwspSpvcState(Integer32, TextualConvention):
    status = "current"
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("genSpvcErr", 1),
          ("mCmtHalfFail", 9),
          ("mInstlPvcFail", 5),
          ("mInstlXconnFail", 11),
          ("mPvcDelFail", 2),
          ("mRecmtPvcFail", 7),
          ("mRelPendHalfTmout", 4),
          ("masterSpvcAutoDelete", 15),
          ("sCmtHalfFail", 10),
          ("sInstlPvcFail", 6),
          ("sPvcDelFail", 3),
          ("sRecmtPvcFail", 8),
          ("sRecvSetupConfmMismatch", 12),
          ("sRecvSetupServMismatch", 13),
          ("sRecvSetupTrafParmMismatch", 14),
          ("slaveSpvcAutoDelete", 16))
    )



class CwspControllerState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("unavilable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWANSvcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWANSvcMIBObjects = _CiscoWANSvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1)
)
_CiscoWANSvcInfo_ObjectIdentity = ObjectIdentity
ciscoWANSvcInfo = _CiscoWANSvcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 1)
)
_CwsSwRevision_Type = DisplayString
_CwsSwRevision_Object = MibScalar
cwsSwRevision = _CwsSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 1, 1),
    _CwsSwRevision_Type()
)
cwsSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSwRevision.setStatus("current")
_CwsControllerStatus_Type = CwspControllerState
_CwsControllerStatus_Object = MibScalar
cwsControllerStatus = _CwsControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 1, 6),
    _CwsControllerStatus_Type()
)
cwsControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsControllerStatus.setStatus("current")
_CwspPnniStndbyControllerStatus_Type = CwspControllerState
_CwspPnniStndbyControllerStatus_Object = MibScalar
cwspPnniStndbyControllerStatus = _CwspPnniStndbyControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 1, 7),
    _CwspPnniStndbyControllerStatus_Type()
)
cwspPnniStndbyControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspPnniStndbyControllerStatus.setStatus("current")


class _CwspPnniControllerStatus_Type(Integer32):
    """Custom type cwspPnniControllerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stndby", 2),
          ("unavailable", 3))
    )


_CwspPnniControllerStatus_Type.__name__ = "Integer32"
_CwspPnniControllerStatus_Object = MibScalar
cwspPnniControllerStatus = _CwspPnniControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 1, 8),
    _CwspPnniControllerStatus_Type()
)
cwspPnniControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspPnniControllerStatus.setStatus("current")


class _CwspPnniControllerPhySlot_Type(Integer32):
    """Custom type cwspPnniControllerPhySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CwspPnniControllerPhySlot_Type.__name__ = "Integer32"
_CwspPnniControllerPhySlot_Object = MibScalar
cwspPnniControllerPhySlot = _CwspPnniControllerPhySlot_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 1, 9),
    _CwspPnniControllerPhySlot_Type()
)
cwspPnniControllerPhySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspPnniControllerPhySlot.setStatus("current")
_CiscoWANSvcPort_ObjectIdentity = ObjectIdentity
ciscoWANSvcPort = _CiscoWANSvcPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2)
)
_CwspConfig_ObjectIdentity = ObjectIdentity
cwspConfig = _CwspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1)
)
_CwspConfigTable_Object = MibTable
cwspConfigTable = _CwspConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwspConfigTable.setStatus("current")
_CwspConfigEntry_Object = MibTableRow
cwspConfigEntry = _CwspConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1)
)
cwspConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspConfigEntry.setStatus("current")


class _CwspAdminStatus_Type(Integer32):
    """Custom type cwspAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("outService", 2))
    )


_CwspAdminStatus_Type.__name__ = "Integer32"
_CwspAdminStatus_Object = MibTableColumn
cwspAdminStatus = _CwspAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 1),
    _CwspAdminStatus_Type()
)
cwspAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAdminStatus.setStatus("current")


class _CwspOperStatus_Type(Integer32):
    """Custom type cwspOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("other", 3))
    )


_CwspOperStatus_Type.__name__ = "Integer32"
_CwspOperStatus_Object = MibTableColumn
cwspOperStatus = _CwspOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 2),
    _CwspOperStatus_Type()
)
cwspOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperStatus.setStatus("current")


class _CwspSvcBlocked_Type(TruthValue):
    """Custom type cwspSvcBlocked based on TruthValue"""


_CwspSvcBlocked_Object = MibTableColumn
cwspSvcBlocked = _CwspSvcBlocked_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 3),
    _CwspSvcBlocked_Type()
)
cwspSvcBlocked.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspSvcBlocked.setStatus("current")


class _CwspSpvcBlocked_Type(TruthValue):
    """Custom type cwspSpvcBlocked based on TruthValue"""


_CwspSpvcBlocked_Object = MibTableColumn
cwspSpvcBlocked = _CwspSpvcBlocked_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 4),
    _CwspSpvcBlocked_Type()
)
cwspSpvcBlocked.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspSpvcBlocked.setStatus("current")


class _CwspIlmiAddrRegEnable_Type(TruthValue):
    """Custom type cwspIlmiAddrRegEnable based on TruthValue"""


_CwspIlmiAddrRegEnable_Object = MibTableColumn
cwspIlmiAddrRegEnable = _CwspIlmiAddrRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 5),
    _CwspIlmiAddrRegEnable_Type()
)
cwspIlmiAddrRegEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiAddrRegEnable.setStatus("current")


class _CwspIlmiAutoConfEnable_Type(TruthValue):
    """Custom type cwspIlmiAutoConfEnable based on TruthValue"""


_CwspIlmiAutoConfEnable_Object = MibTableColumn
cwspIlmiAutoConfEnable = _CwspIlmiAutoConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 6),
    _CwspIlmiAutoConfEnable_Type()
)
cwspIlmiAutoConfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiAutoConfEnable.setStatus("current")


class _CwspIlmiServRegEnable_Type(TruthValue):
    """Custom type cwspIlmiServRegEnable based on TruthValue"""


_CwspIlmiServRegEnable_Object = MibTableColumn
cwspIlmiServRegEnable = _CwspIlmiServRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 7),
    _CwspIlmiServRegEnable_Type()
)
cwspIlmiServRegEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiServRegEnable.setStatus("current")
_CwspPhyIdentifier_Type = DisplayString
_CwspPhyIdentifier_Object = MibTableColumn
cwspPhyIdentifier = _CwspPhyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 8),
    _CwspPhyIdentifier_Type()
)
cwspPhyIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspPhyIdentifier.setStatus("current")


class _CwspSignallingVpi_Type(Integer32):
    """Custom type cwspSignallingVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspSignallingVpi_Type.__name__ = "Integer32"
_CwspSignallingVpi_Object = MibTableColumn
cwspSignallingVpi = _CwspSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 9),
    _CwspSignallingVpi_Type()
)
cwspSignallingVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspSignallingVpi.setStatus("current")


class _CwspSignallingVci_Type(Integer32):
    """Custom type cwspSignallingVci based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspSignallingVci_Type.__name__ = "Integer32"
_CwspSignallingVci_Object = MibTableColumn
cwspSignallingVci = _CwspSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 10),
    _CwspSignallingVci_Type()
)
cwspSignallingVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspSignallingVci.setStatus("current")


class _CwspRoutingVpi_Type(Integer32):
    """Custom type cwspRoutingVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspRoutingVpi_Type.__name__ = "Integer32"
_CwspRoutingVpi_Object = MibTableColumn
cwspRoutingVpi = _CwspRoutingVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 11),
    _CwspRoutingVpi_Type()
)
cwspRoutingVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspRoutingVpi.setStatus("current")


class _CwspRoutingVci_Type(Integer32):
    """Custom type cwspRoutingVci based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspRoutingVci_Type.__name__ = "Integer32"
_CwspRoutingVci_Object = MibTableColumn
cwspRoutingVci = _CwspRoutingVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 12),
    _CwspRoutingVci_Type()
)
cwspRoutingVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspRoutingVci.setStatus("current")


class _CwspMaxVpiBits_Type(Integer32):
    """Custom type cwspMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_CwspMaxVpiBits_Type.__name__ = "Integer32"
_CwspMaxVpiBits_Object = MibTableColumn
cwspMaxVpiBits = _CwspMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 13),
    _CwspMaxVpiBits_Type()
)
cwspMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspMaxVpiBits.setStatus("current")


class _CwspMaxVciBits_Type(Integer32):
    """Custom type cwspMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CwspMaxVciBits_Type.__name__ = "Integer32"
_CwspMaxVciBits_Object = MibTableColumn
cwspMaxVciBits = _CwspMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 14),
    _CwspMaxVciBits_Type()
)
cwspMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspMaxVciBits.setStatus("current")


class _CwspUniVersion_Type(Integer32):
    """Custom type cwspUniVersion based on Integer32"""
    defaultValue = 7

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
        *(("frf4", 6),
          ("ip", 8),
          ("ituDss2", 5),
          ("self", 9),
          ("uni20", 1),
          ("uni30", 2),
          ("uni31", 3),
          ("uni40", 4),
          ("unsupported", 7))
    )


_CwspUniVersion_Type.__name__ = "Integer32"
_CwspUniVersion_Object = MibTableColumn
cwspUniVersion = _CwspUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 15),
    _CwspUniVersion_Type()
)
cwspUniVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspUniVersion.setStatus("current")


class _CwspNniVersion_Type(Integer32):
    """Custom type cwspNniVersion based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aini", 5),
          ("enni", 4),
          ("iisp30", 1),
          ("iisp31", 2),
          ("pnni10", 3),
          ("unsupported", 7))
    )


_CwspNniVersion_Type.__name__ = "Integer32"
_CwspNniVersion_Object = MibTableColumn
cwspNniVersion = _CwspNniVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 16),
    _CwspNniVersion_Type()
)
cwspNniVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspNniVersion.setStatus("current")


class _CwspUniType_Type(Integer32):
    """Custom type cwspUniType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_CwspUniType_Type.__name__ = "Integer32"
_CwspUniType_Object = MibTableColumn
cwspUniType = _CwspUniType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 17),
    _CwspUniType_Type()
)
cwspUniType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspUniType.setStatus("current")


class _CwspSide_Type(Integer32):
    """Custom type cwspSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_CwspSide_Type.__name__ = "Integer32"
_CwspSide_Object = MibTableColumn
cwspSide = _CwspSide_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 18),
    _CwspSide_Type()
)
cwspSide.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspSide.setStatus("current")


class _CwspMaxP2pCalls_Type(Integer32):
    """Custom type cwspMaxP2pCalls based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspMaxP2pCalls_Type.__name__ = "Integer32"
_CwspMaxP2pCalls_Object = MibTableColumn
cwspMaxP2pCalls = _CwspMaxP2pCalls_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 19),
    _CwspMaxP2pCalls_Type()
)
cwspMaxP2pCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMaxP2pCalls.setStatus("current")


class _CwspMaxP2mpRoots_Type(Integer32):
    """Custom type cwspMaxP2mpRoots based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspMaxP2mpRoots_Type.__name__ = "Integer32"
_CwspMaxP2mpRoots_Object = MibTableColumn
cwspMaxP2mpRoots = _CwspMaxP2mpRoots_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 20),
    _CwspMaxP2mpRoots_Type()
)
cwspMaxP2mpRoots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMaxP2mpRoots.setStatus("current")


class _CwspMaxP2mpLeafs_Type(Integer32):
    """Custom type cwspMaxP2mpLeafs based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspMaxP2mpLeafs_Type.__name__ = "Integer32"
_CwspMaxP2mpLeafs_Object = MibTableColumn
cwspMaxP2mpLeafs = _CwspMaxP2mpLeafs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 21),
    _CwspMaxP2mpLeafs_Type()
)
cwspMaxP2mpLeafs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMaxP2mpLeafs.setStatus("current")


class _CwspMinSvccVpi_Type(Integer32):
    """Custom type cwspMinSvccVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspMinSvccVpi_Type.__name__ = "Integer32"
_CwspMinSvccVpi_Object = MibTableColumn
cwspMinSvccVpi = _CwspMinSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 22),
    _CwspMinSvccVpi_Type()
)
cwspMinSvccVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMinSvccVpi.setStatus("current")


class _CwspMaxSvccVpi_Type(Integer32):
    """Custom type cwspMaxSvccVpi based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspMaxSvccVpi_Type.__name__ = "Integer32"
_CwspMaxSvccVpi_Object = MibTableColumn
cwspMaxSvccVpi = _CwspMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 23),
    _CwspMaxSvccVpi_Type()
)
cwspMaxSvccVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMaxSvccVpi.setStatus("current")


class _CwspMinSvccVci_Type(Integer32):
    """Custom type cwspMinSvccVci based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspMinSvccVci_Type.__name__ = "Integer32"
_CwspMinSvccVci_Object = MibTableColumn
cwspMinSvccVci = _CwspMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 24),
    _CwspMinSvccVci_Type()
)
cwspMinSvccVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMinSvccVci.setStatus("current")


class _CwspMaxSvccVci_Type(Integer32):
    """Custom type cwspMaxSvccVci based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 65535),
    )


_CwspMaxSvccVci_Type.__name__ = "Integer32"
_CwspMaxSvccVci_Object = MibTableColumn
cwspMaxSvccVci = _CwspMaxSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 25),
    _CwspMaxSvccVci_Type()
)
cwspMaxSvccVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMaxSvccVci.setStatus("current")


class _CwspMinSvpcVpi_Type(Integer32):
    """Custom type cwspMinSvpcVpi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CwspMinSvpcVpi_Type.__name__ = "Integer32"
_CwspMinSvpcVpi_Object = MibTableColumn
cwspMinSvpcVpi = _CwspMinSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 26),
    _CwspMinSvpcVpi_Type()
)
cwspMinSvpcVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMinSvpcVpi.setStatus("current")


class _CwspMaxSvpcVpi_Type(Integer32):
    """Custom type cwspMaxSvpcVpi based on Integer32"""
    defaultValue = 4095

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CwspMaxSvpcVpi_Type.__name__ = "Integer32"
_CwspMaxSvpcVpi_Object = MibTableColumn
cwspMaxSvpcVpi = _CwspMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 27),
    _CwspMaxSvpcVpi_Type()
)
cwspMaxSvpcVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspMaxSvpcVpi.setStatus("current")


class _CwspEnhancedIisp_Type(TruthValue):
    """Custom type cwspEnhancedIisp based on TruthValue"""


_CwspEnhancedIisp_Object = MibTableColumn
cwspEnhancedIisp = _CwspEnhancedIisp_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 28),
    _CwspEnhancedIisp_Type()
)
cwspEnhancedIisp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspEnhancedIisp.setStatus("current")
_CwspConfigTableRowStatus_Type = RowStatus
_CwspConfigTableRowStatus_Object = MibTableColumn
cwspConfigTableRowStatus = _CwspConfigTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 29),
    _CwspConfigTableRowStatus_Type()
)
cwspConfigTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConfigTableRowStatus.setStatus("current")


class _CwspAddrPlanSupported_Type(Integer32):
    """Custom type cwspAddrPlanSupported based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 2),
          ("both", 1),
          ("e164", 3))
    )


_CwspAddrPlanSupported_Type.__name__ = "Integer32"
_CwspAddrPlanSupported_Object = MibTableColumn
cwspAddrPlanSupported = _CwspAddrPlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 30),
    _CwspAddrPlanSupported_Type()
)
cwspAddrPlanSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddrPlanSupported.setStatus("current")


class _CwspIlmiSecureLink_Type(TruthValue):
    """Custom type cwspIlmiSecureLink based on TruthValue"""


_CwspIlmiSecureLink_Object = MibTableColumn
cwspIlmiSecureLink = _CwspIlmiSecureLink_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 31),
    _CwspIlmiSecureLink_Type()
)
cwspIlmiSecureLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiSecureLink.setStatus("current")


class _CwspIlmiAttachmentPoint_Type(TruthValue):
    """Custom type cwspIlmiAttachmentPoint based on TruthValue"""


_CwspIlmiAttachmentPoint_Object = MibTableColumn
cwspIlmiAttachmentPoint = _CwspIlmiAttachmentPoint_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 32),
    _CwspIlmiAttachmentPoint_Type()
)
cwspIlmiAttachmentPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiAttachmentPoint.setStatus("current")


class _CwspIlmiLocalAttrStd_Type(TruthValue):
    """Custom type cwspIlmiLocalAttrStd based on TruthValue"""


_CwspIlmiLocalAttrStd_Object = MibTableColumn
cwspIlmiLocalAttrStd = _CwspIlmiLocalAttrStd_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 33),
    _CwspIlmiLocalAttrStd_Type()
)
cwspIlmiLocalAttrStd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiLocalAttrStd.setStatus("current")


class _CwspIlmiUCSMEnable_Type(TruthValue):
    """Custom type cwspIlmiUCSMEnable based on TruthValue"""


_CwspIlmiUCSMEnable_Object = MibTableColumn
cwspIlmiUCSMEnable = _CwspIlmiUCSMEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 34),
    _CwspIlmiUCSMEnable_Type()
)
cwspIlmiUCSMEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspIlmiUCSMEnable.setStatus("current")


class _CwspRoutingPriority_Type(Integer32):
    """Custom type cwspRoutingPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CwspRoutingPriority_Type.__name__ = "Integer32"
_CwspRoutingPriority_Object = MibTableColumn
cwspRoutingPriority = _CwspRoutingPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 35),
    _CwspRoutingPriority_Type()
)
cwspRoutingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspRoutingPriority.setStatus("current")
_CwspSpvcAddress_Type = CiscoWanNsapAtmAddress
_CwspSpvcAddress_Object = MibTableColumn
cwspSpvcAddress = _CwspSpvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 1, 1, 1, 36),
    _CwspSpvcAddress_Type()
)
cwspSpvcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSpvcAddress.setStatus("current")
_CwspCacConfig_ObjectIdentity = ObjectIdentity
cwspCacConfig = _CwspCacConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2)
)
_CwspCacConfigTable_Object = MibTable
cwspCacConfigTable = _CwspCacConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwspCacConfigTable.setStatus("current")
_CwspCacConfigEntry_Object = MibTableRow
cwspCacConfigEntry = _CwspCacConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1)
)
cwspCacConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspCacConfigEntry.setStatus("current")


class _CwspUtilFactorCbr_Type(Integer32):
    """Custom type cwspUtilFactorCbr based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CwspUtilFactorCbr_Type.__name__ = "Integer32"
_CwspUtilFactorCbr_Object = MibTableColumn
cwspUtilFactorCbr = _CwspUtilFactorCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 1),
    _CwspUtilFactorCbr_Type()
)
cwspUtilFactorCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspUtilFactorCbr.setStatus("current")


class _CwspUtilFactorRtVbr_Type(Integer32):
    """Custom type cwspUtilFactorRtVbr based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CwspUtilFactorRtVbr_Type.__name__ = "Integer32"
_CwspUtilFactorRtVbr_Object = MibTableColumn
cwspUtilFactorRtVbr = _CwspUtilFactorRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 2),
    _CwspUtilFactorRtVbr_Type()
)
cwspUtilFactorRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspUtilFactorRtVbr.setStatus("current")


class _CwspUtilFactorNrtVbr_Type(Integer32):
    """Custom type cwspUtilFactorNrtVbr based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CwspUtilFactorNrtVbr_Type.__name__ = "Integer32"
_CwspUtilFactorNrtVbr_Object = MibTableColumn
cwspUtilFactorNrtVbr = _CwspUtilFactorNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 3),
    _CwspUtilFactorNrtVbr_Type()
)
cwspUtilFactorNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspUtilFactorNrtVbr.setStatus("current")


class _CwspUtilFactorAbr_Type(Integer32):
    """Custom type cwspUtilFactorAbr based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CwspUtilFactorAbr_Type.__name__ = "Integer32"
_CwspUtilFactorAbr_Object = MibTableColumn
cwspUtilFactorAbr = _CwspUtilFactorAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 4),
    _CwspUtilFactorAbr_Type()
)
cwspUtilFactorAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspUtilFactorAbr.setStatus("current")


class _CwspUtilFactorUbr_Type(Integer32):
    """Custom type cwspUtilFactorUbr based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CwspUtilFactorUbr_Type.__name__ = "Integer32"
_CwspUtilFactorUbr_Object = MibTableColumn
cwspUtilFactorUbr = _CwspUtilFactorUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 5),
    _CwspUtilFactorUbr_Type()
)
cwspUtilFactorUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspUtilFactorUbr.setStatus("current")


class _CwspMaxBwCbr_Type(Integer32):
    """Custom type cwspMaxBwCbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxBwCbr_Type.__name__ = "Integer32"
_CwspMaxBwCbr_Object = MibTableColumn
cwspMaxBwCbr = _CwspMaxBwCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 6),
    _CwspMaxBwCbr_Type()
)
cwspMaxBwCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxBwCbr.setStatus("current")


class _CwspMaxBwRtVbr_Type(Integer32):
    """Custom type cwspMaxBwRtVbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxBwRtVbr_Type.__name__ = "Integer32"
_CwspMaxBwRtVbr_Object = MibTableColumn
cwspMaxBwRtVbr = _CwspMaxBwRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 7),
    _CwspMaxBwRtVbr_Type()
)
cwspMaxBwRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxBwRtVbr.setStatus("current")


class _CwspMaxBwNrtVbr_Type(Integer32):
    """Custom type cwspMaxBwNrtVbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxBwNrtVbr_Type.__name__ = "Integer32"
_CwspMaxBwNrtVbr_Object = MibTableColumn
cwspMaxBwNrtVbr = _CwspMaxBwNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 8),
    _CwspMaxBwNrtVbr_Type()
)
cwspMaxBwNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxBwNrtVbr.setStatus("current")


class _CwspMaxBwAbr_Type(Integer32):
    """Custom type cwspMaxBwAbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxBwAbr_Type.__name__ = "Integer32"
_CwspMaxBwAbr_Object = MibTableColumn
cwspMaxBwAbr = _CwspMaxBwAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 9),
    _CwspMaxBwAbr_Type()
)
cwspMaxBwAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxBwAbr.setStatus("current")


class _CwspMaxBwUbr_Type(Integer32):
    """Custom type cwspMaxBwUbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxBwUbr_Type.__name__ = "Integer32"
_CwspMaxBwUbr_Object = MibTableColumn
cwspMaxBwUbr = _CwspMaxBwUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 10),
    _CwspMaxBwUbr_Type()
)
cwspMaxBwUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxBwUbr.setStatus("current")


class _CwspMinBwCbr_Type(Integer32):
    """Custom type cwspMinBwCbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinBwCbr_Type.__name__ = "Integer32"
_CwspMinBwCbr_Object = MibTableColumn
cwspMinBwCbr = _CwspMinBwCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 11),
    _CwspMinBwCbr_Type()
)
cwspMinBwCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinBwCbr.setStatus("current")


class _CwspMinBwRtVbr_Type(Integer32):
    """Custom type cwspMinBwRtVbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinBwRtVbr_Type.__name__ = "Integer32"
_CwspMinBwRtVbr_Object = MibTableColumn
cwspMinBwRtVbr = _CwspMinBwRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 12),
    _CwspMinBwRtVbr_Type()
)
cwspMinBwRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinBwRtVbr.setStatus("current")


class _CwspMinBwNrtVbr_Type(Integer32):
    """Custom type cwspMinBwNrtVbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinBwNrtVbr_Type.__name__ = "Integer32"
_CwspMinBwNrtVbr_Object = MibTableColumn
cwspMinBwNrtVbr = _CwspMinBwNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 13),
    _CwspMinBwNrtVbr_Type()
)
cwspMinBwNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinBwNrtVbr.setStatus("current")


class _CwspMinBwAbr_Type(Integer32):
    """Custom type cwspMinBwAbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinBwAbr_Type.__name__ = "Integer32"
_CwspMinBwAbr_Object = MibTableColumn
cwspMinBwAbr = _CwspMinBwAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 14),
    _CwspMinBwAbr_Type()
)
cwspMinBwAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinBwAbr.setStatus("current")


class _CwspMinBwUbr_Type(Integer32):
    """Custom type cwspMinBwUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinBwUbr_Type.__name__ = "Integer32"
_CwspMinBwUbr_Object = MibTableColumn
cwspMinBwUbr = _CwspMinBwUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 15),
    _CwspMinBwUbr_Type()
)
cwspMinBwUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspMinBwUbr.setStatus("current")


class _CwspMaxVcCbr_Type(Integer32):
    """Custom type cwspMaxVcCbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcCbr_Type.__name__ = "Integer32"
_CwspMaxVcCbr_Object = MibTableColumn
cwspMaxVcCbr = _CwspMaxVcCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 16),
    _CwspMaxVcCbr_Type()
)
cwspMaxVcCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcCbr.setStatus("current")


class _CwspMaxVcRtVbr_Type(Integer32):
    """Custom type cwspMaxVcRtVbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcRtVbr_Type.__name__ = "Integer32"
_CwspMaxVcRtVbr_Object = MibTableColumn
cwspMaxVcRtVbr = _CwspMaxVcRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 17),
    _CwspMaxVcRtVbr_Type()
)
cwspMaxVcRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcRtVbr.setStatus("current")


class _CwspMaxVcNrtVbr_Type(Integer32):
    """Custom type cwspMaxVcNrtVbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcNrtVbr_Type.__name__ = "Integer32"
_CwspMaxVcNrtVbr_Object = MibTableColumn
cwspMaxVcNrtVbr = _CwspMaxVcNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 18),
    _CwspMaxVcNrtVbr_Type()
)
cwspMaxVcNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcNrtVbr.setStatus("current")


class _CwspMaxVcAbr_Type(Integer32):
    """Custom type cwspMaxVcAbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcAbr_Type.__name__ = "Integer32"
_CwspMaxVcAbr_Object = MibTableColumn
cwspMaxVcAbr = _CwspMaxVcAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 19),
    _CwspMaxVcAbr_Type()
)
cwspMaxVcAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcAbr.setStatus("current")


class _CwspMaxVcUbr_Type(Integer32):
    """Custom type cwspMaxVcUbr based on Integer32"""
    defaultValue = 1000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcUbr_Type.__name__ = "Integer32"
_CwspMaxVcUbr_Object = MibTableColumn
cwspMaxVcUbr = _CwspMaxVcUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 20),
    _CwspMaxVcUbr_Type()
)
cwspMaxVcUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcUbr.setStatus("current")


class _CwspMinVcCbr_Type(Integer32):
    """Custom type cwspMinVcCbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinVcCbr_Type.__name__ = "Integer32"
_CwspMinVcCbr_Object = MibTableColumn
cwspMinVcCbr = _CwspMinVcCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 21),
    _CwspMinVcCbr_Type()
)
cwspMinVcCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinVcCbr.setStatus("current")


class _CwspMinVcRtVbr_Type(Integer32):
    """Custom type cwspMinVcRtVbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinVcRtVbr_Type.__name__ = "Integer32"
_CwspMinVcRtVbr_Object = MibTableColumn
cwspMinVcRtVbr = _CwspMinVcRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 22),
    _CwspMinVcRtVbr_Type()
)
cwspMinVcRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinVcRtVbr.setStatus("current")


class _CwspMinVcNrtVbr_Type(Integer32):
    """Custom type cwspMinVcNrtVbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinVcNrtVbr_Type.__name__ = "Integer32"
_CwspMinVcNrtVbr_Object = MibTableColumn
cwspMinVcNrtVbr = _CwspMinVcNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 23),
    _CwspMinVcNrtVbr_Type()
)
cwspMinVcNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinVcNrtVbr.setStatus("current")


class _CwspMinVcAbr_Type(Integer32):
    """Custom type cwspMinVcAbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinVcAbr_Type.__name__ = "Integer32"
_CwspMinVcAbr_Object = MibTableColumn
cwspMinVcAbr = _CwspMinVcAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 24),
    _CwspMinVcAbr_Type()
)
cwspMinVcAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinVcAbr.setStatus("current")


class _CwspMinVcUbr_Type(Integer32):
    """Custom type cwspMinVcUbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMinVcUbr_Type.__name__ = "Integer32"
_CwspMinVcUbr_Object = MibTableColumn
cwspMinVcUbr = _CwspMinVcUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 25),
    _CwspMinVcUbr_Type()
)
cwspMinVcUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMinVcUbr.setStatus("current")


class _CwspMaxVcBwCbr_Type(Integer32):
    """Custom type cwspMaxVcBwCbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcBwCbr_Type.__name__ = "Integer32"
_CwspMaxVcBwCbr_Object = MibTableColumn
cwspMaxVcBwCbr = _CwspMaxVcBwCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 26),
    _CwspMaxVcBwCbr_Type()
)
cwspMaxVcBwCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcBwCbr.setStatus("current")


class _CwspMaxVcBwRtVbr_Type(Integer32):
    """Custom type cwspMaxVcBwRtVbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcBwRtVbr_Type.__name__ = "Integer32"
_CwspMaxVcBwRtVbr_Object = MibTableColumn
cwspMaxVcBwRtVbr = _CwspMaxVcBwRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 27),
    _CwspMaxVcBwRtVbr_Type()
)
cwspMaxVcBwRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcBwRtVbr.setStatus("current")


class _CwspMaxVcBwNrtVbr_Type(Integer32):
    """Custom type cwspMaxVcBwNrtVbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcBwNrtVbr_Type.__name__ = "Integer32"
_CwspMaxVcBwNrtVbr_Object = MibTableColumn
cwspMaxVcBwNrtVbr = _CwspMaxVcBwNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 28),
    _CwspMaxVcBwNrtVbr_Type()
)
cwspMaxVcBwNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcBwNrtVbr.setStatus("current")


class _CwspMaxVcBwAbr_Type(Integer32):
    """Custom type cwspMaxVcBwAbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcBwAbr_Type.__name__ = "Integer32"
_CwspMaxVcBwAbr_Object = MibTableColumn
cwspMaxVcBwAbr = _CwspMaxVcBwAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 29),
    _CwspMaxVcBwAbr_Type()
)
cwspMaxVcBwAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcBwAbr.setStatus("current")


class _CwspMaxVcBwUbr_Type(Integer32):
    """Custom type cwspMaxVcBwUbr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CwspMaxVcBwUbr_Type.__name__ = "Integer32"
_CwspMaxVcBwUbr_Object = MibTableColumn
cwspMaxVcBwUbr = _CwspMaxVcBwUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 30),
    _CwspMaxVcBwUbr_Type()
)
cwspMaxVcBwUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspMaxVcBwUbr.setStatus("current")


class _CwspDefaultCdvtCbr_Type(Integer32):
    """Custom type cwspDefaultCdvtCbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultCdvtCbr_Type.__name__ = "Integer32"
_CwspDefaultCdvtCbr_Object = MibTableColumn
cwspDefaultCdvtCbr = _CwspDefaultCdvtCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 31),
    _CwspDefaultCdvtCbr_Type()
)
cwspDefaultCdvtCbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultCdvtCbr.setStatus("current")


class _CwspDefaultCdvtRtVbr_Type(Integer32):
    """Custom type cwspDefaultCdvtRtVbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultCdvtRtVbr_Type.__name__ = "Integer32"
_CwspDefaultCdvtRtVbr_Object = MibTableColumn
cwspDefaultCdvtRtVbr = _CwspDefaultCdvtRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 32),
    _CwspDefaultCdvtRtVbr_Type()
)
cwspDefaultCdvtRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultCdvtRtVbr.setStatus("current")


class _CwspDefaultCdvtNrtVbr_Type(Integer32):
    """Custom type cwspDefaultCdvtNrtVbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultCdvtNrtVbr_Type.__name__ = "Integer32"
_CwspDefaultCdvtNrtVbr_Object = MibTableColumn
cwspDefaultCdvtNrtVbr = _CwspDefaultCdvtNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 33),
    _CwspDefaultCdvtNrtVbr_Type()
)
cwspDefaultCdvtNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultCdvtNrtVbr.setStatus("current")


class _CwspDefaultCdvtAbr_Type(Integer32):
    """Custom type cwspDefaultCdvtAbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultCdvtAbr_Type.__name__ = "Integer32"
_CwspDefaultCdvtAbr_Object = MibTableColumn
cwspDefaultCdvtAbr = _CwspDefaultCdvtAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 34),
    _CwspDefaultCdvtAbr_Type()
)
cwspDefaultCdvtAbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultCdvtAbr.setStatus("current")


class _CwspDefaultCdvtUbr_Type(Integer32):
    """Custom type cwspDefaultCdvtUbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultCdvtUbr_Type.__name__ = "Integer32"
_CwspDefaultCdvtUbr_Object = MibTableColumn
cwspDefaultCdvtUbr = _CwspDefaultCdvtUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 35),
    _CwspDefaultCdvtUbr_Type()
)
cwspDefaultCdvtUbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultCdvtUbr.setStatus("current")


class _CwspDefaultMbsRtVbr_Type(Integer32):
    """Custom type cwspDefaultMbsRtVbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultMbsRtVbr_Type.__name__ = "Integer32"
_CwspDefaultMbsRtVbr_Object = MibTableColumn
cwspDefaultMbsRtVbr = _CwspDefaultMbsRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 36),
    _CwspDefaultMbsRtVbr_Type()
)
cwspDefaultMbsRtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultMbsRtVbr.setStatus("current")


class _CwspDefaultMbsNrtVbr_Type(Integer32):
    """Custom type cwspDefaultMbsNrtVbr based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspDefaultMbsNrtVbr_Type.__name__ = "Integer32"
_CwspDefaultMbsNrtVbr_Object = MibTableColumn
cwspDefaultMbsNrtVbr = _CwspDefaultMbsNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 2, 1, 1, 37),
    _CwspDefaultMbsNrtVbr_Type()
)
cwspDefaultMbsNrtVbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspDefaultMbsNrtVbr.setStatus("current")
_CwspSigConfig_ObjectIdentity = ObjectIdentity
cwspSigConfig = _CwspSigConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3)
)
_CwspSigConfigTable_Object = MibTable
cwspSigConfigTable = _CwspSigConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cwspSigConfigTable.setStatus("current")
_CwspSigConfigEntry_Object = MibTableRow
cwspSigConfigEntry = _CwspSigConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1)
)
cwspSigConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspSigConfigEntry.setStatus("current")


class _CwspSigCfgT301_Type(Integer32):
    """Custom type cwspSigCfgT301 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 240),
    )


_CwspSigCfgT301_Type.__name__ = "Integer32"
_CwspSigCfgT301_Object = MibTableColumn
cwspSigCfgT301 = _CwspSigCfgT301_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 1),
    _CwspSigCfgT301_Type()
)
cwspSigCfgT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT301.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT301.setUnits("seconds")


class _CwspSigCfgT303_Type(Integer32):
    """Custom type cwspSigCfgT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_CwspSigCfgT303_Type.__name__ = "Integer32"
_CwspSigCfgT303_Object = MibTableColumn
cwspSigCfgT303 = _CwspSigCfgT303_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 2),
    _CwspSigCfgT303_Type()
)
cwspSigCfgT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT303.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT303.setUnits("seconds")


class _CwspSigCfgT308_Type(Integer32):
    """Custom type cwspSigCfgT308 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 45),
    )


_CwspSigCfgT308_Type.__name__ = "Integer32"
_CwspSigCfgT308_Object = MibTableColumn
cwspSigCfgT308 = _CwspSigCfgT308_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 3),
    _CwspSigCfgT308_Type()
)
cwspSigCfgT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT308.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT308.setUnits("seconds")


class _CwspSigCfgT310_Type(Integer32):
    """Custom type cwspSigCfgT310 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_CwspSigCfgT310_Type.__name__ = "Integer32"
_CwspSigCfgT310_Object = MibTableColumn
cwspSigCfgT310 = _CwspSigCfgT310_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 4),
    _CwspSigCfgT310_Type()
)
cwspSigCfgT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT310.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT310.setUnits("seconds")


class _CwspSigCfgT316_Type(Integer32):
    """Custom type cwspSigCfgT316 based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 300),
    )


_CwspSigCfgT316_Type.__name__ = "Integer32"
_CwspSigCfgT316_Object = MibTableColumn
cwspSigCfgT316 = _CwspSigCfgT316_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 5),
    _CwspSigCfgT316_Type()
)
cwspSigCfgT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT316.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT316.setUnits("seconds")


class _CwspSigCfgT317_Type(Integer32):
    """Custom type cwspSigCfgT317 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_CwspSigCfgT317_Type.__name__ = "Integer32"
_CwspSigCfgT317_Object = MibTableColumn
cwspSigCfgT317 = _CwspSigCfgT317_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 6),
    _CwspSigCfgT317_Type()
)
cwspSigCfgT317.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT317.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT317.setUnits("seconds")


class _CwspSigCfgT322_Type(Integer32):
    """Custom type cwspSigCfgT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_CwspSigCfgT322_Type.__name__ = "Integer32"
_CwspSigCfgT322_Object = MibTableColumn
cwspSigCfgT322 = _CwspSigCfgT322_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 7),
    _CwspSigCfgT322_Type()
)
cwspSigCfgT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT322.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT322.setUnits("seconds")


class _CwspSigCfgT397_Type(Integer32):
    """Custom type cwspSigCfgT397 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 240),
    )


_CwspSigCfgT397_Type.__name__ = "Integer32"
_CwspSigCfgT397_Object = MibTableColumn
cwspSigCfgT397 = _CwspSigCfgT397_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 8),
    _CwspSigCfgT397_Type()
)
cwspSigCfgT397.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT397.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT397.setUnits("seconds")


class _CwspSigCfgT398_Type(Integer32):
    """Custom type cwspSigCfgT398 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_CwspSigCfgT398_Type.__name__ = "Integer32"
_CwspSigCfgT398_Object = MibTableColumn
cwspSigCfgT398 = _CwspSigCfgT398_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 9),
    _CwspSigCfgT398_Type()
)
cwspSigCfgT398.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT398.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT398.setUnits("seconds")


class _CwspSigCfgT399_Type(Integer32):
    """Custom type cwspSigCfgT399 based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 124),
    )


_CwspSigCfgT399_Type.__name__ = "Integer32"
_CwspSigCfgT399_Object = MibTableColumn
cwspSigCfgT399 = _CwspSigCfgT399_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 3, 1, 1, 10),
    _CwspSigCfgT399_Type()
)
cwspSigCfgT399.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCfgT399.setStatus("current")
if mibBuilder.loadTexts:
    cwspSigCfgT399.setUnits("seconds")
_CwspSscopConfig_ObjectIdentity = ObjectIdentity
cwspSscopConfig = _CwspSscopConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4)
)
_CwspSscopTable_Object = MibTable
cwspSscopTable = _CwspSscopTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cwspSscopTable.setStatus("current")
_CwspSscopEntry_Object = MibTableRow
cwspSscopEntry = _CwspSscopEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1)
)
cwspSscopEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspSscopEntry.setStatus("current")


class _CwspSscopTmrCC_Type(Integer32):
    """Custom type cwspSscopTmrCC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopTmrCC_Type.__name__ = "Integer32"
_CwspSscopTmrCC_Object = MibTableColumn
cwspSscopTmrCC = _CwspSscopTmrCC_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 1),
    _CwspSscopTmrCC_Type()
)
cwspSscopTmrCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopTmrCC.setStatus("current")
if mibBuilder.loadTexts:
    cwspSscopTmrCC.setUnits("seconds")


class _CwspSscopTmrKeepAlive_Type(Integer32):
    """Custom type cwspSscopTmrKeepAlive based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopTmrKeepAlive_Type.__name__ = "Integer32"
_CwspSscopTmrKeepAlive_Object = MibTableColumn
cwspSscopTmrKeepAlive = _CwspSscopTmrKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 2),
    _CwspSscopTmrKeepAlive_Type()
)
cwspSscopTmrKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopTmrKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    cwspSscopTmrKeepAlive.setUnits("seconds")


class _CwspSscopTmrNoResp_Type(Integer32):
    """Custom type cwspSscopTmrNoResp based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopTmrNoResp_Type.__name__ = "Integer32"
_CwspSscopTmrNoResp_Object = MibTableColumn
cwspSscopTmrNoResp = _CwspSscopTmrNoResp_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 3),
    _CwspSscopTmrNoResp_Type()
)
cwspSscopTmrNoResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopTmrNoResp.setStatus("current")
if mibBuilder.loadTexts:
    cwspSscopTmrNoResp.setUnits("seconds")


class _CwspSscopTmrPoll_Type(Integer32):
    """Custom type cwspSscopTmrPoll based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopTmrPoll_Type.__name__ = "Integer32"
_CwspSscopTmrPoll_Object = MibTableColumn
cwspSscopTmrPoll = _CwspSscopTmrPoll_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 4),
    _CwspSscopTmrPoll_Type()
)
cwspSscopTmrPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopTmrPoll.setStatus("current")
if mibBuilder.loadTexts:
    cwspSscopTmrPoll.setUnits("seconds")


class _CwspSscopTmtIdle_Type(Integer32):
    """Custom type cwspSscopTmtIdle based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopTmtIdle_Type.__name__ = "Integer32"
_CwspSscopTmtIdle_Object = MibTableColumn
cwspSscopTmtIdle = _CwspSscopTmtIdle_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 5),
    _CwspSscopTmtIdle_Type()
)
cwspSscopTmtIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopTmtIdle.setStatus("current")
if mibBuilder.loadTexts:
    cwspSscopTmtIdle.setUnits("seconds")


class _CwspSscopMaxCC_Type(Integer32):
    """Custom type cwspSscopMaxCC based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopMaxCC_Type.__name__ = "Integer32"
_CwspSscopMaxCC_Object = MibTableColumn
cwspSscopMaxCC = _CwspSscopMaxCC_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 6),
    _CwspSscopMaxCC_Type()
)
cwspSscopMaxCC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopMaxCC.setStatus("current")


class _CwspSscopMaxPD_Type(Integer32):
    """Custom type cwspSscopMaxPD based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopMaxPD_Type.__name__ = "Integer32"
_CwspSscopMaxPD_Object = MibTableColumn
cwspSscopMaxPD = _CwspSscopMaxPD_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 7),
    _CwspSscopMaxPD_Type()
)
cwspSscopMaxPD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopMaxPD.setStatus("current")


class _CwspSscopMaxSTAT_Type(Integer32):
    """Custom type cwspSscopMaxSTAT based on Integer32"""
    defaultValue = 67

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspSscopMaxSTAT_Type.__name__ = "Integer32"
_CwspSscopMaxSTAT_Object = MibTableColumn
cwspSscopMaxSTAT = _CwspSscopMaxSTAT_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 4, 1, 1, 8),
    _CwspSscopMaxSTAT_Type()
)
cwspSscopMaxSTAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopMaxSTAT.setStatus("current")
_CwspCallStats_ObjectIdentity = ObjectIdentity
cwspCallStats = _CwspCallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5)
)
_CwspCallStatsTable_Object = MibTable
cwspCallStatsTable = _CwspCallStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cwspCallStatsTable.setStatus("current")
_CwspCallStatsEntry_Object = MibTableRow
cwspCallStatsEntry = _CwspCallStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1)
)
cwspCallStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspCallStatsEntry.setStatus("current")


class _CwspCountReset_Type(Integer32):
    """Custom type cwspCountReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_CwspCountReset_Type.__name__ = "Integer32"
_CwspCountReset_Object = MibTableColumn
cwspCountReset = _CwspCountReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 1),
    _CwspCountReset_Type()
)
cwspCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspCountReset.setStatus("current")
_CwspInCallAttempts_Type = Counter32
_CwspInCallAttempts_Object = MibTableColumn
cwspInCallAttempts = _CwspInCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 2),
    _CwspInCallAttempts_Type()
)
cwspInCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInCallAttempts.setStatus("current")
_CwspInCallEstabs_Type = Counter32
_CwspInCallEstabs_Object = MibTableColumn
cwspInCallEstabs = _CwspInCallEstabs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 3),
    _CwspInCallEstabs_Type()
)
cwspInCallEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInCallEstabs.setStatus("current")
_CwspInCallFailures_Type = Counter32
_CwspInCallFailures_Object = MibTableColumn
cwspInCallFailures = _CwspInCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 4),
    _CwspInCallFailures_Type()
)
cwspInCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInCallFailures.setStatus("current")
_CwspInFilterFailures_Type = Counter32
_CwspInFilterFailures_Object = MibTableColumn
cwspInFilterFailures = _CwspInFilterFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 5),
    _CwspInFilterFailures_Type()
)
cwspInFilterFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInFilterFailures.setStatus("current")
_CwspInRouteFailures_Type = Counter32
_CwspInRouteFailures_Object = MibTableColumn
cwspInRouteFailures = _CwspInRouteFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 6),
    _CwspInRouteFailures_Type()
)
cwspInRouteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInRouteFailures.setStatus("current")
_CwspInResrcFailures_Type = Counter32
_CwspInResrcFailures_Object = MibTableColumn
cwspInResrcFailures = _CwspInResrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 7),
    _CwspInResrcFailures_Type()
)
cwspInResrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInResrcFailures.setStatus("current")
_CwspInTimerFailures_Type = Counter32
_CwspInTimerFailures_Object = MibTableColumn
cwspInTimerFailures = _CwspInTimerFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 8),
    _CwspInTimerFailures_Type()
)
cwspInTimerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInTimerFailures.setStatus("current")
_CwspInCrankbacks_Type = Counter32
_CwspInCrankbacks_Object = MibTableColumn
cwspInCrankbacks = _CwspInCrankbacks_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 9),
    _CwspInCrankbacks_Type()
)
cwspInCrankbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspInCrankbacks.setStatus("current")
_CwspOutCallAttempts_Type = Counter32
_CwspOutCallAttempts_Object = MibTableColumn
cwspOutCallAttempts = _CwspOutCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 10),
    _CwspOutCallAttempts_Type()
)
cwspOutCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutCallAttempts.setStatus("current")
_CwspOutCallEstabs_Type = Counter32
_CwspOutCallEstabs_Object = MibTableColumn
cwspOutCallEstabs = _CwspOutCallEstabs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 11),
    _CwspOutCallEstabs_Type()
)
cwspOutCallEstabs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutCallEstabs.setStatus("current")
_CwspOutCallFailures_Type = Counter32
_CwspOutCallFailures_Object = MibTableColumn
cwspOutCallFailures = _CwspOutCallFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 12),
    _CwspOutCallFailures_Type()
)
cwspOutCallFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutCallFailures.setStatus("current")
_CwspOutFilterFailures_Type = Counter32
_CwspOutFilterFailures_Object = MibTableColumn
cwspOutFilterFailures = _CwspOutFilterFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 13),
    _CwspOutFilterFailures_Type()
)
cwspOutFilterFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutFilterFailures.setStatus("current")
_CwspOutRouteFailures_Type = Counter32
_CwspOutRouteFailures_Object = MibTableColumn
cwspOutRouteFailures = _CwspOutRouteFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 14),
    _CwspOutRouteFailures_Type()
)
cwspOutRouteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutRouteFailures.setStatus("current")
_CwspOutResrcFailures_Type = Counter32
_CwspOutResrcFailures_Object = MibTableColumn
cwspOutResrcFailures = _CwspOutResrcFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 15),
    _CwspOutResrcFailures_Type()
)
cwspOutResrcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutResrcFailures.setStatus("current")
_CwspOutTimerFailures_Type = Counter32
_CwspOutTimerFailures_Object = MibTableColumn
cwspOutTimerFailures = _CwspOutTimerFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 16),
    _CwspOutTimerFailures_Type()
)
cwspOutTimerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutTimerFailures.setStatus("current")
_CwspOutCrankbacks_Type = Counter32
_CwspOutCrankbacks_Object = MibTableColumn
cwspOutCrankbacks = _CwspOutCrankbacks_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 5, 1, 1, 17),
    _CwspOutCrankbacks_Type()
)
cwspOutCrankbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOutCrankbacks.setStatus("current")
_CwspSigStats_ObjectIdentity = ObjectIdentity
cwspSigStats = _CwspSigStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6)
)
_CwspSigStatsTable_Object = MibTable
cwspSigStatsTable = _CwspSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cwspSigStatsTable.setStatus("current")
_CwspSigStatsEntry_Object = MibTableRow
cwspSigStatsEntry = _CwspSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1)
)
cwspSigStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspSigStatsEntry.setStatus("current")


class _CwspSigCounterReset_Type(Integer32):
    """Custom type cwspSigCounterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_CwspSigCounterReset_Type.__name__ = "Integer32"
_CwspSigCounterReset_Object = MibTableColumn
cwspSigCounterReset = _CwspSigCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 1),
    _CwspSigCounterReset_Type()
)
cwspSigCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSigCounterReset.setStatus("current")
_CwspCallProcRcv_Type = Counter32
_CwspCallProcRcv_Object = MibTableColumn
cwspCallProcRcv = _CwspCallProcRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 2),
    _CwspCallProcRcv_Type()
)
cwspCallProcRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallProcRcv.setStatus("current")
_CwspConnectRcv_Type = Counter32
_CwspConnectRcv_Object = MibTableColumn
cwspConnectRcv = _CwspConnectRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 3),
    _CwspConnectRcv_Type()
)
cwspConnectRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnectRcv.setStatus("current")
_CwspConnectAckRcv_Type = Counter32
_CwspConnectAckRcv_Object = MibTableColumn
cwspConnectAckRcv = _CwspConnectAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 4),
    _CwspConnectAckRcv_Type()
)
cwspConnectAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnectAckRcv.setStatus("current")
_CwspSetupRcv_Type = Counter32
_CwspSetupRcv_Object = MibTableColumn
cwspSetupRcv = _CwspSetupRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 5),
    _CwspSetupRcv_Type()
)
cwspSetupRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSetupRcv.setStatus("current")
_CwspReleaseRcv_Type = Counter32
_CwspReleaseRcv_Object = MibTableColumn
cwspReleaseRcv = _CwspReleaseRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 6),
    _CwspReleaseRcv_Type()
)
cwspReleaseRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspReleaseRcv.setStatus("current")
_CwspReleaseComplRcv_Type = Counter32
_CwspReleaseComplRcv_Object = MibTableColumn
cwspReleaseComplRcv = _CwspReleaseComplRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 7),
    _CwspReleaseComplRcv_Type()
)
cwspReleaseComplRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspReleaseComplRcv.setStatus("current")
_CwspRestartRcv_Type = Counter32
_CwspRestartRcv_Object = MibTableColumn
cwspRestartRcv = _CwspRestartRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 8),
    _CwspRestartRcv_Type()
)
cwspRestartRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspRestartRcv.setStatus("current")
_CwspRestartAckRcv_Type = Counter32
_CwspRestartAckRcv_Object = MibTableColumn
cwspRestartAckRcv = _CwspRestartAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 9),
    _CwspRestartAckRcv_Type()
)
cwspRestartAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspRestartAckRcv.setStatus("current")
_CwspStatusRcv_Type = Counter32
_CwspStatusRcv_Object = MibTableColumn
cwspStatusRcv = _CwspStatusRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 10),
    _CwspStatusRcv_Type()
)
cwspStatusRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspStatusRcv.setStatus("current")
_CwspStatusEnqRcv_Type = Counter32
_CwspStatusEnqRcv_Object = MibTableColumn
cwspStatusEnqRcv = _CwspStatusEnqRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 11),
    _CwspStatusEnqRcv_Type()
)
cwspStatusEnqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspStatusEnqRcv.setStatus("current")
_CwspNotifyRcv_Type = Counter32
_CwspNotifyRcv_Object = MibTableColumn
cwspNotifyRcv = _CwspNotifyRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 12),
    _CwspNotifyRcv_Type()
)
cwspNotifyRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspNotifyRcv.setStatus("current")
_CwspAlertRcv_Type = Counter32
_CwspAlertRcv_Object = MibTableColumn
cwspAlertRcv = _CwspAlertRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 13),
    _CwspAlertRcv_Type()
)
cwspAlertRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAlertRcv.setStatus("current")
_CwspProgressRcv_Type = Counter32
_CwspProgressRcv_Object = MibTableColumn
cwspProgressRcv = _CwspProgressRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 14),
    _CwspProgressRcv_Type()
)
cwspProgressRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspProgressRcv.setStatus("current")
_CwspAddPtyRcv_Type = Counter32
_CwspAddPtyRcv_Object = MibTableColumn
cwspAddPtyRcv = _CwspAddPtyRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 15),
    _CwspAddPtyRcv_Type()
)
cwspAddPtyRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAddPtyRcv.setStatus("current")
_CwspAddPtyAckRcv_Type = Counter32
_CwspAddPtyAckRcv_Object = MibTableColumn
cwspAddPtyAckRcv = _CwspAddPtyAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 16),
    _CwspAddPtyAckRcv_Type()
)
cwspAddPtyAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAddPtyAckRcv.setStatus("current")
_CwspAddPtyRejRcv_Type = Counter32
_CwspAddPtyRejRcv_Object = MibTableColumn
cwspAddPtyRejRcv = _CwspAddPtyRejRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 17),
    _CwspAddPtyRejRcv_Type()
)
cwspAddPtyRejRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAddPtyRejRcv.setStatus("current")
_CwspDropPtyRcv_Type = Counter32
_CwspDropPtyRcv_Object = MibTableColumn
cwspDropPtyRcv = _CwspDropPtyRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 18),
    _CwspDropPtyRcv_Type()
)
cwspDropPtyRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspDropPtyRcv.setStatus("current")
_CwspIncorrectMsgRcv_Type = Counter32
_CwspIncorrectMsgRcv_Object = MibTableColumn
cwspIncorrectMsgRcv = _CwspIncorrectMsgRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 20),
    _CwspIncorrectMsgRcv_Type()
)
cwspIncorrectMsgRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspIncorrectMsgRcv.setStatus("current")
_CwspTimerExpiries_Type = Counter32
_CwspTimerExpiries_Object = MibTableColumn
cwspTimerExpiries = _CwspTimerExpiries_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 21),
    _CwspTimerExpiries_Type()
)
cwspTimerExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspTimerExpiries.setStatus("current")
_CwspLastCause_Type = Counter32
_CwspLastCause_Object = MibTableColumn
cwspLastCause = _CwspLastCause_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 22),
    _CwspLastCause_Type()
)
cwspLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLastCause.setStatus("current")


class _CwspLastDiagnostic_Type(Integer32):
    """Custom type cwspLastDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 214743647),
    )


_CwspLastDiagnostic_Type.__name__ = "Integer32"
_CwspLastDiagnostic_Object = MibTableColumn
cwspLastDiagnostic = _CwspLastDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 23),
    _CwspLastDiagnostic_Type()
)
cwspLastDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLastDiagnostic.setStatus("current")
_CwspCallProcXmt_Type = Counter32
_CwspCallProcXmt_Object = MibTableColumn
cwspCallProcXmt = _CwspCallProcXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 24),
    _CwspCallProcXmt_Type()
)
cwspCallProcXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallProcXmt.setStatus("current")
_CwspConnectXmt_Type = Counter32
_CwspConnectXmt_Object = MibTableColumn
cwspConnectXmt = _CwspConnectXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 25),
    _CwspConnectXmt_Type()
)
cwspConnectXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnectXmt.setStatus("current")
_CwspConnectAckXmt_Type = Counter32
_CwspConnectAckXmt_Object = MibTableColumn
cwspConnectAckXmt = _CwspConnectAckXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 26),
    _CwspConnectAckXmt_Type()
)
cwspConnectAckXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnectAckXmt.setStatus("current")
_CwspSetupXmt_Type = Counter32
_CwspSetupXmt_Object = MibTableColumn
cwspSetupXmt = _CwspSetupXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 27),
    _CwspSetupXmt_Type()
)
cwspSetupXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSetupXmt.setStatus("current")
_CwspReleaseXmt_Type = Counter32
_CwspReleaseXmt_Object = MibTableColumn
cwspReleaseXmt = _CwspReleaseXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 28),
    _CwspReleaseXmt_Type()
)
cwspReleaseXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspReleaseXmt.setStatus("current")
_CwspReleaseComplXmt_Type = Counter32
_CwspReleaseComplXmt_Object = MibTableColumn
cwspReleaseComplXmt = _CwspReleaseComplXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 29),
    _CwspReleaseComplXmt_Type()
)
cwspReleaseComplXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspReleaseComplXmt.setStatus("current")
_CwspRestartXmt_Type = Counter32
_CwspRestartXmt_Object = MibTableColumn
cwspRestartXmt = _CwspRestartXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 30),
    _CwspRestartXmt_Type()
)
cwspRestartXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspRestartXmt.setStatus("current")
_CwspRestartAckXmt_Type = Counter32
_CwspRestartAckXmt_Object = MibTableColumn
cwspRestartAckXmt = _CwspRestartAckXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 31),
    _CwspRestartAckXmt_Type()
)
cwspRestartAckXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspRestartAckXmt.setStatus("current")
_CwspStatusXmt_Type = Counter32
_CwspStatusXmt_Object = MibTableColumn
cwspStatusXmt = _CwspStatusXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 32),
    _CwspStatusXmt_Type()
)
cwspStatusXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspStatusXmt.setStatus("current")
_CwspStatusEnqXmt_Type = Counter32
_CwspStatusEnqXmt_Object = MibTableColumn
cwspStatusEnqXmt = _CwspStatusEnqXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 33),
    _CwspStatusEnqXmt_Type()
)
cwspStatusEnqXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspStatusEnqXmt.setStatus("current")
_CwspNotifyXmt_Type = Counter32
_CwspNotifyXmt_Object = MibTableColumn
cwspNotifyXmt = _CwspNotifyXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 34),
    _CwspNotifyXmt_Type()
)
cwspNotifyXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspNotifyXmt.setStatus("current")
_CwspAlertXmt_Type = Counter32
_CwspAlertXmt_Object = MibTableColumn
cwspAlertXmt = _CwspAlertXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 35),
    _CwspAlertXmt_Type()
)
cwspAlertXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAlertXmt.setStatus("current")
_CwspProgressXmt_Type = Counter32
_CwspProgressXmt_Object = MibTableColumn
cwspProgressXmt = _CwspProgressXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 36),
    _CwspProgressXmt_Type()
)
cwspProgressXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspProgressXmt.setStatus("current")
_CwspAddPtyXmt_Type = Counter32
_CwspAddPtyXmt_Object = MibTableColumn
cwspAddPtyXmt = _CwspAddPtyXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 37),
    _CwspAddPtyXmt_Type()
)
cwspAddPtyXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAddPtyXmt.setStatus("current")
_CwspAddPtyAckXmt_Type = Counter32
_CwspAddPtyAckXmt_Object = MibTableColumn
cwspAddPtyAckXmt = _CwspAddPtyAckXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 38),
    _CwspAddPtyAckXmt_Type()
)
cwspAddPtyAckXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAddPtyAckXmt.setStatus("current")
_CwspAddPtyRejXmt_Type = Counter32
_CwspAddPtyRejXmt_Object = MibTableColumn
cwspAddPtyRejXmt = _CwspAddPtyRejXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 39),
    _CwspAddPtyRejXmt_Type()
)
cwspAddPtyRejXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAddPtyRejXmt.setStatus("current")
_CwspDropPtyXmt_Type = Counter32
_CwspDropPtyXmt_Object = MibTableColumn
cwspDropPtyXmt = _CwspDropPtyXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 40),
    _CwspDropPtyXmt_Type()
)
cwspDropPtyXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspDropPtyXmt.setStatus("current")


class _CwspSscopStatus_Type(Integer32):
    """Custom type cwspSscopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CwspSscopStatus_Type.__name__ = "Integer32"
_CwspSscopStatus_Object = MibTableColumn
cwspSscopStatus = _CwspSscopStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 6, 1, 1, 42),
    _CwspSscopStatus_Type()
)
cwspSscopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopStatus.setStatus("current")
_CwspSscopStats_ObjectIdentity = ObjectIdentity
cwspSscopStats = _CwspSscopStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7)
)
_CwspSscopStatsTable_Object = MibTable
cwspSscopStatsTable = _CwspSscopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cwspSscopStatsTable.setStatus("current")
_CwspSscopStatsEntry_Object = MibTableRow
cwspSscopStatsEntry = _CwspSscopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1)
)
cwspSscopStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspSscopStatsEntry.setStatus("current")


class _CwspSscopCounterReset_Type(Integer32):
    """Custom type cwspSscopCounterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_CwspSscopCounterReset_Type.__name__ = "Integer32"
_CwspSscopCounterReset_Object = MibTableColumn
cwspSscopCounterReset = _CwspSscopCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 1),
    _CwspSscopCounterReset_Type()
)
cwspSscopCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSscopCounterReset.setStatus("current")
_CwspSscopIgnoredPduRcv_Type = Counter32
_CwspSscopIgnoredPduRcv_Object = MibTableColumn
cwspSscopIgnoredPduRcv = _CwspSscopIgnoredPduRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 2),
    _CwspSscopIgnoredPduRcv_Type()
)
cwspSscopIgnoredPduRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopIgnoredPduRcv.setStatus("current")
_CwspSscopBgnRcv_Type = Counter32
_CwspSscopBgnRcv_Object = MibTableColumn
cwspSscopBgnRcv = _CwspSscopBgnRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 3),
    _CwspSscopBgnRcv_Type()
)
cwspSscopBgnRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopBgnRcv.setStatus("current")
_CwspSscopBgakRcv_Type = Counter32
_CwspSscopBgakRcv_Object = MibTableColumn
cwspSscopBgakRcv = _CwspSscopBgakRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 4),
    _CwspSscopBgakRcv_Type()
)
cwspSscopBgakRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopBgakRcv.setStatus("current")
_CwspSscopEndRcv_Type = Counter32
_CwspSscopEndRcv_Object = MibTableColumn
cwspSscopEndRcv = _CwspSscopEndRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 5),
    _CwspSscopEndRcv_Type()
)
cwspSscopEndRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopEndRcv.setStatus("current")
_CwspSscopEndakRcv_Type = Counter32
_CwspSscopEndakRcv_Object = MibTableColumn
cwspSscopEndakRcv = _CwspSscopEndakRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 6),
    _CwspSscopEndakRcv_Type()
)
cwspSscopEndakRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopEndakRcv.setStatus("current")
_CwspSscopRsRcv_Type = Counter32
_CwspSscopRsRcv_Object = MibTableColumn
cwspSscopRsRcv = _CwspSscopRsRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 7),
    _CwspSscopRsRcv_Type()
)
cwspSscopRsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopRsRcv.setStatus("current")
_CwspSscopRsakRcv_Type = Counter32
_CwspSscopRsakRcv_Object = MibTableColumn
cwspSscopRsakRcv = _CwspSscopRsakRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 8),
    _CwspSscopRsakRcv_Type()
)
cwspSscopRsakRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopRsakRcv.setStatus("current")
_CwspSscopBgrejRcv_Type = Counter32
_CwspSscopBgrejRcv_Object = MibTableColumn
cwspSscopBgrejRcv = _CwspSscopBgrejRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 9),
    _CwspSscopBgrejRcv_Type()
)
cwspSscopBgrejRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopBgrejRcv.setStatus("current")
_CwspSscopSdRcv_Type = Counter32
_CwspSscopSdRcv_Object = MibTableColumn
cwspSscopSdRcv = _CwspSscopSdRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 10),
    _CwspSscopSdRcv_Type()
)
cwspSscopSdRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopSdRcv.setStatus("current")
_CwspSscopSdpRcv_Type = Counter32
_CwspSscopSdpRcv_Object = MibTableColumn
cwspSscopSdpRcv = _CwspSscopSdpRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 11),
    _CwspSscopSdpRcv_Type()
)
cwspSscopSdpRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopSdpRcv.setStatus("current")
_CwspSscopPollRcv_Type = Counter32
_CwspSscopPollRcv_Object = MibTableColumn
cwspSscopPollRcv = _CwspSscopPollRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 12),
    _CwspSscopPollRcv_Type()
)
cwspSscopPollRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopPollRcv.setStatus("current")
_CwspSscopStatRcv_Type = Counter32
_CwspSscopStatRcv_Object = MibTableColumn
cwspSscopStatRcv = _CwspSscopStatRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 13),
    _CwspSscopStatRcv_Type()
)
cwspSscopStatRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopStatRcv.setStatus("current")
_CwspSscopUstatRcv_Type = Counter32
_CwspSscopUstatRcv_Object = MibTableColumn
cwspSscopUstatRcv = _CwspSscopUstatRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 14),
    _CwspSscopUstatRcv_Type()
)
cwspSscopUstatRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopUstatRcv.setStatus("current")
_CwspSscopUdRcv_Type = Counter32
_CwspSscopUdRcv_Object = MibTableColumn
cwspSscopUdRcv = _CwspSscopUdRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 15),
    _CwspSscopUdRcv_Type()
)
cwspSscopUdRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopUdRcv.setStatus("current")
_CwspSscopMdRcv_Type = Counter32
_CwspSscopMdRcv_Object = MibTableColumn
cwspSscopMdRcv = _CwspSscopMdRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 16),
    _CwspSscopMdRcv_Type()
)
cwspSscopMdRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopMdRcv.setStatus("current")
_CwspSscopErakRcv_Type = Counter32
_CwspSscopErakRcv_Object = MibTableColumn
cwspSscopErakRcv = _CwspSscopErakRcv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 17),
    _CwspSscopErakRcv_Type()
)
cwspSscopErakRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopErakRcv.setStatus("current")
_CwspSscopBgnXmt_Type = Counter32
_CwspSscopBgnXmt_Object = MibTableColumn
cwspSscopBgnXmt = _CwspSscopBgnXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 18),
    _CwspSscopBgnXmt_Type()
)
cwspSscopBgnXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopBgnXmt.setStatus("current")
_CwspSscopBgakXmt_Type = Counter32
_CwspSscopBgakXmt_Object = MibTableColumn
cwspSscopBgakXmt = _CwspSscopBgakXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 19),
    _CwspSscopBgakXmt_Type()
)
cwspSscopBgakXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopBgakXmt.setStatus("current")
_CwspSscopEndXmt_Type = Counter32
_CwspSscopEndXmt_Object = MibTableColumn
cwspSscopEndXmt = _CwspSscopEndXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 20),
    _CwspSscopEndXmt_Type()
)
cwspSscopEndXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopEndXmt.setStatus("current")
_CwspSscopEndakXmt_Type = Counter32
_CwspSscopEndakXmt_Object = MibTableColumn
cwspSscopEndakXmt = _CwspSscopEndakXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 21),
    _CwspSscopEndakXmt_Type()
)
cwspSscopEndakXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopEndakXmt.setStatus("current")
_CwspSscopRsXmt_Type = Counter32
_CwspSscopRsXmt_Object = MibTableColumn
cwspSscopRsXmt = _CwspSscopRsXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 22),
    _CwspSscopRsXmt_Type()
)
cwspSscopRsXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopRsXmt.setStatus("current")
_CwspSscopRsakXmt_Type = Counter32
_CwspSscopRsakXmt_Object = MibTableColumn
cwspSscopRsakXmt = _CwspSscopRsakXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 23),
    _CwspSscopRsakXmt_Type()
)
cwspSscopRsakXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopRsakXmt.setStatus("current")
_CwspSscopBgrejXmt_Type = Counter32
_CwspSscopBgrejXmt_Object = MibTableColumn
cwspSscopBgrejXmt = _CwspSscopBgrejXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 24),
    _CwspSscopBgrejXmt_Type()
)
cwspSscopBgrejXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopBgrejXmt.setStatus("current")
_CwspSscopSdXmt_Type = Counter32
_CwspSscopSdXmt_Object = MibTableColumn
cwspSscopSdXmt = _CwspSscopSdXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 25),
    _CwspSscopSdXmt_Type()
)
cwspSscopSdXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopSdXmt.setStatus("current")
_CwspSscopSdpXmt_Type = Counter32
_CwspSscopSdpXmt_Object = MibTableColumn
cwspSscopSdpXmt = _CwspSscopSdpXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 26),
    _CwspSscopSdpXmt_Type()
)
cwspSscopSdpXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopSdpXmt.setStatus("current")
_CwspSscopPollXmt_Type = Counter32
_CwspSscopPollXmt_Object = MibTableColumn
cwspSscopPollXmt = _CwspSscopPollXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 27),
    _CwspSscopPollXmt_Type()
)
cwspSscopPollXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopPollXmt.setStatus("current")
_CwspSscopStatXmt_Type = Counter32
_CwspSscopStatXmt_Object = MibTableColumn
cwspSscopStatXmt = _CwspSscopStatXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 28),
    _CwspSscopStatXmt_Type()
)
cwspSscopStatXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopStatXmt.setStatus("current")
_CwspSscopUstatXmt_Type = Counter32
_CwspSscopUstatXmt_Object = MibTableColumn
cwspSscopUstatXmt = _CwspSscopUstatXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 29),
    _CwspSscopUstatXmt_Type()
)
cwspSscopUstatXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopUstatXmt.setStatus("current")
_CwspSscopUdXmt_Type = Counter32
_CwspSscopUdXmt_Object = MibTableColumn
cwspSscopUdXmt = _CwspSscopUdXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 30),
    _CwspSscopUdXmt_Type()
)
cwspSscopUdXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopUdXmt.setStatus("current")
_CwspSscopMdXmt_Type = Counter32
_CwspSscopMdXmt_Object = MibTableColumn
cwspSscopMdXmt = _CwspSscopMdXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 31),
    _CwspSscopMdXmt_Type()
)
cwspSscopMdXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopMdXmt.setStatus("current")
_CwspSscopErakXmt_Type = Counter32
_CwspSscopErakXmt_Object = MibTableColumn
cwspSscopErakXmt = _CwspSscopErakXmt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 7, 1, 1, 32),
    _CwspSscopErakXmt_Type()
)
cwspSscopErakXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspSscopErakXmt.setStatus("current")
_CwspCall_ObjectIdentity = ObjectIdentity
cwspCall = _CwspCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8)
)
_CwspCallTable_Object = MibTable
cwspCallTable = _CwspCallTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cwspCallTable.setStatus("current")
_CwspCallEntry_Object = MibTableRow
cwspCallEntry = _CwspCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1)
)
cwspCallEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-SVC-MIB", "cwspCallVpi"),
    (0, "CISCO-WAN-SVC-MIB", "cwspCallVci"),
    (0, "CISCO-WAN-SVC-MIB", "cwspCallLeafReference"),
)
if mibBuilder.loadTexts:
    cwspCallEntry.setStatus("current")


class _CwspCallVpi_Type(Integer32):
    """Custom type cwspCallVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspCallVpi_Type.__name__ = "Integer32"
_CwspCallVpi_Object = MibTableColumn
cwspCallVpi = _CwspCallVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 1),
    _CwspCallVpi_Type()
)
cwspCallVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspCallVpi.setStatus("current")


class _CwspCallVci_Type(Integer32):
    """Custom type cwspCallVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspCallVci_Type.__name__ = "Integer32"
_CwspCallVci_Object = MibTableColumn
cwspCallVci = _CwspCallVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 2),
    _CwspCallVci_Type()
)
cwspCallVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspCallVci.setStatus("current")


class _CwspCallLeafReference_Type(Integer32):
    """Custom type cwspCallLeafReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspCallLeafReference_Type.__name__ = "Integer32"
_CwspCallLeafReference_Object = MibTableColumn
cwspCallLeafReference = _CwspCallLeafReference_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 3),
    _CwspCallLeafReference_Type()
)
cwspCallLeafReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspCallLeafReference.setStatus("current")


class _CwspCallCallRef_Type(Integer32):
    """Custom type cwspCallCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallCallRef_Type.__name__ = "Integer32"
_CwspCallCallRef_Object = MibTableColumn
cwspCallCallRef = _CwspCallCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 4),
    _CwspCallCallRef_Type()
)
cwspCallCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallCallRef.setStatus("current")
_CwspCallCallingAddress_Type = AtmAddress
_CwspCallCallingAddress_Object = MibTableColumn
cwspCallCallingAddress = _CwspCallCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 5),
    _CwspCallCallingAddress_Type()
)
cwspCallCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallCallingAddress.setStatus("current")
_CwspCallCalledAddress_Type = AtmAddress
_CwspCallCalledAddress_Object = MibTableColumn
cwspCallCalledAddress = _CwspCallCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 6),
    _CwspCallCalledAddress_Type()
)
cwspCallCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallCalledAddress.setStatus("current")
_CwspCallCallingSubAddr_Type = AtmAddress
_CwspCallCallingSubAddr_Object = MibTableColumn
cwspCallCallingSubAddr = _CwspCallCallingSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 7),
    _CwspCallCallingSubAddr_Type()
)
cwspCallCallingSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallCallingSubAddr.setStatus("current")
_CwspCallCalledSubAddr_Type = AtmAddress
_CwspCallCalledSubAddr_Object = MibTableColumn
cwspCallCalledSubAddr = _CwspCallCalledSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 8),
    _CwspCallCalledSubAddr_Type()
)
cwspCallCalledSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallCalledSubAddr.setStatus("current")


class _CwspCallOtherIntfIndex_Type(Integer32):
    """Custom type cwspCallOtherIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallOtherIntfIndex_Type.__name__ = "Integer32"
_CwspCallOtherIntfIndex_Object = MibTableColumn
cwspCallOtherIntfIndex = _CwspCallOtherIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 9),
    _CwspCallOtherIntfIndex_Type()
)
cwspCallOtherIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallOtherIntfIndex.setStatus("current")


class _CwspCallOtherIntfVpi_Type(Integer32):
    """Custom type cwspCallOtherIntfVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspCallOtherIntfVpi_Type.__name__ = "Integer32"
_CwspCallOtherIntfVpi_Object = MibTableColumn
cwspCallOtherIntfVpi = _CwspCallOtherIntfVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 10),
    _CwspCallOtherIntfVpi_Type()
)
cwspCallOtherIntfVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallOtherIntfVpi.setStatus("current")


class _CwspCallOtherIntfVci_Type(Integer32):
    """Custom type cwspCallOtherIntfVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspCallOtherIntfVci_Type.__name__ = "Integer32"
_CwspCallOtherIntfVci_Object = MibTableColumn
cwspCallOtherIntfVci = _CwspCallOtherIntfVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 11),
    _CwspCallOtherIntfVci_Type()
)
cwspCallOtherIntfVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallOtherIntfVci.setStatus("current")


class _CwspCallOtherIntfCallRef_Type(Integer32):
    """Custom type cwspCallOtherIntfCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallOtherIntfCallRef_Type.__name__ = "Integer32"
_CwspCallOtherIntfCallRef_Object = MibTableColumn
cwspCallOtherIntfCallRef = _CwspCallOtherIntfCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 12),
    _CwspCallOtherIntfCallRef_Type()
)
cwspCallOtherIntfCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallOtherIntfCallRef.setStatus("current")


class _CwspCallType_Type(Integer32):
    """Custom type cwspCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spvc", 2),
          ("svc", 1))
    )


_CwspCallType_Type.__name__ = "Integer32"
_CwspCallType_Object = MibTableColumn
cwspCallType = _CwspCallType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 13),
    _CwspCallType_Type()
)
cwspCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallType.setStatus("current")
_CwspCallStartTime_Type = TimeStamp
_CwspCallStartTime_Object = MibTableColumn
cwspCallStartTime = _CwspCallStartTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 14),
    _CwspCallStartTime_Type()
)
cwspCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallStartTime.setStatus("current")


class _CwspCallBearerClass_Type(Integer32):
    """Custom type cwspCallBearerClass based on Integer32"""
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
        *(("bcobA", 1),
          ("bcobC", 2),
          ("bcobX", 3),
          ("vp", 4))
    )


_CwspCallBearerClass_Type.__name__ = "Integer32"
_CwspCallBearerClass_Object = MibTableColumn
cwspCallBearerClass = _CwspCallBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 15),
    _CwspCallBearerClass_Type()
)
cwspCallBearerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBearerClass.setStatus("current")


class _CwspCallServiceCategory_Type(Integer32):
    """Custom type cwspCallServiceCategory based on Integer32"""
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
        *(("abr", 4),
          ("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 5))
    )


_CwspCallServiceCategory_Type.__name__ = "Integer32"
_CwspCallServiceCategory_Object = MibTableColumn
cwspCallServiceCategory = _CwspCallServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 16),
    _CwspCallServiceCategory_Type()
)
cwspCallServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallServiceCategory.setStatus("current")


class _CwspCallCastType_Type(Integer32):
    """Custom type cwspCallCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mp2p", 3),
          ("p2mp", 2),
          ("p2p", 1))
    )


_CwspCallCastType_Type.__name__ = "Integer32"
_CwspCallCastType_Object = MibTableColumn
cwspCallCastType = _CwspCallCastType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 17),
    _CwspCallCastType_Type()
)
cwspCallCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallCastType.setStatus("current")


class _CwspCallClipSusceptibility_Type(Integer32):
    """Custom type cwspCallClipSusceptibility based on Integer32"""
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


_CwspCallClipSusceptibility_Type.__name__ = "Integer32"
_CwspCallClipSusceptibility_Object = MibTableColumn
cwspCallClipSusceptibility = _CwspCallClipSusceptibility_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 18),
    _CwspCallClipSusceptibility_Type()
)
cwspCallClipSusceptibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallClipSusceptibility.setStatus("current")


class _CwspCallFwdConformance_Type(Integer32):
    """Custom type cwspCallFwdConformance based on Integer32"""
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
        *(("abr", 7),
          ("cbr1", 1),
          ("cbr2", 2),
          ("cbr3", 3),
          ("ubr1", 8),
          ("ubr2", 9),
          ("vbr1", 4),
          ("vbr2", 5),
          ("vbr3", 6))
    )


_CwspCallFwdConformance_Type.__name__ = "Integer32"
_CwspCallFwdConformance_Object = MibTableColumn
cwspCallFwdConformance = _CwspCallFwdConformance_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 19),
    _CwspCallFwdConformance_Type()
)
cwspCallFwdConformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallFwdConformance.setStatus("current")


class _CwspCallFwdPcr_Type(Integer32):
    """Custom type cwspCallFwdPcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallFwdPcr_Type.__name__ = "Integer32"
_CwspCallFwdPcr_Object = MibTableColumn
cwspCallFwdPcr = _CwspCallFwdPcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 20),
    _CwspCallFwdPcr_Type()
)
cwspCallFwdPcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallFwdPcr.setStatus("current")


class _CwspCallFwdScr_Type(Integer32):
    """Custom type cwspCallFwdScr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallFwdScr_Type.__name__ = "Integer32"
_CwspCallFwdScr_Object = MibTableColumn
cwspCallFwdScr = _CwspCallFwdScr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 21),
    _CwspCallFwdScr_Type()
)
cwspCallFwdScr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallFwdScr.setStatus("current")


class _CwspCallFwdMbs_Type(Integer32):
    """Custom type cwspCallFwdMbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallFwdMbs_Type.__name__ = "Integer32"
_CwspCallFwdMbs_Object = MibTableColumn
cwspCallFwdMbs = _CwspCallFwdMbs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 22),
    _CwspCallFwdMbs_Type()
)
cwspCallFwdMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallFwdMbs.setStatus("current")


class _CwspCallFwdCdvt_Type(Integer32):
    """Custom type cwspCallFwdCdvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallFwdCdvt_Type.__name__ = "Integer32"
_CwspCallFwdCdvt_Object = MibTableColumn
cwspCallFwdCdvt = _CwspCallFwdCdvt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 23),
    _CwspCallFwdCdvt_Type()
)
cwspCallFwdCdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallFwdCdvt.setStatus("current")


class _CwspCallFwdFrameDiscard_Type(Integer32):
    """Custom type cwspCallFwdFrameDiscard based on Integer32"""
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


_CwspCallFwdFrameDiscard_Type.__name__ = "Integer32"
_CwspCallFwdFrameDiscard_Object = MibTableColumn
cwspCallFwdFrameDiscard = _CwspCallFwdFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 24),
    _CwspCallFwdFrameDiscard_Type()
)
cwspCallFwdFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallFwdFrameDiscard.setStatus("current")


class _CwspCallBwdConformance_Type(Integer32):
    """Custom type cwspCallBwdConformance based on Integer32"""
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
        *(("abr", 7),
          ("cbr1", 1),
          ("cbr2", 2),
          ("cbr3", 3),
          ("ubr1", 8),
          ("ubr2", 9),
          ("vbr1", 4),
          ("vbr2", 5),
          ("vbr3", 6))
    )


_CwspCallBwdConformance_Type.__name__ = "Integer32"
_CwspCallBwdConformance_Object = MibTableColumn
cwspCallBwdConformance = _CwspCallBwdConformance_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 25),
    _CwspCallBwdConformance_Type()
)
cwspCallBwdConformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBwdConformance.setStatus("current")


class _CwspCallBwdPcr_Type(Integer32):
    """Custom type cwspCallBwdPcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallBwdPcr_Type.__name__ = "Integer32"
_CwspCallBwdPcr_Object = MibTableColumn
cwspCallBwdPcr = _CwspCallBwdPcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 26),
    _CwspCallBwdPcr_Type()
)
cwspCallBwdPcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBwdPcr.setStatus("current")


class _CwspCallBwdScr_Type(Integer32):
    """Custom type cwspCallBwdScr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallBwdScr_Type.__name__ = "Integer32"
_CwspCallBwdScr_Object = MibTableColumn
cwspCallBwdScr = _CwspCallBwdScr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 27),
    _CwspCallBwdScr_Type()
)
cwspCallBwdScr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBwdScr.setStatus("current")


class _CwspCallBwdMbs_Type(Integer32):
    """Custom type cwspCallBwdMbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallBwdMbs_Type.__name__ = "Integer32"
_CwspCallBwdMbs_Object = MibTableColumn
cwspCallBwdMbs = _CwspCallBwdMbs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 28),
    _CwspCallBwdMbs_Type()
)
cwspCallBwdMbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBwdMbs.setStatus("current")


class _CwspCallBwdCdvt_Type(Integer32):
    """Custom type cwspCallBwdCdvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallBwdCdvt_Type.__name__ = "Integer32"
_CwspCallBwdCdvt_Object = MibTableColumn
cwspCallBwdCdvt = _CwspCallBwdCdvt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 29),
    _CwspCallBwdCdvt_Type()
)
cwspCallBwdCdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBwdCdvt.setStatus("current")


class _CwspCallBwdFrameDiscard_Type(Integer32):
    """Custom type cwspCallBwdFrameDiscard based on Integer32"""
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


_CwspCallBwdFrameDiscard_Type.__name__ = "Integer32"
_CwspCallBwdFrameDiscard_Object = MibTableColumn
cwspCallBwdFrameDiscard = _CwspCallBwdFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 30),
    _CwspCallBwdFrameDiscard_Type()
)
cwspCallBwdFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallBwdFrameDiscard.setStatus("current")


class _CwspCallMaxCtd_Type(Integer32):
    """Custom type cwspCallMaxCtd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallMaxCtd_Type.__name__ = "Integer32"
_CwspCallMaxCtd_Object = MibTableColumn
cwspCallMaxCtd = _CwspCallMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 31),
    _CwspCallMaxCtd_Type()
)
cwspCallMaxCtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallMaxCtd.setStatus("current")


class _CwspCallMaxFwdCdv_Type(Integer32):
    """Custom type cwspCallMaxFwdCdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallMaxFwdCdv_Type.__name__ = "Integer32"
_CwspCallMaxFwdCdv_Object = MibTableColumn
cwspCallMaxFwdCdv = _CwspCallMaxFwdCdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 32),
    _CwspCallMaxFwdCdv_Type()
)
cwspCallMaxFwdCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallMaxFwdCdv.setStatus("current")


class _CwspCallMaxFwdClr_Type(Integer32):
    """Custom type cwspCallMaxFwdClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallMaxFwdClr_Type.__name__ = "Integer32"
_CwspCallMaxFwdClr_Object = MibTableColumn
cwspCallMaxFwdClr = _CwspCallMaxFwdClr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 33),
    _CwspCallMaxFwdClr_Type()
)
cwspCallMaxFwdClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallMaxFwdClr.setStatus("current")


class _CwspCallMaxBwdCdv_Type(Integer32):
    """Custom type cwspCallMaxBwdCdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallMaxBwdCdv_Type.__name__ = "Integer32"
_CwspCallMaxBwdCdv_Object = MibTableColumn
cwspCallMaxBwdCdv = _CwspCallMaxBwdCdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 34),
    _CwspCallMaxBwdCdv_Type()
)
cwspCallMaxBwdCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallMaxBwdCdv.setStatus("current")


class _CwspCallMaxBwdClr_Type(Integer32):
    """Custom type cwspCallMaxBwdClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspCallMaxBwdClr_Type.__name__ = "Integer32"
_CwspCallMaxBwdClr_Object = MibTableColumn
cwspCallMaxBwdClr = _CwspCallMaxBwdClr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 8, 1, 1, 35),
    _CwspCallMaxBwdClr_Type()
)
cwspCallMaxBwdClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspCallMaxBwdClr.setStatus("current")
_CwspAbrCall_ObjectIdentity = ObjectIdentity
cwspAbrCall = _CwspAbrCall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9)
)
_CwspAbrCallTable_Object = MibTable
cwspAbrCallTable = _CwspAbrCallTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cwspAbrCallTable.setStatus("current")
_CwspAbrCallEntry_Object = MibTableRow
cwspAbrCallEntry = _CwspAbrCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1)
)
cwspAbrCallEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-SVC-MIB", "cwspAbrCallVpi"),
    (0, "CISCO-WAN-SVC-MIB", "cwspAbrCallVci"),
)
if mibBuilder.loadTexts:
    cwspAbrCallEntry.setStatus("current")


class _CwspAbrCallVpi_Type(Integer32):
    """Custom type cwspAbrCallVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspAbrCallVpi_Type.__name__ = "Integer32"
_CwspAbrCallVpi_Object = MibTableColumn
cwspAbrCallVpi = _CwspAbrCallVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 1),
    _CwspAbrCallVpi_Type()
)
cwspAbrCallVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspAbrCallVpi.setStatus("current")


class _CwspAbrCallVci_Type(Integer32):
    """Custom type cwspAbrCallVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspAbrCallVci_Type.__name__ = "Integer32"
_CwspAbrCallVci_Object = MibTableColumn
cwspAbrCallVci = _CwspAbrCallVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 2),
    _CwspAbrCallVci_Type()
)
cwspAbrCallVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspAbrCallVci.setStatus("current")


class _CwspAbrCallCallRef_Type(Integer32):
    """Custom type cwspAbrCallCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallCallRef_Type.__name__ = "Integer32"
_CwspAbrCallCallRef_Object = MibTableColumn
cwspAbrCallCallRef = _CwspAbrCallCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 3),
    _CwspAbrCallCallRef_Type()
)
cwspAbrCallCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallCallRef.setStatus("current")
_CwspAbrCallClgAddress_Type = AtmAddress
_CwspAbrCallClgAddress_Object = MibTableColumn
cwspAbrCallClgAddress = _CwspAbrCallClgAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 4),
    _CwspAbrCallClgAddress_Type()
)
cwspAbrCallClgAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallClgAddress.setStatus("current")
_CwspAbrCallCldAddress_Type = AtmAddress
_CwspAbrCallCldAddress_Object = MibTableColumn
cwspAbrCallCldAddress = _CwspAbrCallCldAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 5),
    _CwspAbrCallCldAddress_Type()
)
cwspAbrCallCldAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallCldAddress.setStatus("current")
_CwspAbrCallClgSubAddr_Type = AtmAddress
_CwspAbrCallClgSubAddr_Object = MibTableColumn
cwspAbrCallClgSubAddr = _CwspAbrCallClgSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 6),
    _CwspAbrCallClgSubAddr_Type()
)
cwspAbrCallClgSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallClgSubAddr.setStatus("current")
_CwspAbrCallCldSubAddr_Type = AtmAddress
_CwspAbrCallCldSubAddr_Object = MibTableColumn
cwspAbrCallCldSubAddr = _CwspAbrCallCldSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 7),
    _CwspAbrCallCldSubAddr_Type()
)
cwspAbrCallCldSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallCldSubAddr.setStatus("current")


class _CwspAbrCallOtherIntfIndex_Type(Integer32):
    """Custom type cwspAbrCallOtherIntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallOtherIntfIndex_Type.__name__ = "Integer32"
_CwspAbrCallOtherIntfIndex_Object = MibTableColumn
cwspAbrCallOtherIntfIndex = _CwspAbrCallOtherIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 8),
    _CwspAbrCallOtherIntfIndex_Type()
)
cwspAbrCallOtherIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallOtherIntfIndex.setStatus("current")


class _CwspAbrCallOtherIntfVpi_Type(Integer32):
    """Custom type cwspAbrCallOtherIntfVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspAbrCallOtherIntfVpi_Type.__name__ = "Integer32"
_CwspAbrCallOtherIntfVpi_Object = MibTableColumn
cwspAbrCallOtherIntfVpi = _CwspAbrCallOtherIntfVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 9),
    _CwspAbrCallOtherIntfVpi_Type()
)
cwspAbrCallOtherIntfVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallOtherIntfVpi.setStatus("current")


class _CwspAbrCallOtherIntfVci_Type(Integer32):
    """Custom type cwspAbrCallOtherIntfVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspAbrCallOtherIntfVci_Type.__name__ = "Integer32"
_CwspAbrCallOtherIntfVci_Object = MibTableColumn
cwspAbrCallOtherIntfVci = _CwspAbrCallOtherIntfVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 10),
    _CwspAbrCallOtherIntfVci_Type()
)
cwspAbrCallOtherIntfVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallOtherIntfVci.setStatus("current")


class _CwspAbrCallOtherIntfCallRef_Type(Integer32):
    """Custom type cwspAbrCallOtherIntfCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallOtherIntfCallRef_Type.__name__ = "Integer32"
_CwspAbrCallOtherIntfCallRef_Object = MibTableColumn
cwspAbrCallOtherIntfCallRef = _CwspAbrCallOtherIntfCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 11),
    _CwspAbrCallOtherIntfCallRef_Type()
)
cwspAbrCallOtherIntfCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallOtherIntfCallRef.setStatus("current")


class _CwspAbrCallType_Type(Integer32):
    """Custom type cwspAbrCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spvc", 2),
          ("svc", 1))
    )


_CwspAbrCallType_Type.__name__ = "Integer32"
_CwspAbrCallType_Object = MibTableColumn
cwspAbrCallType = _CwspAbrCallType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 12),
    _CwspAbrCallType_Type()
)
cwspAbrCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallType.setStatus("current")
_CwspAbrCallStartTime_Type = TimeStamp
_CwspAbrCallStartTime_Object = MibTableColumn
cwspAbrCallStartTime = _CwspAbrCallStartTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 13),
    _CwspAbrCallStartTime_Type()
)
cwspAbrCallStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallStartTime.setStatus("current")


class _CwspAbrCallBearerClass_Type(Integer32):
    """Custom type cwspAbrCallBearerClass based on Integer32"""
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
        *(("bcobA", 1),
          ("bcobC", 2),
          ("bcobX", 3),
          ("vp", 4))
    )


_CwspAbrCallBearerClass_Type.__name__ = "Integer32"
_CwspAbrCallBearerClass_Object = MibTableColumn
cwspAbrCallBearerClass = _CwspAbrCallBearerClass_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 14),
    _CwspAbrCallBearerClass_Type()
)
cwspAbrCallBearerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBearerClass.setStatus("current")


class _CwspAbrCallServiceCategory_Type(Integer32):
    """Custom type cwspAbrCallServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("abr", 4)
    )


_CwspAbrCallServiceCategory_Type.__name__ = "Integer32"
_CwspAbrCallServiceCategory_Object = MibTableColumn
cwspAbrCallServiceCategory = _CwspAbrCallServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 15),
    _CwspAbrCallServiceCategory_Type()
)
cwspAbrCallServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallServiceCategory.setStatus("current")


class _CwspAbrCallCastType_Type(Integer32):
    """Custom type cwspAbrCallCastType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("p2p", 1)
    )


_CwspAbrCallCastType_Type.__name__ = "Integer32"
_CwspAbrCallCastType_Object = MibTableColumn
cwspAbrCallCastType = _CwspAbrCallCastType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 16),
    _CwspAbrCallCastType_Type()
)
cwspAbrCallCastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallCastType.setStatus("current")


class _CwspAbrCallClipSusceptibility_Type(Integer32):
    """Custom type cwspAbrCallClipSusceptibility based on Integer32"""
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


_CwspAbrCallClipSusceptibility_Type.__name__ = "Integer32"
_CwspAbrCallClipSusceptibility_Object = MibTableColumn
cwspAbrCallClipSusceptibility = _CwspAbrCallClipSusceptibility_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 17),
    _CwspAbrCallClipSusceptibility_Type()
)
cwspAbrCallClipSusceptibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallClipSusceptibility.setStatus("current")


class _CwspAbrCallFwdConformance_Type(Integer32):
    """Custom type cwspAbrCallFwdConformance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            7
        )
    )
    namedValues = NamedValues(
        ("abr", 7)
    )


_CwspAbrCallFwdConformance_Type.__name__ = "Integer32"
_CwspAbrCallFwdConformance_Object = MibTableColumn
cwspAbrCallFwdConformance = _CwspAbrCallFwdConformance_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 18),
    _CwspAbrCallFwdConformance_Type()
)
cwspAbrCallFwdConformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdConformance.setStatus("current")


class _CwspAbrCallFwdPcr_Type(Integer32):
    """Custom type cwspAbrCallFwdPcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallFwdPcr_Type.__name__ = "Integer32"
_CwspAbrCallFwdPcr_Object = MibTableColumn
cwspAbrCallFwdPcr = _CwspAbrCallFwdPcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 19),
    _CwspAbrCallFwdPcr_Type()
)
cwspAbrCallFwdPcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdPcr.setStatus("current")


class _CwspAbrCallFwdMcr_Type(Integer32):
    """Custom type cwspAbrCallFwdMcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallFwdMcr_Type.__name__ = "Integer32"
_CwspAbrCallFwdMcr_Object = MibTableColumn
cwspAbrCallFwdMcr = _CwspAbrCallFwdMcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 20),
    _CwspAbrCallFwdMcr_Type()
)
cwspAbrCallFwdMcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdMcr.setStatus("current")


class _CwspAbrCallFwdIcr_Type(Integer32):
    """Custom type cwspAbrCallFwdIcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallFwdIcr_Type.__name__ = "Integer32"
_CwspAbrCallFwdIcr_Object = MibTableColumn
cwspAbrCallFwdIcr = _CwspAbrCallFwdIcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 21),
    _CwspAbrCallFwdIcr_Type()
)
cwspAbrCallFwdIcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdIcr.setStatus("current")


class _CwspAbrCallFwdRif_Type(Integer32):
    """Custom type cwspAbrCallFwdRif based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("rifOne", 16),
          ("rifOneOver1024", 6),
          ("rifOneOver128", 9),
          ("rifOneOver16", 12),
          ("rifOneOver16384", 2),
          ("rifOneOver2", 15),
          ("rifOneOver2048", 5),
          ("rifOneOver256", 8),
          ("rifOneOver32", 11),
          ("rifOneOver32768", 1),
          ("rifOneOver4", 14),
          ("rifOneOver4096", 4),
          ("rifOneOver512", 7),
          ("rifOneOver64", 10),
          ("rifOneOver8", 13),
          ("rifOneOver8192", 3))
    )


_CwspAbrCallFwdRif_Type.__name__ = "Integer32"
_CwspAbrCallFwdRif_Object = MibTableColumn
cwspAbrCallFwdRif = _CwspAbrCallFwdRif_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 22),
    _CwspAbrCallFwdRif_Type()
)
cwspAbrCallFwdRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdRif.setStatus("current")


class _CwspAbrCallFwdRdf_Type(Integer32):
    """Custom type cwspAbrCallFwdRdf based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("rdfOne", 16),
          ("rdfOneOver1024", 6),
          ("rdfOneOver128", 9),
          ("rdfOneOver16", 12),
          ("rdfOneOver16384", 2),
          ("rdfOneOver2", 15),
          ("rdfOneOver2048", 5),
          ("rdfOneOver256", 8),
          ("rdfOneOver32", 11),
          ("rdfOneOver32768", 1),
          ("rdfOneOver4", 14),
          ("rdfOneOver4096", 4),
          ("rdfOneOver512", 7),
          ("rdfOneOver64", 10),
          ("rdfOneOver8", 13),
          ("rdfOneOver8192", 3))
    )


_CwspAbrCallFwdRdf_Type.__name__ = "Integer32"
_CwspAbrCallFwdRdf_Object = MibTableColumn
cwspAbrCallFwdRdf = _CwspAbrCallFwdRdf_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 23),
    _CwspAbrCallFwdRdf_Type()
)
cwspAbrCallFwdRdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdRdf.setStatus("current")


class _CwspAbrCallFwdTbe_Type(Integer32):
    """Custom type cwspAbrCallFwdTbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallFwdTbe_Type.__name__ = "Integer32"
_CwspAbrCallFwdTbe_Object = MibTableColumn
cwspAbrCallFwdTbe = _CwspAbrCallFwdTbe_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 24),
    _CwspAbrCallFwdTbe_Type()
)
cwspAbrCallFwdTbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdTbe.setStatus("current")


class _CwspAbrCallFwdNrm_Type(Integer32):
    """Custom type cwspAbrCallFwdNrm based on Integer32"""
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
        *(("nrm128", 7),
          ("nrm16", 4),
          ("nrm2", 1),
          ("nrm256", 8),
          ("nrm32", 5),
          ("nrm4", 2),
          ("nrm64", 6),
          ("nrm8", 3))
    )


_CwspAbrCallFwdNrm_Type.__name__ = "Integer32"
_CwspAbrCallFwdNrm_Object = MibTableColumn
cwspAbrCallFwdNrm = _CwspAbrCallFwdNrm_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 25),
    _CwspAbrCallFwdNrm_Type()
)
cwspAbrCallFwdNrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdNrm.setStatus("current")


class _CwspAbrCallFwdTrm_Type(Integer32):
    """Custom type cwspAbrCallFwdTrm based on Integer32"""
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
        *(("trm0point78125", 1),
          ("trm100", 8),
          ("trm12point5", 5),
          ("trm1point5625", 2),
          ("trm25", 6),
          ("trm3point125", 3),
          ("trm50", 7),
          ("trm6point25", 4))
    )


_CwspAbrCallFwdTrm_Type.__name__ = "Integer32"
_CwspAbrCallFwdTrm_Object = MibTableColumn
cwspAbrCallFwdTrm = _CwspAbrCallFwdTrm_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 26),
    _CwspAbrCallFwdTrm_Type()
)
cwspAbrCallFwdTrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdTrm.setStatus("current")


class _CwspAbrCallFwdAdtf_Type(Integer32):
    """Custom type cwspAbrCallFwdAdtf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CwspAbrCallFwdAdtf_Type.__name__ = "Integer32"
_CwspAbrCallFwdAdtf_Object = MibTableColumn
cwspAbrCallFwdAdtf = _CwspAbrCallFwdAdtf_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 27),
    _CwspAbrCallFwdAdtf_Type()
)
cwspAbrCallFwdAdtf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdAdtf.setStatus("current")


class _CwspAbrCallFwdCdf_Type(Integer32):
    """Custom type cwspAbrCallFwdCdf based on Integer32"""
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
        *(("cdf0", 1),
          ("cdfOne", 8),
          ("cdfOneOver16", 4),
          ("cdfOneOver2", 7),
          ("cdfOneOver32", 3),
          ("cdfOneOver4", 6),
          ("cdfOneOver64", 2),
          ("cdfOneOver8", 5))
    )


_CwspAbrCallFwdCdf_Type.__name__ = "Integer32"
_CwspAbrCallFwdCdf_Object = MibTableColumn
cwspAbrCallFwdCdf = _CwspAbrCallFwdCdf_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 28),
    _CwspAbrCallFwdCdf_Type()
)
cwspAbrCallFwdCdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdCdf.setStatus("current")


class _CwspAbrCallFwdFrameDiscard_Type(Integer32):
    """Custom type cwspAbrCallFwdFrameDiscard based on Integer32"""
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


_CwspAbrCallFwdFrameDiscard_Type.__name__ = "Integer32"
_CwspAbrCallFwdFrameDiscard_Object = MibTableColumn
cwspAbrCallFwdFrameDiscard = _CwspAbrCallFwdFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 29),
    _CwspAbrCallFwdFrameDiscard_Type()
)
cwspAbrCallFwdFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFwdFrameDiscard.setStatus("current")


class _CwspAbrCallBwdPcr_Type(Integer32):
    """Custom type cwspAbrCallBwdPcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallBwdPcr_Type.__name__ = "Integer32"
_CwspAbrCallBwdPcr_Object = MibTableColumn
cwspAbrCallBwdPcr = _CwspAbrCallBwdPcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 30),
    _CwspAbrCallBwdPcr_Type()
)
cwspAbrCallBwdPcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdPcr.setStatus("current")


class _CwspAbrCallBwdMcr_Type(Integer32):
    """Custom type cwspAbrCallBwdMcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallBwdMcr_Type.__name__ = "Integer32"
_CwspAbrCallBwdMcr_Object = MibTableColumn
cwspAbrCallBwdMcr = _CwspAbrCallBwdMcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 31),
    _CwspAbrCallBwdMcr_Type()
)
cwspAbrCallBwdMcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdMcr.setStatus("current")


class _CwspAbrCallBwdIcr_Type(Integer32):
    """Custom type cwspAbrCallBwdIcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallBwdIcr_Type.__name__ = "Integer32"
_CwspAbrCallBwdIcr_Object = MibTableColumn
cwspAbrCallBwdIcr = _CwspAbrCallBwdIcr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 32),
    _CwspAbrCallBwdIcr_Type()
)
cwspAbrCallBwdIcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdIcr.setStatus("current")


class _CwspAbrCallBwdRif_Type(Integer32):
    """Custom type cwspAbrCallBwdRif based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("rifOne", 16),
          ("rifOneOver1024", 6),
          ("rifOneOver128", 9),
          ("rifOneOver16", 12),
          ("rifOneOver16384", 2),
          ("rifOneOver2", 15),
          ("rifOneOver2048", 5),
          ("rifOneOver256", 8),
          ("rifOneOver32", 11),
          ("rifOneOver32768", 1),
          ("rifOneOver4", 14),
          ("rifOneOver4096", 4),
          ("rifOneOver512", 7),
          ("rifOneOver64", 10),
          ("rifOneOver8", 13),
          ("rifOneOver8192", 3))
    )


_CwspAbrCallBwdRif_Type.__name__ = "Integer32"
_CwspAbrCallBwdRif_Object = MibTableColumn
cwspAbrCallBwdRif = _CwspAbrCallBwdRif_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 33),
    _CwspAbrCallBwdRif_Type()
)
cwspAbrCallBwdRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdRif.setStatus("current")


class _CwspAbrCallBwdRdf_Type(Integer32):
    """Custom type cwspAbrCallBwdRdf based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("rdfOne", 16),
          ("rdfOneOver1024", 6),
          ("rdfOneOver128", 9),
          ("rdfOneOver16", 12),
          ("rdfOneOver16384", 2),
          ("rdfOneOver2", 15),
          ("rdfOneOver2048", 5),
          ("rdfOneOver256", 8),
          ("rdfOneOver32", 11),
          ("rdfOneOver32768", 1),
          ("rdfOneOver4", 14),
          ("rdfOneOver4096", 4),
          ("rdfOneOver512", 7),
          ("rdfOneOver64", 10),
          ("rdfOneOver8", 13),
          ("rdfOneOver8192", 3))
    )


_CwspAbrCallBwdRdf_Type.__name__ = "Integer32"
_CwspAbrCallBwdRdf_Object = MibTableColumn
cwspAbrCallBwdRdf = _CwspAbrCallBwdRdf_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 34),
    _CwspAbrCallBwdRdf_Type()
)
cwspAbrCallBwdRdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdRdf.setStatus("current")


class _CwspAbrCallBwdTbe_Type(Integer32):
    """Custom type cwspAbrCallBwdTbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallBwdTbe_Type.__name__ = "Integer32"
_CwspAbrCallBwdTbe_Object = MibTableColumn
cwspAbrCallBwdTbe = _CwspAbrCallBwdTbe_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 35),
    _CwspAbrCallBwdTbe_Type()
)
cwspAbrCallBwdTbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdTbe.setStatus("current")


class _CwspAbrCallBwdNrm_Type(Integer32):
    """Custom type cwspAbrCallBwdNrm based on Integer32"""
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
        *(("nrm128", 7),
          ("nrm16", 4),
          ("nrm2", 1),
          ("nrm256", 8),
          ("nrm32", 5),
          ("nrm4", 2),
          ("nrm64", 6),
          ("nrm8", 3))
    )


_CwspAbrCallBwdNrm_Type.__name__ = "Integer32"
_CwspAbrCallBwdNrm_Object = MibTableColumn
cwspAbrCallBwdNrm = _CwspAbrCallBwdNrm_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 36),
    _CwspAbrCallBwdNrm_Type()
)
cwspAbrCallBwdNrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdNrm.setStatus("current")


class _CwspAbrCallBwdTrm_Type(Integer32):
    """Custom type cwspAbrCallBwdTrm based on Integer32"""
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
        *(("trm0point78125", 1),
          ("trm100", 8),
          ("trm12point5", 5),
          ("trm1point5625", 2),
          ("trm25", 6),
          ("trm3point125", 3),
          ("trm50", 7),
          ("trm6point25", 4))
    )


_CwspAbrCallBwdTrm_Type.__name__ = "Integer32"
_CwspAbrCallBwdTrm_Object = MibTableColumn
cwspAbrCallBwdTrm = _CwspAbrCallBwdTrm_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 37),
    _CwspAbrCallBwdTrm_Type()
)
cwspAbrCallBwdTrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdTrm.setStatus("current")


class _CwspAbrCallBwdAdtf_Type(Integer32):
    """Custom type cwspAbrCallBwdAdtf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_CwspAbrCallBwdAdtf_Type.__name__ = "Integer32"
_CwspAbrCallBwdAdtf_Object = MibTableColumn
cwspAbrCallBwdAdtf = _CwspAbrCallBwdAdtf_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 38),
    _CwspAbrCallBwdAdtf_Type()
)
cwspAbrCallBwdAdtf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdAdtf.setStatus("current")


class _CwspAbrCallBwdCdf_Type(Integer32):
    """Custom type cwspAbrCallBwdCdf based on Integer32"""
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
        *(("cdf0", 1),
          ("cdfOne", 8),
          ("cdfOneOver16", 4),
          ("cdfOneOver2", 7),
          ("cdfOneOver32", 3),
          ("cdfOneOver4", 6),
          ("cdfOneOver64", 2),
          ("cdfOneOver8", 5))
    )


_CwspAbrCallBwdCdf_Type.__name__ = "Integer32"
_CwspAbrCallBwdCdf_Object = MibTableColumn
cwspAbrCallBwdCdf = _CwspAbrCallBwdCdf_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 39),
    _CwspAbrCallBwdCdf_Type()
)
cwspAbrCallBwdCdf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdCdf.setStatus("current")


class _CwspAbrCallBwdFrameDiscard_Type(Integer32):
    """Custom type cwspAbrCallBwdFrameDiscard based on Integer32"""
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


_CwspAbrCallBwdFrameDiscard_Type.__name__ = "Integer32"
_CwspAbrCallBwdFrameDiscard_Object = MibTableColumn
cwspAbrCallBwdFrameDiscard = _CwspAbrCallBwdFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 40),
    _CwspAbrCallBwdFrameDiscard_Type()
)
cwspAbrCallBwdFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallBwdFrameDiscard.setStatus("current")


class _CwspAbrCallFrtt_Type(Integer32):
    """Custom type cwspAbrCallFrtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallFrtt_Type.__name__ = "Integer32"
_CwspAbrCallFrtt_Object = MibTableColumn
cwspAbrCallFrtt = _CwspAbrCallFrtt_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 41),
    _CwspAbrCallFrtt_Type()
)
cwspAbrCallFrtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallFrtt.setStatus("current")


class _CwspAbrCallMaxCtd_Type(Integer32):
    """Custom type cwspAbrCallMaxCtd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallMaxCtd_Type.__name__ = "Integer32"
_CwspAbrCallMaxCtd_Object = MibTableColumn
cwspAbrCallMaxCtd = _CwspAbrCallMaxCtd_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 42),
    _CwspAbrCallMaxCtd_Type()
)
cwspAbrCallMaxCtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallMaxCtd.setStatus("current")


class _CwspAbrCallMaxFwdCdv_Type(Integer32):
    """Custom type cwspAbrCallMaxFwdCdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallMaxFwdCdv_Type.__name__ = "Integer32"
_CwspAbrCallMaxFwdCdv_Object = MibTableColumn
cwspAbrCallMaxFwdCdv = _CwspAbrCallMaxFwdCdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 43),
    _CwspAbrCallMaxFwdCdv_Type()
)
cwspAbrCallMaxFwdCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallMaxFwdCdv.setStatus("current")


class _CwspAbrCallMaxFwdClr_Type(Integer32):
    """Custom type cwspAbrCallMaxFwdClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallMaxFwdClr_Type.__name__ = "Integer32"
_CwspAbrCallMaxFwdClr_Object = MibTableColumn
cwspAbrCallMaxFwdClr = _CwspAbrCallMaxFwdClr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 44),
    _CwspAbrCallMaxFwdClr_Type()
)
cwspAbrCallMaxFwdClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallMaxFwdClr.setStatus("current")


class _CwspAbrCallMaxBwdCdv_Type(Integer32):
    """Custom type cwspAbrCallMaxBwdCdv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallMaxBwdCdv_Type.__name__ = "Integer32"
_CwspAbrCallMaxBwdCdv_Object = MibTableColumn
cwspAbrCallMaxBwdCdv = _CwspAbrCallMaxBwdCdv_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 45),
    _CwspAbrCallMaxBwdCdv_Type()
)
cwspAbrCallMaxBwdCdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallMaxBwdCdv.setStatus("current")


class _CwspAbrCallMaxBwdClr_Type(Integer32):
    """Custom type cwspAbrCallMaxBwdClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspAbrCallMaxBwdClr_Type.__name__ = "Integer32"
_CwspAbrCallMaxBwdClr_Object = MibTableColumn
cwspAbrCallMaxBwdClr = _CwspAbrCallMaxBwdClr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 9, 1, 1, 46),
    _CwspAbrCallMaxBwdClr_Type()
)
cwspAbrCallMaxBwdClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspAbrCallMaxBwdClr.setStatus("current")
_CwspPrefix_ObjectIdentity = ObjectIdentity
cwspPrefix = _CwspPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 10)
)
_CwspPrefixTable_Object = MibTable
cwspPrefixTable = _CwspPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    cwspPrefixTable.setStatus("current")
_CwspPrefixEntry_Object = MibTableRow
cwspPrefixEntry = _CwspPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 10, 1, 1)
)
cwspPrefixEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-SVC-MIB", "cwspNetPrefix"),
)
if mibBuilder.loadTexts:
    cwspPrefixEntry.setStatus("current")
_CwspNetPrefix_Type = NetPrefix
_CwspNetPrefix_Object = MibTableColumn
cwspNetPrefix = _CwspNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 10, 1, 1, 1),
    _CwspNetPrefix_Type()
)
cwspNetPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspNetPrefix.setStatus("current")
_CwspPrefixRowStatus_Type = RowStatus
_CwspPrefixRowStatus_Object = MibTableColumn
cwspPrefixRowStatus = _CwspPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 10, 1, 1, 2),
    _CwspPrefixRowStatus_Type()
)
cwspPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspPrefixRowStatus.setStatus("current")
_CwspAddress_ObjectIdentity = ObjectIdentity
cwspAddress = _CwspAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11)
)
_CwspAddressTable_Object = MibTable
cwspAddressTable = _CwspAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1)
)
if mibBuilder.loadTexts:
    cwspAddressTable.setStatus("current")
_CwspAddressEntry_Object = MibTableRow
cwspAddressEntry = _CwspAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1)
)
cwspAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-SVC-MIB", "cwspAtmAddress"),
    (0, "CISCO-WAN-SVC-MIB", "cwspAddrLen"),
)
if mibBuilder.loadTexts:
    cwspAddressEntry.setStatus("current")
_CwspAtmAddress_Type = AtmAddress
_CwspAtmAddress_Object = MibTableColumn
cwspAtmAddress = _CwspAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 1),
    _CwspAtmAddress_Type()
)
cwspAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspAtmAddress.setStatus("current")


class _CwspAddrLen_Type(Integer32):
    """Custom type cwspAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 160),
    )


_CwspAddrLen_Type.__name__ = "Integer32"
_CwspAddrLen_Object = MibTableColumn
cwspAddrLen = _CwspAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 2),
    _CwspAddrLen_Type()
)
cwspAddrLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspAddrLen.setStatus("current")


class _CwspAddrType_Type(Integer32):
    """Custom type cwspAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exterior", 2),
          ("internal", 1))
    )


_CwspAddrType_Type.__name__ = "Integer32"
_CwspAddrType_Object = MibTableColumn
cwspAddrType = _CwspAddrType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 3),
    _CwspAddrType_Type()
)
cwspAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddrType.setStatus("current")


class _CwspAddrProto_Type(Integer32):
    """Custom type cwspAddrProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("static", 2))
    )


_CwspAddrProto_Type.__name__ = "Integer32"
_CwspAddrProto_Object = MibTableColumn
cwspAddrProto = _CwspAddrProto_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 4),
    _CwspAddrProto_Type()
)
cwspAddrProto.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddrProto.setStatus("current")


class _CwspAddrPlan_Type(Integer32):
    """Custom type cwspAddrPlan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("nsap", 2))
    )


_CwspAddrPlan_Type.__name__ = "Integer32"
_CwspAddrPlan_Object = MibTableColumn
cwspAddrPlan = _CwspAddrPlan_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 5),
    _CwspAddrPlan_Type()
)
cwspAddrPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddrPlan.setStatus("current")


class _CwspAddrScope_Type(Integer32):
    """Custom type cwspAddrScope based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_CwspAddrScope_Type.__name__ = "Integer32"
_CwspAddrScope_Object = MibTableColumn
cwspAddrScope = _CwspAddrScope_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 6),
    _CwspAddrScope_Type()
)
cwspAddrScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddrScope.setStatus("current")


class _CwspAddrRedistribute_Type(TruthValue):
    """Custom type cwspAddrRedistribute based on TruthValue"""


_CwspAddrRedistribute_Object = MibTableColumn
cwspAddrRedistribute = _CwspAddrRedistribute_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 7),
    _CwspAddrRedistribute_Type()
)
cwspAddrRedistribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddrRedistribute.setStatus("current")
_CwspAddressRowStatus_Type = RowStatus
_CwspAddressRowStatus_Object = MibTableColumn
cwspAddressRowStatus = _CwspAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 11, 1, 1, 8),
    _CwspAddressRowStatus_Type()
)
cwspAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspAddressRowStatus.setStatus("current")
_CwspRegAddress_ObjectIdentity = ObjectIdentity
cwspRegAddress = _CwspRegAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 12)
)
_CwspRegAddressTable_Object = MibTable
cwspRegAddressTable = _CwspRegAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    cwspRegAddressTable.setStatus("current")
_CwspRegAddressEntry_Object = MibTableRow
cwspRegAddressEntry = _CwspRegAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 12, 1, 1)
)
cwspRegAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-SVC-MIB", "cwspRegAtmAddress"),
)
if mibBuilder.loadTexts:
    cwspRegAddressEntry.setStatus("current")
_CwspRegAtmAddress_Type = AtmAddress
_CwspRegAtmAddress_Object = MibTableColumn
cwspRegAtmAddress = _CwspRegAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 12, 1, 1, 1),
    _CwspRegAtmAddress_Type()
)
cwspRegAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspRegAtmAddress.setStatus("current")


class _CwspRegAddressOrgSscope_Type(Integer32):
    """Custom type cwspRegAddressOrgSscope based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              15)
        )
    )
    namedValues = NamedValues(
        *(("global", 15),
          ("localNetwork", 1))
    )


_CwspRegAddressOrgSscope_Type.__name__ = "Integer32"
_CwspRegAddressOrgSscope_Object = MibTableColumn
cwspRegAddressOrgSscope = _CwspRegAddressOrgSscope_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 12, 1, 1, 2),
    _CwspRegAddressOrgSscope_Type()
)
cwspRegAddressOrgSscope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspRegAddressOrgSscope.setStatus("current")
_CwspLoad_ObjectIdentity = ObjectIdentity
cwspLoad = _CwspLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13)
)
_CwspLoadTable_Object = MibTable
cwspLoadTable = _CwspLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    cwspLoadTable.setStatus("current")
_CwspLoadEntry_Object = MibTableRow
cwspLoadEntry = _CwspLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1)
)
cwspLoadEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspLoadEntry.setStatus("current")


class _CwspLoadBwTotal_Type(Integer32):
    """Custom type cwspLoadBwTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadBwTotal_Type.__name__ = "Integer32"
_CwspLoadBwTotal_Object = MibTableColumn
cwspLoadBwTotal = _CwspLoadBwTotal_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 1),
    _CwspLoadBwTotal_Type()
)
cwspLoadBwTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadBwTotal.setStatus("current")


class _CwspLoadMaxBwCbr_Type(Integer32):
    """Custom type cwspLoadMaxBwCbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMaxBwCbr_Type.__name__ = "Integer32"
_CwspLoadMaxBwCbr_Object = MibTableColumn
cwspLoadMaxBwCbr = _CwspLoadMaxBwCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 2),
    _CwspLoadMaxBwCbr_Type()
)
cwspLoadMaxBwCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMaxBwCbr.setStatus("current")


class _CwspLoadMaxBwRtVbr_Type(Integer32):
    """Custom type cwspLoadMaxBwRtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMaxBwRtVbr_Type.__name__ = "Integer32"
_CwspLoadMaxBwRtVbr_Object = MibTableColumn
cwspLoadMaxBwRtVbr = _CwspLoadMaxBwRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 3),
    _CwspLoadMaxBwRtVbr_Type()
)
cwspLoadMaxBwRtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMaxBwRtVbr.setStatus("current")


class _CwspLoadMaxBwNrtVbr_Type(Integer32):
    """Custom type cwspLoadMaxBwNrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMaxBwNrtVbr_Type.__name__ = "Integer32"
_CwspLoadMaxBwNrtVbr_Object = MibTableColumn
cwspLoadMaxBwNrtVbr = _CwspLoadMaxBwNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 4),
    _CwspLoadMaxBwNrtVbr_Type()
)
cwspLoadMaxBwNrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMaxBwNrtVbr.setStatus("current")


class _CwspLoadMaxBwAbr_Type(Integer32):
    """Custom type cwspLoadMaxBwAbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMaxBwAbr_Type.__name__ = "Integer32"
_CwspLoadMaxBwAbr_Object = MibTableColumn
cwspLoadMaxBwAbr = _CwspLoadMaxBwAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 5),
    _CwspLoadMaxBwAbr_Type()
)
cwspLoadMaxBwAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMaxBwAbr.setStatus("current")


class _CwspLoadMaxBwUbr_Type(Integer32):
    """Custom type cwspLoadMaxBwUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMaxBwUbr_Type.__name__ = "Integer32"
_CwspLoadMaxBwUbr_Object = MibTableColumn
cwspLoadMaxBwUbr = _CwspLoadMaxBwUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 6),
    _CwspLoadMaxBwUbr_Type()
)
cwspLoadMaxBwUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMaxBwUbr.setStatus("current")


class _CwspLoadBwAvail_Type(Integer32):
    """Custom type cwspLoadBwAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadBwAvail_Type.__name__ = "Integer32"
_CwspLoadBwAvail_Object = MibTableColumn
cwspLoadBwAvail = _CwspLoadBwAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 7),
    _CwspLoadBwAvail_Type()
)
cwspLoadBwAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadBwAvail.setStatus("current")


class _CwspLoadAvlBwCbr_Type(Integer32):
    """Custom type cwspLoadAvlBwCbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlBwCbr_Type.__name__ = "Integer32"
_CwspLoadAvlBwCbr_Object = MibTableColumn
cwspLoadAvlBwCbr = _CwspLoadAvlBwCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 8),
    _CwspLoadAvlBwCbr_Type()
)
cwspLoadAvlBwCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlBwCbr.setStatus("current")


class _CwspLoadAvlBwRtVbr_Type(Integer32):
    """Custom type cwspLoadAvlBwRtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlBwRtVbr_Type.__name__ = "Integer32"
_CwspLoadAvlBwRtVbr_Object = MibTableColumn
cwspLoadAvlBwRtVbr = _CwspLoadAvlBwRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 9),
    _CwspLoadAvlBwRtVbr_Type()
)
cwspLoadAvlBwRtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlBwRtVbr.setStatus("current")


class _CwspLoadAvlBwNrtVbr_Type(Integer32):
    """Custom type cwspLoadAvlBwNrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlBwNrtVbr_Type.__name__ = "Integer32"
_CwspLoadAvlBwNrtVbr_Object = MibTableColumn
cwspLoadAvlBwNrtVbr = _CwspLoadAvlBwNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 10),
    _CwspLoadAvlBwNrtVbr_Type()
)
cwspLoadAvlBwNrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlBwNrtVbr.setStatus("current")


class _CwspLoadAvlBwAbr_Type(Integer32):
    """Custom type cwspLoadAvlBwAbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlBwAbr_Type.__name__ = "Integer32"
_CwspLoadAvlBwAbr_Object = MibTableColumn
cwspLoadAvlBwAbr = _CwspLoadAvlBwAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 11),
    _CwspLoadAvlBwAbr_Type()
)
cwspLoadAvlBwAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlBwAbr.setStatus("current")


class _CwspLoadAvlBwUbr_Type(Integer32):
    """Custom type cwspLoadAvlBwUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlBwUbr_Type.__name__ = "Integer32"
_CwspLoadAvlBwUbr_Object = MibTableColumn
cwspLoadAvlBwUbr = _CwspLoadAvlBwUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 12),
    _CwspLoadAvlBwUbr_Type()
)
cwspLoadAvlBwUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlBwUbr.setStatus("current")


class _CwspLoadVcAvail_Type(Integer32):
    """Custom type cwspLoadVcAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadVcAvail_Type.__name__ = "Integer32"
_CwspLoadVcAvail_Object = MibTableColumn
cwspLoadVcAvail = _CwspLoadVcAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 13),
    _CwspLoadVcAvail_Type()
)
cwspLoadVcAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadVcAvail.setStatus("current")


class _CwspLoadAvlVcCbr_Type(Integer32):
    """Custom type cwspLoadAvlVcCbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlVcCbr_Type.__name__ = "Integer32"
_CwspLoadAvlVcCbr_Object = MibTableColumn
cwspLoadAvlVcCbr = _CwspLoadAvlVcCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 14),
    _CwspLoadAvlVcCbr_Type()
)
cwspLoadAvlVcCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlVcCbr.setStatus("current")


class _CwspLoadAvlVcRtVbr_Type(Integer32):
    """Custom type cwspLoadAvlVcRtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlVcRtVbr_Type.__name__ = "Integer32"
_CwspLoadAvlVcRtVbr_Object = MibTableColumn
cwspLoadAvlVcRtVbr = _CwspLoadAvlVcRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 15),
    _CwspLoadAvlVcRtVbr_Type()
)
cwspLoadAvlVcRtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlVcRtVbr.setStatus("current")


class _CwspLoadAvlVcNrtVbr_Type(Integer32):
    """Custom type cwspLoadAvlVcNrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlVcNrtVbr_Type.__name__ = "Integer32"
_CwspLoadAvlVcNrtVbr_Object = MibTableColumn
cwspLoadAvlVcNrtVbr = _CwspLoadAvlVcNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 16),
    _CwspLoadAvlVcNrtVbr_Type()
)
cwspLoadAvlVcNrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlVcNrtVbr.setStatus("current")


class _CwspLoadAvlVcAbr_Type(Integer32):
    """Custom type cwspLoadAvlVcAbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlVcAbr_Type.__name__ = "Integer32"
_CwspLoadAvlVcAbr_Object = MibTableColumn
cwspLoadAvlVcAbr = _CwspLoadAvlVcAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 17),
    _CwspLoadAvlVcAbr_Type()
)
cwspLoadAvlVcAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlVcAbr.setStatus("current")


class _CwspLoadAvlVcUbr_Type(Integer32):
    """Custom type cwspLoadAvlVcUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadAvlVcUbr_Type.__name__ = "Integer32"
_CwspLoadAvlVcUbr_Object = MibTableColumn
cwspLoadAvlVcUbr = _CwspLoadAvlVcUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 18),
    _CwspLoadAvlVcUbr_Type()
)
cwspLoadAvlVcUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadAvlVcUbr.setStatus("current")


class _CwspLoadCtdCbr_Type(Integer32):
    """Custom type cwspLoadCtdCbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCtdCbr_Type.__name__ = "Integer32"
_CwspLoadCtdCbr_Object = MibTableColumn
cwspLoadCtdCbr = _CwspLoadCtdCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 19),
    _CwspLoadCtdCbr_Type()
)
cwspLoadCtdCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCtdCbr.setStatus("current")


class _CwspLoadCtdRtVbr_Type(Integer32):
    """Custom type cwspLoadCtdRtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCtdRtVbr_Type.__name__ = "Integer32"
_CwspLoadCtdRtVbr_Object = MibTableColumn
cwspLoadCtdRtVbr = _CwspLoadCtdRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 20),
    _CwspLoadCtdRtVbr_Type()
)
cwspLoadCtdRtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCtdRtVbr.setStatus("current")


class _CwspLoadCtdNrtVbr_Type(Integer32):
    """Custom type cwspLoadCtdNrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCtdNrtVbr_Type.__name__ = "Integer32"
_CwspLoadCtdNrtVbr_Object = MibTableColumn
cwspLoadCtdNrtVbr = _CwspLoadCtdNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 21),
    _CwspLoadCtdNrtVbr_Type()
)
cwspLoadCtdNrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCtdNrtVbr.setStatus("current")


class _CwspLoadCtdAbr_Type(Integer32):
    """Custom type cwspLoadCtdAbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCtdAbr_Type.__name__ = "Integer32"
_CwspLoadCtdAbr_Object = MibTableColumn
cwspLoadCtdAbr = _CwspLoadCtdAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 22),
    _CwspLoadCtdAbr_Type()
)
cwspLoadCtdAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCtdAbr.setStatus("current")


class _CwspLoadCtdUbr_Type(Integer32):
    """Custom type cwspLoadCtdUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCtdUbr_Type.__name__ = "Integer32"
_CwspLoadCtdUbr_Object = MibTableColumn
cwspLoadCtdUbr = _CwspLoadCtdUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 23),
    _CwspLoadCtdUbr_Type()
)
cwspLoadCtdUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCtdUbr.setStatus("current")


class _CwspLoadCdvCbr_Type(Integer32):
    """Custom type cwspLoadCdvCbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCdvCbr_Type.__name__ = "Integer32"
_CwspLoadCdvCbr_Object = MibTableColumn
cwspLoadCdvCbr = _CwspLoadCdvCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 24),
    _CwspLoadCdvCbr_Type()
)
cwspLoadCdvCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCdvCbr.setStatus("current")


class _CwspLoadCdvRtVbr_Type(Integer32):
    """Custom type cwspLoadCdvRtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCdvRtVbr_Type.__name__ = "Integer32"
_CwspLoadCdvRtVbr_Object = MibTableColumn
cwspLoadCdvRtVbr = _CwspLoadCdvRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 25),
    _CwspLoadCdvRtVbr_Type()
)
cwspLoadCdvRtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCdvRtVbr.setStatus("current")


class _CwspLoadCdvNrtVbr_Type(Integer32):
    """Custom type cwspLoadCdvNrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCdvNrtVbr_Type.__name__ = "Integer32"
_CwspLoadCdvNrtVbr_Object = MibTableColumn
cwspLoadCdvNrtVbr = _CwspLoadCdvNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 26),
    _CwspLoadCdvNrtVbr_Type()
)
cwspLoadCdvNrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCdvNrtVbr.setStatus("current")


class _CwspLoadCdvAbr_Type(Integer32):
    """Custom type cwspLoadCdvAbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCdvAbr_Type.__name__ = "Integer32"
_CwspLoadCdvAbr_Object = MibTableColumn
cwspLoadCdvAbr = _CwspLoadCdvAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 27),
    _CwspLoadCdvAbr_Type()
)
cwspLoadCdvAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCdvAbr.setStatus("current")


class _CwspLoadCdvUbr_Type(Integer32):
    """Custom type cwspLoadCdvUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadCdvUbr_Type.__name__ = "Integer32"
_CwspLoadCdvUbr_Object = MibTableColumn
cwspLoadCdvUbr = _CwspLoadCdvUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 28),
    _CwspLoadCdvUbr_Type()
)
cwspLoadCdvUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadCdvUbr.setStatus("current")


class _CwspLoadClr0Cbr_Type(Integer32):
    """Custom type cwspLoadClr0Cbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr0Cbr_Type.__name__ = "Integer32"
_CwspLoadClr0Cbr_Object = MibTableColumn
cwspLoadClr0Cbr = _CwspLoadClr0Cbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 29),
    _CwspLoadClr0Cbr_Type()
)
cwspLoadClr0Cbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr0Cbr.setStatus("current")


class _CwspLoadClr0RtVbr_Type(Integer32):
    """Custom type cwspLoadClr0RtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr0RtVbr_Type.__name__ = "Integer32"
_CwspLoadClr0RtVbr_Object = MibTableColumn
cwspLoadClr0RtVbr = _CwspLoadClr0RtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 30),
    _CwspLoadClr0RtVbr_Type()
)
cwspLoadClr0RtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr0RtVbr.setStatus("current")


class _CwspLoadClr0NrtVbr_Type(Integer32):
    """Custom type cwspLoadClr0NrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr0NrtVbr_Type.__name__ = "Integer32"
_CwspLoadClr0NrtVbr_Object = MibTableColumn
cwspLoadClr0NrtVbr = _CwspLoadClr0NrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 31),
    _CwspLoadClr0NrtVbr_Type()
)
cwspLoadClr0NrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr0NrtVbr.setStatus("current")


class _CwspLoadClr0Abr_Type(Integer32):
    """Custom type cwspLoadClr0Abr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr0Abr_Type.__name__ = "Integer32"
_CwspLoadClr0Abr_Object = MibTableColumn
cwspLoadClr0Abr = _CwspLoadClr0Abr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 32),
    _CwspLoadClr0Abr_Type()
)
cwspLoadClr0Abr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr0Abr.setStatus("current")


class _CwspLoadClr0Ubr_Type(Integer32):
    """Custom type cwspLoadClr0Ubr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr0Ubr_Type.__name__ = "Integer32"
_CwspLoadClr0Ubr_Object = MibTableColumn
cwspLoadClr0Ubr = _CwspLoadClr0Ubr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 33),
    _CwspLoadClr0Ubr_Type()
)
cwspLoadClr0Ubr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr0Ubr.setStatus("current")


class _CwspLoadClr01Cbr_Type(Integer32):
    """Custom type cwspLoadClr01Cbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr01Cbr_Type.__name__ = "Integer32"
_CwspLoadClr01Cbr_Object = MibTableColumn
cwspLoadClr01Cbr = _CwspLoadClr01Cbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 34),
    _CwspLoadClr01Cbr_Type()
)
cwspLoadClr01Cbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr01Cbr.setStatus("current")


class _CwspLoadClr01RtVbr_Type(Integer32):
    """Custom type cwspLoadClr01RtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr01RtVbr_Type.__name__ = "Integer32"
_CwspLoadClr01RtVbr_Object = MibTableColumn
cwspLoadClr01RtVbr = _CwspLoadClr01RtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 35),
    _CwspLoadClr01RtVbr_Type()
)
cwspLoadClr01RtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr01RtVbr.setStatus("current")


class _CwspLoadClr01NrtVbr_Type(Integer32):
    """Custom type cwspLoadClr01NrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr01NrtVbr_Type.__name__ = "Integer32"
_CwspLoadClr01NrtVbr_Object = MibTableColumn
cwspLoadClr01NrtVbr = _CwspLoadClr01NrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 36),
    _CwspLoadClr01NrtVbr_Type()
)
cwspLoadClr01NrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr01NrtVbr.setStatus("current")


class _CwspLoadClr01Abr_Type(Integer32):
    """Custom type cwspLoadClr01Abr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr01Abr_Type.__name__ = "Integer32"
_CwspLoadClr01Abr_Object = MibTableColumn
cwspLoadClr01Abr = _CwspLoadClr01Abr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 37),
    _CwspLoadClr01Abr_Type()
)
cwspLoadClr01Abr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr01Abr.setStatus("current")


class _CwspLoadClr01Ubr_Type(Integer32):
    """Custom type cwspLoadClr01Ubr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadClr01Ubr_Type.__name__ = "Integer32"
_CwspLoadClr01Ubr_Object = MibTableColumn
cwspLoadClr01Ubr = _CwspLoadClr01Ubr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 38),
    _CwspLoadClr01Ubr_Type()
)
cwspLoadClr01Ubr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadClr01Ubr.setStatus("current")


class _CwspLoadMinGurCrCbr_Type(Integer32):
    """Custom type cwspLoadMinGurCrCbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMinGurCrCbr_Type.__name__ = "Integer32"
_CwspLoadMinGurCrCbr_Object = MibTableColumn
cwspLoadMinGurCrCbr = _CwspLoadMinGurCrCbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 39),
    _CwspLoadMinGurCrCbr_Type()
)
cwspLoadMinGurCrCbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMinGurCrCbr.setStatus("current")


class _CwspLoadMinGurCrRtVbr_Type(Integer32):
    """Custom type cwspLoadMinGurCrRtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMinGurCrRtVbr_Type.__name__ = "Integer32"
_CwspLoadMinGurCrRtVbr_Object = MibTableColumn
cwspLoadMinGurCrRtVbr = _CwspLoadMinGurCrRtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 40),
    _CwspLoadMinGurCrRtVbr_Type()
)
cwspLoadMinGurCrRtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMinGurCrRtVbr.setStatus("current")


class _CwspLoadMinGurCrNrtVbr_Type(Integer32):
    """Custom type cwspLoadMinGurCrNrtVbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMinGurCrNrtVbr_Type.__name__ = "Integer32"
_CwspLoadMinGurCrNrtVbr_Object = MibTableColumn
cwspLoadMinGurCrNrtVbr = _CwspLoadMinGurCrNrtVbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 41),
    _CwspLoadMinGurCrNrtVbr_Type()
)
cwspLoadMinGurCrNrtVbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMinGurCrNrtVbr.setStatus("current")


class _CwspLoadMinGurCrAbr_Type(Integer32):
    """Custom type cwspLoadMinGurCrAbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMinGurCrAbr_Type.__name__ = "Integer32"
_CwspLoadMinGurCrAbr_Object = MibTableColumn
cwspLoadMinGurCrAbr = _CwspLoadMinGurCrAbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 42),
    _CwspLoadMinGurCrAbr_Type()
)
cwspLoadMinGurCrAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMinGurCrAbr.setStatus("current")


class _CwspLoadMinGurCrUbr_Type(Integer32):
    """Custom type cwspLoadMinGurCrUbr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspLoadMinGurCrUbr_Type.__name__ = "Integer32"
_CwspLoadMinGurCrUbr_Object = MibTableColumn
cwspLoadMinGurCrUbr = _CwspLoadMinGurCrUbr_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 13, 1, 1, 43),
    _CwspLoadMinGurCrUbr_Type()
)
cwspLoadMinGurCrUbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspLoadMinGurCrUbr.setStatus("current")
_CwspConnTrace_ObjectIdentity = ObjectIdentity
cwspConnTrace = _CwspConnTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14)
)


class _CwspConnTraceAvail_Type(Integer32):
    """Custom type cwspConnTraceAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwspConnTraceAvail_Type.__name__ = "Integer32"
_CwspConnTraceAvail_Object = MibScalar
cwspConnTraceAvail = _CwspConnTraceAvail_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 1),
    _CwspConnTraceAvail_Type()
)
cwspConnTraceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceAvail.setStatus("current")


class _CwspConnTraceNextIndex_Type(Integer32):
    """Custom type cwspConnTraceNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwspConnTraceNextIndex_Type.__name__ = "Integer32"
_CwspConnTraceNextIndex_Object = MibScalar
cwspConnTraceNextIndex = _CwspConnTraceNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 2),
    _CwspConnTraceNextIndex_Type()
)
cwspConnTraceNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceNextIndex.setStatus("current")
_CwspConnTraceCntlTable_Object = MibTable
cwspConnTraceCntlTable = _CwspConnTraceCntlTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    cwspConnTraceCntlTable.setStatus("current")
_CwspConnTraceCntlEntry_Object = MibTableRow
cwspConnTraceCntlEntry = _CwspConnTraceCntlEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1)
)
cwspConnTraceCntlEntry.setIndexNames(
    (0, "CISCO-WAN-SVC-MIB", "cwspConnTraceIndex"),
)
if mibBuilder.loadTexts:
    cwspConnTraceCntlEntry.setStatus("current")


class _CwspConnTraceIndex_Type(Integer32):
    """Custom type cwspConnTraceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwspConnTraceIndex_Type.__name__ = "Integer32"
_CwspConnTraceIndex_Object = MibTableColumn
cwspConnTraceIndex = _CwspConnTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 1),
    _CwspConnTraceIndex_Type()
)
cwspConnTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspConnTraceIndex.setStatus("current")
_CwspConnTraceifIndex_Type = InterfaceIndex
_CwspConnTraceifIndex_Object = MibTableColumn
cwspConnTraceifIndex = _CwspConnTraceifIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 2),
    _CwspConnTraceifIndex_Type()
)
cwspConnTraceifIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConnTraceifIndex.setStatus("current")


class _CwspConnTraceSrcVpi_Type(Integer32):
    """Custom type cwspConnTraceSrcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspConnTraceSrcVpi_Type.__name__ = "Integer32"
_CwspConnTraceSrcVpi_Object = MibTableColumn
cwspConnTraceSrcVpi = _CwspConnTraceSrcVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 3),
    _CwspConnTraceSrcVpi_Type()
)
cwspConnTraceSrcVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConnTraceSrcVpi.setStatus("current")


class _CwspConnTraceSrcVci_Type(Integer32):
    """Custom type cwspConnTraceSrcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspConnTraceSrcVci_Type.__name__ = "Integer32"
_CwspConnTraceSrcVci_Object = MibTableColumn
cwspConnTraceSrcVci = _CwspConnTraceSrcVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 4),
    _CwspConnTraceSrcVci_Type()
)
cwspConnTraceSrcVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConnTraceSrcVci.setStatus("current")


class _CwspConnTraceType_Type(Integer32):
    """Custom type cwspConnTraceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("p2mp", 2),
          ("p2p", 1))
    )


_CwspConnTraceType_Type.__name__ = "Integer32"
_CwspConnTraceType_Object = MibTableColumn
cwspConnTraceType = _CwspConnTraceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 5),
    _CwspConnTraceType_Type()
)
cwspConnTraceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConnTraceType.setStatus("current")


class _CwspConnTraceCallRef_Type(Integer32):
    """Custom type cwspConnTraceCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspConnTraceCallRef_Type.__name__ = "Integer32"
_CwspConnTraceCallRef_Object = MibTableColumn
cwspConnTraceCallRef = _CwspConnTraceCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 6),
    _CwspConnTraceCallRef_Type()
)
cwspConnTraceCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceCallRef.setStatus("current")


class _CwspConnTraceLeafRef_Type(Integer32):
    """Custom type cwspConnTraceLeafRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspConnTraceLeafRef_Type.__name__ = "Integer32"
_CwspConnTraceLeafRef_Object = MibTableColumn
cwspConnTraceLeafRef = _CwspConnTraceLeafRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 7),
    _CwspConnTraceLeafRef_Type()
)
cwspConnTraceLeafRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConnTraceLeafRef.setStatus("current")


class _CwspConnTraceDestVpi_Type(Integer32):
    """Custom type cwspConnTraceDestVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspConnTraceDestVpi_Type.__name__ = "Integer32"
_CwspConnTraceDestVpi_Object = MibTableColumn
cwspConnTraceDestVpi = _CwspConnTraceDestVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 8),
    _CwspConnTraceDestVpi_Type()
)
cwspConnTraceDestVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceDestVpi.setStatus("current")


class _CwspConnTraceDestVci_Type(Integer32):
    """Custom type cwspConnTraceDestVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspConnTraceDestVci_Type.__name__ = "Integer32"
_CwspConnTraceDestVci_Object = MibTableColumn
cwspConnTraceDestVci = _CwspConnTraceDestVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 9),
    _CwspConnTraceDestVci_Type()
)
cwspConnTraceDestVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceDestVci.setStatus("current")


class _CwspConnTraceDestCallRef_Type(Integer32):
    """Custom type cwspConnTraceDestCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspConnTraceDestCallRef_Type.__name__ = "Integer32"
_CwspConnTraceDestCallRef_Object = MibTableColumn
cwspConnTraceDestCallRef = _CwspConnTraceDestCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 10),
    _CwspConnTraceDestCallRef_Type()
)
cwspConnTraceDestCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceDestCallRef.setStatus("current")


class _CwspConnTraceResultStatus_Type(Integer32):
    """Custom type cwspConnTraceResultStatus based on Integer32"""
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
        *(("traceCompleted", 2),
          ("traceContRefused", 5),
          ("traceExceededLength", 4),
          ("traceInProgress", 1),
          ("traceIncompleted", 3),
          ("traceLackResource", 6))
    )


_CwspConnTraceResultStatus_Type.__name__ = "Integer32"
_CwspConnTraceResultStatus_Object = MibTableColumn
cwspConnTraceResultStatus = _CwspConnTraceResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 11),
    _CwspConnTraceResultStatus_Type()
)
cwspConnTraceResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceResultStatus.setStatus("current")
_CwspConnTraceQueryStatus_Type = RowStatus
_CwspConnTraceQueryStatus_Object = MibTableColumn
cwspConnTraceQueryStatus = _CwspConnTraceQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 3, 1, 12),
    _CwspConnTraceQueryStatus_Type()
)
cwspConnTraceQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwspConnTraceQueryStatus.setStatus("current")
_CwspConnTraceTable_Object = MibTable
cwspConnTraceTable = _CwspConnTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4)
)
if mibBuilder.loadTexts:
    cwspConnTraceTable.setStatus("current")
_CwspConnTraceEntry_Object = MibTableRow
cwspConnTraceEntry = _CwspConnTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1)
)
cwspConnTraceEntry.setIndexNames(
    (0, "CISCO-WAN-SVC-MIB", "cwspConnTraceIndex"),
    (0, "CISCO-WAN-SVC-MIB", "cwspConnTraceDataIndex"),
)
if mibBuilder.loadTexts:
    cwspConnTraceEntry.setStatus("current")


class _CwspConnTraceDataIndex_Type(Integer32):
    """Custom type cwspConnTraceDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwspConnTraceDataIndex_Type.__name__ = "Integer32"
_CwspConnTraceDataIndex_Object = MibTableColumn
cwspConnTraceDataIndex = _CwspConnTraceDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 1),
    _CwspConnTraceDataIndex_Type()
)
cwspConnTraceDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwspConnTraceDataIndex.setStatus("current")
_CwspConnTraceNodeId_Type = PnniNodeId
_CwspConnTraceNodeId_Object = MibTableColumn
cwspConnTraceNodeId = _CwspConnTraceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 2),
    _CwspConnTraceNodeId_Type()
)
cwspConnTraceNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceNodeId.setStatus("current")
_CwspConnTraceEgressPortId_Type = PnniPortId
_CwspConnTraceEgressPortId_Object = MibTableColumn
cwspConnTraceEgressPortId = _CwspConnTraceEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 3),
    _CwspConnTraceEgressPortId_Type()
)
cwspConnTraceEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceEgressPortId.setStatus("current")


class _CwspConnTraceEgressVpi_Type(Integer32):
    """Custom type cwspConnTraceEgressVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspConnTraceEgressVpi_Type.__name__ = "Integer32"
_CwspConnTraceEgressVpi_Object = MibTableColumn
cwspConnTraceEgressVpi = _CwspConnTraceEgressVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 4),
    _CwspConnTraceEgressVpi_Type()
)
cwspConnTraceEgressVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceEgressVpi.setStatus("current")


class _CwspConnTraceEgressVci_Type(Integer32):
    """Custom type cwspConnTraceEgressVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspConnTraceEgressVci_Type.__name__ = "Integer32"
_CwspConnTraceEgressVci_Object = MibTableColumn
cwspConnTraceEgressVci = _CwspConnTraceEgressVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 5),
    _CwspConnTraceEgressVci_Type()
)
cwspConnTraceEgressVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceEgressVci.setStatus("current")


class _CwspConnTraceEgressCallRef_Type(Integer32):
    """Custom type cwspConnTraceEgressCallRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwspConnTraceEgressCallRef_Type.__name__ = "Integer32"
_CwspConnTraceEgressCallRef_Object = MibTableColumn
cwspConnTraceEgressCallRef = _CwspConnTraceEgressCallRef_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 6),
    _CwspConnTraceEgressCallRef_Type()
)
cwspConnTraceEgressCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceEgressCallRef.setStatus("current")


class _CwspConnTraceEgressPhyPortId_Type(OctetString):
    """Custom type cwspConnTraceEgressPhyPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CwspConnTraceEgressPhyPortId_Type.__name__ = "OctetString"
_CwspConnTraceEgressPhyPortId_Object = MibTableColumn
cwspConnTraceEgressPhyPortId = _CwspConnTraceEgressPhyPortId_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 7),
    _CwspConnTraceEgressPhyPortId_Type()
)
cwspConnTraceEgressPhyPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceEgressPhyPortId.setStatus("current")
_CwspConnTraceLastNode_Type = TruthValue
_CwspConnTraceLastNode_Object = MibTableColumn
cwspConnTraceLastNode = _CwspConnTraceLastNode_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 14, 4, 1, 8),
    _CwspConnTraceLastNode_Type()
)
cwspConnTraceLastNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspConnTraceLastNode.setStatus("current")
_CwspOperation_ObjectIdentity = ObjectIdentity
cwspOperation = _CwspOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15)
)
_CwspOperationTable_Object = MibTable
cwspOperationTable = _CwspOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    cwspOperationTable.setStatus("current")
_CwspOperationEntry_Object = MibTableRow
cwspOperationEntry = _CwspOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1)
)
cwspOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwspOperationEntry.setStatus("current")
_CwspOperIlmiEnable_Type = TruthValue
_CwspOperIlmiEnable_Object = MibTableColumn
cwspOperIlmiEnable = _CwspOperIlmiEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 1),
    _CwspOperIlmiEnable_Type()
)
cwspOperIlmiEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperIlmiEnable.setStatus("current")


class _CwspOperIfcType_Type(Integer32):
    """Custom type cwspOperIfcType based on Integer32"""
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
        *(("aini", 5),
          ("enni", 6),
          ("iisp", 3),
          ("pnni", 4),
          ("privateUni", 2),
          ("publicUni", 1))
    )


_CwspOperIfcType_Type.__name__ = "Integer32"
_CwspOperIfcType_Object = MibTableColumn
cwspOperIfcType = _CwspOperIfcType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 2),
    _CwspOperIfcType_Type()
)
cwspOperIfcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperIfcType.setStatus("current")


class _CwspOperIfcSide_Type(Integer32):
    """Custom type cwspOperIfcSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 2),
          ("symmetric", 3),
          ("userSide", 1))
    )


_CwspOperIfcSide_Type.__name__ = "Integer32"
_CwspOperIfcSide_Object = MibTableColumn
cwspOperIfcSide = _CwspOperIfcSide_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 3),
    _CwspOperIfcSide_Type()
)
cwspOperIfcSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperIfcSide.setStatus("current")


class _CwspOperMaxVPCs_Type(Integer32):
    """Custom type cwspOperMaxVPCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CwspOperMaxVPCs_Type.__name__ = "Integer32"
_CwspOperMaxVPCs_Object = MibTableColumn
cwspOperMaxVPCs = _CwspOperMaxVPCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 4),
    _CwspOperMaxVPCs_Type()
)
cwspOperMaxVPCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxVPCs.setStatus("current")


class _CwspOperMaxVCCs_Type(Integer32):
    """Custom type cwspOperMaxVCCs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CwspOperMaxVCCs_Type.__name__ = "Integer32"
_CwspOperMaxVCCs_Object = MibTableColumn
cwspOperMaxVCCs = _CwspOperMaxVCCs_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 5),
    _CwspOperMaxVCCs_Type()
)
cwspOperMaxVCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxVCCs.setStatus("current")


class _CwspOperMaxVpiBits_Type(Integer32):
    """Custom type cwspOperMaxVpiBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_CwspOperMaxVpiBits_Type.__name__ = "Integer32"
_CwspOperMaxVpiBits_Object = MibTableColumn
cwspOperMaxVpiBits = _CwspOperMaxVpiBits_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 6),
    _CwspOperMaxVpiBits_Type()
)
cwspOperMaxVpiBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxVpiBits.setStatus("current")


class _CwspOperMaxVciBits_Type(Integer32):
    """Custom type cwspOperMaxVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CwspOperMaxVciBits_Type.__name__ = "Integer32"
_CwspOperMaxVciBits_Object = MibTableColumn
cwspOperMaxVciBits = _CwspOperMaxVciBits_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 7),
    _CwspOperMaxVciBits_Type()
)
cwspOperMaxVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxVciBits.setStatus("current")


class _CwspOperUniType_Type(Integer32):
    """Custom type cwspOperUniType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 2),
          ("public", 1))
    )


_CwspOperUniType_Type.__name__ = "Integer32"
_CwspOperUniType_Object = MibTableColumn
cwspOperUniType = _CwspOperUniType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 8),
    _CwspOperUniType_Type()
)
cwspOperUniType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperUniType.setStatus("current")


class _CwspOperUniVersion_Type(Integer32):
    """Custom type cwspOperUniVersion based on Integer32"""
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
        *(("unsupported", 5),
          ("version2point0", 1),
          ("version3poing0", 2),
          ("version3poing1", 3),
          ("version4poing0", 4))
    )


_CwspOperUniVersion_Type.__name__ = "Integer32"
_CwspOperUniVersion_Object = MibTableColumn
cwspOperUniVersion = _CwspOperUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 9),
    _CwspOperUniVersion_Type()
)
cwspOperUniVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperUniVersion.setStatus("current")


class _CwspOperDeviceType_Type(Integer32):
    """Custom type cwspOperDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("user", 1))
    )


_CwspOperDeviceType_Type.__name__ = "Integer32"
_CwspOperDeviceType_Object = MibTableColumn
cwspOperDeviceType = _CwspOperDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 10),
    _CwspOperDeviceType_Type()
)
cwspOperDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperDeviceType.setStatus("current")


class _CwspOperIlmiVersion_Type(Integer32):
    """Custom type cwspOperIlmiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("version4point0", 2))
    )


_CwspOperIlmiVersion_Type.__name__ = "Integer32"
_CwspOperIlmiVersion_Object = MibTableColumn
cwspOperIlmiVersion = _CwspOperIlmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 11),
    _CwspOperIlmiVersion_Type()
)
cwspOperIlmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperIlmiVersion.setStatus("current")


class _CwspOperNniSigVersion_Type(Integer32):
    """Custom type cwspOperNniSigVersion based on Integer32"""
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
        *(("aini", 5),
          ("enni", 4),
          ("iisp", 2),
          ("pnniVersion1point0", 3),
          ("unsupported", 1))
    )


_CwspOperNniSigVersion_Type.__name__ = "Integer32"
_CwspOperNniSigVersion_Object = MibTableColumn
cwspOperNniSigVersion = _CwspOperNniSigVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 12),
    _CwspOperNniSigVersion_Type()
)
cwspOperNniSigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperNniSigVersion.setStatus("current")


class _CwspOperMaxSvpcVpi_Type(Integer32):
    """Custom type cwspOperMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CwspOperMaxSvpcVpi_Type.__name__ = "Integer32"
_CwspOperMaxSvpcVpi_Object = MibTableColumn
cwspOperMaxSvpcVpi = _CwspOperMaxSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 13),
    _CwspOperMaxSvpcVpi_Type()
)
cwspOperMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxSvpcVpi.setStatus("current")


class _CwspOperMinSvpcVpi_Type(Integer32):
    """Custom type cwspOperMinSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CwspOperMinSvpcVpi_Type.__name__ = "Integer32"
_CwspOperMinSvpcVpi_Object = MibTableColumn
cwspOperMinSvpcVpi = _CwspOperMinSvpcVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 14),
    _CwspOperMinSvpcVpi_Type()
)
cwspOperMinSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMinSvpcVpi.setStatus("current")


class _CwspOperMaxSvccVpi_Type(Integer32):
    """Custom type cwspOperMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspOperMaxSvccVpi_Type.__name__ = "Integer32"
_CwspOperMaxSvccVpi_Object = MibTableColumn
cwspOperMaxSvccVpi = _CwspOperMaxSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 15),
    _CwspOperMaxSvccVpi_Type()
)
cwspOperMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxSvccVpi.setStatus("current")


class _CwspOperMinSvccVpi_Type(Integer32):
    """Custom type cwspOperMinSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CwspOperMinSvccVpi_Type.__name__ = "Integer32"
_CwspOperMinSvccVpi_Object = MibTableColumn
cwspOperMinSvccVpi = _CwspOperMinSvccVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 16),
    _CwspOperMinSvccVpi_Type()
)
cwspOperMinSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMinSvccVpi.setStatus("current")


class _CwspOperMaxSvccVci_Type(Integer32):
    """Custom type cwspOperMaxSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 65535),
    )


_CwspOperMaxSvccVci_Type.__name__ = "Integer32"
_CwspOperMaxSvccVci_Object = MibTableColumn
cwspOperMaxSvccVci = _CwspOperMaxSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 17),
    _CwspOperMaxSvccVci_Type()
)
cwspOperMaxSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMaxSvccVci.setStatus("current")


class _CwspOperMinSvccVci_Type(Integer32):
    """Custom type cwspOperMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwspOperMinSvccVci_Type.__name__ = "Integer32"
_CwspOperMinSvccVci_Object = MibTableColumn
cwspOperMinSvccVci = _CwspOperMinSvccVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 18),
    _CwspOperMinSvccVci_Type()
)
cwspOperMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperMinSvccVci.setStatus("current")


class _CwspOperAddrPlanSupported_Type(Integer32):
    """Custom type cwspOperAddrPlanSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aesa", 2),
          ("both", 1),
          ("e164", 3))
    )


_CwspOperAddrPlanSupported_Type.__name__ = "Integer32"
_CwspOperAddrPlanSupported_Object = MibTableColumn
cwspOperAddrPlanSupported = _CwspOperAddrPlanSupported_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 1, 1, 19),
    _CwspOperAddrPlanSupported_Type()
)
cwspOperAddrPlanSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperAddrPlanSupported.setStatus("current")


class _CwspOperFailReason_Type(Integer32):
    """Custom type cwspOperFailReason based on Integer32"""
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
        *(("ilmiDown", 1),
          ("neighIpChanged", 5),
          ("portDown", 2),
          ("vccfailure", 4),
          ("vsiAdminDown", 7),
          ("vsiOperDown", 3),
          ("vsiRemove", 6))
    )


_CwspOperFailReason_Type.__name__ = "Integer32"
_CwspOperFailReason_Object = MibScalar
cwspOperFailReason = _CwspOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 2, 15, 2),
    _CwspOperFailReason_Type()
)
cwspOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwspOperFailReason.setStatus("current")
_CiscoWANPnniRouting_ObjectIdentity = ObjectIdentity
ciscoWANPnniRouting = _CiscoWANPnniRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 3)
)


class _CiscoWANPnniLinkStatus_Type(Integer32):
    """Custom type ciscoWANPnniLinkStatus based on Integer32"""
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
        *(("in2win", 1),
          ("in2wout", 3),
          ("inCout", 5),
          ("out2win", 2),
          ("out2wout", 4),
          ("outCout", 6))
    )


_CiscoWANPnniLinkStatus_Type.__name__ = "Integer32"
_CiscoWANPnniLinkStatus_Object = MibScalar
ciscoWANPnniLinkStatus = _CiscoWANPnniLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 3, 1),
    _CiscoWANPnniLinkStatus_Type()
)
ciscoWANPnniLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWANPnniLinkStatus.setStatus("current")


class _CiscoWANPnniPglStatus_Type(Integer32):
    """Custom type ciscoWANPnniPglStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hung", 2),
          ("ok", 1))
    )


_CiscoWANPnniPglStatus_Type.__name__ = "Integer32"
_CiscoWANPnniPglStatus_Object = MibScalar
ciscoWANPnniPglStatus = _CiscoWANPnniPglStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 3, 2),
    _CiscoWANPnniPglStatus_Type()
)
ciscoWANPnniPglStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWANPnniPglStatus.setStatus("current")


class _CiscoWANPnniReachability_Type(Integer32):
    """Custom type ciscoWANPnniReachability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_CiscoWANPnniReachability_Type.__name__ = "Integer32"
_CiscoWANPnniReachability_Object = MibScalar
ciscoWANPnniReachability = _CiscoWANPnniReachability_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 3, 3),
    _CiscoWANPnniReachability_Type()
)
ciscoWANPnniReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWANPnniReachability.setStatus("current")
_CiscoWANPnniRemoteNodeId_Type = PnniNodeId
_CiscoWANPnniRemoteNodeId_Object = MibScalar
ciscoWANPnniRemoteNodeId = _CiscoWANPnniRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 3, 4),
    _CiscoWANPnniRemoteNodeId_Type()
)
ciscoWANPnniRemoteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWANPnniRemoteNodeId.setStatus("current")
_CiscoWANPnniPortId_Type = PnniPortId
_CiscoWANPnniPortId_Object = MibScalar
ciscoWANPnniPortId = _CiscoWANPnniPortId_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 3, 5),
    _CiscoWANPnniPortId_Type()
)
ciscoWANPnniPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWANPnniPortId.setStatus("current")
_CiscoWANSpvc_ObjectIdentity = ObjectIdentity
ciscoWANSpvc = _CiscoWANSpvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 4)
)
_CiscoWANSpvcFailReason_Type = CwspSpvcState
_CiscoWANSpvcFailReason_Object = MibScalar
ciscoWANSpvcFailReason = _CiscoWANSpvcFailReason_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 4, 1),
    _CiscoWANSpvcFailReason_Type()
)
ciscoWANSpvcFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWANSpvcFailReason.setStatus("current")


class _CwspSpvcNodePrefix_Type(OctetString):
    """Custom type cwspSpvcNodePrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_CwspSpvcNodePrefix_Type.__name__ = "OctetString"
_CwspSpvcNodePrefix_Object = MibScalar
cwspSpvcNodePrefix = _CwspSpvcNodePrefix_Object(
    (1, 3, 6, 1, 4, 1, 351, 140, 1, 4, 2),
    _CwspSpvcNodePrefix_Type()
)
cwspSpvcNodePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwspSpvcNodePrefix.setStatus("current")
_CiscoWANSvcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWANSvcMIBConformance = _CiscoWANSvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 3)
)
_CiscoWANSvcMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWANSvcMIBCompliances = _CiscoWANSvcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 1)
)
_CiscoWANSvcMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWANSvcMIBGroups = _CiscoWANSvcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2)
)

# Managed Objects groups

cwsInfoGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 1)
)
cwsInfoGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwsSwRevision"),
        ("CISCO-WAN-SVC-MIB", "cwsControllerStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspPnniStndbyControllerStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspPnniControllerStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspPnniControllerPhySlot"))
)
if mibBuilder.loadTexts:
    cwsInfoGrp.setStatus("current")

cwspConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 2)
)
cwspConfigGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspAdminStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspOperStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspSvcBlocked"),
        ("CISCO-WAN-SVC-MIB", "cwspSpvcBlocked"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAddrRegEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAutoConfEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiServRegEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspPhyIdentifier"),
        ("CISCO-WAN-SVC-MIB", "cwspSignallingVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspSignallingVci"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVpiBits"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVciBits"),
        ("CISCO-WAN-SVC-MIB", "cwspUniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspNniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspUniType"),
        ("CISCO-WAN-SVC-MIB", "cwspSide"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2pCalls"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2mpRoots"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2mpLeafs"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspEnhancedIisp"),
        ("CISCO-WAN-SVC-MIB", "cwspConfigTableRowStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrPlanSupported"))
)
if mibBuilder.loadTexts:
    cwspConfigGrp.setStatus("deprecated")

cwspCacConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 3)
)
cwspCacConfigGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspUtilFactorCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspUtilFactorRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspUtilFactorNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspUtilFactorAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspUtilFactorUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxBwCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxBwRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxBwNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxBwAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxBwUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinBwCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinBwRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinBwNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinBwAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinBwUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinVcCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinVcRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinVcNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinVcAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMinVcUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcBwCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcBwRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcBwNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcBwAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVcBwUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultCdvtCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultCdvtRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultCdvtNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultCdvtAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultCdvtUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultMbsRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspDefaultMbsNrtVbr"))
)
if mibBuilder.loadTexts:
    cwspCacConfigGrp.setStatus("current")

cwspCallStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 4)
)
cwspCallStatsGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspCountReset"),
        ("CISCO-WAN-SVC-MIB", "cwspInCallAttempts"),
        ("CISCO-WAN-SVC-MIB", "cwspInCallEstabs"),
        ("CISCO-WAN-SVC-MIB", "cwspInCallFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspInFilterFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspInRouteFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspInResrcFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspInTimerFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspInCrankbacks"),
        ("CISCO-WAN-SVC-MIB", "cwspOutCallAttempts"),
        ("CISCO-WAN-SVC-MIB", "cwspOutCallEstabs"),
        ("CISCO-WAN-SVC-MIB", "cwspOutCallFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspOutFilterFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspOutRouteFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspOutResrcFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspOutTimerFailures"),
        ("CISCO-WAN-SVC-MIB", "cwspOutCrankbacks"))
)
if mibBuilder.loadTexts:
    cwspCallStatsGrp.setStatus("current")

cwspSigStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 5)
)
cwspSigStatsGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspSigCounterReset"),
        ("CISCO-WAN-SVC-MIB", "cwspCallProcRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspConnectRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspConnectAckRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSetupRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspReleaseRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspReleaseComplRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspRestartRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspRestartAckRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspStatusRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspStatusEnqRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspNotifyRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspAlertRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspProgressRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspAddPtyRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspAddPtyAckRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspAddPtyRejRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspDropPtyRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspIncorrectMsgRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspTimerExpiries"),
        ("CISCO-WAN-SVC-MIB", "cwspLastCause"),
        ("CISCO-WAN-SVC-MIB", "cwspLastDiagnostic"),
        ("CISCO-WAN-SVC-MIB", "cwspCallProcXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspConnectXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspConnectAckXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSetupXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspReleaseXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspReleaseComplXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspRestartXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspRestartAckXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspStatusXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspStatusEnqXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspNotifyXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspAlertXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspProgressXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspAddPtyXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspAddPtyAckXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspAddPtyRejXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspDropPtyXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopStatus"))
)
if mibBuilder.loadTexts:
    cwspSigStatsGrp.setStatus("current")

cwspCallGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 6)
)
cwspCallGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspCallCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspCallCallingAddress"),
        ("CISCO-WAN-SVC-MIB", "cwspCallCalledAddress"),
        ("CISCO-WAN-SVC-MIB", "cwspCallCallingSubAddr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallCalledSubAddr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallOtherIntfIndex"),
        ("CISCO-WAN-SVC-MIB", "cwspCallOtherIntfVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspCallOtherIntfVci"),
        ("CISCO-WAN-SVC-MIB", "cwspCallOtherIntfCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspCallType"),
        ("CISCO-WAN-SVC-MIB", "cwspCallStartTime"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBearerClass"),
        ("CISCO-WAN-SVC-MIB", "cwspCallServiceCategory"),
        ("CISCO-WAN-SVC-MIB", "cwspCallCastType"),
        ("CISCO-WAN-SVC-MIB", "cwspCallClipSusceptibility"),
        ("CISCO-WAN-SVC-MIB", "cwspCallFwdConformance"),
        ("CISCO-WAN-SVC-MIB", "cwspCallFwdPcr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallFwdScr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallFwdMbs"),
        ("CISCO-WAN-SVC-MIB", "cwspCallFwdCdvt"),
        ("CISCO-WAN-SVC-MIB", "cwspCallFwdFrameDiscard"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBwdConformance"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBwdPcr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBwdScr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBwdMbs"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBwdCdvt"),
        ("CISCO-WAN-SVC-MIB", "cwspCallBwdFrameDiscard"),
        ("CISCO-WAN-SVC-MIB", "cwspCallMaxCtd"),
        ("CISCO-WAN-SVC-MIB", "cwspCallMaxFwdCdv"),
        ("CISCO-WAN-SVC-MIB", "cwspCallMaxFwdClr"),
        ("CISCO-WAN-SVC-MIB", "cwspCallMaxBwdCdv"),
        ("CISCO-WAN-SVC-MIB", "cwspCallMaxBwdClr"))
)
if mibBuilder.loadTexts:
    cwspCallGrp.setStatus("current")

cwspAbrCallGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 7)
)
cwspAbrCallGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspAbrCallCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallClgAddress"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallCldAddress"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallClgSubAddr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallCldSubAddr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallOtherIntfIndex"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallOtherIntfVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallOtherIntfVci"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallOtherIntfCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallType"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallStartTime"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBearerClass"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallServiceCategory"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallCastType"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallClipSusceptibility"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdConformance"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdPcr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdMcr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdIcr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdRif"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdRdf"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdTbe"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdNrm"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdTrm"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdAdtf"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdCdf"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFwdFrameDiscard"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdPcr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdMcr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdIcr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdRif"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdRdf"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdTbe"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdNrm"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdTrm"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdAdtf"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdCdf"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallBwdFrameDiscard"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallFrtt"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallMaxCtd"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallMaxFwdCdv"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallMaxFwdClr"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallMaxBwdCdv"),
        ("CISCO-WAN-SVC-MIB", "cwspAbrCallMaxBwdClr"))
)
if mibBuilder.loadTexts:
    cwspAbrCallGrp.setStatus("current")

cwspPrefixGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 8)
)
cwspPrefixGrp.setObjects(
    ("CISCO-WAN-SVC-MIB", "cwspPrefixRowStatus")
)
if mibBuilder.loadTexts:
    cwspPrefixGrp.setStatus("current")

cwspLoadGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 9)
)
cwspLoadGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspLoadBwTotal"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMaxBwCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMaxBwRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMaxBwNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMaxBwAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMaxBwUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadBwAvail"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlBwCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlBwRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlBwNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlBwAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlBwUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadVcAvail"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlVcCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlVcRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlVcNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlVcAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadAvlVcUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCtdCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCtdRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCtdNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCtdAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCtdUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCdvCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCdvRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCdvNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCdvAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadCdvUbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr0Cbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr0RtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr0NrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr0Abr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr0Ubr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr01Cbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr01RtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr01NrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr01Abr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadClr01Ubr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMinGurCrCbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMinGurCrRtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMinGurCrNrtVbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMinGurCrAbr"),
        ("CISCO-WAN-SVC-MIB", "cwspLoadMinGurCrUbr"))
)
if mibBuilder.loadTexts:
    cwspLoadGrp.setStatus("current")

cwspAddressGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 10)
)
cwspAddressGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspAddrType"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrProto"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrPlan"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrScope"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrRedistribute"),
        ("CISCO-WAN-SVC-MIB", "cwspAddressRowStatus"))
)
if mibBuilder.loadTexts:
    cwspAddressGrp.setStatus("current")

cwspSigConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 11)
)
cwspSigConfigGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspSigCfgT301"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT303"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT308"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT310"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT316"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT317"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT322"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT397"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT398"),
        ("CISCO-WAN-SVC-MIB", "cwspSigCfgT399"))
)
if mibBuilder.loadTexts:
    cwspSigConfigGrp.setStatus("current")

cwspSscopConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 12)
)
cwspSscopConfigGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspSscopTmrCC"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopTmrKeepAlive"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopTmrNoResp"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopTmrPoll"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopTmtIdle"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopMaxCC"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopMaxPD"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopMaxSTAT"))
)
if mibBuilder.loadTexts:
    cwspSscopConfigGrp.setStatus("current")

cwspSscopStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 13)
)
cwspSscopStatsGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspSscopCounterReset"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopIgnoredPduRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopBgnRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopBgakRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopEndRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopEndakRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopRsRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopRsakRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopBgrejRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopSdRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopSdpRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopPollRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopStatRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopUstatRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopUdRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopMdRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopErakRcv"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopBgnXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopBgakXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopEndXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopEndakXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopRsXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopRsakXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopBgrejXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopSdXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopSdpXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopPollXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopStatXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopUstatXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopUdXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopMdXmt"),
        ("CISCO-WAN-SVC-MIB", "cwspSscopErakXmt"))
)
if mibBuilder.loadTexts:
    cwspSscopStatsGrp.setStatus("current")

cwspRegAddressGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 14)
)
cwspRegAddressGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspRegAtmAddress"),
        ("CISCO-WAN-SVC-MIB", "cwspRegAddressOrgSscope"))
)
if mibBuilder.loadTexts:
    cwspRegAddressGrp.setStatus("current")

cwspRoutingGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 15)
)
cwspRoutingGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "ciscoWANPnniLinkStatus"),
        ("CISCO-WAN-SVC-MIB", "ciscoWANPnniPglStatus"),
        ("CISCO-WAN-SVC-MIB", "ciscoWANPnniReachability"),
        ("CISCO-WAN-SVC-MIB", "ciscoWANPnniRemoteNodeId"),
        ("CISCO-WAN-SVC-MIB", "ciscoWANPnniPortId"))
)
if mibBuilder.loadTexts:
    cwspRoutingGrp.setStatus("current")

cwspConnTraceGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 16)
)
cwspConnTraceGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspConnTraceAvail"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceNextIndex"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceifIndex"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceSrcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceSrcVci"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceType"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceLeafRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceDestVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceDestVci"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceDestCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceResultStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceQueryStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceNodeId"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressPortId"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressVci"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressPhyPortId"))
)
if mibBuilder.loadTexts:
    cwspConnTraceGrp.setStatus("deprecated")

cwspOperationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 17)
)
cwspOperationGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspOperIlmiEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspOperIfcType"),
        ("CISCO-WAN-SVC-MIB", "cwspOperIfcSide"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxVPCs"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxVCCs"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxVpiBits"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxVciBits"),
        ("CISCO-WAN-SVC-MIB", "cwspOperUniType"),
        ("CISCO-WAN-SVC-MIB", "cwspOperUniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspOperDeviceType"),
        ("CISCO-WAN-SVC-MIB", "cwspOperIlmiVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspOperNniSigVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMinSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMinSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMaxSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspOperMinSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspOperFailReason"),
        ("CISCO-WAN-SVC-MIB", "cwspOperAddrPlanSupported"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiSecureLink"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAttachmentPoint"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiLocalAttrStd"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiUCSMEnable"))
)
if mibBuilder.loadTexts:
    cwspOperationGrp.setStatus("current")

cwspSpvcGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 18)
)
cwspSpvcGrp.setObjects(
      *(("CISCO-WAN-SVC-MIB", "ciscoWANSpvcFailReason"),
        ("CISCO-WAN-SVC-MIB", "cwspSpvcNodePrefix"))
)
if mibBuilder.loadTexts:
    cwspSpvcGrp.setStatus("current")

cwspConnTraceGrp2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 19)
)
cwspConnTraceGrp2.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspConnTraceAvail"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceNextIndex"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceifIndex"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceSrcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceSrcVci"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceType"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceLeafRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceDestVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceDestVci"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceDestCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceResultStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceQueryStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceNodeId"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressPortId"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressVci"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressCallRef"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceEgressPhyPortId"),
        ("CISCO-WAN-SVC-MIB", "cwspConnTraceLastNode"))
)
if mibBuilder.loadTexts:
    cwspConnTraceGrp2.setStatus("current")

cwspConfigGrp2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 20)
)
cwspConfigGrp2.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspAdminStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspOperStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspSvcBlocked"),
        ("CISCO-WAN-SVC-MIB", "cwspSpvcBlocked"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAddrRegEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAutoConfEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiServRegEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspPhyIdentifier"),
        ("CISCO-WAN-SVC-MIB", "cwspSignallingVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspSignallingVci"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVpiBits"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVciBits"),
        ("CISCO-WAN-SVC-MIB", "cwspUniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspNniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspUniType"),
        ("CISCO-WAN-SVC-MIB", "cwspSide"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2pCalls"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2mpRoots"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2mpLeafs"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspEnhancedIisp"),
        ("CISCO-WAN-SVC-MIB", "cwspConfigTableRowStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrPlanSupported"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiSecureLink"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAttachmentPoint"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiLocalAttrStd"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiUCSMEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingPriority"))
)
if mibBuilder.loadTexts:
    cwspConfigGrp2.setStatus("deprecated")

cwspConfigGrp3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 2, 21)
)
cwspConfigGrp3.setObjects(
      *(("CISCO-WAN-SVC-MIB", "cwspAdminStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspOperStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspSvcBlocked"),
        ("CISCO-WAN-SVC-MIB", "cwspSpvcBlocked"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAddrRegEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAutoConfEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiServRegEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspPhyIdentifier"),
        ("CISCO-WAN-SVC-MIB", "cwspSignallingVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspSignallingVci"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVpiBits"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxVciBits"),
        ("CISCO-WAN-SVC-MIB", "cwspUniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspNniVersion"),
        ("CISCO-WAN-SVC-MIB", "cwspUniType"),
        ("CISCO-WAN-SVC-MIB", "cwspSide"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2pCalls"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2mpRoots"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxP2mpLeafs"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvccVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvccVci"),
        ("CISCO-WAN-SVC-MIB", "cwspMinSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspMaxSvpcVpi"),
        ("CISCO-WAN-SVC-MIB", "cwspEnhancedIisp"),
        ("CISCO-WAN-SVC-MIB", "cwspConfigTableRowStatus"),
        ("CISCO-WAN-SVC-MIB", "cwspAddrPlanSupported"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiSecureLink"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiAttachmentPoint"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiLocalAttrStd"),
        ("CISCO-WAN-SVC-MIB", "cwspIlmiUCSMEnable"),
        ("CISCO-WAN-SVC-MIB", "cwspRoutingPriority"),
        ("CISCO-WAN-SVC-MIB", "cwspSpvcAddress"))
)
if mibBuilder.loadTexts:
    cwspConfigGrp3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWANSvcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWANSvcMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWANSvcMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWANSvcMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoWANSvcMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 140, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWANSvcMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-SVC-MIB",
    **{"CwspSpvcState": CwspSpvcState,
       "CwspControllerState": CwspControllerState,
       "ciscoWANSvcMIB": ciscoWANSvcMIB,
       "ciscoWANSvcMIBObjects": ciscoWANSvcMIBObjects,
       "ciscoWANSvcInfo": ciscoWANSvcInfo,
       "cwsSwRevision": cwsSwRevision,
       "cwsControllerStatus": cwsControllerStatus,
       "cwspPnniStndbyControllerStatus": cwspPnniStndbyControllerStatus,
       "cwspPnniControllerStatus": cwspPnniControllerStatus,
       "cwspPnniControllerPhySlot": cwspPnniControllerPhySlot,
       "ciscoWANSvcPort": ciscoWANSvcPort,
       "cwspConfig": cwspConfig,
       "cwspConfigTable": cwspConfigTable,
       "cwspConfigEntry": cwspConfigEntry,
       "cwspAdminStatus": cwspAdminStatus,
       "cwspOperStatus": cwspOperStatus,
       "cwspSvcBlocked": cwspSvcBlocked,
       "cwspSpvcBlocked": cwspSpvcBlocked,
       "cwspIlmiAddrRegEnable": cwspIlmiAddrRegEnable,
       "cwspIlmiAutoConfEnable": cwspIlmiAutoConfEnable,
       "cwspIlmiServRegEnable": cwspIlmiServRegEnable,
       "cwspPhyIdentifier": cwspPhyIdentifier,
       "cwspSignallingVpi": cwspSignallingVpi,
       "cwspSignallingVci": cwspSignallingVci,
       "cwspRoutingVpi": cwspRoutingVpi,
       "cwspRoutingVci": cwspRoutingVci,
       "cwspMaxVpiBits": cwspMaxVpiBits,
       "cwspMaxVciBits": cwspMaxVciBits,
       "cwspUniVersion": cwspUniVersion,
       "cwspNniVersion": cwspNniVersion,
       "cwspUniType": cwspUniType,
       "cwspSide": cwspSide,
       "cwspMaxP2pCalls": cwspMaxP2pCalls,
       "cwspMaxP2mpRoots": cwspMaxP2mpRoots,
       "cwspMaxP2mpLeafs": cwspMaxP2mpLeafs,
       "cwspMinSvccVpi": cwspMinSvccVpi,
       "cwspMaxSvccVpi": cwspMaxSvccVpi,
       "cwspMinSvccVci": cwspMinSvccVci,
       "cwspMaxSvccVci": cwspMaxSvccVci,
       "cwspMinSvpcVpi": cwspMinSvpcVpi,
       "cwspMaxSvpcVpi": cwspMaxSvpcVpi,
       "cwspEnhancedIisp": cwspEnhancedIisp,
       "cwspConfigTableRowStatus": cwspConfigTableRowStatus,
       "cwspAddrPlanSupported": cwspAddrPlanSupported,
       "cwspIlmiSecureLink": cwspIlmiSecureLink,
       "cwspIlmiAttachmentPoint": cwspIlmiAttachmentPoint,
       "cwspIlmiLocalAttrStd": cwspIlmiLocalAttrStd,
       "cwspIlmiUCSMEnable": cwspIlmiUCSMEnable,
       "cwspRoutingPriority": cwspRoutingPriority,
       "cwspSpvcAddress": cwspSpvcAddress,
       "cwspCacConfig": cwspCacConfig,
       "cwspCacConfigTable": cwspCacConfigTable,
       "cwspCacConfigEntry": cwspCacConfigEntry,
       "cwspUtilFactorCbr": cwspUtilFactorCbr,
       "cwspUtilFactorRtVbr": cwspUtilFactorRtVbr,
       "cwspUtilFactorNrtVbr": cwspUtilFactorNrtVbr,
       "cwspUtilFactorAbr": cwspUtilFactorAbr,
       "cwspUtilFactorUbr": cwspUtilFactorUbr,
       "cwspMaxBwCbr": cwspMaxBwCbr,
       "cwspMaxBwRtVbr": cwspMaxBwRtVbr,
       "cwspMaxBwNrtVbr": cwspMaxBwNrtVbr,
       "cwspMaxBwAbr": cwspMaxBwAbr,
       "cwspMaxBwUbr": cwspMaxBwUbr,
       "cwspMinBwCbr": cwspMinBwCbr,
       "cwspMinBwRtVbr": cwspMinBwRtVbr,
       "cwspMinBwNrtVbr": cwspMinBwNrtVbr,
       "cwspMinBwAbr": cwspMinBwAbr,
       "cwspMinBwUbr": cwspMinBwUbr,
       "cwspMaxVcCbr": cwspMaxVcCbr,
       "cwspMaxVcRtVbr": cwspMaxVcRtVbr,
       "cwspMaxVcNrtVbr": cwspMaxVcNrtVbr,
       "cwspMaxVcAbr": cwspMaxVcAbr,
       "cwspMaxVcUbr": cwspMaxVcUbr,
       "cwspMinVcCbr": cwspMinVcCbr,
       "cwspMinVcRtVbr": cwspMinVcRtVbr,
       "cwspMinVcNrtVbr": cwspMinVcNrtVbr,
       "cwspMinVcAbr": cwspMinVcAbr,
       "cwspMinVcUbr": cwspMinVcUbr,
       "cwspMaxVcBwCbr": cwspMaxVcBwCbr,
       "cwspMaxVcBwRtVbr": cwspMaxVcBwRtVbr,
       "cwspMaxVcBwNrtVbr": cwspMaxVcBwNrtVbr,
       "cwspMaxVcBwAbr": cwspMaxVcBwAbr,
       "cwspMaxVcBwUbr": cwspMaxVcBwUbr,
       "cwspDefaultCdvtCbr": cwspDefaultCdvtCbr,
       "cwspDefaultCdvtRtVbr": cwspDefaultCdvtRtVbr,
       "cwspDefaultCdvtNrtVbr": cwspDefaultCdvtNrtVbr,
       "cwspDefaultCdvtAbr": cwspDefaultCdvtAbr,
       "cwspDefaultCdvtUbr": cwspDefaultCdvtUbr,
       "cwspDefaultMbsRtVbr": cwspDefaultMbsRtVbr,
       "cwspDefaultMbsNrtVbr": cwspDefaultMbsNrtVbr,
       "cwspSigConfig": cwspSigConfig,
       "cwspSigConfigTable": cwspSigConfigTable,
       "cwspSigConfigEntry": cwspSigConfigEntry,
       "cwspSigCfgT301": cwspSigCfgT301,
       "cwspSigCfgT303": cwspSigCfgT303,
       "cwspSigCfgT308": cwspSigCfgT308,
       "cwspSigCfgT310": cwspSigCfgT310,
       "cwspSigCfgT316": cwspSigCfgT316,
       "cwspSigCfgT317": cwspSigCfgT317,
       "cwspSigCfgT322": cwspSigCfgT322,
       "cwspSigCfgT397": cwspSigCfgT397,
       "cwspSigCfgT398": cwspSigCfgT398,
       "cwspSigCfgT399": cwspSigCfgT399,
       "cwspSscopConfig": cwspSscopConfig,
       "cwspSscopTable": cwspSscopTable,
       "cwspSscopEntry": cwspSscopEntry,
       "cwspSscopTmrCC": cwspSscopTmrCC,
       "cwspSscopTmrKeepAlive": cwspSscopTmrKeepAlive,
       "cwspSscopTmrNoResp": cwspSscopTmrNoResp,
       "cwspSscopTmrPoll": cwspSscopTmrPoll,
       "cwspSscopTmtIdle": cwspSscopTmtIdle,
       "cwspSscopMaxCC": cwspSscopMaxCC,
       "cwspSscopMaxPD": cwspSscopMaxPD,
       "cwspSscopMaxSTAT": cwspSscopMaxSTAT,
       "cwspCallStats": cwspCallStats,
       "cwspCallStatsTable": cwspCallStatsTable,
       "cwspCallStatsEntry": cwspCallStatsEntry,
       "cwspCountReset": cwspCountReset,
       "cwspInCallAttempts": cwspInCallAttempts,
       "cwspInCallEstabs": cwspInCallEstabs,
       "cwspInCallFailures": cwspInCallFailures,
       "cwspInFilterFailures": cwspInFilterFailures,
       "cwspInRouteFailures": cwspInRouteFailures,
       "cwspInResrcFailures": cwspInResrcFailures,
       "cwspInTimerFailures": cwspInTimerFailures,
       "cwspInCrankbacks": cwspInCrankbacks,
       "cwspOutCallAttempts": cwspOutCallAttempts,
       "cwspOutCallEstabs": cwspOutCallEstabs,
       "cwspOutCallFailures": cwspOutCallFailures,
       "cwspOutFilterFailures": cwspOutFilterFailures,
       "cwspOutRouteFailures": cwspOutRouteFailures,
       "cwspOutResrcFailures": cwspOutResrcFailures,
       "cwspOutTimerFailures": cwspOutTimerFailures,
       "cwspOutCrankbacks": cwspOutCrankbacks,
       "cwspSigStats": cwspSigStats,
       "cwspSigStatsTable": cwspSigStatsTable,
       "cwspSigStatsEntry": cwspSigStatsEntry,
       "cwspSigCounterReset": cwspSigCounterReset,
       "cwspCallProcRcv": cwspCallProcRcv,
       "cwspConnectRcv": cwspConnectRcv,
       "cwspConnectAckRcv": cwspConnectAckRcv,
       "cwspSetupRcv": cwspSetupRcv,
       "cwspReleaseRcv": cwspReleaseRcv,
       "cwspReleaseComplRcv": cwspReleaseComplRcv,
       "cwspRestartRcv": cwspRestartRcv,
       "cwspRestartAckRcv": cwspRestartAckRcv,
       "cwspStatusRcv": cwspStatusRcv,
       "cwspStatusEnqRcv": cwspStatusEnqRcv,
       "cwspNotifyRcv": cwspNotifyRcv,
       "cwspAlertRcv": cwspAlertRcv,
       "cwspProgressRcv": cwspProgressRcv,
       "cwspAddPtyRcv": cwspAddPtyRcv,
       "cwspAddPtyAckRcv": cwspAddPtyAckRcv,
       "cwspAddPtyRejRcv": cwspAddPtyRejRcv,
       "cwspDropPtyRcv": cwspDropPtyRcv,
       "cwspIncorrectMsgRcv": cwspIncorrectMsgRcv,
       "cwspTimerExpiries": cwspTimerExpiries,
       "cwspLastCause": cwspLastCause,
       "cwspLastDiagnostic": cwspLastDiagnostic,
       "cwspCallProcXmt": cwspCallProcXmt,
       "cwspConnectXmt": cwspConnectXmt,
       "cwspConnectAckXmt": cwspConnectAckXmt,
       "cwspSetupXmt": cwspSetupXmt,
       "cwspReleaseXmt": cwspReleaseXmt,
       "cwspReleaseComplXmt": cwspReleaseComplXmt,
       "cwspRestartXmt": cwspRestartXmt,
       "cwspRestartAckXmt": cwspRestartAckXmt,
       "cwspStatusXmt": cwspStatusXmt,
       "cwspStatusEnqXmt": cwspStatusEnqXmt,
       "cwspNotifyXmt": cwspNotifyXmt,
       "cwspAlertXmt": cwspAlertXmt,
       "cwspProgressXmt": cwspProgressXmt,
       "cwspAddPtyXmt": cwspAddPtyXmt,
       "cwspAddPtyAckXmt": cwspAddPtyAckXmt,
       "cwspAddPtyRejXmt": cwspAddPtyRejXmt,
       "cwspDropPtyXmt": cwspDropPtyXmt,
       "cwspSscopStatus": cwspSscopStatus,
       "cwspSscopStats": cwspSscopStats,
       "cwspSscopStatsTable": cwspSscopStatsTable,
       "cwspSscopStatsEntry": cwspSscopStatsEntry,
       "cwspSscopCounterReset": cwspSscopCounterReset,
       "cwspSscopIgnoredPduRcv": cwspSscopIgnoredPduRcv,
       "cwspSscopBgnRcv": cwspSscopBgnRcv,
       "cwspSscopBgakRcv": cwspSscopBgakRcv,
       "cwspSscopEndRcv": cwspSscopEndRcv,
       "cwspSscopEndakRcv": cwspSscopEndakRcv,
       "cwspSscopRsRcv": cwspSscopRsRcv,
       "cwspSscopRsakRcv": cwspSscopRsakRcv,
       "cwspSscopBgrejRcv": cwspSscopBgrejRcv,
       "cwspSscopSdRcv": cwspSscopSdRcv,
       "cwspSscopSdpRcv": cwspSscopSdpRcv,
       "cwspSscopPollRcv": cwspSscopPollRcv,
       "cwspSscopStatRcv": cwspSscopStatRcv,
       "cwspSscopUstatRcv": cwspSscopUstatRcv,
       "cwspSscopUdRcv": cwspSscopUdRcv,
       "cwspSscopMdRcv": cwspSscopMdRcv,
       "cwspSscopErakRcv": cwspSscopErakRcv,
       "cwspSscopBgnXmt": cwspSscopBgnXmt,
       "cwspSscopBgakXmt": cwspSscopBgakXmt,
       "cwspSscopEndXmt": cwspSscopEndXmt,
       "cwspSscopEndakXmt": cwspSscopEndakXmt,
       "cwspSscopRsXmt": cwspSscopRsXmt,
       "cwspSscopRsakXmt": cwspSscopRsakXmt,
       "cwspSscopBgrejXmt": cwspSscopBgrejXmt,
       "cwspSscopSdXmt": cwspSscopSdXmt,
       "cwspSscopSdpXmt": cwspSscopSdpXmt,
       "cwspSscopPollXmt": cwspSscopPollXmt,
       "cwspSscopStatXmt": cwspSscopStatXmt,
       "cwspSscopUstatXmt": cwspSscopUstatXmt,
       "cwspSscopUdXmt": cwspSscopUdXmt,
       "cwspSscopMdXmt": cwspSscopMdXmt,
       "cwspSscopErakXmt": cwspSscopErakXmt,
       "cwspCall": cwspCall,
       "cwspCallTable": cwspCallTable,
       "cwspCallEntry": cwspCallEntry,
       "cwspCallVpi": cwspCallVpi,
       "cwspCallVci": cwspCallVci,
       "cwspCallLeafReference": cwspCallLeafReference,
       "cwspCallCallRef": cwspCallCallRef,
       "cwspCallCallingAddress": cwspCallCallingAddress,
       "cwspCallCalledAddress": cwspCallCalledAddress,
       "cwspCallCallingSubAddr": cwspCallCallingSubAddr,
       "cwspCallCalledSubAddr": cwspCallCalledSubAddr,
       "cwspCallOtherIntfIndex": cwspCallOtherIntfIndex,
       "cwspCallOtherIntfVpi": cwspCallOtherIntfVpi,
       "cwspCallOtherIntfVci": cwspCallOtherIntfVci,
       "cwspCallOtherIntfCallRef": cwspCallOtherIntfCallRef,
       "cwspCallType": cwspCallType,
       "cwspCallStartTime": cwspCallStartTime,
       "cwspCallBearerClass": cwspCallBearerClass,
       "cwspCallServiceCategory": cwspCallServiceCategory,
       "cwspCallCastType": cwspCallCastType,
       "cwspCallClipSusceptibility": cwspCallClipSusceptibility,
       "cwspCallFwdConformance": cwspCallFwdConformance,
       "cwspCallFwdPcr": cwspCallFwdPcr,
       "cwspCallFwdScr": cwspCallFwdScr,
       "cwspCallFwdMbs": cwspCallFwdMbs,
       "cwspCallFwdCdvt": cwspCallFwdCdvt,
       "cwspCallFwdFrameDiscard": cwspCallFwdFrameDiscard,
       "cwspCallBwdConformance": cwspCallBwdConformance,
       "cwspCallBwdPcr": cwspCallBwdPcr,
       "cwspCallBwdScr": cwspCallBwdScr,
       "cwspCallBwdMbs": cwspCallBwdMbs,
       "cwspCallBwdCdvt": cwspCallBwdCdvt,
       "cwspCallBwdFrameDiscard": cwspCallBwdFrameDiscard,
       "cwspCallMaxCtd": cwspCallMaxCtd,
       "cwspCallMaxFwdCdv": cwspCallMaxFwdCdv,
       "cwspCallMaxFwdClr": cwspCallMaxFwdClr,
       "cwspCallMaxBwdCdv": cwspCallMaxBwdCdv,
       "cwspCallMaxBwdClr": cwspCallMaxBwdClr,
       "cwspAbrCall": cwspAbrCall,
       "cwspAbrCallTable": cwspAbrCallTable,
       "cwspAbrCallEntry": cwspAbrCallEntry,
       "cwspAbrCallVpi": cwspAbrCallVpi,
       "cwspAbrCallVci": cwspAbrCallVci,
       "cwspAbrCallCallRef": cwspAbrCallCallRef,
       "cwspAbrCallClgAddress": cwspAbrCallClgAddress,
       "cwspAbrCallCldAddress": cwspAbrCallCldAddress,
       "cwspAbrCallClgSubAddr": cwspAbrCallClgSubAddr,
       "cwspAbrCallCldSubAddr": cwspAbrCallCldSubAddr,
       "cwspAbrCallOtherIntfIndex": cwspAbrCallOtherIntfIndex,
       "cwspAbrCallOtherIntfVpi": cwspAbrCallOtherIntfVpi,
       "cwspAbrCallOtherIntfVci": cwspAbrCallOtherIntfVci,
       "cwspAbrCallOtherIntfCallRef": cwspAbrCallOtherIntfCallRef,
       "cwspAbrCallType": cwspAbrCallType,
       "cwspAbrCallStartTime": cwspAbrCallStartTime,
       "cwspAbrCallBearerClass": cwspAbrCallBearerClass,
       "cwspAbrCallServiceCategory": cwspAbrCallServiceCategory,
       "cwspAbrCallCastType": cwspAbrCallCastType,
       "cwspAbrCallClipSusceptibility": cwspAbrCallClipSusceptibility,
       "cwspAbrCallFwdConformance": cwspAbrCallFwdConformance,
       "cwspAbrCallFwdPcr": cwspAbrCallFwdPcr,
       "cwspAbrCallFwdMcr": cwspAbrCallFwdMcr,
       "cwspAbrCallFwdIcr": cwspAbrCallFwdIcr,
       "cwspAbrCallFwdRif": cwspAbrCallFwdRif,
       "cwspAbrCallFwdRdf": cwspAbrCallFwdRdf,
       "cwspAbrCallFwdTbe": cwspAbrCallFwdTbe,
       "cwspAbrCallFwdNrm": cwspAbrCallFwdNrm,
       "cwspAbrCallFwdTrm": cwspAbrCallFwdTrm,
       "cwspAbrCallFwdAdtf": cwspAbrCallFwdAdtf,
       "cwspAbrCallFwdCdf": cwspAbrCallFwdCdf,
       "cwspAbrCallFwdFrameDiscard": cwspAbrCallFwdFrameDiscard,
       "cwspAbrCallBwdPcr": cwspAbrCallBwdPcr,
       "cwspAbrCallBwdMcr": cwspAbrCallBwdMcr,
       "cwspAbrCallBwdIcr": cwspAbrCallBwdIcr,
       "cwspAbrCallBwdRif": cwspAbrCallBwdRif,
       "cwspAbrCallBwdRdf": cwspAbrCallBwdRdf,
       "cwspAbrCallBwdTbe": cwspAbrCallBwdTbe,
       "cwspAbrCallBwdNrm": cwspAbrCallBwdNrm,
       "cwspAbrCallBwdTrm": cwspAbrCallBwdTrm,
       "cwspAbrCallBwdAdtf": cwspAbrCallBwdAdtf,
       "cwspAbrCallBwdCdf": cwspAbrCallBwdCdf,
       "cwspAbrCallBwdFrameDiscard": cwspAbrCallBwdFrameDiscard,
       "cwspAbrCallFrtt": cwspAbrCallFrtt,
       "cwspAbrCallMaxCtd": cwspAbrCallMaxCtd,
       "cwspAbrCallMaxFwdCdv": cwspAbrCallMaxFwdCdv,
       "cwspAbrCallMaxFwdClr": cwspAbrCallMaxFwdClr,
       "cwspAbrCallMaxBwdCdv": cwspAbrCallMaxBwdCdv,
       "cwspAbrCallMaxBwdClr": cwspAbrCallMaxBwdClr,
       "cwspPrefix": cwspPrefix,
       "cwspPrefixTable": cwspPrefixTable,
       "cwspPrefixEntry": cwspPrefixEntry,
       "cwspNetPrefix": cwspNetPrefix,
       "cwspPrefixRowStatus": cwspPrefixRowStatus,
       "cwspAddress": cwspAddress,
       "cwspAddressTable": cwspAddressTable,
       "cwspAddressEntry": cwspAddressEntry,
       "cwspAtmAddress": cwspAtmAddress,
       "cwspAddrLen": cwspAddrLen,
       "cwspAddrType": cwspAddrType,
       "cwspAddrProto": cwspAddrProto,
       "cwspAddrPlan": cwspAddrPlan,
       "cwspAddrScope": cwspAddrScope,
       "cwspAddrRedistribute": cwspAddrRedistribute,
       "cwspAddressRowStatus": cwspAddressRowStatus,
       "cwspRegAddress": cwspRegAddress,
       "cwspRegAddressTable": cwspRegAddressTable,
       "cwspRegAddressEntry": cwspRegAddressEntry,
       "cwspRegAtmAddress": cwspRegAtmAddress,
       "cwspRegAddressOrgSscope": cwspRegAddressOrgSscope,
       "cwspLoad": cwspLoad,
       "cwspLoadTable": cwspLoadTable,
       "cwspLoadEntry": cwspLoadEntry,
       "cwspLoadBwTotal": cwspLoadBwTotal,
       "cwspLoadMaxBwCbr": cwspLoadMaxBwCbr,
       "cwspLoadMaxBwRtVbr": cwspLoadMaxBwRtVbr,
       "cwspLoadMaxBwNrtVbr": cwspLoadMaxBwNrtVbr,
       "cwspLoadMaxBwAbr": cwspLoadMaxBwAbr,
       "cwspLoadMaxBwUbr": cwspLoadMaxBwUbr,
       "cwspLoadBwAvail": cwspLoadBwAvail,
       "cwspLoadAvlBwCbr": cwspLoadAvlBwCbr,
       "cwspLoadAvlBwRtVbr": cwspLoadAvlBwRtVbr,
       "cwspLoadAvlBwNrtVbr": cwspLoadAvlBwNrtVbr,
       "cwspLoadAvlBwAbr": cwspLoadAvlBwAbr,
       "cwspLoadAvlBwUbr": cwspLoadAvlBwUbr,
       "cwspLoadVcAvail": cwspLoadVcAvail,
       "cwspLoadAvlVcCbr": cwspLoadAvlVcCbr,
       "cwspLoadAvlVcRtVbr": cwspLoadAvlVcRtVbr,
       "cwspLoadAvlVcNrtVbr": cwspLoadAvlVcNrtVbr,
       "cwspLoadAvlVcAbr": cwspLoadAvlVcAbr,
       "cwspLoadAvlVcUbr": cwspLoadAvlVcUbr,
       "cwspLoadCtdCbr": cwspLoadCtdCbr,
       "cwspLoadCtdRtVbr": cwspLoadCtdRtVbr,
       "cwspLoadCtdNrtVbr": cwspLoadCtdNrtVbr,
       "cwspLoadCtdAbr": cwspLoadCtdAbr,
       "cwspLoadCtdUbr": cwspLoadCtdUbr,
       "cwspLoadCdvCbr": cwspLoadCdvCbr,
       "cwspLoadCdvRtVbr": cwspLoadCdvRtVbr,
       "cwspLoadCdvNrtVbr": cwspLoadCdvNrtVbr,
       "cwspLoadCdvAbr": cwspLoadCdvAbr,
       "cwspLoadCdvUbr": cwspLoadCdvUbr,
       "cwspLoadClr0Cbr": cwspLoadClr0Cbr,
       "cwspLoadClr0RtVbr": cwspLoadClr0RtVbr,
       "cwspLoadClr0NrtVbr": cwspLoadClr0NrtVbr,
       "cwspLoadClr0Abr": cwspLoadClr0Abr,
       "cwspLoadClr0Ubr": cwspLoadClr0Ubr,
       "cwspLoadClr01Cbr": cwspLoadClr01Cbr,
       "cwspLoadClr01RtVbr": cwspLoadClr01RtVbr,
       "cwspLoadClr01NrtVbr": cwspLoadClr01NrtVbr,
       "cwspLoadClr01Abr": cwspLoadClr01Abr,
       "cwspLoadClr01Ubr": cwspLoadClr01Ubr,
       "cwspLoadMinGurCrCbr": cwspLoadMinGurCrCbr,
       "cwspLoadMinGurCrRtVbr": cwspLoadMinGurCrRtVbr,
       "cwspLoadMinGurCrNrtVbr": cwspLoadMinGurCrNrtVbr,
       "cwspLoadMinGurCrAbr": cwspLoadMinGurCrAbr,
       "cwspLoadMinGurCrUbr": cwspLoadMinGurCrUbr,
       "cwspConnTrace": cwspConnTrace,
       "cwspConnTraceAvail": cwspConnTraceAvail,
       "cwspConnTraceNextIndex": cwspConnTraceNextIndex,
       "cwspConnTraceCntlTable": cwspConnTraceCntlTable,
       "cwspConnTraceCntlEntry": cwspConnTraceCntlEntry,
       "cwspConnTraceIndex": cwspConnTraceIndex,
       "cwspConnTraceifIndex": cwspConnTraceifIndex,
       "cwspConnTraceSrcVpi": cwspConnTraceSrcVpi,
       "cwspConnTraceSrcVci": cwspConnTraceSrcVci,
       "cwspConnTraceType": cwspConnTraceType,
       "cwspConnTraceCallRef": cwspConnTraceCallRef,
       "cwspConnTraceLeafRef": cwspConnTraceLeafRef,
       "cwspConnTraceDestVpi": cwspConnTraceDestVpi,
       "cwspConnTraceDestVci": cwspConnTraceDestVci,
       "cwspConnTraceDestCallRef": cwspConnTraceDestCallRef,
       "cwspConnTraceResultStatus": cwspConnTraceResultStatus,
       "cwspConnTraceQueryStatus": cwspConnTraceQueryStatus,
       "cwspConnTraceTable": cwspConnTraceTable,
       "cwspConnTraceEntry": cwspConnTraceEntry,
       "cwspConnTraceDataIndex": cwspConnTraceDataIndex,
       "cwspConnTraceNodeId": cwspConnTraceNodeId,
       "cwspConnTraceEgressPortId": cwspConnTraceEgressPortId,
       "cwspConnTraceEgressVpi": cwspConnTraceEgressVpi,
       "cwspConnTraceEgressVci": cwspConnTraceEgressVci,
       "cwspConnTraceEgressCallRef": cwspConnTraceEgressCallRef,
       "cwspConnTraceEgressPhyPortId": cwspConnTraceEgressPhyPortId,
       "cwspConnTraceLastNode": cwspConnTraceLastNode,
       "cwspOperation": cwspOperation,
       "cwspOperationTable": cwspOperationTable,
       "cwspOperationEntry": cwspOperationEntry,
       "cwspOperIlmiEnable": cwspOperIlmiEnable,
       "cwspOperIfcType": cwspOperIfcType,
       "cwspOperIfcSide": cwspOperIfcSide,
       "cwspOperMaxVPCs": cwspOperMaxVPCs,
       "cwspOperMaxVCCs": cwspOperMaxVCCs,
       "cwspOperMaxVpiBits": cwspOperMaxVpiBits,
       "cwspOperMaxVciBits": cwspOperMaxVciBits,
       "cwspOperUniType": cwspOperUniType,
       "cwspOperUniVersion": cwspOperUniVersion,
       "cwspOperDeviceType": cwspOperDeviceType,
       "cwspOperIlmiVersion": cwspOperIlmiVersion,
       "cwspOperNniSigVersion": cwspOperNniSigVersion,
       "cwspOperMaxSvpcVpi": cwspOperMaxSvpcVpi,
       "cwspOperMinSvpcVpi": cwspOperMinSvpcVpi,
       "cwspOperMaxSvccVpi": cwspOperMaxSvccVpi,
       "cwspOperMinSvccVpi": cwspOperMinSvccVpi,
       "cwspOperMaxSvccVci": cwspOperMaxSvccVci,
       "cwspOperMinSvccVci": cwspOperMinSvccVci,
       "cwspOperAddrPlanSupported": cwspOperAddrPlanSupported,
       "cwspOperFailReason": cwspOperFailReason,
       "ciscoWANPnniRouting": ciscoWANPnniRouting,
       "ciscoWANPnniLinkStatus": ciscoWANPnniLinkStatus,
       "ciscoWANPnniPglStatus": ciscoWANPnniPglStatus,
       "ciscoWANPnniReachability": ciscoWANPnniReachability,
       "ciscoWANPnniRemoteNodeId": ciscoWANPnniRemoteNodeId,
       "ciscoWANPnniPortId": ciscoWANPnniPortId,
       "ciscoWANSpvc": ciscoWANSpvc,
       "ciscoWANSpvcFailReason": ciscoWANSpvcFailReason,
       "cwspSpvcNodePrefix": cwspSpvcNodePrefix,
       "ciscoWANSvcMIBConformance": ciscoWANSvcMIBConformance,
       "ciscoWANSvcMIBCompliances": ciscoWANSvcMIBCompliances,
       "ciscoWANSvcMIBCompliance": ciscoWANSvcMIBCompliance,
       "ciscoWANSvcMIBCompliance2": ciscoWANSvcMIBCompliance2,
       "ciscoWANSvcMIBCompliance3": ciscoWANSvcMIBCompliance3,
       "ciscoWANSvcMIBGroups": ciscoWANSvcMIBGroups,
       "cwsInfoGrp": cwsInfoGrp,
       "cwspConfigGrp": cwspConfigGrp,
       "cwspCacConfigGrp": cwspCacConfigGrp,
       "cwspCallStatsGrp": cwspCallStatsGrp,
       "cwspSigStatsGrp": cwspSigStatsGrp,
       "cwspCallGrp": cwspCallGrp,
       "cwspAbrCallGrp": cwspAbrCallGrp,
       "cwspPrefixGrp": cwspPrefixGrp,
       "cwspLoadGrp": cwspLoadGrp,
       "cwspAddressGrp": cwspAddressGrp,
       "cwspSigConfigGrp": cwspSigConfigGrp,
       "cwspSscopConfigGrp": cwspSscopConfigGrp,
       "cwspSscopStatsGrp": cwspSscopStatsGrp,
       "cwspRegAddressGrp": cwspRegAddressGrp,
       "cwspRoutingGrp": cwspRoutingGrp,
       "cwspConnTraceGrp": cwspConnTraceGrp,
       "cwspOperationGrp": cwspOperationGrp,
       "cwspSpvcGrp": cwspSpvcGrp,
       "cwspConnTraceGrp2": cwspConnTraceGrp2,
       "cwspConfigGrp2": cwspConfigGrp2,
       "cwspConfigGrp3": cwspConfigGrp3}
)
