# SNMP MIB module (JUNIPER-SUBSCRIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SUBSCRIBER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:17 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(jnxSubscriberMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxSubscriberMibRoot")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxSubscriberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1)
)
jnxSubscriberMIB.setRevisions(
        ("2010-05-11 00:00",
         "2012-05-02 00:00",
         "2013-12-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxSubscriberState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("configured", 1),
          ("init", 0),
          ("terminated", 4),
          ("terminating", 3),
          ("unknown", 5))
    )



class JnxSubscriberClientType(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxSubscriberObjects_ObjectIdentity = ObjectIdentity
jnxSubscriberObjects = _JnxSubscriberObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1)
)
_JnxSubscriberGeneral_ObjectIdentity = ObjectIdentity
jnxSubscriberGeneral = _JnxSubscriberGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1)
)
_JnxSubscriberTotalCount_Type = CounterBasedGauge64
_JnxSubscriberTotalCount_Object = MibScalar
jnxSubscriberTotalCount = _JnxSubscriberTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 1),
    _JnxSubscriberTotalCount_Type()
)
jnxSubscriberTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberTotalCount.setStatus("current")
_JnxSubscriberActiveCount_Type = CounterBasedGauge64
_JnxSubscriberActiveCount_Object = MibScalar
jnxSubscriberActiveCount = _JnxSubscriberActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 2),
    _JnxSubscriberActiveCount_Type()
)
jnxSubscriberActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberActiveCount.setStatus("current")
_JnxSubscriberTable_Object = MibTable
jnxSubscriberTable = _JnxSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxSubscriberTable.setStatus("current")
_JnxSubscriberEntry_Object = MibTableRow
jnxSubscriberEntry = _JnxSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1)
)
jnxSubscriberEntry.setIndexNames(
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberHandleHiWord"),
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberHandleLoWord"),
)
if mibBuilder.loadTexts:
    jnxSubscriberEntry.setStatus("current")


class _JnxSubscriberHandleHiWord_Type(Unsigned32):
    """Custom type jnxSubscriberHandleHiWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberHandleHiWord_Type.__name__ = "Unsigned32"
_JnxSubscriberHandleHiWord_Object = MibTableColumn
jnxSubscriberHandleHiWord = _JnxSubscriberHandleHiWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 1),
    _JnxSubscriberHandleHiWord_Type()
)
jnxSubscriberHandleHiWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberHandleHiWord.setStatus("current")


class _JnxSubscriberHandleLoWord_Type(Unsigned32):
    """Custom type jnxSubscriberHandleLoWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberHandleLoWord_Type.__name__ = "Unsigned32"
_JnxSubscriberHandleLoWord_Object = MibTableColumn
jnxSubscriberHandleLoWord = _JnxSubscriberHandleLoWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 2),
    _JnxSubscriberHandleLoWord_Type()
)
jnxSubscriberHandleLoWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberHandleLoWord.setStatus("current")
_JnxSubscriberUserName_Type = DisplayString
_JnxSubscriberUserName_Object = MibTableColumn
jnxSubscriberUserName = _JnxSubscriberUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 3),
    _JnxSubscriberUserName_Type()
)
jnxSubscriberUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberUserName.setStatus("current")
_JnxSubscriberClientType_Type = JnxSubscriberClientType
_JnxSubscriberClientType_Object = MibTableColumn
jnxSubscriberClientType = _JnxSubscriberClientType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 4),
    _JnxSubscriberClientType_Type()
)
jnxSubscriberClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberClientType.setStatus("current")
_JnxSubscriberIpAddress_Type = IpAddress
_JnxSubscriberIpAddress_Object = MibTableColumn
jnxSubscriberIpAddress = _JnxSubscriberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 5),
    _JnxSubscriberIpAddress_Type()
)
jnxSubscriberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberIpAddress.setStatus("current")
_JnxSubscriberIpAddressMask_Type = IpAddress
_JnxSubscriberIpAddressMask_Object = MibTableColumn
jnxSubscriberIpAddressMask = _JnxSubscriberIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 6),
    _JnxSubscriberIpAddressMask_Type()
)
jnxSubscriberIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberIpAddressMask.setStatus("current")


