# SNMP MIB module (ORALISTENER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORALISTENER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:39 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oracle_ObjectIdentity = ObjectIdentity
oracle = _Oracle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111)
)
_OraListenerMIB_ObjectIdentity = ObjectIdentity
oraListenerMIB = _OraListenerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 5)
)
_OraListenerObjects_ObjectIdentity = ObjectIdentity
oraListenerObjects = _OraListenerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 5, 1)
)
_OraListenerTable_Object = MibTable
oraListenerTable = _OraListenerTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1)
)
if mibBuilder.loadTexts:
    oraListenerTable.setStatus("mandatory")
_OraListenerEntry_Object = MibTableRow
oraListenerEntry = _OraListenerEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1)
)
oraListenerEntry.setIndexNames(
    (0, "ORALISTENER-MIB", "oraListenerIndex"),
)
if mibBuilder.loadTexts:
    oraListenerEntry.setStatus("mandatory")
_OraListenerIndex_Type = Integer32
_OraListenerIndex_Object = MibTableColumn
oraListenerIndex = _OraListenerIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 1),
    _OraListenerIndex_Type()
)
oraListenerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerIndex.setStatus("mandatory")
_OraListenerName_Type = DisplayString
_OraListenerName_Object = MibTableColumn
oraListenerName = _OraListenerName_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 2),
    _OraListenerName_Type()
)
oraListenerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerName.setStatus("mandatory")
_OraListenerVersion_Type = DisplayString
_OraListenerVersion_Object = MibTableColumn
oraListenerVersion = _OraListenerVersion_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 3),
    _OraListenerVersion_Type()
)
oraListenerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerVersion.setStatus("mandatory")
_OraListenerStartDate_Type = DisplayString
_OraListenerStartDate_Object = MibTableColumn
oraListenerStartDate = _OraListenerStartDate_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 4),
    _OraListenerStartDate_Type()
)
oraListenerStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerStartDate.setStatus("mandatory")
_OraListenerUptime_Type = TimeTicks
_OraListenerUptime_Object = MibTableColumn
oraListenerUptime = _OraListenerUptime_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 5),
    _OraListenerUptime_Type()
)
oraListenerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerUptime.setStatus("mandatory")


