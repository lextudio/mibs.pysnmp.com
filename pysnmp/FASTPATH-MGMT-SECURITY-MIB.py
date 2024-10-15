# SNMP MIB module (FASTPATH-MGMT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FASTPATH-MGMT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:56 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "BROADCOM-REF-MIB",
    "fastPath")

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

fastPathMgmtSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11)
)
fastPathMgmtSecurity.setRevisions(
        ("2007-05-23 00:00",
         "2003-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSSLConfigGroup_ObjectIdentity = ObjectIdentity
agentSSLConfigGroup = _AgentSSLConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1)
)


class _AgentSSLAdminMode_Type(Integer32):
    """Custom type agentSSLAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSSLAdminMode_Type.__name__ = "Integer32"
_AgentSSLAdminMode_Object = MibScalar
agentSSLAdminMode = _AgentSSLAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 1),
    _AgentSSLAdminMode_Type()
)
agentSSLAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLAdminMode.setStatus("current")


class _AgentSSLSecurePort_Type(Integer32):
    """Custom type agentSSLSecurePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentSSLSecurePort_Type.__name__ = "Integer32"
_AgentSSLSecurePort_Object = MibScalar
agentSSLSecurePort = _AgentSSLSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 2),
    _AgentSSLSecurePort_Type()
)
agentSSLSecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLSecurePort.setStatus("current")


class _AgentSSLProtocolLevel_Type(Integer32):
    """Custom type agentSSLProtocolLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ssl30", 1),
          ("tls10", 2))
    )


_AgentSSLProtocolLevel_Type.__name__ = "Integer32"
_AgentSSLProtocolLevel_Object = MibScalar
agentSSLProtocolLevel = _AgentSSLProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 3),
    _AgentSSLProtocolLevel_Type()
)
agentSSLProtocolLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSLProtocolLevel.setStatus("current")


class _AgentSSLMaxSessions_Type(Integer32):
    """Custom type agentSSLMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AgentSSLMaxSessions_Type.__name__ = "Integer32"
_AgentSSLMaxSessions_Object = MibScalar
agentSSLMaxSessions = _AgentSSLMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 4),
    _AgentSSLMaxSessions_Type()
)
agentSSLMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLMaxSessions.setStatus("current")


class _AgentSSLHardTimeout_Type(Integer32):
    """Custom type agentSSLHardTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_AgentSSLHardTimeout_Type.__name__ = "Integer32"
_AgentSSLHardTimeout_Object = MibScalar
agentSSLHardTimeout = _AgentSSLHardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 5),
    _AgentSSLHardTimeout_Type()
)
agentSSLHardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLHardTimeout.setStatus("current")


class _AgentSSLSoftTimeout_Type(Integer32):
    """Custom type agentSSLSoftTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AgentSSLSoftTimeout_Type.__name__ = "Integer32"
_AgentSSLSoftTimeout_Object = MibScalar
agentSSLSoftTimeout = _AgentSSLSoftTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 6),
    _AgentSSLSoftTimeout_Type()
)
agentSSLSoftTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLSoftTimeout.setStatus("current")
_AgentSSLCertificatePresent_Type = TruthValue
_AgentSSLCertificatePresent_Object = MibScalar
agentSSLCertificatePresent = _AgentSSLCertificatePresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 7),
    _AgentSSLCertificatePresent_Type()
)
agentSSLCertificatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSLCertificatePresent.setStatus("current")


class _AgentSSLCertificateControl_Type(Integer32):
    """Custom type agentSSLCertificateControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("generate", 2),
          ("noop", 1))
    )


_AgentSSLCertificateControl_Type.__name__ = "Integer32"
_AgentSSLCertificateControl_Object = MibScalar
agentSSLCertificateControl = _AgentSSLCertificateControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 8),
    _AgentSSLCertificateControl_Type()
)
agentSSLCertificateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLCertificateControl.setStatus("current")
_AgentSSLCertificateGenerationStatus_Type = TruthValue
_AgentSSLCertificateGenerationStatus_Object = MibScalar
agentSSLCertificateGenerationStatus = _AgentSSLCertificateGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 1, 9),
    _AgentSSLCertificateGenerationStatus_Type()
)
agentSSLCertificateGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSLCertificateGenerationStatus.setStatus("current")
_AgentSSHConfigGroup_ObjectIdentity = ObjectIdentity
agentSSHConfigGroup = _AgentSSHConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2)
)


class _AgentSSHAdminMode_Type(Integer32):
    """Custom type agentSSHAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSSHAdminMode_Type.__name__ = "Integer32"
_AgentSSHAdminMode_Object = MibScalar
agentSSHAdminMode = _AgentSSHAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 1),
    _AgentSSHAdminMode_Type()
)
agentSSHAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHAdminMode.setStatus("current")