class _JnxSubscriberLogicalSystem_Type(OctetString):
    """Custom type jnxSubscriberLogicalSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxSubscriberLogicalSystem_Type.__name__ = "OctetString"
_JnxSubscriberLogicalSystem_Object = MibTableColumn
jnxSubscriberLogicalSystem = _JnxSubscriberLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 7),
    _JnxSubscriberLogicalSystem_Type()
)
jnxSubscriberLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystem.setStatus("current")


class _JnxSubscriberRoutingInstance_Type(OctetString):
    """Custom type jnxSubscriberRoutingInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxSubscriberRoutingInstance_Type.__name__ = "OctetString"
_JnxSubscriberRoutingInstance_Object = MibTableColumn
jnxSubscriberRoutingInstance = _JnxSubscriberRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 8),
    _JnxSubscriberRoutingInstance_Type()
)
jnxSubscriberRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstance.setStatus("current")
_JnxSubscriberInterface_Type = DisplayString
_JnxSubscriberInterface_Object = MibTableColumn
jnxSubscriberInterface = _JnxSubscriberInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 9),
    _JnxSubscriberInterface_Type()
)
jnxSubscriberInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberInterface.setStatus("current")


class _JnxSubscriberInterfaceType_Type(Integer32):
    """Custom type jnxSubscriberInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("none", 0),
          ("static", 1))
    )


_JnxSubscriberInterfaceType_Type.__name__ = "Integer32"
_JnxSubscriberInterfaceType_Object = MibTableColumn
jnxSubscriberInterfaceType = _JnxSubscriberInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 10),
    _JnxSubscriberInterfaceType_Type()
)
jnxSubscriberInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberInterfaceType.setStatus("current")
_JnxSubscriberMacAddress_Type = MacAddress
_JnxSubscriberMacAddress_Object = MibTableColumn
jnxSubscriberMacAddress = _JnxSubscriberMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 11),
    _JnxSubscriberMacAddress_Type()
)
jnxSubscriberMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberMacAddress.setStatus("current")
_JnxSubscriberState_Type = JnxSubscriberState
_JnxSubscriberState_Object = MibTableColumn
jnxSubscriberState = _JnxSubscriberState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 12),
    _JnxSubscriberState_Type()
)
jnxSubscriberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberState.setStatus("current")
_JnxSubscriberLoginTime_Type = DisplayString
_JnxSubscriberLoginTime_Object = MibTableColumn
jnxSubscriberLoginTime = _JnxSubscriberLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 13),
    _JnxSubscriberLoginTime_Type()
)
jnxSubscriberLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberLoginTime.setStatus("current")
_JnxSubscriberAcctSessionId_Type = DisplayString
_JnxSubscriberAcctSessionId_Object = MibTableColumn
jnxSubscriberAcctSessionId = _JnxSubscriberAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 3, 1, 14),
    _JnxSubscriberAcctSessionId_Type()
)
jnxSubscriberAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAcctSessionId.setStatus("current")
_JnxSubscriberInterfaceHardwareIndexTable_Object = MibTable
jnxSubscriberInterfaceHardwareIndexTable = _JnxSubscriberInterfaceHardwareIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxSubscriberInterfaceHardwareIndexTable.setStatus("current")
_JnxSubscriberInterfaceHardwareIndexEntry_Object = MibTableRow
jnxSubscriberInterfaceHardwareIndexEntry = _JnxSubscriberInterfaceHardwareIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 4, 1)
)
jnxSubscriberInterfaceHardwareIndexEntry.setIndexNames(
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberInterfaceHardwareIndexHandleHiWord"),
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberInterfaceHardwareIndexHandleLoWord"),
)
if mibBuilder.loadTexts:
    jnxSubscriberInterfaceHardwareIndexEntry.setStatus("current")


class _JnxSubscriberInterfaceHardwareIndexHandleHiWord_Type(Unsigned32):
    """Custom type jnxSubscriberInterfaceHardwareIndexHandleHiWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberInterfaceHardwareIndexHandleHiWord_Type.__name__ = "Unsigned32"
