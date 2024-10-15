# SNMP MIB module (RMON2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RMON2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:58 2024
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

(OwnerString,
 channelEntry,
 etherStatsEntry,
 filter,
 filterEntry,
 history,
 historyControlEntry,
 hostControlEntry,
 hosts,
 matrix,
 matrixControlEntry,
 statistics) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "channelEntry",
    "etherStatsEntry",
    "filter",
    "filterEntry",
    "history",
    "historyControlEntry",
    "hostControlEntry",
    "hosts",
    "matrix",
    "matrixControlEntry",
    "statistics")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rmon = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class LastCreateTime(TimeStamp, TextualConvention):
    status = "current"


class TimeFilter(TimeTicks, TextualConvention):
    status = "current"


class DataSource(ObjectIdentifier, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ProtocolDir_ObjectIdentity = ObjectIdentity
protocolDir = _ProtocolDir_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 11)
)
_ProtocolDist_ObjectIdentity = ObjectIdentity
protocolDist = _ProtocolDist_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 12)
)
_AddressMap_ObjectIdentity = ObjectIdentity
addressMap = _AddressMap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 13)
)
_NlHost_ObjectIdentity = ObjectIdentity
nlHost = _NlHost_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 14)
)
_NlMatrix_ObjectIdentity = ObjectIdentity
nlMatrix = _NlMatrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 15)
)
_AlHost_ObjectIdentity = ObjectIdentity
alHost = _AlHost_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 16)
)
_AlMatrix_ObjectIdentity = ObjectIdentity
alMatrix = _AlMatrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 17)
)
_UsrHistory_ObjectIdentity = ObjectIdentity
usrHistory = _UsrHistory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 18)
)
_ProbeConfig_ObjectIdentity = ObjectIdentity
probeConfig = _ProbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 19)
)
_RmonConformance_ObjectIdentity = ObjectIdentity
rmonConformance = _RmonConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RMON2-MIB",
    **{"ZeroBasedCounter32": ZeroBasedCounter32,
       "LastCreateTime": LastCreateTime,
       "TimeFilter": TimeFilter,
       "DataSource": DataSource,
       "rmon": rmon,
       "protocolDir": protocolDir,
       "protocolDist": protocolDist,
       "addressMap": addressMap,
       "nlHost": nlHost,
       "nlMatrix": nlMatrix,
       "alHost": alHost,
       "alMatrix": alMatrix,
       "usrHistory": usrHistory,
       "probeConfig": probeConfig,
       "rmonConformance": rmonConformance}
)
