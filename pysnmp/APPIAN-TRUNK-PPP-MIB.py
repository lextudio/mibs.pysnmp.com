# SNMP MIB module (APPIAN-TRUNK-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-TRUNK-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:47 2024
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

(acTrunks,) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "acTrunks")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acPppTrunk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3)
)
acPppTrunk.setRevisions(
        ("1900-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPppTrunkTable_Object = MibTable
acPppTrunkTable = _AcPppTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    acPppTrunkTable.setStatus("current")
_AcPppTrunkEntry_Object = MibTableRow
acPppTrunkEntry = _AcPppTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1)
)
acPppTrunkEntry.setIndexNames(
    (0, "APPIAN-TRUNK-PPP-MIB", "acPppTrunkIndex"),
)
if mibBuilder.loadTexts:
    acPppTrunkEntry.setStatus("current")


class _AcPppTrunkIndex_Type(Integer32):
    """Custom type acPppTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPppTrunkIndex_Type.__name__ = "Integer32"
_AcPppTrunkIndex_Object = MibTableColumn
acPppTrunkIndex = _AcPppTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 1),
    _AcPppTrunkIndex_Type()
)
acPppTrunkIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acPppTrunkIndex.setStatus("current")


class _AcPppTrunkMru_Type(Integer32):
    """Custom type acPppTrunkMru based on Integer32"""
    defaultValue = 1520

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2048),
    )


_AcPppTrunkMru_Type.__name__ = "Integer32"
_AcPppTrunkMru_Object = MibTableColumn
acPppTrunkMru = _AcPppTrunkMru_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 2),
    _AcPppTrunkMru_Type()
)
acPppTrunkMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMru.setStatus("deprecated")


class _AcPppTrunkMrru_Type(Integer32):
    """Custom type acPppTrunkMrru based on Integer32"""
    defaultValue = 1520

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2048),
    )


_AcPppTrunkMrru_Type.__name__ = "Integer32"
_AcPppTrunkMrru_Object = MibTableColumn
acPppTrunkMrru = _AcPppTrunkMrru_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 3),
    _AcPppTrunkMrru_Type()
)
acPppTrunkMrru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMrru.setStatus("deprecated")


class _AcPppTrunkSeqNum_Type(Integer32):
    """Custom type acPppTrunkSeqNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("short", 1))
    )


_AcPppTrunkSeqNum_Type.__name__ = "Integer32"
_AcPppTrunkSeqNum_Object = MibTableColumn
acPppTrunkSeqNum = _AcPppTrunkSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 4),
    _AcPppTrunkSeqNum_Type()
)
acPppTrunkSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkSeqNum.setStatus("current")


class _AcPppTrunkMagicNumberEnable_Type(TruthValue):
    """Custom type acPppTrunkMagicNumberEnable based on TruthValue"""


_AcPppTrunkMagicNumberEnable_Object = MibTableColumn
acPppTrunkMagicNumberEnable = _AcPppTrunkMagicNumberEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 5),
    _AcPppTrunkMagicNumberEnable_Type()
)
acPppTrunkMagicNumberEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMagicNumberEnable.setStatus("current")


class _AcPppTrunkLCPEchoEnable_Type(TruthValue):
    """Custom type acPppTrunkLCPEchoEnable based on TruthValue"""


_AcPppTrunkLCPEchoEnable_Object = MibTableColumn
acPppTrunkLCPEchoEnable = _AcPppTrunkLCPEchoEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 6),
    _AcPppTrunkLCPEchoEnable_Type()
)
acPppTrunkLCPEchoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkLCPEchoEnable.setStatus("current")


class _AcPppTrunkLCPEchoInterval_Type(Integer32):
    """Custom type acPppTrunkLCPEchoInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AcPppTrunkLCPEchoInterval_Type.__name__ = "Integer32"
_AcPppTrunkLCPEchoInterval_Object = MibTableColumn
acPppTrunkLCPEchoInterval = _AcPppTrunkLCPEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 7),
    _AcPppTrunkLCPEchoInterval_Type()
)
acPppTrunkLCPEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkLCPEchoInterval.setStatus("current")


class _AcPppTrunkMgmtAccess_Type(TruthValue):
    """Custom type acPppTrunkMgmtAccess based on TruthValue"""


_AcPppTrunkMgmtAccess_Object = MibTableColumn
acPppTrunkMgmtAccess = _AcPppTrunkMgmtAccess_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 8),
    _AcPppTrunkMgmtAccess_Type()
)
acPppTrunkMgmtAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMgmtAccess.setStatus("current")


class _AcPppTrunkIPCPAddressEnable_Type(TruthValue):
    """Custom type acPppTrunkIPCPAddressEnable based on TruthValue"""


_AcPppTrunkIPCPAddressEnable_Object = MibTableColumn
acPppTrunkIPCPAddressEnable = _AcPppTrunkIPCPAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 9),
    _AcPppTrunkIPCPAddressEnable_Type()
)
acPppTrunkIPCPAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkIPCPAddressEnable.setStatus("current")


class _AcPppTrunkMaxTerminate_Type(Integer32):
    """Custom type acPppTrunkMaxTerminate based on Integer32"""
    defaultValue = 2


_AcPppTrunkMaxTerminate_Object = MibTableColumn
acPppTrunkMaxTerminate = _AcPppTrunkMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 10),
    _AcPppTrunkMaxTerminate_Type()
)
acPppTrunkMaxTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMaxTerminate.setStatus("current")


class _AcPppTrunkMaxConfigure_Type(Integer32):
    """Custom type acPppTrunkMaxConfigure based on Integer32"""
    defaultValue = 10


_AcPppTrunkMaxConfigure_Object = MibTableColumn
acPppTrunkMaxConfigure = _AcPppTrunkMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 11),
    _AcPppTrunkMaxConfigure_Type()
)
acPppTrunkMaxConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMaxConfigure.setStatus("current")


class _AcPppTrunkMaxFailure_Type(Integer32):
    """Custom type acPppTrunkMaxFailure based on Integer32"""
    defaultValue = 5


_AcPppTrunkMaxFailure_Object = MibTableColumn
acPppTrunkMaxFailure = _AcPppTrunkMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 6, 3, 1, 1, 12),
    _AcPppTrunkMaxFailure_Type()
)
acPppTrunkMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPppTrunkMaxFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-TRUNK-PPP-MIB",
    **{"acPppTrunk": acPppTrunk,
       "acPppTrunkTable": acPppTrunkTable,
       "acPppTrunkEntry": acPppTrunkEntry,
       "acPppTrunkIndex": acPppTrunkIndex,
       "acPppTrunkMru": acPppTrunkMru,
       "acPppTrunkMrru": acPppTrunkMrru,
       "acPppTrunkSeqNum": acPppTrunkSeqNum,
       "acPppTrunkMagicNumberEnable": acPppTrunkMagicNumberEnable,
       "acPppTrunkLCPEchoEnable": acPppTrunkLCPEchoEnable,
       "acPppTrunkLCPEchoInterval": acPppTrunkLCPEchoInterval,
       "acPppTrunkMgmtAccess": acPppTrunkMgmtAccess,
       "acPppTrunkIPCPAddressEnable": acPppTrunkIPCPAddressEnable,
       "acPppTrunkMaxTerminate": acPppTrunkMaxTerminate,
       "acPppTrunkMaxConfigure": acPppTrunkMaxConfigure,
       "acPppTrunkMaxFailure": acPppTrunkMaxFailure}
)