_JnxSubscriberInterfaceHardwareIndexHandleHiWord_Object = MibTableColumn
jnxSubscriberInterfaceHardwareIndexHandleHiWord = _JnxSubscriberInterfaceHardwareIndexHandleHiWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 4, 1, 1),
    _JnxSubscriberInterfaceHardwareIndexHandleHiWord_Type()
)
jnxSubscriberInterfaceHardwareIndexHandleHiWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberInterfaceHardwareIndexHandleHiWord.setStatus("current")


class _JnxSubscriberInterfaceHardwareIndexHandleLoWord_Type(Unsigned32):
    """Custom type jnxSubscriberInterfaceHardwareIndexHandleLoWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberInterfaceHardwareIndexHandleLoWord_Type.__name__ = "Unsigned32"
_JnxSubscriberInterfaceHardwareIndexHandleLoWord_Object = MibTableColumn
jnxSubscriberInterfaceHardwareIndexHandleLoWord = _JnxSubscriberInterfaceHardwareIndexHandleLoWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 4, 1, 2),
    _JnxSubscriberInterfaceHardwareIndexHandleLoWord_Type()
)
jnxSubscriberInterfaceHardwareIndexHandleLoWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberInterfaceHardwareIndexHandleLoWord.setStatus("current")


class _JnxSubscriberInterfaceHardwareIndex_Type(Unsigned32):
    """Custom type jnxSubscriberInterfaceHardwareIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberInterfaceHardwareIndex_Type.__name__ = "Unsigned32"
_JnxSubscriberInterfaceHardwareIndex_Object = MibTableColumn
jnxSubscriberInterfaceHardwareIndex = _JnxSubscriberInterfaceHardwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 4, 1, 3),
    _JnxSubscriberInterfaceHardwareIndex_Type()
)
jnxSubscriberInterfaceHardwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberInterfaceHardwareIndex.setStatus("current")
_JnxSubscriberPortCountTable_Object = MibTable
jnxSubscriberPortCountTable = _JnxSubscriberPortCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxSubscriberPortCountTable.setStatus("current")
_JnxSubscriberPortCountEntry_Object = MibTableRow
jnxSubscriberPortCountEntry = _JnxSubscriberPortCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 5, 1)
)
jnxSubscriberPortCountEntry.setIndexNames(
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberPort"),
)
if mibBuilder.loadTexts:
    jnxSubscriberPortCountEntry.setStatus("current")


class _JnxSubscriberPort_Type(DisplayString):
    """Custom type jnxSubscriberPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxSubscriberPort_Type.__name__ = "DisplayString"
_JnxSubscriberPort_Object = MibTableColumn
jnxSubscriberPort = _JnxSubscriberPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 5, 1, 1),
    _JnxSubscriberPort_Type()
)
jnxSubscriberPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberPort.setStatus("current")
_JnxSubscriberPortTunneledCounter_Type = CounterBasedGauge64
_JnxSubscriberPortTunneledCounter_Object = MibTableColumn
jnxSubscriberPortTunneledCounter = _JnxSubscriberPortTunneledCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 5, 1, 2),
    _JnxSubscriberPortTunneledCounter_Type()
)
jnxSubscriberPortTunneledCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberPortTunneledCounter.setStatus("current")
_JnxSubscriberPortTerminatedCounter_Type = CounterBasedGauge64
_JnxSubscriberPortTerminatedCounter_Object = MibTableColumn
jnxSubscriberPortTerminatedCounter = _JnxSubscriberPortTerminatedCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 5, 1, 3),
    _JnxSubscriberPortTerminatedCounter_Type()
)
jnxSubscriberPortTerminatedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberPortTerminatedCounter.setStatus("current")
_JnxSubscriberAccountingTable_Object = MibTable
jnxSubscriberAccountingTable = _JnxSubscriberAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxSubscriberAccountingTable.setStatus("current")
_JnxSubscriberAccountingEntry_Object = MibTableRow
jnxSubscriberAccountingEntry = _JnxSubscriberAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1)
)
jnxSubscriberAccountingEntry.setIndexNames(
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberAccountingHandleHiWord"),
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberAccountingHandleLoWord"),
)
if mibBuilder.loadTexts:
    jnxSubscriberAccountingEntry.setStatus("current")


class _JnxSubscriberAccountingHandleHiWord_Type(Unsigned32):
    """Custom type jnxSubscriberAccountingHandleHiWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberAccountingHandleHiWord_Type.__name__ = "Unsigned32"
