# SNMP MIB module (AISLCASYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AISLCASYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:20 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiSLCAsync = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 23)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSLCAsyncTable_Object = MibTable
aiSLCAsyncTable = _AiSLCAsyncTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1)
)
if mibBuilder.loadTexts:
    aiSLCAsyncTable.setStatus("current")
_AiSLCAsyncEntry_Object = MibTableRow
aiSLCAsyncEntry = _AiSLCAsyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1)
)
aiSLCAsyncEntry.setIndexNames(
    (0, "AISLCASYNC-MIB", "aislcasyLinkNumber"),
)
if mibBuilder.loadTexts:
    aiSLCAsyncEntry.setStatus("current")
_AislcasyLinkNumber_Type = PositiveInteger
_AislcasyLinkNumber_Object = MibTableColumn
aislcasyLinkNumber = _AislcasyLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 1),
    _AislcasyLinkNumber_Type()
)
aislcasyLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcasyLinkNumber.setStatus("current")


class _AislcasyApplication_Type(Integer32):
    """Custom type aislcasyApplication based on Integer32"""
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
        *(("callMenu", 4),
          ("destination", 2),
          ("directConnect", 3),
          ("login", 1))
    )


_AislcasyApplication_Type.__name__ = "Integer32"
_AislcasyApplication_Object = MibTableColumn
aislcasyApplication = _AislcasyApplication_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 2),
    _AislcasyApplication_Type()
)
aislcasyApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcasyApplication.setStatus("current")
_AislcasyDirectConnectAlias_Type = DisplayString
_AislcasyDirectConnectAlias_Object = MibTableColumn
aislcasyDirectConnectAlias = _AislcasyDirectConnectAlias_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 3),
    _AislcasyDirectConnectAlias_Type()
)
aislcasyDirectConnectAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcasyDirectConnectAlias.setStatus("current")


class _AislcasyXonInterval_Type(Integer32):
    """Custom type aislcasyXonInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AislcasyXonInterval_Type.__name__ = "Integer32"
_AislcasyXonInterval_Object = MibTableColumn
aislcasyXonInterval = _AislcasyXonInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 4),
    _AislcasyXonInterval_Type()
)
aislcasyXonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcasyXonInterval.setStatus("current")
if mibBuilder.loadTexts:
    aislcasyXonInterval.setUnits("seconds")
_AislcasyCallState_Type = DisplayString
_AislcasyCallState_Object = MibTableColumn
aislcasyCallState = _AislcasyCallState_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 5),
    _AislcasyCallState_Type()
)
aislcasyCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcasyCallState.setStatus("current")
_AislcasyMinimizeLatency_Type = TruthValue
_AislcasyMinimizeLatency_Object = MibTableColumn
aislcasyMinimizeLatency = _AislcasyMinimizeLatency_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 6),
    _AislcasyMinimizeLatency_Type()
)
aislcasyMinimizeLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcasyMinimizeLatency.setStatus("current")
_AiSLCAsyncConnOptTable_Object = MibTable
aiSLCAsyncConnOptTable = _AiSLCAsyncConnOptTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2)
)
if mibBuilder.loadTexts:
    aiSLCAsyncConnOptTable.setStatus("current")
_AiSLCAsyncConnOptEntry_Object = MibTableRow
aiSLCAsyncConnOptEntry = _AiSLCAsyncConnOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1)
)
aiSLCAsyncConnOptEntry.setIndexNames(
    (0, "AISLCASYNC-MIB", "aislcacoLinkNumber"),
)
if mibBuilder.loadTexts:
    aiSLCAsyncConnOptEntry.setStatus("current")
_AislcacoLinkNumber_Type = PositiveInteger
_AislcacoLinkNumber_Object = MibTableColumn
aislcacoLinkNumber = _AislcacoLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 1),
    _AislcacoLinkNumber_Type()
)
aislcacoLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcacoLinkNumber.setStatus("current")
_AislcacoOnActiveDSR_Type = TruthValue
_AislcacoOnActiveDSR_Object = MibTableColumn
aislcacoOnActiveDSR = _AislcacoOnActiveDSR_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 2),
    _AislcacoOnActiveDSR_Type()
)
aislcacoOnActiveDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcacoOnActiveDSR.setStatus("current")
_AislcacoOnActiveDCD_Type = TruthValue
_AislcacoOnActiveDCD_Object = MibTableColumn
aislcacoOnActiveDCD = _AislcacoOnActiveDCD_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 3),
    _AislcacoOnActiveDCD_Type()
)
aislcacoOnActiveDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcacoOnActiveDCD.setStatus("current")
_AislcacoOnIncomingChar_Type = TruthValue
_AislcacoOnIncomingChar_Object = MibTableColumn
aislcacoOnIncomingChar = _AislcacoOnIncomingChar_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 4),
    _AislcacoOnIncomingChar_Type()
)
aislcacoOnIncomingChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcacoOnIncomingChar.setStatus("current")
_AislcacoDirectConnect_Type = TruthValue
_AislcacoDirectConnect_Object = MibTableColumn
aislcacoDirectConnect = _AislcacoDirectConnect_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 5),
    _AislcacoDirectConnect_Type()
)
aislcacoDirectConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcacoDirectConnect.setStatus("current")


class _AislcacoRetryTimer_Type(Integer32):
    """Custom type aislcacoRetryTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AislcacoRetryTimer_Type.__name__ = "Integer32"