class _OraListenerTraceLevel_Type(Integer32):
    """Custom type oraListenerTraceLevel based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("admin", 6),
          ("level1", 1),
          ("level10", 10),
          ("level11", 11),
          ("level12", 12),
          ("level13", 13),
          ("level14", 14),
          ("level15", 15),
          ("level16", 16),
          ("level2", 2),
          ("level3", 3),
          ("level5", 5),
          ("level7", 7),
          ("level8", 8),
          ("level9", 9),
          ("off", 17),
          ("user", 4))
    )


_OraListenerTraceLevel_Type.__name__ = "Integer32"
_OraListenerTraceLevel_Object = MibTableColumn
oraListenerTraceLevel = _OraListenerTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 6),
    _OraListenerTraceLevel_Type()
)
oraListenerTraceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerTraceLevel.setStatus("mandatory")


class _OraListenerSecurityLevel_Type(Integer32):
    """Custom type oraListenerSecurityLevel based on Integer32"""
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


_OraListenerSecurityLevel_Type.__name__ = "Integer32"
_OraListenerSecurityLevel_Object = MibTableColumn
oraListenerSecurityLevel = _OraListenerSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 7),
    _OraListenerSecurityLevel_Type()
)
oraListenerSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerSecurityLevel.setStatus("mandatory")
_OraListenerParameterFile_Type = DisplayString
_OraListenerParameterFile_Object = MibTableColumn
oraListenerParameterFile = _OraListenerParameterFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 8),
    _OraListenerParameterFile_Type()
)
oraListenerParameterFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerParameterFile.setStatus("mandatory")
_OraListenerLogFile_Type = DisplayString
_OraListenerLogFile_Object = MibTableColumn
oraListenerLogFile = _OraListenerLogFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 9),
    _OraListenerLogFile_Type()
)
oraListenerLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerLogFile.setStatus("mandatory")
_OraListenerTraceFile_Type = DisplayString
_OraListenerTraceFile_Object = MibTableColumn
oraListenerTraceFile = _OraListenerTraceFile_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 10),
    _OraListenerTraceFile_Type()
)
oraListenerTraceFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerTraceFile.setStatus("mandatory")


class _OraListenerState_Type(Integer32):
    """Custom type oraListenerState based on Integer32"""
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


_OraListenerState_Type.__name__ = "Integer32"
_OraListenerState_Object = MibTableColumn
oraListenerState = _OraListenerState_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 11),
    _OraListenerState_Type()
)
oraListenerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerState.setStatus("mandatory")
_OraListenerNumberOfServices_Type = Integer32
_OraListenerNumberOfServices_Object = MibTableColumn
oraListenerNumberOfServices = _OraListenerNumberOfServices_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 12),
    _OraListenerNumberOfServices_Type()
)
oraListenerNumberOfServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenerNumberOfServices.setStatus("mandatory")
_OraListenerContact_Type = DisplayString
_OraListenerContact_Object = MibTableColumn
oraListenerContact = _OraListenerContact_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 1, 1, 13),
    _OraListenerContact_Type()
)
oraListenerContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oraListenerContact.setStatus("mandatory")
_OraDedicatedSrvTable_Object = MibTable
oraDedicatedSrvTable = _OraDedicatedSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 2)
)
if mibBuilder.loadTexts:
    oraDedicatedSrvTable.setStatus("mandatory")
_OraDedicatedSrvEntry_Object = MibTableRow
oraDedicatedSrvEntry = _OraDedicatedSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 2, 1)
)
oraDedicatedSrvEntry.setIndexNames(
    (0, "ORALISTENER-MIB", "oraSIDName"),
    (0, "ORALISTENER-MIB", "oraDedicatedSrvIndex"),
)
if mibBuilder.loadTexts:
    oraDedicatedSrvEntry.setStatus("mandatory")
_OraDedicatedSrvIndex_Type = Integer32
_OraDedicatedSrvIndex_Object = MibTableColumn
oraDedicatedSrvIndex = _OraDedicatedSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 2, 1, 1),
    _OraDedicatedSrvIndex_Type()
)
oraDedicatedSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDedicatedSrvIndex.setStatus("mandatory")
_OraDedicatedSrvEstablishedConnections_Type = Counter32
_OraDedicatedSrvEstablishedConnections_Object = MibTableColumn
oraDedicatedSrvEstablishedConnections = _OraDedicatedSrvEstablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 2, 1, 2),
    _OraDedicatedSrvEstablishedConnections_Type()
)
oraDedicatedSrvEstablishedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDedicatedSrvEstablishedConnections.setStatus("mandatory")
_OraDedicatedSrvRejectedConnections_Type = Counter32
_OraDedicatedSrvRejectedConnections_Object = MibTableColumn
oraDedicatedSrvRejectedConnections = _OraDedicatedSrvRejectedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 2, 1, 3),
    _OraDedicatedSrvRejectedConnections_Type()
)
oraDedicatedSrvRejectedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDedicatedSrvRejectedConnections.setStatus("mandatory")
_OraDispatcherTable_Object = MibTable
oraDispatcherTable = _OraDispatcherTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3)
)
if mibBuilder.loadTexts:
    oraDispatcherTable.setStatus("mandatory")
_OraDispatcherEntry_Object = MibTableRow
oraDispatcherEntry = _OraDispatcherEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1)
)
oraDispatcherEntry.setIndexNames(
    (0, "ORALISTENER-MIB", "oraSIDName"),
    (0, "ORALISTENER-MIB", "oraDispatcherIndex"),
)
if mibBuilder.loadTexts:
    oraDispatcherEntry.setStatus("mandatory")
_OraDispatcherIndex_Type = Integer32
_OraDispatcherIndex_Object = MibTableColumn
oraDispatcherIndex = _OraDispatcherIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 1),
    _OraDispatcherIndex_Type()
)
oraDispatcherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherIndex.setStatus("mandatory")
_OraDispatcherEstablishedConnections_Type = Counter32
_OraDispatcherEstablishedConnections_Object = MibTableColumn
oraDispatcherEstablishedConnections = _OraDispatcherEstablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 2),
    _OraDispatcherEstablishedConnections_Type()
)
oraDispatcherEstablishedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherEstablishedConnections.setStatus("mandatory")
_OraDispatcherRejectedConnections_Type = Counter32
_OraDispatcherRejectedConnections_Object = MibTableColumn
oraDispatcherRejectedConnections = _OraDispatcherRejectedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 3),
    _OraDispatcherRejectedConnections_Type()
)
oraDispatcherRejectedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherRejectedConnections.setStatus("mandatory")
_OraDispatcherCurrentConnections_Type = Gauge32
_OraDispatcherCurrentConnections_Object = MibTableColumn
oraDispatcherCurrentConnections = _OraDispatcherCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 4),
    _OraDispatcherCurrentConnections_Type()
)
oraDispatcherCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherCurrentConnections.setStatus("mandatory")
_OraDispatcherMaximumConnections_Type = Integer32
_OraDispatcherMaximumConnections_Object = MibTableColumn
oraDispatcherMaximumConnections = _OraDispatcherMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 5),
    _OraDispatcherMaximumConnections_Type()
)
oraDispatcherMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherMaximumConnections.setStatus("mandatory")


class _OraDispatcherState_Type(Integer32):
    """Custom type oraDispatcherState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("ready", 2))
    )