_JnxSubscriberAccountingHandleHiWord_Object = MibTableColumn
jnxSubscriberAccountingHandleHiWord = _JnxSubscriberAccountingHandleHiWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 1),
    _JnxSubscriberAccountingHandleHiWord_Type()
)
jnxSubscriberAccountingHandleHiWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingHandleHiWord.setStatus("current")


class _JnxSubscriberAccountingHandleLoWord_Type(Unsigned32):
    """Custom type jnxSubscriberAccountingHandleLoWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberAccountingHandleLoWord_Type.__name__ = "Unsigned32"
_JnxSubscriberAccountingHandleLoWord_Object = MibTableColumn
jnxSubscriberAccountingHandleLoWord = _JnxSubscriberAccountingHandleLoWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 2),
    _JnxSubscriberAccountingHandleLoWord_Type()
)
jnxSubscriberAccountingHandleLoWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingHandleLoWord.setStatus("current")
_JnxSubscriberAccountingUserName_Type = DisplayString
_JnxSubscriberAccountingUserName_Object = MibTableColumn
jnxSubscriberAccountingUserName = _JnxSubscriberAccountingUserName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 3),
    _JnxSubscriberAccountingUserName_Type()
)
jnxSubscriberAccountingUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingUserName.setStatus("current")
_JnxSubscriberAccountingClientType_Type = JnxSubscriberClientType
_JnxSubscriberAccountingClientType_Object = MibTableColumn
jnxSubscriberAccountingClientType = _JnxSubscriberAccountingClientType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 4),
    _JnxSubscriberAccountingClientType_Type()
)
jnxSubscriberAccountingClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingClientType.setStatus("current")
_JnxSubscriberAccountingIpAddress_Type = IpAddress
_JnxSubscriberAccountingIpAddress_Object = MibTableColumn
jnxSubscriberAccountingIpAddress = _JnxSubscriberAccountingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 5),
    _JnxSubscriberAccountingIpAddress_Type()
)
jnxSubscriberAccountingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingIpAddress.setStatus("current")
_JnxSubscriberAccountingIpAddressMask_Type = IpAddress
_JnxSubscriberAccountingIpAddressMask_Object = MibTableColumn
jnxSubscriberAccountingIpAddressMask = _JnxSubscriberAccountingIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 6),
    _JnxSubscriberAccountingIpAddressMask_Type()
)
jnxSubscriberAccountingIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingIpAddressMask.setStatus("current")


class _JnxSubscriberAccountingLogicalSystem_Type(OctetString):
    """Custom type jnxSubscriberAccountingLogicalSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxSubscriberAccountingLogicalSystem_Type.__name__ = "OctetString"
_JnxSubscriberAccountingLogicalSystem_Object = MibTableColumn
jnxSubscriberAccountingLogicalSystem = _JnxSubscriberAccountingLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 7),
    _JnxSubscriberAccountingLogicalSystem_Type()
)
jnxSubscriberAccountingLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingLogicalSystem.setStatus("current")