_AislcacoRetryTimer_Object = MibTableColumn
aislcacoRetryTimer = _AislcacoRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 6),
    _AislcacoRetryTimer_Type()
)
aislcacoRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcacoRetryTimer.setStatus("current")
if mibBuilder.loadTexts:
    aislcacoRetryTimer.setUnits("seconds")


class _AislcacoConnectString_Type(DisplayString):
    """Custom type aislcacoConnectString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcacoConnectString_Type.__name__ = "DisplayString"
_AislcacoConnectString_Object = MibTableColumn
aislcacoConnectString = _AislcacoConnectString_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 7),
    _AislcacoConnectString_Type()
)
aislcacoConnectString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcacoConnectString.setStatus("current")
_AiSLCAsyncDiscOptTable_Object = MibTable
aiSLCAsyncDiscOptTable = _AiSLCAsyncDiscOptTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3)
)
if mibBuilder.loadTexts:
    aiSLCAsyncDiscOptTable.setStatus("current")
_AiSLCAsyncDiscOptEntry_Object = MibTableRow
aiSLCAsyncDiscOptEntry = _AiSLCAsyncDiscOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1)
)
aiSLCAsyncDiscOptEntry.setIndexNames(
    (0, "AISLCASYNC-MIB", "aislcadoLinkNumber"),
)
if mibBuilder.loadTexts:
    aiSLCAsyncDiscOptEntry.setStatus("current")
_AislcadoLinkNumber_Type = PositiveInteger
_AislcadoLinkNumber_Object = MibTableColumn
aislcadoLinkNumber = _AislcadoLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 1),
    _AislcadoLinkNumber_Type()
)
aislcadoLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcadoLinkNumber.setStatus("current")
_AislcadoOnLostDSR_Type = TruthValue
_AislcadoOnLostDSR_Object = MibTableColumn
aislcadoOnLostDSR = _AislcadoOnLostDSR_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 2),
    _AislcadoOnLostDSR_Type()
)
aislcadoOnLostDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcadoOnLostDSR.setStatus("current")
_AislcadoOnLostDCD_Type = TruthValue
_AislcadoOnLostDCD_Object = MibTableColumn
aislcadoOnLostDCD = _AislcadoOnLostDCD_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 3),
    _AislcadoOnLostDCD_Type()
)
aislcadoOnLostDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcadoOnLostDCD.setStatus("current")
_AislcadoOnBreak_Type = TruthValue
_AislcadoOnBreak_Object = MibTableColumn
aislcadoOnBreak = _AislcadoOnBreak_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 4),
    _AislcadoOnBreak_Type()
)
aislcadoOnBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcadoOnBreak.setStatus("current")


class _AislcadoInactivityTimer_Type(Integer32):
    """Custom type aislcadoInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AislcadoInactivityTimer_Type.__name__ = "Integer32"
_AislcadoInactivityTimer_Object = MibTableColumn
aislcadoInactivityTimer = _AislcadoInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 5),
    _AislcadoInactivityTimer_Type()
)
aislcadoInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcadoInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    aislcadoInactivityTimer.setUnits("seconds")


