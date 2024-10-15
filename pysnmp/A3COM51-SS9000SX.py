# SNMP MIB module (A3COM51-SS9000SX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM51-SS9000SX
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:24 2024
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

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_SuperStackSwitch9000SX_ObjectIdentity = ObjectIdentity
superStackSwitch9000SX = _SuperStackSwitch9000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 32)
)
_SuperStackSwitch3800_ObjectIdentity = ObjectIdentity
superStackSwitch3800 = _SuperStackSwitch3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 34)
)
_SuperStackSwitch9100_ObjectIdentity = ObjectIdentity
superStackSwitch9100 = _SuperStackSwitch9100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 36)
)
_SuperStackSwitch9000SX_mib_ObjectIdentity = ObjectIdentity
superStackSwitch9000SX_mib = _SuperStackSwitch9000SX_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 27)
)


class _Ss9000UnitPaceMode_Type(Integer32):
    """Custom type ss9000UnitPaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lowLatency", 3),
          ("normalEthernet", 2),
          ("notApplicable", 1))
    )


_Ss9000UnitPaceMode_Type.__name__ = "Integer32"
_Ss9000UnitPaceMode_Object = MibScalar
ss9000UnitPaceMode = _Ss9000UnitPaceMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 1),
    _Ss9000UnitPaceMode_Type()
)
ss9000UnitPaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss9000UnitPaceMode.setStatus("mandatory")
_Ss9000PortTable_Object = MibTable
ss9000PortTable = _Ss9000PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2)
)
if mibBuilder.loadTexts:
    ss9000PortTable.setStatus("mandatory")
_Ss9000PortTableEntry_Object = MibTableRow
ss9000PortTableEntry = _Ss9000PortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1)
)
ss9000PortTableEntry.setIndexNames(
    (0, "A3COM51-SS9000SX", "ss9000PortIndex"),
)
if mibBuilder.loadTexts:
    ss9000PortTableEntry.setStatus("mandatory")
_Ss9000PortIndex_Type = Integer32
_Ss9000PortIndex_Object = MibTableColumn
ss9000PortIndex = _Ss9000PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 1),
    _Ss9000PortIndex_Type()
)
ss9000PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortIndex.setStatus("mandatory")
_Ss9000PortRxPktCtLow_Type = Counter32
_Ss9000PortRxPktCtLow_Object = MibTableColumn
ss9000PortRxPktCtLow = _Ss9000PortRxPktCtLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 2),
    _Ss9000PortRxPktCtLow_Type()
)
ss9000PortRxPktCtLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortRxPktCtLow.setStatus("mandatory")
_Ss9000PortRxPktCtHigh_Type = Counter32
_Ss9000PortRxPktCtHigh_Object = MibTableColumn
ss9000PortRxPktCtHigh = _Ss9000PortRxPktCtHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 3),
    _Ss9000PortRxPktCtHigh_Type()
)
ss9000PortRxPktCtHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortRxPktCtHigh.setStatus("mandatory")
_Ss9000PortRxByteCtLow_Type = Counter32
_Ss9000PortRxByteCtLow_Object = MibTableColumn
ss9000PortRxByteCtLow = _Ss9000PortRxByteCtLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 4),
    _Ss9000PortRxByteCtLow_Type()
)
ss9000PortRxByteCtLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortRxByteCtLow.setStatus("mandatory")
_Ss9000PortRxByteCtHigh_Type = Counter32
_Ss9000PortRxByteCtHigh_Object = MibTableColumn
ss9000PortRxByteCtHigh = _Ss9000PortRxByteCtHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 5),
    _Ss9000PortRxByteCtHigh_Type()
)
ss9000PortRxByteCtHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortRxByteCtHigh.setStatus("mandatory")
_Ss9000PortTxPktCtLow_Type = Counter32
_Ss9000PortTxPktCtLow_Object = MibTableColumn
ss9000PortTxPktCtLow = _Ss9000PortTxPktCtLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 6),
    _Ss9000PortTxPktCtLow_Type()
)
ss9000PortTxPktCtLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortTxPktCtLow.setStatus("mandatory")
_Ss9000PortTxPktCtHigh_Type = Counter32
_Ss9000PortTxPktCtHigh_Object = MibTableColumn
ss9000PortTxPktCtHigh = _Ss9000PortTxPktCtHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 7),
    _Ss9000PortTxPktCtHigh_Type()
)
ss9000PortTxPktCtHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortTxPktCtHigh.setStatus("mandatory")
_Ss9000PortTxByteCtLow_Type = Counter32
_Ss9000PortTxByteCtLow_Object = MibTableColumn
ss9000PortTxByteCtLow = _Ss9000PortTxByteCtLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 8),
    _Ss9000PortTxByteCtLow_Type()
)
ss9000PortTxByteCtLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortTxByteCtLow.setStatus("mandatory")
_Ss9000PortTxByteCtHigh_Type = Counter32
_Ss9000PortTxByteCtHigh_Object = MibTableColumn
ss9000PortTxByteCtHigh = _Ss9000PortTxByteCtHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 2, 1, 9),
    _Ss9000PortTxByteCtHigh_Type()
)
ss9000PortTxByteCtHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000PortTxByteCtHigh.setStatus("mandatory")


class _Ss9000SaveConfiguration_Type(Integer32):
    """Custom type ss9000SaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveToPrimary", 1),
          ("saveToSecondary", 2))
    )