class _JnxSubscriberAccountingRoutingInstance_Type(OctetString):
    """Custom type jnxSubscriberAccountingRoutingInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxSubscriberAccountingRoutingInstance_Type.__name__ = "OctetString"
_JnxSubscriberAccountingRoutingInstance_Object = MibTableColumn
jnxSubscriberAccountingRoutingInstance = _JnxSubscriberAccountingRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 8),
    _JnxSubscriberAccountingRoutingInstance_Type()
)
jnxSubscriberAccountingRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingRoutingInstance.setStatus("current")
_JnxSubscriberAccountingInterface_Type = DisplayString
_JnxSubscriberAccountingInterface_Object = MibTableColumn
jnxSubscriberAccountingInterface = _JnxSubscriberAccountingInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 9),
    _JnxSubscriberAccountingInterface_Type()
)
jnxSubscriberAccountingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingInterface.setStatus("current")


class _JnxSubscriberAccountingInterfaceType_Type(Integer32):
    """Custom type jnxSubscriberAccountingInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("none", 0),
          ("static", 1))
    )


_JnxSubscriberAccountingInterfaceType_Type.__name__ = "Integer32"
_JnxSubscriberAccountingInterfaceType_Object = MibTableColumn
jnxSubscriberAccountingInterfaceType = _JnxSubscriberAccountingInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 10),
    _JnxSubscriberAccountingInterfaceType_Type()
)
jnxSubscriberAccountingInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingInterfaceType.setStatus("current")
_JnxSubscriberAccountingMacAddress_Type = MacAddress
_JnxSubscriberAccountingMacAddress_Object = MibTableColumn
jnxSubscriberAccountingMacAddress = _JnxSubscriberAccountingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 11),
    _JnxSubscriberAccountingMacAddress_Type()
)
jnxSubscriberAccountingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingMacAddress.setStatus("current")
_JnxSubscriberAccountingState_Type = JnxSubscriberState
_JnxSubscriberAccountingState_Object = MibTableColumn
jnxSubscriberAccountingState = _JnxSubscriberAccountingState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 12),
    _JnxSubscriberAccountingState_Type()
)
jnxSubscriberAccountingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingState.setStatus("current")
_JnxSubscriberAccountingLoginTime_Type = DisplayString
_JnxSubscriberAccountingLoginTime_Object = MibTableColumn
jnxSubscriberAccountingLoginTime = _JnxSubscriberAccountingLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 13),
    _JnxSubscriberAccountingLoginTime_Type()
)
jnxSubscriberAccountingLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingLoginTime.setStatus("current")
_JnxSubscriberAccountingAcctSessionId_Type = DisplayString
_JnxSubscriberAccountingAcctSessionId_Object = MibTableColumn
jnxSubscriberAccountingAcctSessionId = _JnxSubscriberAccountingAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 1, 6, 1, 14),
    _JnxSubscriberAccountingAcctSessionId_Type()
)
jnxSubscriberAccountingAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberAccountingAcctSessionId.setStatus("current")
_JnxSubscriberLogicalSystemObjects_ObjectIdentity = ObjectIdentity
jnxSubscriberLogicalSystemObjects = _JnxSubscriberLogicalSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2)
)
_JnxSubscriberLogicalSystemTotalCount_Type = CounterBasedGauge64
_JnxSubscriberLogicalSystemTotalCount_Object = MibScalar
jnxSubscriberLogicalSystemTotalCount = _JnxSubscriberLogicalSystemTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 1),
    _JnxSubscriberLogicalSystemTotalCount_Type()
)
jnxSubscriberLogicalSystemTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemTotalCount.setStatus("current")
_JnxSubscriberLogicalSystemActiveCount_Type = CounterBasedGauge64
_JnxSubscriberLogicalSystemActiveCount_Object = MibScalar
jnxSubscriberLogicalSystemActiveCount = _JnxSubscriberLogicalSystemActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 2),
    _JnxSubscriberLogicalSystemActiveCount_Type()
)
jnxSubscriberLogicalSystemActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemActiveCount.setStatus("current")
_JnxSubscriberLogicalSystemTable_Object = MibTable
jnxSubscriberLogicalSystemTable = _JnxSubscriberLogicalSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemTable.setStatus("current")
_JnxSubscriberLogicalSystemEntry_Object = MibTableRow
jnxSubscriberLogicalSystemEntry = _JnxSubscriberLogicalSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 3, 1)
)
jnxSubscriberLogicalSystemEntry.setIndexNames(
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberLogicalSystemHandleHiWord"),
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberLogicalSystemHandleLoWord"),
)
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemEntry.setStatus("current")