_OraDispatcherState_Type.__name__ = "Integer32"
_OraDispatcherState_Object = MibTableColumn
oraDispatcherState = _OraDispatcherState_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 6),
    _OraDispatcherState_Type()
)
oraDispatcherState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherState.setStatus("mandatory")
_OraDispatcherProtocolInfo_Type = DisplayString
_OraDispatcherProtocolInfo_Object = MibTableColumn
oraDispatcherProtocolInfo = _OraDispatcherProtocolInfo_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 3, 1, 7),
    _OraDispatcherProtocolInfo_Type()
)
oraDispatcherProtocolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraDispatcherProtocolInfo.setStatus("mandatory")
_OraPrespawnedSrvTable_Object = MibTable
oraPrespawnedSrvTable = _OraPrespawnedSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4)
)
if mibBuilder.loadTexts:
    oraPrespawnedSrvTable.setStatus("mandatory")
_OraPrespawnedSrvEntry_Object = MibTableRow
oraPrespawnedSrvEntry = _OraPrespawnedSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1)
)
oraPrespawnedSrvEntry.setIndexNames(
    (0, "ORALISTENER-MIB", "oraSIDName"),
    (0, "ORALISTENER-MIB", "oraPrespawnedSrvIndex"),
)
if mibBuilder.loadTexts:
    oraPrespawnedSrvEntry.setStatus("mandatory")
_OraPrespawnedSrvIndex_Type = Integer32
_OraPrespawnedSrvIndex_Object = MibTableColumn
oraPrespawnedSrvIndex = _OraPrespawnedSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 1),
    _OraPrespawnedSrvIndex_Type()
)
oraPrespawnedSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvIndex.setStatus("mandatory")
_OraPrespawnedSrvEstablishedConnections_Type = Counter32
_OraPrespawnedSrvEstablishedConnections_Object = MibTableColumn
oraPrespawnedSrvEstablishedConnections = _OraPrespawnedSrvEstablishedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 2),
    _OraPrespawnedSrvEstablishedConnections_Type()
)
oraPrespawnedSrvEstablishedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvEstablishedConnections.setStatus("mandatory")
_OraPrespawnedSrvRejectedConnections_Type = Counter32
_OraPrespawnedSrvRejectedConnections_Object = MibTableColumn
oraPrespawnedSrvRejectedConnections = _OraPrespawnedSrvRejectedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 3),
    _OraPrespawnedSrvRejectedConnections_Type()
)
oraPrespawnedSrvRejectedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvRejectedConnections.setStatus("mandatory")
_OraPrespawnedSrvCurrentConnections_Type = Gauge32
_OraPrespawnedSrvCurrentConnections_Object = MibTableColumn
oraPrespawnedSrvCurrentConnections = _OraPrespawnedSrvCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 4),
    _OraPrespawnedSrvCurrentConnections_Type()
)
oraPrespawnedSrvCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvCurrentConnections.setStatus("mandatory")
_OraPrespawnedSrvMaximumConnections_Type = Integer32
_OraPrespawnedSrvMaximumConnections_Object = MibTableColumn
oraPrespawnedSrvMaximumConnections = _OraPrespawnedSrvMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 5),
    _OraPrespawnedSrvMaximumConnections_Type()
)
oraPrespawnedSrvMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvMaximumConnections.setStatus("mandatory")


