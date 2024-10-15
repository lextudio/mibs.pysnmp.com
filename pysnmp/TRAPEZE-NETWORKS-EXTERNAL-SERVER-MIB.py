# SNMP MIB module (TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:31 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(TrpzIpPort,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzIpPort")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzExternalServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7)
)
trpzExternalServerMib.setRevisions(
        ("2011-06-22 00:40",
         "2009-10-02 00:21",
         "2008-10-24 00:10",
         "2006-07-31 00:04")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzSyslogServerEnable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzExternalServerObjects_ObjectIdentity = ObjectIdentity
trpzExternalServerObjects = _TrpzExternalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1)
)
_TrpzExternalServerDataObjects_ObjectIdentity = ObjectIdentity
trpzExternalServerDataObjects = _TrpzExternalServerDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1)
)
_TrpzExtServerSyslogTable_Object = MibTable
trpzExtServerSyslogTable = _TrpzExtServerSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trpzExtServerSyslogTable.setStatus("current")
_TrpzExtServerSyslogEntry_Object = MibTableRow
trpzExtServerSyslogEntry = _TrpzExtServerSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1)
)
trpzExtServerSyslogEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogIndex"),
)
if mibBuilder.loadTexts:
    trpzExtServerSyslogEntry.setStatus("current")
_TrpzExtServerSyslogIndex_Type = Unsigned32
_TrpzExtServerSyslogIndex_Object = MibTableColumn
trpzExtServerSyslogIndex = _TrpzExtServerSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 1),
    _TrpzExtServerSyslogIndex_Type()
)
trpzExtServerSyslogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzExtServerSyslogIndex.setStatus("current")
_TrpzExtServerSyslogAddress_Type = IpAddress
_TrpzExtServerSyslogAddress_Object = MibTableColumn
trpzExtServerSyslogAddress = _TrpzExtServerSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 2),
    _TrpzExtServerSyslogAddress_Type()
)
trpzExtServerSyslogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzExtServerSyslogAddress.setStatus("current")
_TrpzExtServerSyslogPort_Type = TrpzIpPort
_TrpzExtServerSyslogPort_Object = MibTableColumn
trpzExtServerSyslogPort = _TrpzExtServerSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 3),
    _TrpzExtServerSyslogPort_Type()
)
trpzExtServerSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzExtServerSyslogPort.setStatus("current")
_TrpzExtServerSyslogEnable_Type = TrpzSyslogServerEnable
_TrpzExtServerSyslogEnable_Object = MibTableColumn
trpzExtServerSyslogEnable = _TrpzExtServerSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 4),
    _TrpzExtServerSyslogEnable_Type()
)
trpzExtServerSyslogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzExtServerSyslogEnable.setStatus("current")
_TrpzExternalServerGlobalObjects_ObjectIdentity = ObjectIdentity
trpzExternalServerGlobalObjects = _TrpzExternalServerGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2)
)
_TrpzExtServerPrimaryDnsIpAddress_Type = IpAddress
_TrpzExtServerPrimaryDnsIpAddress_Object = MibScalar
trpzExtServerPrimaryDnsIpAddress = _TrpzExtServerPrimaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2, 1),
    _TrpzExtServerPrimaryDnsIpAddress_Type()
)
trpzExtServerPrimaryDnsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzExtServerPrimaryDnsIpAddress.setStatus("current")
_TrpzExtServerSecondaryDnsIpAddress_Type = IpAddress
_TrpzExtServerSecondaryDnsIpAddress_Object = MibScalar
trpzExtServerSecondaryDnsIpAddress = _TrpzExtServerSecondaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2, 2),
    _TrpzExtServerSecondaryDnsIpAddress_Type()
)
trpzExtServerSecondaryDnsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzExtServerSecondaryDnsIpAddress.setStatus("current")
_TrpzExternalServerConformance_ObjectIdentity = ObjectIdentity
trpzExternalServerConformance = _TrpzExternalServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2)
)
_TrpzExternalServerCompliances_ObjectIdentity = ObjectIdentity
trpzExternalServerCompliances = _TrpzExternalServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1)
)
_TrpzExternalServerGroups_ObjectIdentity = ObjectIdentity
trpzExternalServerGroups = _TrpzExternalServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2)
)

# Managed Objects groups

trpzExternalServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2, 1)
)
trpzExternalServerConfigGroup.setObjects(
      *(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogAddress"),
        ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogPort"),
        ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogEnable"))
)
if mibBuilder.loadTexts:
    trpzExternalServerConfigGroup.setStatus("current")

trpzExternalServerDnsServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2, 2)
)
trpzExternalServerDnsServerGroup.setObjects(
      *(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerPrimaryDnsIpAddress"),
        ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSecondaryDnsIpAddress"))
)
if mibBuilder.loadTexts:
    trpzExternalServerDnsServerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzExternalServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzExternalServerCompliance.setStatus(
        "obsolete"
    )

trpzExternalServerComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    trpzExternalServerComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB",
    **{"TrpzSyslogServerEnable": TrpzSyslogServerEnable,
       "trpzExternalServerMib": trpzExternalServerMib,
       "trpzExternalServerObjects": trpzExternalServerObjects,
       "trpzExternalServerDataObjects": trpzExternalServerDataObjects,
       "trpzExtServerSyslogTable": trpzExtServerSyslogTable,
       "trpzExtServerSyslogEntry": trpzExtServerSyslogEntry,
       "trpzExtServerSyslogIndex": trpzExtServerSyslogIndex,
       "trpzExtServerSyslogAddress": trpzExtServerSyslogAddress,
       "trpzExtServerSyslogPort": trpzExtServerSyslogPort,
       "trpzExtServerSyslogEnable": trpzExtServerSyslogEnable,
       "trpzExternalServerGlobalObjects": trpzExternalServerGlobalObjects,
       "trpzExtServerPrimaryDnsIpAddress": trpzExtServerPrimaryDnsIpAddress,
       "trpzExtServerSecondaryDnsIpAddress": trpzExtServerSecondaryDnsIpAddress,
       "trpzExternalServerConformance": trpzExternalServerConformance,
       "trpzExternalServerCompliances": trpzExternalServerCompliances,
       "trpzExternalServerCompliance": trpzExternalServerCompliance,
       "trpzExternalServerComplianceRev2": trpzExternalServerComplianceRev2,
       "trpzExternalServerGroups": trpzExternalServerGroups,
       "trpzExternalServerConfigGroup": trpzExternalServerConfigGroup,
       "trpzExternalServerDnsServerGroup": trpzExternalServerDnsServerGroup}
)