class _JnxSubscriberLogicalSystemHandleHiWord_Type(Unsigned32):
    """Custom type jnxSubscriberLogicalSystemHandleHiWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberLogicalSystemHandleHiWord_Type.__name__ = "Unsigned32"
_JnxSubscriberLogicalSystemHandleHiWord_Object = MibTableColumn
jnxSubscriberLogicalSystemHandleHiWord = _JnxSubscriberLogicalSystemHandleHiWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 3, 1, 1),
    _JnxSubscriberLogicalSystemHandleHiWord_Type()
)
jnxSubscriberLogicalSystemHandleHiWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemHandleHiWord.setStatus("current")


class _JnxSubscriberLogicalSystemHandleLoWord_Type(Unsigned32):
    """Custom type jnxSubscriberLogicalSystemHandleLoWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberLogicalSystemHandleLoWord_Type.__name__ = "Unsigned32"
_JnxSubscriberLogicalSystemHandleLoWord_Object = MibTableColumn
jnxSubscriberLogicalSystemHandleLoWord = _JnxSubscriberLogicalSystemHandleLoWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 3, 1, 2),
    _JnxSubscriberLogicalSystemHandleLoWord_Type()
)
jnxSubscriberLogicalSystemHandleLoWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemHandleLoWord.setStatus("current")
_JnxSubscriberLogicalSystemState_Type = JnxSubscriberState
_JnxSubscriberLogicalSystemState_Object = MibTableColumn
jnxSubscriberLogicalSystemState = _JnxSubscriberLogicalSystemState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 2, 3, 1, 3),
    _JnxSubscriberLogicalSystemState_Type()
)
jnxSubscriberLogicalSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberLogicalSystemState.setStatus("current")
_JnxSubscriberRoutingInstanceObjects_ObjectIdentity = ObjectIdentity
jnxSubscriberRoutingInstanceObjects = _JnxSubscriberRoutingInstanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3)
)
_JnxSubscriberRoutingInstanceTotalCount_Type = CounterBasedGauge64
_JnxSubscriberRoutingInstanceTotalCount_Object = MibScalar
jnxSubscriberRoutingInstanceTotalCount = _JnxSubscriberRoutingInstanceTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 1),
    _JnxSubscriberRoutingInstanceTotalCount_Type()
)
jnxSubscriberRoutingInstanceTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceTotalCount.setStatus("current")
_JnxSubscriberRoutingInstanceActiveCount_Type = CounterBasedGauge64
_JnxSubscriberRoutingInstanceActiveCount_Object = MibScalar
jnxSubscriberRoutingInstanceActiveCount = _JnxSubscriberRoutingInstanceActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 2),
    _JnxSubscriberRoutingInstanceActiveCount_Type()
)
jnxSubscriberRoutingInstanceActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceActiveCount.setStatus("current")
_JnxSubscriberRoutingInstanceTable_Object = MibTable
jnxSubscriberRoutingInstanceTable = _JnxSubscriberRoutingInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceTable.setStatus("current")
_JnxSubscriberRoutingInstanceEntry_Object = MibTableRow
jnxSubscriberRoutingInstanceEntry = _JnxSubscriberRoutingInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 3, 1)
)
jnxSubscriberRoutingInstanceEntry.setIndexNames(
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberRoutingInstanceHandleHiWord"),
    (0, "JUNIPER-SUBSCRIBER-MIB", "jnxSubscriberRoutingInstanceHandleLoWord"),
)
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceEntry.setStatus("current")


