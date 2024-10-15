# SNMP MIB module (WS-INFRA-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-INFRA-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:24 2024
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

(wsInfra,) = mibBuilder.importSymbols(
    "WS-SMI",
    "wsInfra")


# MODULE-IDENTITY

wslInfraMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 1)
)
wslInfraMIB.setRevisions(
        ("2008-05-01 13:27",
         "2007-01-12 11:54",
         "2006-05-24 14:42",
         "2005-12-19 10:35",
         "2005-07-28 19:00",
         "2005-06-24 11:00",
         "2005-06-22 11:36",
         "2005-05-23 17:36",
         "2005-05-04 16:09",
         "2005-05-04 15:58",
         "2005-05-04 10:32")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsInfraFileMgmt_ObjectIdentity = ObjectIdentity
wsInfraFileMgmt = _WsInfraFileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 2)
)
_WsInfraSysMsg_ObjectIdentity = ObjectIdentity
wsInfraSysMsg = _WsInfraSysMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 3)
)
_WsInfraPM_ObjectIdentity = ObjectIdentity
wsInfraPM = _WsInfraPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 5)
)
_WsInfraDiag_ObjectIdentity = ObjectIdentity
wsInfraDiag = _WsInfraDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 6)
)
_WsInfraCluster_ObjectIdentity = ObjectIdentity
wsInfraCluster = _WsInfraCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 8)
)
_WsInfraLic_ObjectIdentity = ObjectIdentity
wsInfraLic = _WsInfraLic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 9)
)
_WsInfraNTP_ObjectIdentity = ObjectIdentity
wsInfraNTP = _WsInfraNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 10)
)
_WsInfraAutoUpdate_ObjectIdentity = ObjectIdentity
wsInfraAutoUpdate = _WsInfraAutoUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 11)
)
_WsInfraSmtpNotify_ObjectIdentity = ObjectIdentity
wsInfraSmtpNotify = _WsInfraSmtpNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 1, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-INFRA-SMI-MIB",
    **{"wslInfraMIB": wslInfraMIB,
       "wsInfraFileMgmt": wsInfraFileMgmt,
       "wsInfraSysMsg": wsInfraSysMsg,
       "wsInfraPM": wsInfraPM,
       "wsInfraDiag": wsInfraDiag,
       "wsInfraCluster": wsInfraCluster,
       "wsInfraLic": wsInfraLic,
       "wsInfraNTP": wsInfraNTP,
       "wsInfraAutoUpdate": wsInfraAutoUpdate,
       "wsInfraSmtpNotify": wsInfraSmtpNotify}
)
