# SNMP MIB module (FNET-OPTIVIEW-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FNET-OPTIVIEW-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:17 2024
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

(fnetOptiViewGeneric,) = mibBuilder.importSymbols(
    "FNET-GLOBAL-REG",
    "fnetOptiViewGeneric")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OvTrapSeverity(Integer32):
    """Custom type OvTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("inform", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )





class OvTrapStatus(Integer32):
    """Custom type OvTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discovered", 1),
          ("resolved", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OvStdTraps_ObjectIdentity = ObjectIdentity
ovStdTraps = _OvStdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1)
)


class _OvTrapAgentSysName_Type(DisplayString):
    """Custom type ovTrapAgentSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OvTrapAgentSysName_Type.__name__ = "DisplayString"
_OvTrapAgentSysName_Object = MibScalar
ovTrapAgentSysName = _OvTrapAgentSysName_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 1),
    _OvTrapAgentSysName_Type()
)
ovTrapAgentSysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapAgentSysName.setStatus("mandatory")
_OvTrapSeverity_Type = OvTrapSeverity
_OvTrapSeverity_Object = MibScalar
ovTrapSeverity = _OvTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 2),
    _OvTrapSeverity_Type()
)
ovTrapSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapSeverity.setStatus("mandatory")
_OvTrapStatus_Type = OvTrapStatus
_OvTrapStatus_Object = MibScalar
ovTrapStatus = _OvTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 3),
    _OvTrapStatus_Type()
)
ovTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapStatus.setStatus("mandatory")


class _OvTrapDescription_Type(DisplayString):
    """Custom type ovTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OvTrapDescription_Type.__name__ = "DisplayString"
_OvTrapDescription_Object = MibScalar
ovTrapDescription = _OvTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 4),
    _OvTrapDescription_Type()
)
ovTrapDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapDescription.setStatus("mandatory")


class _OvTrapOffenderName_Type(DisplayString):
    """Custom type ovTrapOffenderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OvTrapOffenderName_Type.__name__ = "DisplayString"
_OvTrapOffenderName_Object = MibScalar
ovTrapOffenderName = _OvTrapOffenderName_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 5),
    _OvTrapOffenderName_Type()
)
ovTrapOffenderName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapOffenderName.setStatus("mandatory")


class _OvTrapOffenderNetAddr_Type(DisplayString):
    """Custom type ovTrapOffenderNetAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OvTrapOffenderNetAddr_Type.__name__ = "DisplayString"
_OvTrapOffenderNetAddr_Object = MibScalar
ovTrapOffenderNetAddr = _OvTrapOffenderNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 6),
    _OvTrapOffenderNetAddr_Type()
)
ovTrapOffenderNetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapOffenderNetAddr.setStatus("mandatory")


class _OvTrapOffenderPhyAddr_Type(DisplayString):
    """Custom type ovTrapOffenderPhyAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OvTrapOffenderPhyAddr_Type.__name__ = "DisplayString"
_OvTrapOffenderPhyAddr_Object = MibScalar
ovTrapOffenderPhyAddr = _OvTrapOffenderPhyAddr_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 7),
    _OvTrapOffenderPhyAddr_Type()
)
ovTrapOffenderPhyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapOffenderPhyAddr.setStatus("mandatory")
_OvTrapOffenderSubId_Type = Integer32
_OvTrapOffenderSubId_Object = MibScalar
ovTrapOffenderSubId = _OvTrapOffenderSubId_Object(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 1, 8),
    _OvTrapOffenderSubId_Type()
)
ovTrapOffenderSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ovTrapOffenderSubId.setStatus("optional")

# Managed Objects groups


# Notification objects

ovProbDupIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 1)
)
ovProbDupIp.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderPhyAddr"))
)
if mibBuilder.loadTexts:
    ovProbDupIp.setStatus(
        ""
    )

probBadMask = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 2)
)
probBadMask.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probBadMask.setStatus(
        ""
    )

ovProbBadDefRouter = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 3)
)
ovProbBadDefRouter.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    ovProbBadDefRouter.setStatus(
        ""
    )

probLoneIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 4)
)
probLoneIp.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probLoneIp.setStatus(
        ""
    )

probLoneNbDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 5)
)
probLoneNbDomain.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probLoneNbDomain.setStatus(
        ""
    )

probLoneIpxNet = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 6)
)
probLoneIpxNet.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probLoneIpxNet.setStatus(
        ""
    )

probLoneIpxType = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 7)
)
probLoneIpxType.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probLoneIpxType.setStatus(
        ""
    )

probKeyDevNoResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 8)
)
probKeyDevNoResp.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probKeyDevNoResp.setStatus(
        ""
    )

probReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 9)
)
probReboot.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probReboot.setStatus(
        ""
    )

probRerunTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 1226, 2, 1, 0, 10)
)
probRerunTest.setObjects(
      *(("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapAgentSysName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapSeverity"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapStatus"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapDescription"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderName"),
        ("FNET-OPTIVIEW-GENERIC-MIB", "ovTrapOffenderNetAddr"))
)
if mibBuilder.loadTexts:
    probRerunTest.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FNET-OPTIVIEW-GENERIC-MIB",
    **{"OvTrapSeverity": OvTrapSeverity,
       "OvTrapStatus": OvTrapStatus,
       "ovProbDupIp": ovProbDupIp,
       "probBadMask": probBadMask,
       "ovProbBadDefRouter": ovProbBadDefRouter,
       "probLoneIp": probLoneIp,
       "probLoneNbDomain": probLoneNbDomain,
       "probLoneIpxNet": probLoneIpxNet,
       "probLoneIpxType": probLoneIpxType,
       "probKeyDevNoResp": probKeyDevNoResp,
       "probReboot": probReboot,
       "probRerunTest": probRerunTest,
       "ovStdTraps": ovStdTraps,
       "ovTrapAgentSysName": ovTrapAgentSysName,
       "ovTrapSeverity": ovTrapSeverity,
       "ovTrapStatus": ovTrapStatus,
       "ovTrapDescription": ovTrapDescription,
       "ovTrapOffenderName": ovTrapOffenderName,
       "ovTrapOffenderNetAddr": ovTrapOffenderNetAddr,
       "ovTrapOffenderPhyAddr": ovTrapOffenderPhyAddr,
       "ovTrapOffenderSubId": ovTrapOffenderSubId}
)