class _AgentSSHProtocolLevel_Type(Integer32):
    """Custom type agentSSHProtocolLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ssh10", 1),
          ("ssh20", 2))
    )


_AgentSSHProtocolLevel_Type.__name__ = "Integer32"
_AgentSSHProtocolLevel_Object = MibScalar
agentSSHProtocolLevel = _AgentSSHProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 2),
    _AgentSSHProtocolLevel_Type()
)
agentSSHProtocolLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHProtocolLevel.setStatus("current")
_AgentSSHSessionsCount_Type = Integer32
_AgentSSHSessionsCount_Object = MibScalar
agentSSHSessionsCount = _AgentSSHSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 3),
    _AgentSSHSessionsCount_Type()
)
agentSSHSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHSessionsCount.setStatus("current")


class _AgentSSHMaxSessionsCount_Type(Integer32):
    """Custom type agentSSHMaxSessionsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentSSHMaxSessionsCount_Type.__name__ = "Integer32"
_AgentSSHMaxSessionsCount_Object = MibScalar
agentSSHMaxSessionsCount = _AgentSSHMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 4),
    _AgentSSHMaxSessionsCount_Type()
)
agentSSHMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHMaxSessionsCount.setStatus("current")


class _AgentSSHSessionTimeout_Type(Integer32):
    """Custom type agentSSHSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3932159),
    )


_AgentSSHSessionTimeout_Type.__name__ = "Integer32"
_AgentSSHSessionTimeout_Object = MibScalar
agentSSHSessionTimeout = _AgentSSHSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 5),
    _AgentSSHSessionTimeout_Type()
)
agentSSHSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHSessionTimeout.setStatus("current")


class _AgentSSHKeysPresent_Type(Integer32):
    """Custom type agentSSHKeysPresent based on Integer32"""
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
        *(("both", 3),
          ("dsa", 1),
          ("none", 4),
          ("rsa", 2))
    )


_AgentSSHKeysPresent_Type.__name__ = "Integer32"
_AgentSSHKeysPresent_Object = MibScalar
agentSSHKeysPresent = _AgentSSHKeysPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 6),
    _AgentSSHKeysPresent_Type()
)
agentSSHKeysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHKeysPresent.setStatus("current")


class _AgentSSHKeyGenerationStatus_Type(Integer32):
    """Custom type agentSSHKeyGenerationStatus based on Integer32"""
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
        *(("both", 3),
          ("dsa", 1),
          ("none", 4),
          ("rsa", 2))
    )


_AgentSSHKeyGenerationStatus_Type.__name__ = "Integer32"
_AgentSSHKeyGenerationStatus_Object = MibScalar
agentSSHKeyGenerationStatus = _AgentSSHKeyGenerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 7),
    _AgentSSHKeyGenerationStatus_Type()
)
agentSSHKeyGenerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHKeyGenerationStatus.setStatus("current")


class _AgentSSHRSAKeyControl_Type(Integer32):
    """Custom type agentSSHRSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("generate", 2),
          ("noop", 1))
    )


_AgentSSHRSAKeyControl_Type.__name__ = "Integer32"
_AgentSSHRSAKeyControl_Object = MibScalar
agentSSHRSAKeyControl = _AgentSSHRSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 8),
    _AgentSSHRSAKeyControl_Type()
)
agentSSHRSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHRSAKeyControl.setStatus("current")


class _AgentSSHDSAKeyControl_Type(Integer32):
    """Custom type agentSSHDSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("generate", 2),
          ("noop", 1))
    )


_AgentSSHDSAKeyControl_Type.__name__ = "Integer32"
_AgentSSHDSAKeyControl_Object = MibScalar
agentSSHDSAKeyControl = _AgentSSHDSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 11, 2, 9),
    _AgentSSHDSAKeyControl_Type()
)
agentSSHDSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHDSAKeyControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FASTPATH-MGMT-SECURITY-MIB",
    **{"fastPathMgmtSecurity": fastPathMgmtSecurity,
       "agentSSLConfigGroup": agentSSLConfigGroup,
       "agentSSLAdminMode": agentSSLAdminMode,
       "agentSSLSecurePort": agentSSLSecurePort,
       "agentSSLProtocolLevel": agentSSLProtocolLevel,
       "agentSSLMaxSessions": agentSSLMaxSessions,
       "agentSSLHardTimeout": agentSSLHardTimeout,
       "agentSSLSoftTimeout": agentSSLSoftTimeout,
       "agentSSLCertificatePresent": agentSSLCertificatePresent,
       "agentSSLCertificateControl": agentSSLCertificateControl,
       "agentSSLCertificateGenerationStatus": agentSSLCertificateGenerationStatus,
       "agentSSHConfigGroup": agentSSHConfigGroup,
       "agentSSHAdminMode": agentSSHAdminMode,
       "agentSSHProtocolLevel": agentSSHProtocolLevel,
       "agentSSHSessionsCount": agentSSHSessionsCount,
       "agentSSHMaxSessionsCount": agentSSHMaxSessionsCount,
       "agentSSHSessionTimeout": agentSSHSessionTimeout,
       "agentSSHKeysPresent": agentSSHKeysPresent,
       "agentSSHKeyGenerationStatus": agentSSHKeyGenerationStatus,
       "agentSSHRSAKeyControl": agentSSHRSAKeyControl,
       "agentSSHDSAKeyControl": agentSSHDSAKeyControl}
)
