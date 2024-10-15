# SNMP MIB module (IBMIROCDIALOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMIROCDIALOUT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:56 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm2210_ObjectIdentity = ObjectIdentity
ibm2210 = _Ibm2210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 72)
)
_IbmIROC_ObjectIdentity = ObjectIdentity
ibmIROC = _IbmIROC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119)
)
_IbmIROCrouting_ObjectIdentity = ObjectIdentity
ibmIROCrouting = _IbmIROCrouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4)
)
_IbmIROCroutingDialOut_ObjectIdentity = ObjectIdentity
ibmIROCroutingDialOut = _IbmIROCroutingDialOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6)
)
_IbmDialOutTraps_ObjectIdentity = ObjectIdentity
ibmDialOutTraps = _IbmDialOutTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 0)
)
_IbmDialOutMIB_ObjectIdentity = ObjectIdentity
ibmDialOutMIB = _IbmDialOutMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1)
)
_IbmDialOutGeneral_ObjectIdentity = ObjectIdentity
ibmDialOutGeneral = _IbmDialOutGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 1)
)
_DialOutIfTable_Object = MibTable
dialOutIfTable = _DialOutIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2)
)
if mibBuilder.loadTexts:
    dialOutIfTable.setStatus("mandatory")
_DialOutIfEntry_Object = MibTableRow
dialOutIfEntry = _DialOutIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1)
)
dialOutIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dialOutIfEntry.setStatus("mandatory")


class _DialOutIfUserName_Type(DisplayString):
    """Custom type dialOutIfUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 253),
    )


_DialOutIfUserName_Type.__name__ = "DisplayString"
_DialOutIfUserName_Object = MibTableColumn
dialOutIfUserName = _DialOutIfUserName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 1),
    _DialOutIfUserName_Type()
)
dialOutIfUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutIfUserName.setStatus("mandatory")


class _DialOutIfTimeRemaining_Type(Integer32):
    """Custom type dialOutIfTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialOutIfTimeRemaining_Type.__name__ = "Integer32"
_DialOutIfTimeRemaining_Object = MibTableColumn
dialOutIfTimeRemaining = _DialOutIfTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 2),
    _DialOutIfTimeRemaining_Type()
)
dialOutIfTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutIfTimeRemaining.setStatus("mandatory")


class _DialOutIfInactivityTimer_Type(Integer32):
    """Custom type dialOutIfInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialOutIfInactivityTimer_Type.__name__ = "Integer32"
_DialOutIfInactivityTimer_Object = MibTableColumn
dialOutIfInactivityTimer = _DialOutIfInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 3),
    _DialOutIfInactivityTimer_Type()
)
dialOutIfInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutIfInactivityTimer.setStatus("mandatory")


class _DialOutIfDTRState_Type(Integer32):
    """Custom type dialOutIfDTRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noChange", 0),
          ("off", 2),
          ("on", 1))
    )


_DialOutIfDTRState_Type.__name__ = "Integer32"
_DialOutIfDTRState_Object = MibTableColumn
dialOutIfDTRState = _DialOutIfDTRState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 4),
    _DialOutIfDTRState_Type()
)
dialOutIfDTRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutIfDTRState.setStatus("mandatory")


class _DialOutIfProtocol_Type(Integer32):
    """Custom type dialOutIfProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hose", 2),
          ("telnet", 3),
          ("undefined", 1))
    )


_DialOutIfProtocol_Type.__name__ = "Integer32"
_DialOutIfProtocol_Object = MibTableColumn
dialOutIfProtocol = _DialOutIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 5),
    _DialOutIfProtocol_Type()
)
dialOutIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutIfProtocol.setStatus("mandatory")
_DialOutEnableComport_Type = TruthValue
_DialOutEnableComport_Object = MibTableColumn
dialOutEnableComport = _DialOutEnableComport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 6),
    _DialOutEnableComport_Type()
)
dialOutEnableComport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutEnableComport.setStatus("mandatory")
_DialOutSendBinary_Type = TruthValue
_DialOutSendBinary_Object = MibTableColumn
dialOutSendBinary = _DialOutSendBinary_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 7),
    _DialOutSendBinary_Type()
)
dialOutSendBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutSendBinary.setStatus("mandatory")
_DialOutSupressGoAhead_Type = TruthValue
_DialOutSupressGoAhead_Object = MibTableColumn
dialOutSupressGoAhead = _DialOutSupressGoAhead_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 8),
    _DialOutSupressGoAhead_Type()
)
dialOutSupressGoAhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutSupressGoAhead.setStatus("mandatory")
_DialOutDisableEcho_Type = TruthValue
_DialOutDisableEcho_Object = MibTableColumn
dialOutDisableEcho = _DialOutDisableEcho_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 9),
    _DialOutDisableEcho_Type()
)
dialOutDisableEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialOutDisableEcho.setStatus("mandatory")


class _DialOutPortName_Type(DisplayString):
    """Custom type dialOutPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DialOutPortName_Type.__name__ = "DisplayString"
_DialOutPortName_Object = MibTableColumn
dialOutPortName = _DialOutPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 10),
    _DialOutPortName_Type()
)
dialOutPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialOutPortName.setStatus("mandatory")
_IbmDialOutDomains_ObjectIdentity = ObjectIdentity
ibmDialOutDomains = _IbmDialOutDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 2)
)
_IbmDialOutConformance_ObjectIdentity = ObjectIdentity
ibmDialOutConformance = _IbmDialOutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3)
)
_DialOutCompliances_ObjectIdentity = ObjectIdentity
dialOutCompliances = _DialOutCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 1)
)
_DialOutCoreCompliance_ObjectIdentity = ObjectIdentity
dialOutCoreCompliance = _DialOutCoreCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 1, 1)
)
_DialOutGroups_ObjectIdentity = ObjectIdentity
dialOutGroups = _DialOutGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 2)
)
_DialOutIfGroup_ObjectIdentity = ObjectIdentity
dialOutIfGroup = _DialOutIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMIROCDIALOUT-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm2210": ibm2210,
       "ibmIROC": ibmIROC,
       "ibmIROCrouting": ibmIROCrouting,
       "ibmIROCroutingDialOut": ibmIROCroutingDialOut,
       "ibmDialOutTraps": ibmDialOutTraps,
       "ibmDialOutMIB": ibmDialOutMIB,
       "ibmDialOutGeneral": ibmDialOutGeneral,
       "dialOutIfTable": dialOutIfTable,
       "dialOutIfEntry": dialOutIfEntry,
       "dialOutIfUserName": dialOutIfUserName,
       "dialOutIfTimeRemaining": dialOutIfTimeRemaining,
       "dialOutIfInactivityTimer": dialOutIfInactivityTimer,
       "dialOutIfDTRState": dialOutIfDTRState,
       "dialOutIfProtocol": dialOutIfProtocol,
       "dialOutEnableComport": dialOutEnableComport,
       "dialOutSendBinary": dialOutSendBinary,
       "dialOutSupressGoAhead": dialOutSupressGoAhead,
       "dialOutDisableEcho": dialOutDisableEcho,
       "dialOutPortName": dialOutPortName,
       "ibmDialOutDomains": ibmDialOutDomains,
       "ibmDialOutConformance": ibmDialOutConformance,
       "dialOutCompliances": dialOutCompliances,
       "dialOutCoreCompliance": dialOutCoreCompliance,
       "dialOutGroups": dialOutGroups,
       "dialOutIfGroup": dialOutIfGroup}
)