class _AislcadoDisconnectString_Type(DisplayString):
    """Custom type aislcadoDisconnectString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcadoDisconnectString_Type.__name__ = "DisplayString"
_AislcadoDisconnectString_Object = MibTableColumn
aislcadoDisconnectString = _AislcadoDisconnectString_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 6),
    _AislcadoDisconnectString_Type()
)
aislcadoDisconnectString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcadoDisconnectString.setStatus("current")
_AislcadoInactivityReceive_Type = TruthValue
_AislcadoInactivityReceive_Object = MibTableColumn
aislcadoInactivityReceive = _AislcadoInactivityReceive_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 7),
    _AislcadoInactivityReceive_Type()
)
aislcadoInactivityReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcadoInactivityReceive.setStatus("current")
_AiSLCAsyncModemOptTable_Object = MibTable
aiSLCAsyncModemOptTable = _AiSLCAsyncModemOptTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4)
)
if mibBuilder.loadTexts:
    aiSLCAsyncModemOptTable.setStatus("current")
_AiSLCAsyncModemOptEntry_Object = MibTableRow
aiSLCAsyncModemOptEntry = _AiSLCAsyncModemOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1)
)
aiSLCAsyncModemOptEntry.setIndexNames(
    (0, "AISLCASYNC-MIB", "aislcmdmLinkNumber"),
)
if mibBuilder.loadTexts:
    aiSLCAsyncModemOptEntry.setStatus("current")
_AislcmdmLinkNumber_Type = PositiveInteger
_AislcmdmLinkNumber_Object = MibTableColumn
aislcmdmLinkNumber = _AislcmdmLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 1),
    _AislcmdmLinkNumber_Type()
)
aislcmdmLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aislcmdmLinkNumber.setStatus("current")


class _AislcmdmInitString_Type(DisplayString):
    """Custom type aislcmdmInitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcmdmInitString_Type.__name__ = "DisplayString"
_AislcmdmInitString_Object = MibTableColumn
aislcmdmInitString = _AislcmdmInitString_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 2),
    _AislcmdmInitString_Type()
)
aislcmdmInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmInitString.setStatus("current")


class _AislcmdmTermString_Type(DisplayString):
    """Custom type aislcmdmTermString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AislcmdmTermString_Type.__name__ = "DisplayString"
_AislcmdmTermString_Object = MibTableColumn
aislcmdmTermString = _AislcmdmTermString_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 3),
    _AislcmdmTermString_Type()
)
aislcmdmTermString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmTermString.setStatus("current")


class _AislcmdmTimeToConnect_Type(Integer32):
    """Custom type aislcmdmTimeToConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_AislcmdmTimeToConnect_Type.__name__ = "Integer32"
_AislcmdmTimeToConnect_Object = MibTableColumn
aislcmdmTimeToConnect = _AislcmdmTimeToConnect_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 4),
    _AislcmdmTimeToConnect_Type()
)
aislcmdmTimeToConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmTimeToConnect.setStatus("current")
if mibBuilder.loadTexts:
    aislcmdmTimeToConnect.setUnits("seconds")


class _AislcmdmMaxDialAttempts_Type(Integer32):
    """Custom type aislcmdmMaxDialAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AislcmdmMaxDialAttempts_Type.__name__ = "Integer32"
_AislcmdmMaxDialAttempts_Object = MibTableColumn
aislcmdmMaxDialAttempts = _AislcmdmMaxDialAttempts_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 5),
    _AislcmdmMaxDialAttempts_Type()
)
aislcmdmMaxDialAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmMaxDialAttempts.setStatus("current")


class _AislcmdmDtrConnState_Type(Integer32):
    """Custom type aislcmdmDtrConnState based on Integer32"""
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


_AislcmdmDtrConnState_Type.__name__ = "Integer32"
_AislcmdmDtrConnState_Object = MibTableColumn
aislcmdmDtrConnState = _AislcmdmDtrConnState_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 6),
    _AislcmdmDtrConnState_Type()
)
aislcmdmDtrConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmDtrConnState.setStatus("current")


class _AislcmdmDtrDconnState_Type(Integer32):
    """Custom type aislcmdmDtrDconnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("toggle", 3))
    )


