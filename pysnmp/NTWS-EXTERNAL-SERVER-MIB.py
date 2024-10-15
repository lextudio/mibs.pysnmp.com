# SNMP MIB module (NTWS-EXTERNAL-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:56 2024
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

(NtwsIpPort,) = mibBuilder.importSymbols(
    "NTWS-BASIC-TC",
    "NtwsIpPort")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsExternalServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7)
)
ntwsExternalServerMib.setRevisions(
        ("2008-10-24 00:10",
         "2007-08-16 00:05",
         "2006-07-31 00:04")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsSyslogServerEnable(Integer32, TextualConvention):
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

_NtwsExternalServerObjects_ObjectIdentity = ObjectIdentity
ntwsExternalServerObjects = _NtwsExternalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1)
)
_NtwsExternalServerDataObjects_ObjectIdentity = ObjectIdentity
ntwsExternalServerDataObjects = _NtwsExternalServerDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1)
)
_NtwsExtServerSyslogTable_Object = MibTable
ntwsExtServerSyslogTable = _NtwsExtServerSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsExtServerSyslogTable.setStatus("current")
_NtwsExtServerSyslogEntry_Object = MibTableRow
ntwsExtServerSyslogEntry = _NtwsExtServerSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1)
)
ntwsExtServerSyslogEntry.setIndexNames(
    (0, "NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogIndex"),
)
if mibBuilder.loadTexts:
    ntwsExtServerSyslogEntry.setStatus("current")
_NtwsExtServerSyslogIndex_Type = Unsigned32
_NtwsExtServerSyslogIndex_Object = MibTableColumn
ntwsExtServerSyslogIndex = _NtwsExtServerSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 1),
    _NtwsExtServerSyslogIndex_Type()
)
ntwsExtServerSyslogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsExtServerSyslogIndex.setStatus("current")
_NtwsExtServerSyslogAddress_Type = IpAddress
_NtwsExtServerSyslogAddress_Object = MibTableColumn
ntwsExtServerSyslogAddress = _NtwsExtServerSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 2),
    _NtwsExtServerSyslogAddress_Type()
)
ntwsExtServerSyslogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsExtServerSyslogAddress.setStatus("current")
_NtwsExtServerSyslogPort_Type = NtwsIpPort
_NtwsExtServerSyslogPort_Object = MibTableColumn
ntwsExtServerSyslogPort = _NtwsExtServerSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 3),
    _NtwsExtServerSyslogPort_Type()
)
ntwsExtServerSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsExtServerSyslogPort.setStatus("current")
_NtwsExtServerSyslogEnable_Type = NtwsSyslogServerEnable
_NtwsExtServerSyslogEnable_Object = MibTableColumn
ntwsExtServerSyslogEnable = _NtwsExtServerSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 4),
    _NtwsExtServerSyslogEnable_Type()
)
ntwsExtServerSyslogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsExtServerSyslogEnable.setStatus("current")
_NtwsExternalServerConformance_ObjectIdentity = ObjectIdentity
ntwsExternalServerConformance = _NtwsExternalServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2)
)
_NtwsExternalServerCompliances_ObjectIdentity = ObjectIdentity
ntwsExternalServerCompliances = _NtwsExternalServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1)
)
_NtwsExternalServerGroups_ObjectIdentity = ObjectIdentity
ntwsExternalServerGroups = _NtwsExternalServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2)
)

# Managed Objects groups

ntwsExternalServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2, 1)
)
ntwsExternalServerConfigGroup.setObjects(
      *(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogAddress"),
        ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogPort"),
        ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogEnable"))
)
if mibBuilder.loadTexts:
    ntwsExternalServerConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsExternalServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsExternalServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-EXTERNAL-SERVER-MIB",
    **{"NtwsSyslogServerEnable": NtwsSyslogServerEnable,
       "ntwsExternalServerMib": ntwsExternalServerMib,
       "ntwsExternalServerObjects": ntwsExternalServerObjects,
       "ntwsExternalServerDataObjects": ntwsExternalServerDataObjects,
       "ntwsExtServerSyslogTable": ntwsExtServerSyslogTable,
       "ntwsExtServerSyslogEntry": ntwsExtServerSyslogEntry,
       "ntwsExtServerSyslogIndex": ntwsExtServerSyslogIndex,
       "ntwsExtServerSyslogAddress": ntwsExtServerSyslogAddress,
       "ntwsExtServerSyslogPort": ntwsExtServerSyslogPort,
       "ntwsExtServerSyslogEnable": ntwsExtServerSyslogEnable,
       "ntwsExternalServerConformance": ntwsExternalServerConformance,
       "ntwsExternalServerCompliances": ntwsExternalServerCompliances,
       "ntwsExternalServerCompliance": ntwsExternalServerCompliance,
       "ntwsExternalServerGroups": ntwsExternalServerGroups,
       "ntwsExternalServerConfigGroup": ntwsExternalServerConfigGroup}
)