_Ss9000SaveConfiguration_Type.__name__ = "Integer32"
_Ss9000SaveConfiguration_Object = MibScalar
ss9000SaveConfiguration = _Ss9000SaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 3),
    _Ss9000SaveConfiguration_Type()
)
ss9000SaveConfiguration.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ss9000SaveConfiguration.setStatus("mandatory")


class _Ss9000SaveStatus_Type(Integer32):
    """Custom type ss9000SaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("saveInProgress", 1),
          ("saveNotInProgress", 2))
    )


_Ss9000SaveStatus_Type.__name__ = "Integer32"
_Ss9000SaveStatus_Object = MibScalar
ss9000SaveStatus = _Ss9000SaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 27, 4),
    _Ss9000SaveStatus_Type()
)
ss9000SaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss9000SaveStatus.setStatus("mandatory")
_Ss9000MauType_ObjectIdentity = ObjectIdentity
ss9000MauType = _Ss9000MauType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 27, 5)
)
_Ss9000MauType1000BaseSX_ObjectIdentity = ObjectIdentity
ss9000MauType1000BaseSX = _Ss9000MauType1000BaseSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 27, 5, 1)
)
_Extreme_ObjectIdentity = ObjectIdentity
extreme = _Extreme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916)
)

# Managed Objects groups


# Notification objects

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 1)
)
overheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

fanfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 2)
)
fanfailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanfailed.setStatus(
        ""
    )

fanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 3)
)
fanOK.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanOK.setStatus(
        ""
    )

invalidLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 0, 4)
)
invalidLoginAttempt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    invalidLoginAttempt.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM51-SS9000SX",
    **{"a3Com": a3Com,
       "products": products,
       "hub": hub,
       "superStackSwitch9000SX": superStackSwitch9000SX,
       "superStackSwitch3800": superStackSwitch3800,
       "superStackSwitch9100": superStackSwitch9100,
       "superStackSwitch9000SX-mib": superStackSwitch9000SX_mib,
       "ss9000UnitPaceMode": ss9000UnitPaceMode,
       "ss9000PortTable": ss9000PortTable,
       "ss9000PortTableEntry": ss9000PortTableEntry,
       "ss9000PortIndex": ss9000PortIndex,
       "ss9000PortRxPktCtLow": ss9000PortRxPktCtLow,
       "ss9000PortRxPktCtHigh": ss9000PortRxPktCtHigh,
       "ss9000PortRxByteCtLow": ss9000PortRxByteCtLow,
       "ss9000PortRxByteCtHigh": ss9000PortRxByteCtHigh,
       "ss9000PortTxPktCtLow": ss9000PortTxPktCtLow,
       "ss9000PortTxPktCtHigh": ss9000PortTxPktCtHigh,
       "ss9000PortTxByteCtLow": ss9000PortTxByteCtLow,
       "ss9000PortTxByteCtHigh": ss9000PortTxByteCtHigh,
       "ss9000SaveConfiguration": ss9000SaveConfiguration,
       "ss9000SaveStatus": ss9000SaveStatus,
       "ss9000MauType": ss9000MauType,
       "ss9000MauType1000BaseSX": ss9000MauType1000BaseSX,
       "extreme": extreme,
       "overheat": overheat,
       "fanfailed": fanfailed,
       "fanOK": fanOK,
       "invalidLoginAttempt": invalidLoginAttempt}
)