_AislcmdmDtrDconnState_Type.__name__ = "Integer32"
_AislcmdmDtrDconnState_Object = MibTableColumn
aislcmdmDtrDconnState = _AislcmdmDtrDconnState_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 7),
    _AislcmdmDtrDconnState_Type()
)
aislcmdmDtrDconnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmDtrDconnState.setStatus("current")


class _AislcmdmRtsConnState_Type(Integer32):
    """Custom type aislcmdmRtsConnState based on Integer32"""
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
        *(("bidirectionalFlowControl", 5),
          ("followsDSR", 3),
          ("followsData", 6),
          ("off", 2),
          ("on", 1),
          ("xmitFlowControl", 4))
    )


_AislcmdmRtsConnState_Type.__name__ = "Integer32"
_AislcmdmRtsConnState_Object = MibTableColumn
aislcmdmRtsConnState = _AislcmdmRtsConnState_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 8),
    _AislcmdmRtsConnState_Type()
)
aislcmdmRtsConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmRtsConnState.setStatus("current")


class _AislcmdmRtsDconnState_Type(Integer32):
    """Custom type aislcmdmRtsDconnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("toggle", 3))
    )


_AislcmdmRtsDconnState_Type.__name__ = "Integer32"
_AislcmdmRtsDconnState_Object = MibTableColumn
aislcmdmRtsDconnState = _AislcmdmRtsDconnState_Object(
    (1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 9),
    _AislcmdmRtsDconnState_Type()
)
aislcmdmRtsDconnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aislcmdmRtsDconnState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AISLCASYNC-MIB",
    **{"PositiveInteger": PositiveInteger,
       "aii": aii,
       "aiSLCAsync": aiSLCAsync,
       "aiSLCAsyncTable": aiSLCAsyncTable,
       "aiSLCAsyncEntry": aiSLCAsyncEntry,
       "aislcasyLinkNumber": aislcasyLinkNumber,
       "aislcasyApplication": aislcasyApplication,
       "aislcasyDirectConnectAlias": aislcasyDirectConnectAlias,
       "aislcasyXonInterval": aislcasyXonInterval,
       "aislcasyCallState": aislcasyCallState,
       "aislcasyMinimizeLatency": aislcasyMinimizeLatency,
       "aiSLCAsyncConnOptTable": aiSLCAsyncConnOptTable,
       "aiSLCAsyncConnOptEntry": aiSLCAsyncConnOptEntry,
       "aislcacoLinkNumber": aislcacoLinkNumber,
       "aislcacoOnActiveDSR": aislcacoOnActiveDSR,
       "aislcacoOnActiveDCD": aislcacoOnActiveDCD,
       "aislcacoOnIncomingChar": aislcacoOnIncomingChar,
       "aislcacoDirectConnect": aislcacoDirectConnect,
       "aislcacoRetryTimer": aislcacoRetryTimer,
       "aislcacoConnectString": aislcacoConnectString,
       "aiSLCAsyncDiscOptTable": aiSLCAsyncDiscOptTable,
       "aiSLCAsyncDiscOptEntry": aiSLCAsyncDiscOptEntry,
       "aislcadoLinkNumber": aislcadoLinkNumber,
       "aislcadoOnLostDSR": aislcadoOnLostDSR,
       "aislcadoOnLostDCD": aislcadoOnLostDCD,
       "aislcadoOnBreak": aislcadoOnBreak,
       "aislcadoInactivityTimer": aislcadoInactivityTimer,
       "aislcadoDisconnectString": aislcadoDisconnectString,
       "aislcadoInactivityReceive": aislcadoInactivityReceive,
       "aiSLCAsyncModemOptTable": aiSLCAsyncModemOptTable,
       "aiSLCAsyncModemOptEntry": aiSLCAsyncModemOptEntry,
       "aislcmdmLinkNumber": aislcmdmLinkNumber,
       "aislcmdmInitString": aislcmdmInitString,
       "aislcmdmTermString": aislcmdmTermString,
       "aislcmdmTimeToConnect": aislcmdmTimeToConnect,
       "aislcmdmMaxDialAttempts": aislcmdmMaxDialAttempts,
       "aislcmdmDtrConnState": aislcmdmDtrConnState,
       "aislcmdmDtrDconnState": aislcmdmDtrDconnState,
       "aislcmdmRtsConnState": aislcmdmRtsConnState,
       "aislcmdmRtsDconnState": aislcmdmRtsDconnState}
)