class _OraPrespawnedSrvState_Type(Integer32):
    """Custom type oraPrespawnedSrvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("ready", 2))
    )


_OraPrespawnedSrvState_Type.__name__ = "Integer32"
_OraPrespawnedSrvState_Object = MibTableColumn
oraPrespawnedSrvState = _OraPrespawnedSrvState_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 6),
    _OraPrespawnedSrvState_Type()
)
oraPrespawnedSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvState.setStatus("mandatory")
_OraPrespawnedSrvProtocolInfo_Type = DisplayString
_OraPrespawnedSrvProtocolInfo_Object = MibTableColumn
oraPrespawnedSrvProtocolInfo = _OraPrespawnedSrvProtocolInfo_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 7),
    _OraPrespawnedSrvProtocolInfo_Type()
)
oraPrespawnedSrvProtocolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvProtocolInfo.setStatus("mandatory")
_OraPrespawnedSrvProcessorID_Type = DisplayString
_OraPrespawnedSrvProcessorID_Object = MibTableColumn
oraPrespawnedSrvProcessorID = _OraPrespawnedSrvProcessorID_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 4, 1, 8),
    _OraPrespawnedSrvProcessorID_Type()
)
oraPrespawnedSrvProcessorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraPrespawnedSrvProcessorID.setStatus("mandatory")
_OraSIDTable_Object = MibTable
oraSIDTable = _OraSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 5)
)
if mibBuilder.loadTexts:
    oraSIDTable.setStatus("mandatory")
_OraSIDEntry_Object = MibTableRow
oraSIDEntry = _OraSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 5, 1)
)
oraSIDEntry.setIndexNames(
    (0, "ORALISTENER-MIB", "oraSIDName"),
)
if mibBuilder.loadTexts:
    oraSIDEntry.setStatus("mandatory")
_OraSIDListenerIndex_Type = Integer32
_OraSIDListenerIndex_Object = MibTableColumn
oraSIDListenerIndex = _OraSIDListenerIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 5, 1, 1),
    _OraSIDListenerIndex_Type()
)
oraSIDListenerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraSIDListenerIndex.setStatus("mandatory")
_OraSIDName_Type = DisplayString
_OraSIDName_Object = MibTableColumn
oraSIDName = _OraSIDName_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 5, 1, 2),
    _OraSIDName_Type()
)
oraSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraSIDName.setStatus("mandatory")
_OraSIDCurrentConnectedClients_Type = Gauge32
_OraSIDCurrentConnectedClients_Object = MibTableColumn
oraSIDCurrentConnectedClients = _OraSIDCurrentConnectedClients_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 5, 1, 3),
    _OraSIDCurrentConnectedClients_Type()
)
oraSIDCurrentConnectedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraSIDCurrentConnectedClients.setStatus("mandatory")
_OraSIDReservedConnections_Type = Counter32
_OraSIDReservedConnections_Object = MibTableColumn
oraSIDReservedConnections = _OraSIDReservedConnections_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 5, 1, 4),
    _OraSIDReservedConnections_Type()
)
oraSIDReservedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraSIDReservedConnections.setStatus("mandatory")
_OraListenAddressTable_Object = MibTable
oraListenAddressTable = _OraListenAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 6)
)
if mibBuilder.loadTexts:
    oraListenAddressTable.setStatus("mandatory")
_OraListenAddressEntry_Object = MibTableRow
oraListenAddressEntry = _OraListenAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 6, 1)
)
oraListenAddressEntry.setIndexNames(
    (0, "ORALISTENER-MIB", "oraListenerIndex"),
    (0, "ORALISTENER-MIB", "oraListenAddressIndex"),
)
if mibBuilder.loadTexts:
    oraListenAddressEntry.setStatus("mandatory")
_OraListenAddressIndex_Type = Integer32
_OraListenAddressIndex_Object = MibTableColumn
oraListenAddressIndex = _OraListenAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 6, 1, 1),
    _OraListenAddressIndex_Type()
)
oraListenAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenAddressIndex.setStatus("mandatory")
_OraListenAddress_Type = DisplayString
_OraListenAddress_Object = MibTableColumn
oraListenAddress = _OraListenAddress_Object(
    (1, 3, 6, 1, 4, 1, 111, 5, 1, 6, 1, 2),
    _OraListenAddress_Type()
)
oraListenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraListenAddress.setStatus("mandatory")
_OraListenerTraps_ObjectIdentity = ObjectIdentity
oraListenerTraps = _OraListenerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 5, 2)
)

# Managed Objects groups


# Notification objects

oraListenerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 111, 5, 2, 0, 1)
)
oraListenerStateChange.setObjects(
    ("ORALISTENER-MIB", "oraListenerState")
)
if mibBuilder.loadTexts:
    oraListenerStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORALISTENER-MIB",
    **{"oracle": oracle,
       "oraListenerMIB": oraListenerMIB,
       "oraListenerObjects": oraListenerObjects,
       "oraListenerTable": oraListenerTable,
       "oraListenerEntry": oraListenerEntry,
       "oraListenerIndex": oraListenerIndex,
       "oraListenerName": oraListenerName,
       "oraListenerVersion": oraListenerVersion,
       "oraListenerStartDate": oraListenerStartDate,
       "oraListenerUptime": oraListenerUptime,
       "oraListenerTraceLevel": oraListenerTraceLevel,
       "oraListenerSecurityLevel": oraListenerSecurityLevel,
       "oraListenerParameterFile": oraListenerParameterFile,
       "oraListenerLogFile": oraListenerLogFile,
       "oraListenerTraceFile": oraListenerTraceFile,
       "oraListenerState": oraListenerState,
       "oraListenerNumberOfServices": oraListenerNumberOfServices,
       "oraListenerContact": oraListenerContact,
       "oraDedicatedSrvTable": oraDedicatedSrvTable,
       "oraDedicatedSrvEntry": oraDedicatedSrvEntry,
       "oraDedicatedSrvIndex": oraDedicatedSrvIndex,
       "oraDedicatedSrvEstablishedConnections": oraDedicatedSrvEstablishedConnections,
       "oraDedicatedSrvRejectedConnections": oraDedicatedSrvRejectedConnections,
       "oraDispatcherTable": oraDispatcherTable,
       "oraDispatcherEntry": oraDispatcherEntry,
       "oraDispatcherIndex": oraDispatcherIndex,
       "oraDispatcherEstablishedConnections": oraDispatcherEstablishedConnections,
       "oraDispatcherRejectedConnections": oraDispatcherRejectedConnections,
       "oraDispatcherCurrentConnections": oraDispatcherCurrentConnections,
       "oraDispatcherMaximumConnections": oraDispatcherMaximumConnections,
       "oraDispatcherState": oraDispatcherState,
       "oraDispatcherProtocolInfo": oraDispatcherProtocolInfo,
       "oraPrespawnedSrvTable": oraPrespawnedSrvTable,
       "oraPrespawnedSrvEntry": oraPrespawnedSrvEntry,
       "oraPrespawnedSrvIndex": oraPrespawnedSrvIndex,
       "oraPrespawnedSrvEstablishedConnections": oraPrespawnedSrvEstablishedConnections,
       "oraPrespawnedSrvRejectedConnections": oraPrespawnedSrvRejectedConnections,
       "oraPrespawnedSrvCurrentConnections": oraPrespawnedSrvCurrentConnections,
       "oraPrespawnedSrvMaximumConnections": oraPrespawnedSrvMaximumConnections,
       "oraPrespawnedSrvState": oraPrespawnedSrvState,
       "oraPrespawnedSrvProtocolInfo": oraPrespawnedSrvProtocolInfo,
       "oraPrespawnedSrvProcessorID": oraPrespawnedSrvProcessorID,
       "oraSIDTable": oraSIDTable,
       "oraSIDEntry": oraSIDEntry,
       "oraSIDListenerIndex": oraSIDListenerIndex,
       "oraSIDName": oraSIDName,
       "oraSIDCurrentConnectedClients": oraSIDCurrentConnectedClients,
       "oraSIDReservedConnections": oraSIDReservedConnections,
       "oraListenAddressTable": oraListenAddressTable,
       "oraListenAddressEntry": oraListenAddressEntry,
       "oraListenAddressIndex": oraListenAddressIndex,
       "oraListenAddress": oraListenAddress,
       "oraListenerTraps": oraListenerTraps,
       "oraListenerStateChange": oraListenerStateChange}
)