class _JnxSubscriberRoutingInstanceHandleHiWord_Type(Unsigned32):
    """Custom type jnxSubscriberRoutingInstanceHandleHiWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberRoutingInstanceHandleHiWord_Type.__name__ = "Unsigned32"
_JnxSubscriberRoutingInstanceHandleHiWord_Object = MibTableColumn
jnxSubscriberRoutingInstanceHandleHiWord = _JnxSubscriberRoutingInstanceHandleHiWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 3, 1, 1),
    _JnxSubscriberRoutingInstanceHandleHiWord_Type()
)
jnxSubscriberRoutingInstanceHandleHiWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceHandleHiWord.setStatus("current")


class _JnxSubscriberRoutingInstanceHandleLoWord_Type(Unsigned32):
    """Custom type jnxSubscriberRoutingInstanceHandleLoWord based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSubscriberRoutingInstanceHandleLoWord_Type.__name__ = "Unsigned32"
_JnxSubscriberRoutingInstanceHandleLoWord_Object = MibTableColumn
jnxSubscriberRoutingInstanceHandleLoWord = _JnxSubscriberRoutingInstanceHandleLoWord_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 3, 1, 2),
    _JnxSubscriberRoutingInstanceHandleLoWord_Type()
)
jnxSubscriberRoutingInstanceHandleLoWord.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceHandleLoWord.setStatus("current")
_JnxSubscriberRoutingInstanceState_Type = JnxSubscriberState
_JnxSubscriberRoutingInstanceState_Object = MibTableColumn
jnxSubscriberRoutingInstanceState = _JnxSubscriberRoutingInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 64, 1, 1, 3, 3, 1, 3),
    _JnxSubscriberRoutingInstanceState_Type()
)
jnxSubscriberRoutingInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSubscriberRoutingInstanceState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SUBSCRIBER-MIB",
    **{"JnxSubscriberState": JnxSubscriberState,
       "JnxSubscriberClientType": JnxSubscriberClientType,
       "jnxSubscriberMIB": jnxSubscriberMIB,
       "jnxSubscriberObjects": jnxSubscriberObjects,
       "jnxSubscriberGeneral": jnxSubscriberGeneral,
       "jnxSubscriberTotalCount": jnxSubscriberTotalCount,
       "jnxSubscriberActiveCount": jnxSubscriberActiveCount,
       "jnxSubscriberTable": jnxSubscriberTable,
       "jnxSubscriberEntry": jnxSubscriberEntry,
       "jnxSubscriberHandleHiWord": jnxSubscriberHandleHiWord,
       "jnxSubscriberHandleLoWord": jnxSubscriberHandleLoWord,
       "jnxSubscriberUserName": jnxSubscriberUserName,
       "jnxSubscriberClientType": jnxSubscriberClientType,
       "jnxSubscriberIpAddress": jnxSubscriberIpAddress,
       "jnxSubscriberIpAddressMask": jnxSubscriberIpAddressMask,
       "jnxSubscriberLogicalSystem": jnxSubscriberLogicalSystem,
       "jnxSubscriberRoutingInstance": jnxSubscriberRoutingInstance,
       "jnxSubscriberInterface": jnxSubscriberInterface,
       "jnxSubscriberInterfaceType": jnxSubscriberInterfaceType,
       "jnxSubscriberMacAddress": jnxSubscriberMacAddress,
       "jnxSubscriberState": jnxSubscriberState,
       "jnxSubscriberLoginTime": jnxSubscriberLoginTime,
       "jnxSubscriberAcctSessionId": jnxSubscriberAcctSessionId,
       "jnxSubscriberInterfaceHardwareIndexTable": jnxSubscriberInterfaceHardwareIndexTable,
       "jnxSubscriberInterfaceHardwareIndexEntry": jnxSubscriberInterfaceHardwareIndexEntry,
       "jnxSubscriberInterfaceHardwareIndexHandleHiWord": jnxSubscriberInterfaceHardwareIndexHandleHiWord,
       "jnxSubscriberInterfaceHardwareIndexHandleLoWord": jnxSubscriberInterfaceHardwareIndexHandleLoWord,
       "jnxSubscriberInterfaceHardwareIndex": jnxSubscriberInterfaceHardwareIndex,
       "jnxSubscriberPortCountTable": jnxSubscriberPortCountTable,
       "jnxSubscriberPortCountEntry": jnxSubscriberPortCountEntry,
       "jnxSubscriberPort": jnxSubscriberPort,
       "jnxSubscriberPortTunneledCounter": jnxSubscriberPortTunneledCounter,
       "jnxSubscriberPortTerminatedCounter": jnxSubscriberPortTerminatedCounter,
       "jnxSubscriberAccountingTable": jnxSubscriberAccountingTable,
       "jnxSubscriberAccountingEntry": jnxSubscriberAccountingEntry,
       "jnxSubscriberAccountingHandleHiWord": jnxSubscriberAccountingHandleHiWord,
       "jnxSubscriberAccountingHandleLoWord": jnxSubscriberAccountingHandleLoWord,
       "jnxSubscriberAccountingUserName": jnxSubscriberAccountingUserName,
       "jnxSubscriberAccountingClientType": jnxSubscriberAccountingClientType,
       "jnxSubscriberAccountingIpAddress": jnxSubscriberAccountingIpAddress,
       "jnxSubscriberAccountingIpAddressMask": jnxSubscriberAccountingIpAddressMask,
       "jnxSubscriberAccountingLogicalSystem": jnxSubscriberAccountingLogicalSystem,
       "jnxSubscriberAccountingRoutingInstance": jnxSubscriberAccountingRoutingInstance,
       "jnxSubscriberAccountingInterface": jnxSubscriberAccountingInterface,
       "jnxSubscriberAccountingInterfaceType": jnxSubscriberAccountingInterfaceType,
       "jnxSubscriberAccountingMacAddress": jnxSubscriberAccountingMacAddress,
       "jnxSubscriberAccountingState": jnxSubscriberAccountingState,
       "jnxSubscriberAccountingLoginTime": jnxSubscriberAccountingLoginTime,
       "jnxSubscriberAccountingAcctSessionId": jnxSubscriberAccountingAcctSessionId,
       "jnxSubscriberLogicalSystemObjects": jnxSubscriberLogicalSystemObjects,
       "jnxSubscriberLogicalSystemTotalCount": jnxSubscriberLogicalSystemTotalCount,
       "jnxSubscriberLogicalSystemActiveCount": jnxSubscriberLogicalSystemActiveCount,
       "jnxSubscriberLogicalSystemTable": jnxSubscriberLogicalSystemTable,
       "jnxSubscriberLogicalSystemEntry": jnxSubscriberLogicalSystemEntry,
       "jnxSubscriberLogicalSystemHandleHiWord": jnxSubscriberLogicalSystemHandleHiWord,
       "jnxSubscriberLogicalSystemHandleLoWord": jnxSubscriberLogicalSystemHandleLoWord,
       "jnxSubscriberLogicalSystemState": jnxSubscriberLogicalSystemState,
       "jnxSubscriberRoutingInstanceObjects": jnxSubscriberRoutingInstanceObjects,
       "jnxSubscriberRoutingInstanceTotalCount": jnxSubscriberRoutingInstanceTotalCount,
       "jnxSubscriberRoutingInstanceActiveCount": jnxSubscriberRoutingInstanceActiveCount,
       "jnxSubscriberRoutingInstanceTable": jnxSubscriberRoutingInstanceTable,
       "jnxSubscriberRoutingInstanceEntry": jnxSubscriberRoutingInstanceEntry,
       "jnxSubscriberRoutingInstanceHandleHiWord": jnxSubscriberRoutingInstanceHandleHiWord,
       "jnxSubscriberRoutingInstanceHandleLoWord": jnxSubscriberRoutingInstanceHandleLoWord,
       "jnxSubscriberRoutingInstanceState": jnxSubscriberRoutingInstanceState}
)
